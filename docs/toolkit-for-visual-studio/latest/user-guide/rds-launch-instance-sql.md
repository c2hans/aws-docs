---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/rds-launch-instance-sql.html
---

# Create a Microsoft SQL Server Database in an RDS Instance
<a name="rds-launch-instance-sql"></a>

Microsoft SQL Server is designed in such a way that, after launching an Amazon RDS instance, you need to create an SQL Server database in the RDS instance.

For information about how to create an Amazon RDS instance, see [Launch an Amazon RDS Database Instance](rds-launch-instance.md#tkv-launch-rds-instance).

 **To create a Microsoft SQL Server database**

1. In AWS Explorer, open the context (right-click) menu for the node that corresponds to your RDS instance for Microsoft SQL Server, and choose **Create SQL Server Database**.
![Context menu for RDS instance showing Create SQL Server Database option.](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/rds-ms-sql-create-db.png)

1. In the **Create SQL Server Database** dialog box, type the password you specified when you created the RDS instance, type a name for the Microsoft SQL Server database, and then choose **OK**.
![Create SQL Server Database dialog box with DB instance, credentials, and database name fields.](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/rds-spec-ms-sql-db.png)

1. The Toolkit for Visual Studio creates the Microsoft SQL Server database and adds it to the Visual Studio Server Explorer.
![Server Explorer showing expanded Data Connections with aws-3.my-ms-sql-db database structure.](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/rds-sql-svr-explorer.png)
