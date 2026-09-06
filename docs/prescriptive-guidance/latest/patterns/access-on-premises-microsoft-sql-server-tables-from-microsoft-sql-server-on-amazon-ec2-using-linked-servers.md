---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-on-premises-microsoft-sql-server-tables-from-microsoft-sql-server-on-amazon-ec2-using-linked-servers.html
---

# Access on-premises Microsoft SQL Server tables from Microsoft SQL Server on Amazon EC2 using linked servers
<a name="access-on-premises-microsoft-sql-server-tables-from-microsoft-sql-server-on-amazon-ec2-using-linked-servers"></a>

*Tirumala Dasari and Eduardo Valentim, Amazon Web Services*

## Summary
<a name="access-on-premises-microsoft-sql-server-tables-from-microsoft-sql-server-on-amazon-ec2-using-linked-servers-summary"></a>

This pattern describes how to access on-premises Microsoft SQL Server database tables running on Microsoft Windows, from Microsoft SQL Server databases running or hosted on Amazon Elastic Compute Cloud (Amazon EC2) Windows or Linux instances by using linked servers.

## Prerequisites and limitations
<a name="access-on-premises-microsoft-sql-server-tables-from-microsoft-sql-server-on-amazon-ec2-using-linked-servers-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Amazon EC2 with Microsoft SQL Server running on Amazon Linux AMI (Amazon Machine Image)
+ AWS Direct Connect between the on-premises Microsoft SQL Server (Windows) server and the Windows or Linux EC2 instance

**Product versions**
+ SQL Server 2016 or later

## Architecture
<a name="access-on-premises-microsoft-sql-server-tables-from-microsoft-sql-server-on-amazon-ec2-using-linked-servers-architecture"></a>

**Source technology stack**
+ On-premises Microsoft SQL Server database running on Windows
+ Amazon EC2 with Microsoft SQL Server running on Windows AMI or Linux AMI

**Target technology stack**
+ Amazon EC2 with Microsoft SQL Server running on Amazon Linux AMI
+ Amazon EC2 with Microsoft SQL Server running on Windows AMI

**Source and target database architecture**

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/8e4a3222-0850-4980-8028-c710dcdb9186/images/fa157992-0ed9-46e1-8059-0cbbb74a98ec.png)

## Tools
<a name="access-on-premises-microsoft-sql-server-tables-from-microsoft-sql-server-on-amazon-ec2-using-linked-servers-tools"></a>
+ [Microsoft SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16) is an integrated environment for managing a SQL Server infrastructure. It provides a user interface and a group of tools with rich script editors that interact with SQL Server.

## Epics
<a name="access-on-premises-microsoft-sql-server-tables-from-microsoft-sql-server-on-amazon-ec2-using-linked-servers-epics"></a>

### Change authentication mode to Windows for SQL Server in Windows SQL Server
<a name="change-authentication-mode-to-windows-for-sql-server-in-windows-sql-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Connect to Windows SQL Server through SSMS. |  | DBA |
| Change the authentication mode to Windows in SQL Server from the context (right-click) menu for the Windows SQL Server instance. |  | DBA |

### Restart the Windows MSSQL service
<a name="restart-the-windows-mssql-service"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Restart the SQL service. | 1. In SSMS Object Explorer, choose the SQL Server instance.<br />2. Open the context (right-click) menu.<br />3. Choose **Restart**. | DBA |

### Create new login and choose databases to access in Windows SQL Server
<a name="create-new-login-and-choose-databases-to-access-in-windows-sql-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| In the Security tab, open the context (right-click) menu for Login and select a new login. |  | DBA |
| In the General tab, choose SQL Server authentication, enter a user name, enter the password, and then confirm the password and clear the option for changing the password at the next login. |  | DBA |
| In the Server Roles tab, choose Public. |  | DBA |
| In the User Mapping tab, choose the database and schema you want to access, and then highlight the database to select database roles. | Select public and db\_datareader to access data from the database tables. | DBA |
| Choose OK to create a user. |  | DBA |

### Add Windows SQL Server IP to Linux SQL Server host file
<a name="add-windows-sql-server-ip-to-linux-sql-server-host-file"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Connect to the Linux SQL Server box through the terminal window. |  | DBA |
| Open the /etc/hosts file and add the IP address of the Windows machine with SQL Server. |  | DBA |
| Save the hosts file. |  | DBA |

### Create linked server on Linux SQL Server
<a name="create-linked-server-on-linux-sql-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a linked server by using the stored procedures master.sys.sp\_addlinkedserver and master.dbo.sp\_addlinkedsrvlogin. | For more information about using these stored procedures, see the *Additional information* section. | DBA, Developer |

### Verify the created linked server and databases in SSMS
<a name="verify-the-created-linked-server-and-databases-in-ssms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| In Linux SQL Server in SSMS, go to Linked Servers and refresh. |  | DBA |
| Expand the created linked servers and catalogs in the left pane. | You'll see the selected SQL Server databases with tables and views. | DBA |

### Verify that you can access Windows SQL Server database tables
<a name="verify-that-you-can-access-windows-sql-server-database-tables"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| In the SSMS query window, run the query: "select top 3 \* from [sqllin].dms\_sample\_win.dbo.mlb\_data". | Note that the FROM clause uses a four-part syntax: computer.database.schema.table (e.g., SELECT name "SQL2 databases" FROM [sqllin].master.sys.databases). In our example, we created an alias for SQL2 in the hosts file, so you don’t need to enter the actual NetBIOS name between the square brackets. If you do use the actual NetBIOS names, note that AWS defaults to NetBIOS names like Win-xxxx, and SQL Server requires square brackets for names with dashes. | DBA, Developer |

## Related resources
<a name="access-on-premises-microsoft-sql-server-tables-from-microsoft-sql-server-on-amazon-ec2-using-linked-servers-resources"></a>
+ [Release notes for SQL Server on Linux](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-release-notes?view=sql-server-2017)

## Additional information
<a name="access-on-premises-microsoft-sql-server-tables-from-microsoft-sql-server-on-amazon-ec2-using-linked-servers-additional"></a>

**Using stored procedures to create linked servers**

SSMS doesn't support the creation of linked servers for Linux SQL Server, so you have to use these stored procedures to create them:

```
EXEC master.sys.sp_addlinkedserver @server= N'SQLLIN' , @srvproduct= N'SQL Server'
EXEC master.dbo.sp_addlinkedsrvlogin @rmtsrvname=N'SQLLIN',@useself=N'False',@locallogin=NULL,@rmtuser=N'username',@rmtpassword='Test123$'
```

Note 1: Enter the sign-in credentials that you created earlier in Windows SQL Server in the stored procedure `master.dbo.sp_addlinkedsrvlogin`.

Note 2: `@server` name `SQLLIN` and host file entry name `172.12.12.4 SQLLIN` should be the same.

 You can use this process to create linked servers for the following scenarios:
+ Linux SQL Server to Windows SQL Server through a linked server (as specified in this pattern)
+ Windows SQL Server to Linux SQL Server through a linked server
+ Linux SQL Server to another Linux SQL Server through a linked server
