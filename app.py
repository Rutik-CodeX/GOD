from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, Employee , TimesheetEntry
from flask import session
from datetime import timedelta , date ,datetime
from sqlalchemy.exc import SQLAlchemyError
import uuid



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ems-database.db'
app.config['SECRET_KEY'] = 'your_secret_key'

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

@app.before_request
def session_management():
    session.permanent = True

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))

# ___________________________________________LOGIN-LOGOUT____________________________________________________________

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Employee.query.filter_by(username=username).first()
        
        if user and user.Password == password:
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# ____________________________________________________________Home_____________________________________________________________________________________


@app.route('/home')
@login_required
def home():
    user_data = {
        "EName": current_user.EName,
        "Profile": current_user.Profile,
        "EEMail": current_user.EEMail,
        "EMPID": current_user.EMPID,
        "LineManager": current_user.LineManager,
        "LineManagerID": current_user.LineManagerID,
        "Team": current_user.Team
    }
    return render_template('home.html', user=user_data)

# ______________________________________________________________Timesheet-Home_______________________________________________________________________________________


@app.route('/timesheethome')
@login_required
def timesheethome():
    # Check if current user is a manager
    is_manager = current_user.Profile == 'Manager'
    return render_template('timesheethome.html', is_manager=is_manager)


# ______________________________________________________________Timesheet-FillForm_______________________________________________________________________________________

# Route to render the form page
@app.route('/filltimesheet', methods=['GET', 'POST'])
@login_required
def filltimesheet():
    if request.method == 'POST':
        return redirect(url_for('submit_timesheet'))
    return render_template('filltimesheet.html', user=current_user)

# Route to handle form submission
@app.route('/submit_timesheet', methods=['POST'])
@login_required
def submit_timesheet():
    try:
        # Fetch the list of dates and split them if necessary
        dates = request.form.getlist('DateofEntry')
        dates = [date.strip() for date in dates[0].split(',')]  # Split and strip if necessary

        hours = float(request.form['hours'])
        minutes = float(request.form['minutes'])
        allocation_type = request.form['AllocationType']
        category_1 = request.form['Category1']
        category_2 = request.form.get('Category2', '')
        category_3 = request.form.get('Category3', '')
        project_code = request.form['ProjectCode']
        comments = request.form.get('comments', '')

        # Calculate total_time and other relevant fields based on the allocation type
        total_time = hours + (minutes / 60.0)
        billable_time = nonbillable_admin_time = nonbillable_training_time = unavailable_time = 0

        if allocation_type == 'billable':
            billable_time = total_time
        elif allocation_type == 'non-billable':
            if category_1.lower() == 'admin':
                nonbillable_admin_time = total_time
            elif category_1.lower() == 'training':
                nonbillable_training_time = total_time
            else:
                unavailable_time = total_time

        # Insert entries for each selected date
        for date in dates:
            try:
                # Parse the date string to a proper date object
                entry_date = datetime.strptime(date, '%Y-%m-%d').date()

                entry = TimesheetEntry(
                    Uniq_ID=str(uuid.uuid4()),
                    EName=current_user.EName,
                    EmpID=current_user.EMPID,
                    Team=current_user.Team,
                    LineManager=current_user.LineManager,
                    DateofEntry=entry_date,  # Use the parsed date here
                    Hours=hours,
                    Minutes=minutes,
                    billable_time=billable_time,
                    nonbillable_admin_time=nonbillable_admin_time,
                    nonbillable_training_time=nonbillable_training_time,
                    unavailable_time=unavailable_time,
                    total_time=total_time,
                    AllocationType=allocation_type,
                    Category1=category_1,
                    Category2=category_2,
                    Category3=category_3,
                    ProjectCode=project_code,
                    Comment=comments,
                    SubmitDate=datetime.utcnow(),
                    LastUploadDate=datetime.utcnow(),
                    LastUpdatedBy=current_user.username
                )
                db.session.add(entry)
                print(f"Added entry: {entry}")  # Debugging

            except Exception as e:
                print(f"Error adding entry: {e}")
                db.session.rollback()
                flash(f"Error adding timesheet entry: {str(e)}", "error")
                return redirect(url_for('filltimesheet'))

        # Commit all entries
        db.session.commit()
        flash("Timesheet successfully submitted.", "success")
        return redirect(url_for('home'))

    except Exception as e:
        db.session.rollback()
        flash(f"Error submitting timesheet: {str(e)}", "error")
        return redirect(url_for('filltimesheet'))

# ______________________________________________________________Timesheet-Summary_______________________________________________________________________________________


@app.route('/timesheetsummary', methods=['GET', 'POST'])
@login_required
def timesheet_summary():
    selected_date_str = request.args.get('selected_date', None)
    if selected_date_str:
        selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d')
    else:
        selected_date = datetime.utcnow()


    monday = selected_date - timedelta(days=selected_date.weekday())
    sunday = monday + timedelta(days=6)

    # Calculate the date range for the current week (Monday to Sunday)
    week_dates = [monday + timedelta(days=i) for i in range(7)]

    week_summary = []
    for day in week_dates:
        entries = TimesheetEntry.query.filter_by(EmpID=current_user.EMPID, DateofEntry=day).all()

        # Calculate the total time for each category
        billable_time = sum(entry.billable_time for entry in entries)
        nonbillable_admin_time = sum(entry.nonbillable_admin_time for entry in entries)
        nonbillable_training_time = sum(entry.nonbillable_training_time for entry in entries)
        unavailable_time = sum(entry.unavailable_time for entry in entries)
        total_time = sum(entry.total_time for entry in entries)

        # Append the summary for each day
        week_summary.append({
            'day': day.strftime('%A'),
            'date': day.strftime('%Y-%m-%d'),
            'billable_time': billable_time,
            'nonbillable_admin_time': nonbillable_admin_time,
            'nonbillable_training_time': nonbillable_training_time,
            'unavailable_time': unavailable_time,
            'total_time': total_time,
        })

    # Compute previous and next week's Monday dates
    prev_week_monday = monday - timedelta(days=7)
    next_week_monday = monday + timedelta(days=7)
    print(f"Entries for the week: {week_summary}")

    return render_template(
        'timesheet_summary.html',
        week_summary=week_summary,
        monday=monday,
        sunday=sunday,
        prev_week_monday=prev_week_monday.strftime('%Y-%m-%d'),
        next_week_monday=next_week_monday.strftime('%Y-%m-%d')
    )





if __name__ == "__main__":
    app.run(debug=True)


# from app import db
# db.create_all()
