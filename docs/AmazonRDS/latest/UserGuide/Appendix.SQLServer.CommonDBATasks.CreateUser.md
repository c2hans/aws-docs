---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.CreateUser.html
---

# Creating a database user for Amazon RDS for SQL Server
<a name="Appendix.SQLServer.CommonDBATasks.CreateUser"></a>

You can create a database user for your Amazon RDS for Microsoft SQL Server DB instance by running a T-SQL script like the following example. Use an application such as SQL Server Management Suite (SSMS). You log into the DB instance as the master user that was created when you created the DB instance.

```
--Initially set context to master database
USE [master];
GO
--Create a server-level login named theirname with password theirpassword
CREATE LOGIN [theirname] WITH PASSWORD = 'theirpassword';
GO
--Set context to msdb database
USE [msdb];
GO
--Create a database user named theirname and link it to server-level login theirname
CREATE USER [theirname] FOR LOGIN [theirname];
GO
```

For an example of adding a database user to a role, see [Adding a user to the SQLAgentUser role](SQLServerAgent.AddUser.md).

**Note**
If you get permission errors when adding a user, you can restore privileges by modifying the DB instance master user password. For more information, see [Resetting the db\_owner role membership for master user for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.ResetPassword.md).
It is not a best practice to clone master user permissions in your applications. For more information, see [How to clone master user permissions in Amazon RDS for SQL Server](https://aws.amazon.com/blogs/database/how-to-clone-master-user-permissions-in-amazon-rds-for-sql-server/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
