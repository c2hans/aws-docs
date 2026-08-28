---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.steps.html
---

# Step-by-step SQL Server database to Amazon Aurora MySQL migration walkthrough
<a name="chap-sqlserver2aurora.steps"></a>

The following steps provide instructions for migrating a Microsoft SQL Server database to an Amazon Aurora MySQL database. These steps assume that you have already prepared your source database as described in [Prerequisites](chap-sqlserver2aurora.prerequisites.md).

**Topics**
+ [Step 1: Install the SQL Drivers and AWS Schema Conversion Tool on Your Local Computer](chap-sqlserver2aurora.steps.installsct.md)
+ [Step 2: Configure Your Microsoft SQL Server Source Database](chap-sqlserver2aurora.steps.configuresqlserver.md)
+ [Step 3: Configure Your Aurora MySQL Target Database](chap-sqlserver2aurora.steps.configureaurora.md)
+ [Step 4: Use AWS SCT to Convert the SQL Server Schema to Aurora MySQL](chap-sqlserver2aurora.steps.convertschema.md)
+ [Step 5: Create an AWS DMS Replication Instance](chap-sqlserver2aurora.steps.createreplicationinstance.md)
+ [Step 6: Create AWS DMS Source and Target Endpoints](chap-sqlserver2aurora.steps.createsourcetargetendpoints.md)
+ [Step 7: Create and Run Your AWS DMS Migration Task](chap-sqlserver2aurora.steps.createmigrationtask.md)
+ [Step 8: Cut Over to Aurora MySQL](chap-sqlserver2aurora.steps.cutover.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
