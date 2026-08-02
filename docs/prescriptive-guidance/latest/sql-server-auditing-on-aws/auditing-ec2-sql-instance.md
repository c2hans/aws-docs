---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-auditing-on-aws/auditing-ec2-sql-instance.html
---

# Auditing SQL Server on Amazon EC2 or Amazon RDS Custom DB instances
<a name="auditing-ec2-sql-instance"></a>

This section provides information about auditing options for SQL Server on Amazon EC2 and Amazon RDS Custom, including creating server and database audits, viewing audit logs, and monitoring results.

## Prerequisites
<a name="ec2-prerequisites"></a>
+ Database login with `ALTER ANY SERVER AUDIT` or `CONTROL SERVER` permission

## Supported versions
<a name="ec2-versions"></a>
+ Any edition of SQL Server version 2016 and later

## Using C2 audit mode
<a name="ec2-c2"></a>

C2 audit mode audits events such as user logins, stored procedure calls, and creation and deletion of objects. This mode can generate lot of data because it audits everything or nothing. C2 audit logs are stored in the default data directory of the SQL Server instance. Each log file can be a maximum of 200 MB. A new file is automatically created when this limit is reached. You can enable C2 auditing by using SQL Server Management Studio. For more information, see the [Microsoft SQL Server documentation](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/c2-audit-mode-server-configuration-option).

**Important**
Microsoft plans to remove C2 audit mode in a future version of SQL Server. We recommend that you avoid using this feature.

To use C2 audit mode to audit failed logins:

1. In SQL Server Management Studio, connect to the SQL Server instance that you want to enable auditing for.

1. Select the SQL Server instance, right-click and choose **Properties**, and then choose **Security**.

1. For **Login auditing**, choose a configuration option. You can audit failed logins only, successful logins only, both, or none. (The default is failed logins only.)

1. For **Options**, select **Enable C2 audit tracing**.

## Creating and viewing audits
<a name="ec2-creating-viewing"></a>

### Creating server audits
<a name="creating-server-audits.9b67b78b-eb60-5c94-845b-cafa2104b67e"></a>

A server audit in SQL Server collects instance-level or database-level actions to monitor. Audit output is saved to an audit destination file path, a Windows security log, or an application log.

To create a server audit:

1. In SQL Server Management Studio, in Object Explorer, expand **Security**, right-click **Audits**, and then choose **New Audit. **This creates a new SQL Server Audit object for server-level auditing.

1. For **Audit destination**, choose a file, a security log, or an application log.

1. If you selected a file as the target, specify the location of the folder.

1. Configure other options, and then choose **OK**.

1. To enable the audit, right-click the new audit configuration, and then choose **Enable Audit**.

For more information, see the [Microsoft SQL Server documentation](https://learn.microsoft.com/en-us/sql/relational-databases/security/auditing/create-a-server-audit-and-server-audit-specification).

### Creating server audit specifications
<a name="creating-server-audit-specifications.768d5e3c-eaff-5888-a5dd-704853a439e5"></a>

The server audit specification collects many server-level action groups raised by the SQL Server Extended Events feature. You can include audit action groups in a server audit specification. These actions are sent to the audit that records them in the target file or log.

To create a server audit specification:

1. In SQL Server Management Studio, in Object Explorer, expand **Security**, right-click **Server Audit Specifications**, and then choose **New Server Audit Specification.**

1. For **Audit**, choose the server audit you created earlier.

1. For **Actions**, choose the audit action type that specifies the server-level audit action groups and audit actions that you want to capture, and then choose **OK**.

1. To enable the server audit specification, right-click the new specification, and then choose **Enable Server Audit Specification.**

For more information, see [Create a Server Audit and Server Audit Specification](https://learn.microsoft.com/en-us/sql/relational-databases/security/auditing/create-a-server-audit-and-server-audit-specification) and [SQL Server Audit Action Groups and Actions](https://learn.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions) in the Microsoft SQL Server documentation.

### Creating database audit specifications
<a name="creating-database-audit-specifications.59f952e8-48d8-5424-9a52-a77cf337c57b"></a>

You can create a database audit specification object for database-level auditing. This specification specifies the database-level audit action groups and audit actions to capture.

To create a database audit specification:

1. In SQL Server Management Studio, in Object Explorer, expand the database that you want to audit.

1. Expand the Security folder, right-click **Database Audit Specifications,** and then choose **New Database Audit Specification.**

1. For **Actions**, configure one or more database audit action types. Select the statements that you want to audit (such as DELETE or INSERT) and the object class to perform the action on.

1. When your selections are complete, choose **OK**.

1. To enable the database audit specification, right-click the new specification, and then choose **Enable Database Audit Specification.**

For more information, see [Create a server audit and database audit specification](https://learn.microsoft.com/en-us/sql/relational-databases/security/auditing/create-a-server-audit-and-database-audit-specification) and [SQL Server Audit Action Groups and Actions](https://learn.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions) in the Microsoft SQL Server documentation.

### Viewing SQL Server audit logs
<a name="viewing-sql-server-audit-logs.2dc9ad6c-d80c-5e0f-aac2-3d3d6d054f4f"></a>

To view audit logs:

1. In SQL Server Management Studio, right-click the SQL Server Audit object, and then choose **View Audit Logs**.

   The Log File Viewer displays the audit log regardless of its location (a file or the Windows Event Log).

1. To customize the log entries that are displayed, choose **Filter**.

1. To export the log to a log file, choose **Export**.

1. When you've finished viewing the log, choose **Close**.

For more information, see the [Microsoft SQL Server documentation](https://learn.microsoft.com/en-us/sql/relational-databases/security/auditing/view-a-sql-server-audit-log).

## Monitoring
<a name="ec2-monitoring"></a>

You can monitor audit logs that are logged to an audit file, an application or security event log, or an audit table in the database by using monitoring solutions such as [Nagios](https://www.nagios.com/solutions/mssql-monitoring/). A monitoring solution that's integrated with a ticketing or alerting mechanism can generate real-time alerts and incidents to notify the systems administrator or database administrator.
