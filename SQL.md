````bash

-- Create the employee table
CREATE TABLE employee (
EMPID INT PRIMARY KEY,
username VARCHAR(255) UNIQUE NOT NULL,
EName VARCHAR(255),
DOJRS VARCHAR(255),
DOJSIPL VARCHAR(255),
Profile VARCHAR(255),
Status VARCHAR(50),
SIPLLevel VARCHAR(50),
RSALevel VARCHAR(50),
EEMail VARCHAR(255),
IEMail VARCHAR(255),
Landline VARCHAR(20),
Mobile VARCHAR(20),
Ext VARCHAR(10),
Secretary VARCHAR(255),
SecretaryID VARCHAR(255),
SystemID VARCHAR(255),
Password VARCHAR(255) NOT NULL,
Team VARCHAR(255),
LineManager VARCHAR(255),
LineManagerID VARCHAR(255)
);

```bash

 -- Create the timesheet_entries table
        CREATE TABLE timesheet_entries (
            Uniq_ID VARCHAR(50) PRIMARY KEY,
            EName VARCHAR(255),
            EmpID VARCHAR(10),
            Team VARCHAR(255),
            LineManager VARCHAR(255),
            DateofEntry VARCHAR(255),
            StartTime VARCHAR(255),
            EndTime VARCHAR(255),
            Hours FLOAT,
            Minutes FLOAT,
            billable_time FLOAT,
            nonbillable_admin_time FLOAT,
            nonbillable_training_time FLOAT,
            unavailable_time FLOAT,
            total_time FLOAT,
            AllocationType VARCHAR(50),
            Category1 VARCHAR(50),
            Category2 VARCHAR(50),
            Category3 VARCHAR(50),
            Category4 VARCHAR(50),
            Category5 VARCHAR(50),
            Category6 VARCHAR(50),
            ProjectCode VARCHAR(10),
            Comment VARCHAR(255),
            Status VARCHAR(20),
            SubmitDate VARCHAR(255),
            LastUploadDate VARCHAR(255),
            LastUpdatedBy VARCHAR(50)
        );

````

```bash
INSERT INTO employee (EMPID, username, EName, DOJRS, DOJSIPL, Profile, Status, SIPLLevel, RSALevel, EEMail, IEMail, Landline, Mobile, Ext, Secretary, SecretaryID, SystemID, Password, Team, LineManager, LineManagerID)
VALUES
(101, '101', 'John Doe', '2020-01-15', '2021-02-20', 'Developer', 'Active', 'Level 1', 'Level A', 'john.doe@example.com', 'j.doe@example.com', '1234567890', '9876543210', '101', 'Alice Smith', 'S101', 'SYS101', 'pass', 'Development', 'Jane Doe', 102),
(102, '102', 'Jane Doe', '2020-01-20', '2021-02-25', 'Manager', 'Active', 'Level 2', 'Level B', 'jane.doe@example.com', 'jane.doe@example.com', '1234567891', '9876543211', '102', 'Bob Johnson', 'S102', 'SYS102', 'pass', 'Development', 'John Doe', 101),
(103, '103', 'Alice Smith', '2020-02-01', '2021-03-10', 'Tester', 'Active', 'Level 1', 'Level C', 'alice.smith@example.com', 'a.smith@example.com', '1234567892', '9876543212', '103', 'Carol Taylor', 'S103', 'SYS103', 'pass', 'QA', 'Jane Doe', 102),
(104, '104', 'Bob Johnson', '2020-02-10', '2021-03-15', 'Designer', 'Active', 'Level 1', 'Level A', 'bob.johnson@example.com', 'b.johnson@example.com', '1234567893', '9876543213', '104', 'David Brown', 'S104', 'SYS104', 'pass', 'Design', 'John Doe', 101),
(105, '105', 'Carol Taylor', '2020-02-15', '2021-04-05', 'Developer', 'Active', 'Level 2', 'Level B', 'carol.taylor@example.com', 'c.taylor@example.com', '1234567894', '9876543214', '105', 'Eve White', 'S105', 'SYS105', 'pass', 'Development', 'Jane Doe', 102),
(106, '106', 'David Brown', '2020-03-01', '2021-05-10', 'Manager', 'Active', 'Level 2', 'Level C', 'david.brown@example.com', 'd.brown@example.com', '1234567895', '9876543215', '106', 'Fay Green', 'S106', 'SYS106', 'pass', 'Management', 'Bob Johnson', 103),
(107, '107', 'Eve White', '2020-03-10', '2021-05-15', 'Tester', 'Active', 'Level 1', 'Level A', 'eve.white@example.com', 'e.white@example.com', '1234567896', '9876543216', '107', 'Grace Black', 'S107', 'SYS107', 'pass', 'QA', 'David Brown', 104),
(108, '108', 'Fay Green', '2020-03-15', '2021-06-01', 'Developer', 'Active', 'Level 1', 'Level B', 'fay.green@example.com', 'f.green@example.com', '1234567897', '9876543217', '108', 'Heidi Grey', 'S108', 'SYS108', 'pass', 'Development', 'Alice Smith', 103),
(109, '109', 'Grace Black', '2020-04-01', '2021-06-15', 'Designer', 'Active', 'Level 1', 'Level C', 'grace.black@example.com', 'g.black@example.com', '1234567898', '9876543218', '109', 'Ivy Blue', 'S109', 'SYS109', 'pass', 'Design', 'Bob Johnson', 104),
(110, '110', 'Heidi Grey', '2020-04-10', '2021-07-05', 'Manager', 'Active', 'Level 2', 'Level A', 'heidi.grey@example.com', 'h.grey@example.com', '1234567899', '9876543219', '110', 'Jack Red', 'S110', 'SYS110', 'pass', 'Management', 'Eve White', 107);

```
