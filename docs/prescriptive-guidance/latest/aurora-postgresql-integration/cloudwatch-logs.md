---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-postgresql-integration/cloudwatch-logs.html
---

# Aurora PostgreSQL-Compatible integration with CloudWatch Logs
<a name="cloudwatch-logs"></a>

Amazon CloudWatch Logs is a log-management service for collecting, monitoring, and analyzing logs from various AWS services. You can stream Amazon Aurora PostgreSQL-Compatible Edition logs, including error logs, slow-query logs, and audit logs, to CloudWatch Logs. You can centralize and monitor your database logs in real time, which makes identifying and troubleshooting issues easier.

You can monitor the logs by using AWS Management Console, or you can query the logs by using the `log_fdw` extension. The `log_fdw` extension supports querying and analyzing PostgreSQL log files directly from within the database. This helps you to gain insights into database performance, troubleshoot issues, and proactively identify potential problems.

To set up `log_fdw` integration with CloudWatch Logs, use the following high-level steps:

1. Connect to your Aurora PostgreSQL-Compatible cluster by using a PostgreSQL client, and create the `log_fdw` extension:

   ```
   CREATE EXTENSION log_fdw;
   ```

   This extension provides the functionality to connect to CloudWatch Logs.

1. Create a log server named `log_server` that points to the directory where PostgreSQL log files are stored. The default location for Aurora PostgreSQL-Compatible log files is `/rdsdbdata/log/`:

   ```
   CREATE SERVER log_server FOREIGN DATA WRAPPER log_fdw OPTIONS (log_directory '/rdsdbdata/log/');
   ```

   For more information about publishing log files from Aurora PostgreSQL-Compatible to CloudWatch Logs, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.CloudWatch.html).

1. To list all the available log files that can be accessed through the `log_fdw` extension, run the following query:

   ```
   SELECT * FROM log_file_list('log_server');
   ```

1. To create a foreign table `log_table` that maps to the `postgres.log` file, run the following command:

   ```
   SELECT create_foreign_table_for_log_file('log_table', 'log_server', 'postgres.log');
   ```

   The table columns correspond to the fields that are present in the PostgreSQL log file format.

1. You can now query the log data as if it were a regular table, filtering and analyzing the log entries based on your requirements:

   ```
   SELECT * FROM log_table
   ```

## Cleanup
<a name="cleanup"></a>

To clean up the created objects, including dropping the `log_fdw` extension, server, and foreign tables, run the following commands:

```
DROP FOREIGN TABLE log_table;
DROP SERVER log_server;
DROP EXTENSION log_fdw;
```
