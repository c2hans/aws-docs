---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-auditing-on-aws/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to frequently asked questions about auditing SQL Server on Amazon RDS and Amazon EC2.

## What are the main components of the SQL Server audit feature?
<a name="what-are-the-main-components-of-the-sql-server-audit-feature-.0b882523-6cc5-590f-9e69-1515f145b1a0"></a>

The SQL Server audit feature has three main components:
+ **SQL Server Audit objects** define the path to store the audit information, the auditing synchronization mode, the audit file rollover mechanism, and the action to be performed in case of audit failures.
+ **Server audit specifications**track and log the changes that are performed at the SQL Server instance level and events that are raised by the SQL Server Extended Events feature.
+ **Database audit specifications** track and log different types of actions that are performed at the database level and events that are raised by the SQL Server Extended Events feature.

## What are some critical events I should consider auditing?
<a name="what-are-some-critical-events-i-should-consider-auditing-.e6d6216f-f10b-598b-98a0-768483cf2199"></a>

Critical events include failed logins, login changes, user changes, schema changes, and audit changes.

## Why is it important to audit failed logins, login changes, and user changes?
<a name="why-is-it-important-to-audit-failed-logins--login-changes--and-user-changes-.8265a6da-98f8-5f6b-8076-5c5e51e059cc"></a>

For example, excessive failed login attempts or user permission changes might signal that an attack is in progress.

## Why is it important to audit schema changes?
<a name="why-is-it-important-to-audit-schema-changes-.ba0372aa-dde5-5bb1-a073-4a3a6074b3dc"></a>

We recommend that you track all database schema changes to detect any changes that weren't authorized.

## Why is it important to audit the auditing system?
<a name="why-is-it-important-to-audit-the-auditing-system-.b6b7e9e1-5c68-53af-bb59-975258925992"></a>

Auditing the changes in your SQL Server auditing solution helps you catch unauthorized users who might be trying to disable the auditing process to perform non-compliant or illegal activities. This audit also helps you meet auditor requirements for the integrity of audit solution logs by providing evidence that covers all scenarios. Another simple use for this audit is to remind the database administrator to reenable the audit in case it was disabled for maintenance purposes.

## How can I use triggers to audit database changes?
<a name="how-can-i-use-triggers-to-audit-database-changes-.b1ddb77a-cc9f-587d-b673-59eae3f15ab9"></a>

You can create triggers on tables that contain critical data to log modified or inserted data, and to compare the data before and after the modification. You can use the `INSTEAD OF` trigger to prevent changes on a specific table and to log the failed action.

## What are the advantages and disadvantages of using CDC to audit database changes? Which versions support CDC?
<a name="what-are-the-advantages-and-disadvantages-of-using-cdc-to-audit-database-changes--which-versions-support-cdc-.e07b586a-b287-560d-9c09-b465bb995c6f"></a>

Change data capture (CDC) is supported in all editions of SQL Server 2016 and later. In earlier versions, only the Enterprise edition supports CDC.

Here are some of the advantages of using CDC to audit database changes:
+ You can use CDC as an asynchronous SQL Server audit solution, to track data manipulation language (DML) operations on tables.
+ CDC tracks `INSERT`, `UPDATE`, and `DELETE` operations on database tables, and records detailed information about these changes in mirrored tables.
+ CDC depends on the SQL Server transaction log as the source of data changes.
+ You can easily configure CDC by using Transact-SQL commands.

Disadvantages:
+ CDC doesn't handle data definition language (DDL) changes on CDC-enabled tables automatically. It requires extra effort to reflect DDL changes in the tracking table.
+ CDC provides no option to track the `SELECT` statement.
+ SQL Server keeps CDC tracking data in the change table for only a configurable number of days.
+ CDC jobs will not work unless the SQL Server agent service is running.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
