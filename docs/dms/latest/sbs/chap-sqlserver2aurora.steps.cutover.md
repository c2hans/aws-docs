---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.steps.cutover.html
---

# Step 8: Cut Over to Aurora MySQL
<a name="chap-sqlserver2aurora.steps.cutover"></a>

To move connections from your Microsoft SQL Server database to your Amazon Aurora MySQL database, do the following:

1. End all SQL Server database dependencies and activities, such as running scripts and client connections. Ensure that the SQL Server Agent service is stopped.

   The following query should return no results other than your connection:

   ```
   SELECT session_id, login_name from sys.dm_exec_sessions where session_id > 50;
   ```

1. Kill any remaining sessions (other than your own).

   ```
   KILL session_id;
   ```

1. Shut down the SQL Server service.

1. Let the AWS DMS task apply the final changes from the SQL Server database on the Amazon Aurora MySQL database.

1. In the AWS DMS console, stop the AWS DMS task by choosing **Stop** for the task, and then confirming that you want to stop the task.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
