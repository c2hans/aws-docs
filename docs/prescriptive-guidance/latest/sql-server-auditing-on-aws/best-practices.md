---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-auditing-on-aws/best-practices.html
---

# Best practices for auditing SQL Server on AWS
<a name="best-practices"></a>

When you audit SQL Server databases on AWS, follow these best practices.
+ **Understand audit requirements.** Check if the audit solution has to meet compliance requirements such as GDPR or HIPAA. For example, the audit solution might have to track and log all changes performed on critical data such as PII and financial information.
+ **Define the audit scope.** Decide if you need to audit all SQL Server instances or only specific instances that host critical databases. At the database level, determine whether you need to audit all tables or only tables that contain critical data.
+ **Identify the list of events that you want to track and log.** For example, your audit list might include login failures, login permission changes, new logins and users, and deleted logins and users.
+ **Choose the right audit tool.** For example, if you want to audit only login and logout events, you can use an error log or extended events. If you want to audit data manipulation language (DML) changes, use change data capture (CDC), change tracking, or temporal tables. If you want to audit changes at the instance and database level, use the SQL Server audit feature. Or you can use a third-party audit tool such as [ApexSQL Audit](https://www.apexsql.com/products/sql-tools-audit/).
+ **Set up real-time alerts** to proactively notify the DBAs or the security team when a specific action doesn't meet compliance requirements.
+ **Review audit data periodically** by creating a simple dashboard or a report that reads the audit data and filters the actions that you are interested in.
+ **Set up an alert** to monitor the changes performed on the auditing solution.
+ **Define retention policies** for the audit data based on your company's requirements, and archive the old audit data.
