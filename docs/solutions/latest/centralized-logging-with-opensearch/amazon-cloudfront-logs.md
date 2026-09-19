---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/amazon-cloudfront-logs.html
---

# Amazon CloudFront logs
<a name="amazon-cloudfront-logs"></a>

 [CloudFront standard logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html) provide detailed records about every request made to a distribution.

You can create a log ingestion into Amazon OpenSearch Service either by using the Centralized Logging with OpenSearch console or by deploying a standalone CloudFormation stack.

**Important**
The CloudFront logging bucket must be the same Region as the Centralized Logging with OpenSearch solution.
The Amazon OpenSearch Service index is rotated on a daily basis by default, and you can adjust the index in the Additional Settings.

## Create log ingestion (OpenSearch Engine)
<a name="create-log-ingestion-opensearch-engine-3"></a>

### Using the Centralized Logging with OpenSearch Console
<a name="using-the-centralized-logging-with-opensearch-console-5"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose the Create a log ingestion button.

1. In the AWS Services section, choose Amazon CloudFront.

1. Choose **Next**.

1. Under **Specify settings**, choose **Automatic** or **Manual** for **CloudFront logs enabling**. The automatic mode will detect the CloudFront log location automatically.
   + For **Automatic mode**, choose the CloudFront distribution and Log Type from the dropdown list.
   + For Standard Log, the solution will automatically detect the log location if logging is enabled.
   + For Real-time log, the solution will prompt you for confirmation to create or replace the CloudFront real-time log configuration.
   + For **Manual mode**, enter the **CloudFront Distribution ID** and **CloudFront Standard Log location**. (Note that CloudFront real-time log is not supported in Manual mode)
   + (Optional) If you are ingesting CloudFront logs from another account, select a [linked account](cross-account-ingestion.md#add-a-member-account) from the **Account** dropdown list first.

1. Choose **Next**.

1. In the Specify OpenSearch domain section, select an imported domain for the Amazon OpenSearch Service domain.

1. Choose **Yes** for **Sample dashboard** if you want to ingest an associated templated Amazon OpenSearch Service dashboard.

1. You can change the **Index Prefix** of the target Amazon OpenSearch Service index if needed. The default prefix is the CloudFront distribution ID.

1. In the **Log Lifecycle** section, input the number of days to manage the Amazon OpenSearch Service index lifecycle. The Centralized Logging with OpenSearch will create the associated [Index State Management (ISM)](https://opensearch.org/docs/latest/im-plugin/ism/index/) policy automatically for this pipeline.

1. In the **Log processor settings** section, choose **Log processor type**, configure the Lambda concurrency if needed, and then choose **Next**.

1. Add tags if needed.

1. Choose **Create**.

### Using the CloudFormation Stack
<a name="using-the-cloudformation-stack-5"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - CloudFront Standard Log Ingestion* template in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CloudFrontLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CloudFrontLog.template)  |
| AWS China Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CloudFrontLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CloudFrontLog.template)  |

1. Log in to the AWS Management Console and select the preceding button to launch the AWS CloudFormation template. You can also download the template as a starting point for your own implementation.

1. To launch the stack in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Log Bucket Name</td><td> {{&lt;Requires input&gt;}} </td><td>The S3 bucket name that stores the logs.</td></tr>
  <tr><td>Log Bucket Prefix</td><td> {{&lt;Requires input&gt;}} </td><td>The S3 bucket path prefix that stores the logs.</td></tr>
  <tr><td>Log Source Account ID</td><td> <i>Optional input</i> </td><td>The AWS Account ID of the S3 bucket. Required for cross-account log ingestion (<a href="cross-account-ingestion.md#add-a-member-account">add a member account</a> first). By default, the Account ID you logged in at <b>Step 1</b> will be used.</td></tr>
  <tr><td>Log Source Region</td><td> <i>Optional input</i> </td><td>The AWS Region of the S3 bucket. By default, the Region you selected at <b>Step 2</b> will be used.</td></tr>
  <tr><td>Log Source Account Assume Role</td><td> <i>Optional input</i> </td><td>The IAM Role ARN used for cross-account log ingestion. Required for cross-account log ingestion (<a href="cross-account-ingestion.md#add-a-member-account">add a member account</a> first).</td></tr>
  <tr><td>KMS-CMK ARN</td><td> <i>Optional input</i> </td><td>The KMS-CMK ARN for encryption. Leave it blank to create a new AWS KMS key.</td></tr>
  <tr><td>Enable OpenSearch Ingestion as processor</td><td> <i>Optional input</i> </td><td>Ingestion table ARN. Leave empty if you do not use OSI as Processor.</td></tr>
  <tr><td>Amazon S3 Backup Bucket</td><td> {{&lt;Requires input&gt;}} </td><td>The Amazon S3 backup bucket name to store the failed ingestion logs.</td></tr>
  <tr><td>Engine Type</td><td> <code>OpenSearch</code> </td><td>The engine type of the OpenSearch.</td></tr>
  <tr><td>OpenSearch Domain Name</td><td> {{&lt;Requires input&gt;}} </td><td>The domain name of the Amazon OpenSearch Service cluster.</td></tr>
  <tr><td>OpenSearch Endpoint</td><td> {{&lt;Requires input&gt;}} </td><td>The OpenSearch endpoint URL. For example, vpc-your_opensearch_domain_name-xcvgw6uu2o6zafsiefxubwuohe.us-east-1.es.amazonaws.com</td></tr>
  <tr><td>Index Prefix</td><td> {{&lt;Requires input&gt;}} </td><td>The common prefix of OpenSearch index for the log. The index name will be &lt;Index Prefix&gt;-&lt;Log Type&gt;-&lt;Other Suffix&gt;.</td></tr>
  <tr><td>Create Sample Dashboard</td><td> <code>Yes</code> </td><td>Whether to create a sample OpenSearch dashboard.</td></tr>
  <tr><td>VPC ID</td><td> {{&lt;Requires input&gt;}} </td><td>Select a VPC that has access to the OpenSearch domain. The log processing Lambda will reside in the selected VPC.</td></tr>
  <tr><td>Subnet IDs</td><td> {{&lt;Requires input&gt;}} </td><td>Select at least two subnets that have access to the OpenSearch domain. The log processing Lambda will reside in the subnets. Make sure that the subnets have access to the Amazon S3 service.</td></tr>
  <tr><td>Security Group ID</td><td> {{&lt;Requires input&gt;}} </td><td>Select a Security Group that will be associated with the log processing Lambda. Make sure that the Security Group has access to the OpenSearch domain.</td></tr>
  <tr><td>Number Of Shards</td><td> <code>5</code> </td><td>Number of shards to distribute the index evenly across all data nodes. Keep the size of each shard between 10-50 GB.</td></tr>
  <tr><td>Number of Replicas</td><td> <code>1</code> </td><td>Number of replicas for OpenSearch Index. Each replica is a full copy of an index. If the OpenSearch option is set to <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html#managedomains-za-standby">Domain with standby</a>, you need to configure it to 2.</td></tr>
  <tr><td>Age to Warm Storage</td><td> <i>Optional input</i> </td><td>The age required to move the index into warm storage (for example, 7d). Index age is the time between its creation and the present. Supported units are d (days) and h (hours). This is only effective when warm storage is enabled in OpenSearch.</td></tr>
  <tr><td>Age to Cold Storage</td><td> <i>Optional input</i> </td><td>The age required to move the index into cold storage (for example, 30d). Index age is the time between its creation and the present. Supported units are d (days) and h (hours). This is only effective when cold storage is enabled in OpenSearch.</td></tr>
  <tr><td>Age to Retain</td><td> <i>Optional input</i> </td><td>The age to retain the index (for example, 180d). Index age is the time between its creation and the present. Supported units are d (days) and h (hours). If the value is "", the index will not be deleted.</td></tr>
  <tr><td>Rollover Index Size</td><td> <i>Optional input</i> </td><td>The minimum size of the shard storage required to roll over the index (for example, 30GB).</td></tr>
  <tr><td>Index Suffix</td><td> <code>yyyy-MM-dd</code> </td><td>The common suffix format of OpenSearch index for the log(Example: yyyy-MM-dd, yyyy-MM-dd-HH). The index name will be &lt;Index Prefix&gt;-&lt;Log Type&gt;-&lt;Index Suffix&gt;-000001.</td></tr>
  <tr><td>Compression type</td><td> <code>best_compression</code> </td><td>The compression type to use to compress stored data. Available values are best_compression and default.</td></tr>
  <tr><td>Refresh Interval</td><td> <code>1s</code> </td><td>How often the index should refresh, which publishes its most recent changes and makes them available for searching. Can be set to -1 to disable refreshing. Default is 1s.</td></tr>
  <tr><td>Plugins</td><td> <i>Optional input</i> </td><td>List of plugins delimited by comma. Leave it blank if there are no available plugins to use. Valid inputs are user_agent, geo_ip.</td></tr>
  <tr><td>EnableS3Notification</td><td> <code>True</code> </td><td>An option to enable or disable notifications for Amazon S3 buckets. The default option is recommended for most cases.</td></tr>
  <tr><td>LogProcessorRoleName</td><td> <i>Optional input</i> </td><td>Specify a role name for the log processor. The name should NOT duplicate an existing role name. If no name is specified, a random name is generated.</td></tr>
  <tr><td>QueueName</td><td> <i>Optional input</i> </td><td>Specify a queue name for an SQS. The name should NOT duplicate an existing queue name. If no name is given, a random name will be generated.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-5"></a>

The dashboard includes the following visualizations.

| Visualization Name | Source Field | Description |
| --- | --- | --- |
| Total Requests | \* log event | Displays the total number of viewer requests received by the Amazon CloudFront, for all HTTP methods and for both HTTP and HTTPS requests. |
| Edge Locations | \* x-edge-location | Shows a pie chart representing the proportion of the locations of CloudFront edge servers. |
| Request History | \* log event | Presents a bar chart that displays the distribution of events over time. |
| Unique Visitors | \* c-ip | Displays unique visitors identified by client IP address. |
| Cache Hit Rate | \* sc-bytes | Shows the proportion of your viewer requests that are served directly from the CloudFront cache instead of going to your origin servers for content. |
| Result Type | \* x-edge-response-result-type | Shows the percentage of hits, misses, and errors to the total viewer requests for the selected CloudFront distribution:<br />\* Hit - A viewer request for which the object is served from a CloudFront edge cache. In access logs, these are requests for which the value of x-edge-response-result-type is Hit \* Miss - A viewer request for which the object isn’t currently in an edge cache, so CloudFront must get the object from your origin. In access logs, these are requests for which the value of x-edge-response-result-type is Miss. \* Error - A viewer request that resulted in an error, so CloudFront didn’t serve the object. In access logs, these are requests for which the value of x-edge-response-result-type is Error, LimitExceeded, or CapacityExceeded.<br />The chart does not include refresh hits—​requests for objects that are in the edge cache but that have expired. In access logs, refresh hits are requests for which the value of x-edge-response-result-type is RefreshHit. |
| Top Miss URI | \* cs-uri-stem \* cs-method | Shows top 10 of the requested objects that are not in the cache. |
| Bandwidth | \* cs-bytes \* sc-bytes | Provides insights into data transfer activities from the locations of CloudFront edge. |
| Bandwidth History | \* cs-bytes \* sc-bytes | Shows the historical trend of the data transfer activities from the locations of CloudFront edge. |
| Top Client IPs | \* c-ip | Provides the top 10 IP address accessing your Amazon CloudFront. |
| Status Code Count | \* sc-status | Displays the count of requests made to the Amazon CloudFront, grouped by HTTP status codes(e.g., 200, 404, 403, etc.). |
| Status History | \* @timestamp \* sc-status | Shows the historical trend of HTTP status codes returned by the Amazon CloudFront over a specific period of time. |
| Status Code | \* sc-status | Identifies the users or IAM roles responsible for changes to EC2 resources, assisting in accountability and tracking of modifications. |
| Average Time Taken | \* time-taken | This visualization calculates and presents the average time taken for various operations in the Amazon CloudFront (e.g., average time for GET, PUT requests, etc.). |
| Average Time History | \* time-taken \* time-to-first-byte \* @timestamp | Shows the historical trend of the average time taken for various operations in the Amazon CloudFront. |
| Http Method | \* cs-method | Displays the count of requests made to the Amazon CloudFront using a pie chart, grouped by HTTP request method names (for example, POST, GET, HEAD). |
| Average Time To First Byte | \* time-to-first-byte | Provides the average time taken in seconds by the origin server to respond back with the first byte of the response. |
| Top Request URIs | \* cs-uri-stem \* cs-method | Provides the top 10 request URIs accessing your CloudFront. |
| Top User Agents | \* cs-user-agent | Provides the top 10 user agents accessing your CloudFront. |
| Edge Location Heatmap | \* x-edge-location \* x-edge-result-type | Shows a heatmap representing the result type of each edge location. |
| Top Referrers | \* cs-referer | Top 10 referrers with the Amazon CloudFront access. |
| Top Countries or Regions | \* c\_country | Top 10 countries with the Amazon CloudFront access. |

You can access the built-in dashboard in Amazon OpenSearch Service to view log data. For more information, see the [Access Dashboard](getting-started.md#step-4-access-the-dashboard).

 **CloudFront logs sample dashboard.**

![image37](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image37.png)

## Create log ingestion (Light Engine)
<a name="create-log-ingestion-light-engine-2"></a>

### Using the Centralized Logging with OpenSearch Console
<a name="using-the-centralized-logging-with-opensearch-console-6"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose the Create a log ingestion button.

1. In the AWS Services section, choose Amazon CloudFront.

1. Choose **Next**.

1. Under **Specify settings**, choose **Automatic** or **Manual** for **CloudFront logs enabling**. The automatic mode will detect the CloudFront log location automatically.
   + For **Automatic mode**, choose the CloudFront distribution and Log Type from the dropdown list.
   + For Standard Log, the solution will automatically detect the log location if logging is enabled.
   + For Real-time log, the solution will prompt you for confirmation to create or replace the CloudFront real-time log configuration.
   + For **Manual mode**, enter the **CloudFront Distribution ID** and **CloudFront Standard Log location**. (Note that CloudFront real-time log is not supported in Manual mode)
   + (Optional) If you are ingesting CloudFront logs from another account, select a [linked account](cross-account-ingestion.md#add-a-member-account) from the **Account** dropdown list first.

1. Choose **Next**.

1. Choose **Log Processing Enriched fields** if needed. The available plugins are **location** and **OS/User Agent**. Enabling rich fields increases data processing latency and processing costs. By default, it is not selected.

1. In the **Specify Light Engine Configuration** section, if you want to ingest associated templated Grafana dashboards, select **Yes** for the sample dashboard.

1. You can choose an existing Grafana, or if you must import a new one, you can go to Grafana for configuration.

1. Select an S3 bucket to store partitioned logs and define a name for the log table. We have provided a predefined table name, but you can modify it according to your business needs.

1. If needed, change the log processing frequency, which is set to **5** minutes by default, with a minimum processing frequency of **1** minute.

1. In the **Log Lifecycle** section, enter the log merge time and log archive time. We have provided default values, but you can adjust them based on your business requirements.

1. Select **Next**.

1. If desired, add tags.

1. Select **Create**.

### Using the CloudFormation Stack
<a name="using-the-cloudformation-stack-6"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - CloudFront Log Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesCloudFrontPipeline.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesCloudFrontPipeline.template)  |
| AWS China Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesCloudFrontPipeline.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesCloudFrontPipeline.template)  |

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
  <tr><td>Pipeline Id</td><td> {{&lt;Requires input&gt;}} </td><td>The unique identifier for the pipeline is essential if you must create multiple Application Load Balancer pipelines and write different Application Load Balancer logs into separate tables. To ensure uniqueness, you can generate a unique pipeline identifier using <a href="https://www.uuidgenerator.net/version4">uuidgenerator</a>.</td></tr>
  <tr><td>Staging Bucket Prefix</td><td> <code>AWSLogs/CloudFrontLogs</code> </td><td>The storage directory for logs in the temporary storage area should ensure the uniqueness and non-overlapping of the Prefix for different pipelines.</td></tr>
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
  <tr><td>Centralized Table Name</td><td> <code>CloudFront</code> </td><td>Table name for writing data to the centralized database. You can modify it if needed.</td></tr>
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
  <tr><td>Recipients</td><td> {{&lt;Requires input&gt;}} </td><td>Alert notification: If the Notification Service is SNS, enter the SNS Topic ARN here to have the necessary permissions. If the Notification Service is SES, enter the email addresses separated by commas here, ensuring that the email addresses are already Verified Identities in SES. The adminEmail provided during the creation of the main stack will receive a verification email by default.</td></tr>
</tbody>
</table>

   1. Parameters for **Dashboard settings**

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Import Dashboards</td><td> <code>FALSE</code> </td><td>Whether to import the Dashboard into Grafana, with a default value of false. If set to true, you must provide the Grafana URL and Grafana Service Account Token.</td></tr>
  <tr><td>Grafana URL</td><td> {{&lt;Requires input&gt;}} </td><td>Grafana access URL for example: https://alb-72277319.us-west-2.elb.amazonaws.com.</td></tr>
  <tr><td>Grafana Service Account Token</td><td> {{&lt;Requires input&gt;}} </td><td>Grafana Service Account Token Service Account Token created in Grafana.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-6"></a>

The dashboard includes the following visualizations.

| Visualization Name | Source Field | Description |
| --- | --- | --- |
| Filters | Filters | The following data can be filtered by query filter conditions. |
| Total Requests | log event | Displays the total number of viewer requests received by the Amazon CloudFront, for all HTTP methods and for both HTTP and HTTPS requests. |
| Unique Visitors | c-ip | Displays unique visitors identified by client IP address. |
| Requests History | log event | Presents a bar chart that displays the distribution of events over time. |
| Request By Edge Location | x-edge-location | Shows a pie chart representing the proportion of the locations of CloudFront edge servers. |
| HTTP Status Code | sc-status | Displays the count of requests made to the Amazon CloudFront, grouped by HTTP status codes (e.g., 200, 404, 403, etc.). |
| Status Code History | sc-status | Shows the historical trend of HTTP status codes returned by the Amazon CloudFront over a specific period of time. |
| Status Code Pie | sc-status | Represents the distribution of requests based on different HTTP status codes using a pie chart. |
| Average Processing Time | time-taken time-to-first-byte | This visualization calculates and presents the average time taken for various operations in the Amazon CloudFront (for example, average time for GET, PUT requests). |
| Avg. Processing Time History | time-taken time-to-first-byte | Shows the historical trend of the average time taken for various operations in the Amazon CloudFront. |
| Avg. Processing Time History | time-taken time-to-first-byte | Shows the historical trend of the average time taken for various operations in the Amazon CloudFront. |
| HTTP Method | cs-method | Displays the count of requests made to the Amazon CloudFront using a pie chart, grouped by HTTP request method names (for example, POST, GET, HEAD). |
| Total Bytes | cs-bytes sc-bytes | Provides insights into data transfer activities, including the total bytes transferred. |
| Response Bytes History | cs-bytes sc-bytes | Displays the historical trend of the received bytes, send bytes. |
| Edge Response Type | x-edge-response-result-type | Shows the percentage of hits, misses, and errors to the total viewer requests for the selected CloudFront distribution: - Hit - A viewer request for which the object is served from a CloudFront edge cache. In access logs, these are requests for which the value of x-edge-response-result-type is Hit. - Miss - A viewer request for which the object isn’t currently in an edge cache, so CloudFront must get the object from your origin. In access logs, these are requests for which the value of x-edge-response-result-type is Miss. - Error - A viewer request that resulted in an error, so CloudFront didn’t serve the object. In access logs, these are requests for which the value of x-edge-response-result-type is Error, LimitExceeded, or CapacityExceeded. The chart does not include refresh hits—​requests for objects that are in the edge cache but that have expired. In access logs, refresh hits are requests for which the value of x-edge-response-result-type is RefreshHit. |
| Requests / Origin Requests | log event | Displays the number of requests made to CloudFront and the number of requests back to the origin. |
| Requests / Origin Requests Latency | log event time-taken | Displays the request latency from the client to CloudFront and the request latency back to the origin. |
| Top 20 URLs with most requests | log event | Top 20 URLs based on the number of requests. |
| Requests 3xx / 4xx / 5xx error rate | log event sc-status | Displays the ratio of 3xx/4xx/5xx status codes from the client to CloudFront. |
| Origin Requests 3xx / 4xx / 5xx error rate | log event sc-status x-edge-detailed-result-type | Display the proportion of 3xx/4xx/5xx status codes returned to the origin. |
| Requests 3xx / 4xx / 5xx error latency | log event sc-status time-taken | Displays the latency from the client to CloudFront for 3xx/4xx/5xx status codes. |
| Origin Requests 3xx / 4xx / 5xx error latency | log event sc-status x-edge-detailed-result-type time-taken | Displays the delay in returning to the source 3xx/4xx/5xx status code. |
| Response Latency (>= 1sec) rate | log event time-taken | Display the proportion of delay above 1s. |
| Bandwidth | sc-bytes | Displays the bandwidth from the client to CloudFront and the bandwidth back to the origin. |
| Data transfer | sc-bytes | Display the response traffic. |
| Top 20 URLs with most traffic | cs-uri-stem sc-bytes | Top 20 URLs calculated by traffic. |
| Cache hit rate (calculated using requests) | log event x-edge-result-type | Displays the cache hit ratio calculated by the number of requests. |
| Cache hit rate (calculated using bandwidth) | log event sc-bytes x-edge-result-type | Displays the cache hit ratio calculated by bandwidth. |
| Cache Result | log event x-edge-result-type | Displays the number of requests of various x-edge-result-types, such as the number of requests that hit the cache and the number of requests that missed the cache. |
| Cache Result Latency | log event sc-bytes x-edge-result-type | Displays the request latency of various x-edge-result-types, such as the request latency that hits the cache and the request latency that misses the cache. |
| Requests by OS | ua\_os | Displays the count of requests made to the Application Load Balancer, grouped by user agent OS. |
| Requests by Device | ua\_device | Displays the count of requests made to the Application Load Balancer, grouped by user agent device. |
| Requests by Browser | ua\_browser | Displays the count of requests made to the Application Load Balancer, grouped by user agent browser. |
| Requests by Category | ua\_category | Displays the count of categories made to the Application Load Balancer, grouped by user agent category (for example, PC, Mobile, Tablet). |
| Requests by Countries or Regions | geo\_iso\_code | Displays the count of requests made to the Application Load Balancer (grouped by the corresponding country or Region resolved by the client IP). |
| Top Countries or Regions | geo\_country | Top 10 countries with the Application Load Balancer Access. |
| Top Cities | geo\_city | Top 10 cities with Application Load Balancer Access. |

 **CloudFront logs sample dashboard.**

![image38](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image38.png)
