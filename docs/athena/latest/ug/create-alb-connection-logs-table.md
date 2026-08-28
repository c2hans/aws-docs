---
source_url: https://docs.aws.amazon.com/athena/latest/ug/create-alb-connection-logs-table.html
---

# Create the table for ALB connection logs
<a name="create-alb-connection-logs-table"></a>

1. Copy and paste the following example `CREATE TABLE` statement into the query editor in the Athena console, and then modify it as necessary for your own log entry requirements. For information about getting started with the Athena console, see [Get started](getting-started.md). Replace the path in the `LOCATION` clause with your Amazon S3 connection log folder location. For more information about connection log file location, see [Connection log files](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-connection-logs.html#connection-log-file-format) in the *User Guide for Application Load Balancers*. For information about each log file field, see [Connection log entries](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-connection-logs.html#connection-log-entry-format).

   ```
   CREATE EXTERNAL TABLE IF NOT EXISTS alb_connection_logs (
            time string,
            client_ip string,
            client_port int,
            listener_port int,
            tls_protocol string,
            tls_cipher string,
            tls_handshake_latency double,
            leaf_client_cert_subject string,
            leaf_client_cert_validity string,
            leaf_client_cert_serial_number string,
            tls_verify_status string,
            conn_trace_id string
            )
            ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
            WITH SERDEPROPERTIES (
            'serialization.format' = '1',
            'input.regex' =
             '([^ ]*) ([^ ]*) ([0-9]*) ([0-9]*) ([A-Za-z0-9.-]*) ([^ ]*) ([-.0-9]*) \"([^\"]*)\" ([^ ]*) ([^ ]*) ([^ ]*) ?([^ ]*)?( .*)?'
            )
            LOCATION 's3://amzn-s3-demo-bucket/{{connection-log-folder-path}}/'
   ```

1. Run the query in the Athena console. After the query completes, Athena registers the `alb_connection_logs` table, making the data in it ready for you to issue queries.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
