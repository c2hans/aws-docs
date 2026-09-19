---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/amazon-rdsaurora-logs.html
---

# Amazon RDS/Aurora logs
<a name="amazon-rdsaurora-logs"></a>

You can [publish database instance logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Procedural.UploadtoCloudWatch.html). Then, you can perform real-time analysis of the log data, store the data in highly durable storage, and manage the data with the CloudWatch Logs Agent.

Prerequisites

Make sure your database logs are enabled. Some databases logs are not enabled by default, and you must update your database parameters to enable the logs.

Refer to [How do I enable and monitor logs for an Amazon RDS MySQL DB instance?](https://aws.amazon.com/premiumsupport/knowledge-center/rds-mysql-logs/) to learn how to output logs to CloudWatch Logs.

The following table lists the requirements for Amazon RDS/Aurora MySQL parameters.

| Parameter | Requirement |
| --- | --- |
| Audit Log | The database instance must use a custom option group with the MARIADB\_AUDIT\_PLUGIN option. |
| General log | The database instance must use a custom parameter group with the parameter setting general\_log = 1 to enable the general log. |
| Slow query log | The database instance must use a custom parameter group with the parameter setting slow\_query\_log = 1 to enable the slow query log. |
| Log output | The database instance must use a custom parameter group with the parameter setting log\_output = FILE to write logs to the file system and publish them to CloudWatch Logs. |

You can create a log ingestion into Amazon OpenSearch Service either by using the Centralized Logging with OpenSearch console or by deploying a standalone CloudFormation stack.

**Important**
The Amazon RDS and CloudWatch Region must be the same as the Centralized Logging with OpenSearch solution Region.
The Amazon OpenSearch Service index is rotated on a daily basis by default, and you can adjust the index in the Additional Settings.

## Create log ingestion (OpenSearch Engine)
<a name="create-log-ingestion-opensearch-engine-2"></a>

### Using the Centralized Logging with OpenSearch Console
<a name="using-the-centralized-logging-with-opensearch-console-3"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose the Create a log ingestion button.

1. In the **AWS Services** section, choose **Amazon RDS**.

1. Choose **Next**.

1. Under **Specify settings**, choose **Automatic** or **Manual** for **RDS log enabling**. The automatic mode will detect your Amazon RDS log configurations and ingest logs from CloudWatch.
   + For **Automatic mode**, choose the Amazon RDS cluster from the dropdown list.
   + For **Manual mode**, enter the **DB identifier**, select the **Database type** and input the CloudWatch log location in **Log type and location**.
   + (Optional) If you are ingesting Amazon RDS/Aurora logs from another account, select a [linked account](cross-account-ingestion.md#add-a-member-account) from the **Account** dropdown first.

1. Choose **Next**.

1. In the Specify OpenSearch domain section, select an imported domain for the Amazon OpenSearch Service domain.

1. Choose **Yes** for **Sample dashboard** if you want to ingest an associated templated Amazon OpenSearch Service dashboard.

1. You can change the **Index Prefix** of the target Amazon OpenSearch Service index if needed. The default prefix is the Database identifier.

1. In the **Log Lifecycle** section, input the number of days to manage the Amazon OpenSearch Service index lifecycle. The Centralized Logging with OpenSearch will create the associated [Index State Management (ISM)](https://opensearch.org/docs/latest/im-plugin/ism/index/) policy automatically for this pipeline.

1. In the **Log processor settings** section, choose **Log processor type**, configure the Lambda concurrency if needed, and then choose **Next**.

1. Add tags if needed.

1. Choose **Create**.

### Using the CloudFormation Stack
<a name="using-the-cloudformation-stack-3"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - RDS Log Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/RDSLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/RDSLog.template)  |
| AWS China Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/RDSLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/RDSLog.template)  |

1. Log in to the AWS Management Console and select the button to launch the AWS CloudFormation template. You can also download the template as a starting point for your own implementation.

1. To launch the Centralized Logging with OpenSearch in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Log Bucket Name</td><td> {{&lt;Requires input&gt;}} </td><td>The S3 bucket name to export the logs.</td></tr>
  <tr><td>Log Bucket Prefix</td><td> {{&lt;Requires input&gt;}} </td><td>The S3 bucket path prefix that stores the logs.</td></tr>
  <tr><td>Log Source Account ID</td><td> <i>Optional input</i> </td><td>The AWS Account ID of the CloudWatch log group. Required for cross-account log ingestion (Please <a href="cross-account-ingestion.md#add-a-member-account">add a member account</a> first). By default, the Account ID you logged in at <b>Step 1</b> will be used.</td></tr>
  <tr><td>Log Source Region</td><td> <i>Optional input</i> </td><td>The AWS Region of the CloudWatch log group. By default, the Region you selected at <b>Step 2</b> will be used.</td></tr>
  <tr><td>Log Source Account Assume Role</td><td> <i>Optional input</i> </td><td>The IAM Role ARN used for cross-account log ingestion. Required for cross-account log ingestion (<a href="cross-account-ingestion.md#add-a-member-account">add a member account</a> first).</td></tr>
  <tr><td>KMS-CMK ARN</td><td> <i>Optional input</i> </td><td>The KMS-CMK ARN for Amazon SQS encryption. Leave it blank to create a new AWS KMS key.</td></tr>
  <tr><td>Enable OpenSearch Ingestion as processor</td><td> <i>Optional input</i> </td><td>Ingestion table ARN. Leave empty if you do not use OSI as Processor.</td></tr>
  <tr><td>Log Group Names</td><td> {{&lt;Requires input&gt;}} </td><td>The names of the CloudWatch log group for the logs.</td></tr>
  <tr><td>Amazon S3 Backup Bucket</td><td> {{&lt;Requires input&gt;}} </td><td>The Amazon S3 backup bucket name to store the failed ingestion logs.</td></tr>
  <tr><td>Engine Type</td><td> <code>OpenSearch</code> </td><td>The engine type of the OpenSearch.</td></tr>
  <tr><td>OpenSearch Domain Name</td><td> {{&lt;Requires input&gt;}} </td><td>The domain name of the Amazon OpenSearch Service cluster.</td></tr>
  <tr><td>OpenSearch Endpoint</td><td> {{&lt;Requires input&gt;}} </td><td>The OpenSearch endpoint URL. For example, vpc-your_opensearch_domain_name-xcvgw6uu2o6zafsiefxubwuohe.us-east-1.es.amazonaws.com</td></tr>
  <tr><td>Index Prefix</td><td> {{&lt;Requires input&gt;}} </td><td>The common prefix of OpenSearch index for the log. The index name will be &lt;Index Prefix&gt;-&lt;Log Type&gt;-&lt;Other Suffix&gt;.</td></tr>
  <tr><td>Create Sample Dashboard</td><td> <code>Yes</code> </td><td>Whether to create a sample OpenSearch dashboard.</td></tr>
  <tr><td>VPC ID</td><td> {{&lt;Requires input&gt;}} </td><td>Select a VPC that has access to the OpenSearch domain. The log processing Lambda will be resides in the selected VPC.</td></tr>
  <tr><td>Subnet IDs</td><td> {{&lt;Requires input&gt;}} </td><td>Select at least two subnets that has access to the OpenSearch domain. The log processing Lambda function will reside in the subnets. Please make sure that the subnetshas access to the Amazon S3 service.</td></tr>
  <tr><td>Security Group ID</td><td> {{&lt;Requires input&gt;}} </td><td>Select a Security Group that will be associated to the log processing Lambda. Please make sure that the Security Group has access to the OpenSearch domain.</td></tr>
  <tr><td>Number Of Shards</td><td> <code>5</code> </td><td>Number of shards to distribute the index evenly across all data nodes. Keep the size of each shard between 10-50 GiB.</td></tr>
  <tr><td>Number of Replicas</td><td> <code>1</code> </td><td>Number of replicas for OpenSearch Index. Each replica is a full copy of an index.</td></tr>
  <tr><td>Age to Warm Storage</td><td> <i>Optional input</i> </td><td>The age required to move the index into warm storage (for example, 7d). Index age is the time between its creation and the present. Supported units are d (days) and h (hours). This is only effective when warm storage is enabled in OpenSearch.</td></tr>
  <tr><td>Age to Cold Storage</td><td> <i>Optional input</i> </td><td>The age required to move the index into cold storage (for example, 30d). Index age is the time between its creation and the present. Supported units are d (days) and h (hours). This is only effective when cold storage is enabled in OpenSearch.</td></tr>
  <tr><td>Age to Retain</td><td> <i>Optional input</i> </td><td>The age to retain the index (for example, 180d). Index age is the time between its creation and the present. Supported units are d (days) and h (hours). If the value is "", the index will not be deleted.</td></tr>
  <tr><td>Rollover Index Size</td><td> <i>Optional input</i> </td><td>The minimum size of the shard storage required to roll over the index (for example, 30GB).</td></tr>
  <tr><td>Index Suffix</td><td> <code>yyyy-MM-dd</code> </td><td>The common suffix format of OpenSearch index for the log(Example: yyyy-MM-dd, yyyy-MM-dd-HH). The index name will be &lt;Index Prefix&gt;-&lt;Log Type&gt;-&lt;Index Suffix&gt;-000001.</td></tr>
  <tr><td>Compression type</td><td> <code>best_compression</code> </td><td>The compression type to use to compress stored data. Available values are best_compression and default.</td></tr>
  <tr><td>Refresh Interval</td><td> <code>1s</code> </td><td>How often the index should refresh, which publishes its most recent changes and makes them available for searching. Can be set to -1 to disable refreshing. Default is 1s.</td></tr>
  <tr><td>EnableS3Notification</td><td> <code>True</code> </td><td>An option to enable or disable notifications for Amazon S3 buckets. The default option is recommended for most cases.</td></tr>
  <tr><td>LogProcessorRoleName</td><td> <i>Optional input</i> </td><td>Specify a role name for the log processor. The name should NOT duplicate an existing role name. If no name is specified, a random name is generated.</td></tr>
  <tr><td>QueueName</td><td> <i>Optional input</i> </td><td>Specify a queue name for an Amazon SQS queue. The name should NOT duplicate an existing queue name. If no name is given, a random name will be generated.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 15 minutes.

### View dashboard
<a name="view-dashboard-3"></a>

The dashboard includes the following visualizations.

| Visualization Name | Source Field | Description |
| --- | --- | --- |
| Controller | \* db-identifier \* sq-table-name | This visualization allows users to filter data based on the db-identifier and sq-table-name fields. |
| Total Log Events Overview | \* db-identifier \* log event | This visualization presents an overview of the total log events for the specified database ('db-identifier'). It helps monitor the frequency of various log events. |
| Slow Query History | \* log event | This visualization shows the historical data of slow query log events. It allows you to track the occurrences of slow queries and identify potential performance issues. |
| Average Slow Query Time History | \* Average sq-duration | This visualization depicts the historical trend of the average duration of slow queries ('sq-duration'). It helps in understanding the database’s performance over time and identifying trends related to slow query durations. |
| Total Slow Queries | \* log event | This visualization provides the total count of slow queries in the log events. It gives an immediate view of how many slow queries have occurred during a specific time period, which is useful for assessing the database’s performance and potential bottlenecks. |
| Average Slow Query Duration | \* Average sq-duration | This visualization shows the average duration of slow queries ('sq-duration') over time. It is valuable for understanding the typical performance of slow queries in the database. |
| Top Slow Query IP | \* sq-ip \* sq-duration | This visualization highlights the IP addresses ('sq-ip') associated with the slowest queries and their respective durations ('sq-duration'). It helps identify sources of slow queries and potential areas for optimization. |
| Slow Query Scatter Plot | \* sq-duration \* sq-ip \* sq-query | This scatter plot visualization represents the relationship between the duration of slow queries ('sq-duration'), the IP addresses ('sq-ip') from which they originated, and the actual query content ('sq-query'). It helps in understanding query performance patterns and identifying potential issues related to specific queries and their sources. |
| Slow Query Pie | \* sq-query | This pie chart visualization shows the distribution of slow queries based on their content ('sq-query'). It provides an overview of the types of queries causing performance issues, allowing you to focus on optimizing specific query patterns. |
| Slow Query Table Name Pie | \* sq-table-name | This pie chart visualization displays the distribution of slow queries based on the table names ('sq-table-name') they access. It helps identify which tables are affected by slow queries, enabling targeted optimization efforts for specific tables. |
| Top Slow Query | \* sq-query | This visualization presents the slowest individual queries based on their content ('sq-query'). It is helpful in pinpointing specific queries that have the most significant impact on performance, allowing developers and administrators to focus on optimizing these critical queries. |
| Slow Query Logs | \* db-identifier \* sq-db-name \* sq-table-name \* sq-query \* sq-ip \* sq-host-name \* sq-rows-examined \* sq-rows-sent \* sq-id \* sq-duration \* sq-lock-wait | This visualization provides detailed logs of slow queries, including database ('sq-db-name'), table ('sq-table-name'), query content ('sq-query'), IP address ('sq-ip'), hostname ('sq-host-name'), rows examined ('sq-rows-examined'), rows sent ('sq-rows-sent'), query ID ('sq-id'), query duration ('sq-duration'), and lock wait time ('sq-lock-wait'). It is beneficial for in-depth analysis and troubleshooting of slow query performance. |
| Total Deadlock Queries | \* log event | This visualization shows the total number of deadlock occurrences based on the log events. Deadlocks are critical issues that can cause database transactions to fail, and monitoring their frequency is essential for database stability. |
| Deadlock History | \* log event | This visualization displays the historical data of deadlock occurrences based on the log events. Understanding the pattern of deadlocks over time can help identify recurring issues and take preventive measures to reduce their impact on the database. |
| Deadlock Query Logs | \* db-identifier \* log-detail \* deadlock-ip-1 \* deadlock-action-1 \* deadlock-os-thread-handle-1 \* deadlock-query-1 \* deadlock-query-id-1 \* deadlock-thread-id-1 \* deadlock-user-1 \* deadlock-action-2 \* deadlock-ip-2 \* deadlock-os-thread-handle-2 \* deadlock-query-2 \* deadlock-query-id-2 \* deadlock-thread-id-2 \* deadlock-user-2 | This visualization provides detailed logs of deadlock occurrences |
| Total Error Logs | \* log event | This visualization presents the total count of error log events. Monitoring error logs helps identify database issues and potential errors that need attention and resolution. |
| Error History | \* log event | This visualization shows the historical data of error log events. Understanding the error patterns over time can aid in identifying recurring issues and taking corrective actions to improve the database’s overall health and stability. |
| Error Logs | \* db-identifier \* err-label \* err-code \* err-detail \* err-sub-system \* err-thread | This visualization displays the error logs generated by the Amazon RDS instance. It provides valuable insights into any errors, warnings, or issues encountered within the database system, helping to identify and troubleshoot problems effectively. Monitoring error logs is essential for maintaining the health and reliability of the database. |
| Audit History | \* log event | This visualization presents the audit history of the Amazon RDS instance. It tracks the various log events and activities related to database access, modifications, and security-related events. Monitoring the audit logs is crucial for compliance, detecting unauthorized access, and tracking changes made to the database. |
| Audit Logs | \* db-identifier \* audit-operation \* audit-ip \* audit-query \* audit-retcode \* audit-connection-id \* audit-host-name \* audit-query-id \* audit-user | This visualization provides an overview of the audit logs generated by the Amazon RDS instance. It shows the operations performed on the database, including queries executed, connection details, IP addresses, and associated users. Monitoring audit logs enhances the security and governance of the database, helping to detect suspicious activities and track user actions. |

You can access the built-in dashboard in Amazon OpenSearch Service to view log data. For more information, see the [Access Dashboard](getting-started.md#step-4-access-the-dashboard).

 **Amazon RDS/Aurora logs sample dashboard.**

![image35](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image35.png)

## Create log ingestion (Light Engine)
<a name="create-log-ingestion-light-engine-1"></a>

### Using the Centralized Logging with OpenSearch Console
<a name="using-the-centralized-logging-with-opensearch-console-4"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose the Create a log ingestion button.

1. In the **AWS Services** section, choose **Amazon RDS**.

1. Choose **Light Engine**, choose **Next**.

1. Under **Specify settings**, choose **Automatic** or **Manual** for **RDS log enabling**. The automatic mode will detect your Amazon RDS log configurations and ingest logs from CloudWatch.
   + For **Automatic mode**, choose the Amazon RDS cluster from the dropdown list.
   + For **Manual mode**, enter the **DB identifier**, select the **Database type** and input the CloudWatch log location in **Log type and location**.
   + (Optional) If you are ingesting Amazon RDS/Aurora logs from another account, select a [linked account](cross-account-ingestion.md#add-a-member-account) from the **Account** dropdown first.

1. Choose **Next**.

1. In the **Specify Light Engine Configuration** section, if you want to ingest associated templated Grafana dashboards, select **Yes** for the sample dashboard.

1. You can choose an existing Grafana, or if you must import a new one, you can go to Grafana for configuration.

1. Select an S3 bucket to store partitioned logs and define a name for the log table. We have provided a predefined table name, but you can modify it according to your business needs.

1. If needed, change the log processing frequency, which is set to **5** minutes by default, with a minimum processing frequency of **1** minute.

1. In the **Log Lifecycle** section, enter the log merge time and log archive time. We have provided default values, but you can adjust them based on your business requirements.

1. Select **Next**.

1. If desired, add tags.

1. Select **Create**.

### Using the CloudFormation Stack
<a name="using-the-cloudformation-stack-4"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - RDS Log Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesRDSPipeline.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesRDSPipeline.template)  |
| AWS China Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesRDSPipeline.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesRDSPipeline.template)  |

1. Log in to the AWS Management Console and select the preceding button to launch the AWS CloudFormation template. You can also download the template as a starting point for your own implementation.

1. To launch the stack in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.

   1. Parameters for **Pipeline settings**

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Pipeline Id</td><td> {{&lt;Requires input&gt;}} </td><td>The unique identifier for the pipeline is essential if you must create multiple Application Load Balancer pipelines and write different Application Load Balancer logs into separate tables. For uniqueness, you can generate a unique pipeline identifier using <a href="https://www.uuidgenerator.net/version4">uuidgenerator</a>.</td></tr>
  <tr><td>Staging Bucket Prefix</td><td> <code>AWSLogs/RDS</code> </td><td>The storage directory for logs in the temporary storage area should ensure the uniqueness and non-overlapping of the Prefix for different pipelines.</td></tr>
</tbody>
</table>

   1. Parameters for **Destination settings**

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Centralized Bucket Name</td><td> {{&lt;Requires input&gt;}} </td><td>Centralized S3 bucket name. For example, centralized-logging-bucket.</td></tr>
  <tr><td>Centralized Bucket Prefix</td><td> <code>datalake</code> </td><td>Centralized bucket prefix. By default, the data base location is s3://{Centralized Bucket Name}/{Centralized Bucket Prefix}/amazon_cl_centralized.</td></tr>
  <tr><td>Centralized Table Name</td><td> <code>rds</code> </td><td>Table name for writing data to the centralized database. You can modify it if needed.</td></tr>
</tbody>
</table>

   1. Parameters for **Scheduler settings**

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>LogProcessor Schedule Expression</td><td> <code>rate(5 minutes)</code> </td><td>Task scheduling expression for performing log processing, with a default value of executing the LogProcessor every 5 minutes. Configuration <a href="https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html">for reference</a>.</td></tr>
  <tr><td>LogMerger Schedule Expression</td><td> <code>cron(0 1 * ? )</code> </td><td>Task scheduling expression for performing log merging, with a default value of executing the LogMerger at 1 AM every day. Configuration <a href="https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html">for reference</a>.</td></tr>
  <tr><td>LogArchive Schedule Expression</td><td> <code>cron(0 2 * ? )</code> </td><td>Task scheduling expression for performing log archiving, with a default value of executing the LogArchive at 2 AM every day. Configuration <a href="https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html">for reference</a>.</td></tr>
  <tr><td>Age to Merge</td><td> <code>7</code> </td><td>Small file retention days, with a default value of 7, indicating that logs older than 7 days will be merged into small files. It can be adjusted as needed.</td></tr>
  <tr><td>Age to Archive</td><td> <code>30</code> </td><td>Log retention days, with a default value of 30, indicating that data older than 30 days will be archived and deleted. It can be adjusted as needed.</td></tr>
</tbody>
</table>

   1. Parameters for **Notification settings**

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Notification Service</td><td> <code>SNS</code> </td><td>Notification method for alerts. If your main stack is using China, you can only choose the SNS method. If your main stack is using Global, you can choose either the SNS or SES method.</td></tr>
  <tr><td>Recipients</td><td> {{&lt;Requires input&gt;}} </td><td>Alert notification: If the Notification Service is SNS, enter the SNS Topic ARN here, ensuring that you have the necessary permissions. If the Notification Service is SES, enter the email addresses separated by commas here, ensuring that the email addresses are already Verified Identities in SES. The adminEmail provided during the creation of the main stack will receive a verification email by default.</td></tr>
</tbody>
</table>

   1. Parameters for **Dashboard settings**

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Import Dashboards</td><td> <code>FALSE</code> </td><td>Whether to import the Dashboard into Grafana, with a default value of false. If set to true, you must provide the Grafana URL and Grafana Service Account Token.</td></tr>
  <tr><td>Grafana URL</td><td> {{&lt;Requires input&gt;}} </td><td>Grafana access URL，for example: https://alb-72277319.us-west-2.elb.amazonaws.com.</td></tr>
  <tr><td>Grafana Service Account Token</td><td> {{&lt;Requires input&gt;}} </td><td>Grafana Service Account Token Service Account Token created in Grafana.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-4"></a>

 **Amazon RDS/Aurora logs sample dashboard.**

![image36](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image36.jpeg)
