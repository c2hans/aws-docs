---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-auditing-on-aws/overview.html
---

# Overview of SQL Server auditing levels and process
<a name="overview"></a>

The following sections provide information about server-level and database-level auditing, auditing processes, benefits, and disadvantages.

## Auditing levels
<a name="auditing-levels"></a>

Auditing can be performed at the SQL Server level, at the database level (which involves logging the events associated with actions), or at both levels.

### Server-level auditing
<a name="server-level-auditing.9d0cfcbd-dd64-5287-a6bf-3c04f3c3071a"></a>

You can use the SQL Server Audit object to audit and collect actions to monitor. You can specify a single instance of server-level actions and groups of actions. You can also create multiple audits for each SQL Server instance.

SQL Server level auditing involves server-level configuration parameters such as [xp\_cmdshell](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/xp-cmdshell-server-configuration-option?view=sql-server-ver16) and [max server memory](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/server-memory-server-configuration-options?view=sql-server-ver16#max_server_memory).  For more information about server memory configurations, see the [Microsoft SQL Server documentation](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/server-memory-server-configuration-options?view=sql-server-ver16).

### Database-level auditing
<a name="database-level-auditing.cd4623ef-328c-537d-a2c3-22db49413dbd"></a>

Database-level auditing involves capturing the actions of database users for security purposes. For example, you can use database-level auditing to ensure that unauthorized users and processes cannot access the database, and to verify that rules are applied to restrict any unauthorized activities. Examples of database-level auditing include capturing all `INSERT`, `UPDATE`, `DELETE`, and `TRIGGERS` operations on the database.

This guide provides instructions and examples of both auditing levels.

## Flow chart
<a name="flow-chart"></a>

The following flow chart illustrates the SQL Server auditing process. When a user or process logs in to the database system, their login credentials are validated. If the login is valid, the audit process checks for authorization. If the user or process is authorized to perform the action, they can complete the action, and the audited data is logged in the database audit table.

![Auditing flowchart for SQL Server database instances](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-auditing-on-aws/images/guide-img/c5879391-b7a1-4ebd-9427-8f0779ed8c01/images/9358622d-3cf3-4cdb-953e-add2e788893b.png)

## Advantages and disadvantages of auditing
<a name="pros-cons"></a>

### Advantages
<a name="advantages.d3c52c2e-13a6-5c13-9090-cf867df1066a"></a>
+ Helps reduce security violation incidents or any other actions that might result in an unauthorized disclosure of classified information.
+ Helps identify security gaps and vulnerabilities, including illicit access to database resources, data, or operations.
+ Provides an audit trail of activities so you can verify and track all types of transactions and processes, and trace queries to analyze performance.
+ Makes organizations more accountable, because they can review tracked audit information and provide feedback to meet security goals and performance objectives.

### Disadvantages
<a name="disadvantages.1f59dbe2-1514-57b5-a662-b411c5ac22bf"></a>
+ In general, performance impact is minimal. However, if auditing involves a high volume of transaction tracking, it can require additional resources.
+ Might generate too many reports and documents to view, and might require providing feedback to multiple management and security teams.
+ Consumption of storage resources to store the audit files might be high.
+ Additional maintenance is required to archive or purge old audit data, or to move tables to different database file groups or storage.
