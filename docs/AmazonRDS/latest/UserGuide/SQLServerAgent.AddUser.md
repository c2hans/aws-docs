---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServerAgent.AddUser.html
---

# Adding a user to the SQLAgentUser role
<a name="SQLServerAgent.AddUser"></a>

To allow an additional login or user to use SQL Server Agent, log in as the master user and do the following:

1. Create another server-level login by using the `CREATE LOGIN` command.

1. Create a user in `msdb` using `CREATE USER` command, and then link this user to the login that you created in the previous step.

1. Add the user to the `SQLAgentUserRole` using the `sp_addrolemember` system stored procedure.

For example, suppose that your master user name is **admin** and you want to give access to SQL Server Agent to a user named **theirname** with a password **theirpassword**. In that case, you can use the following procedure.

**To add a user to the SQLAgentUser role**

1. Log in as the master user.

1. Run the following commands:

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
   --Added database user theirname in msdb to SQLAgentUserRole in msdb
   EXEC sp_addrolemember [SQLAgentUserRole], [theirname];
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
