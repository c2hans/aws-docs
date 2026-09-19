---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/amazon-s3-logs.html
---

# Amazon S3 logs
<a name="amazon-s3-logs"></a>

 [Amazon S3 server access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html) provides detailed records for the requests made to the bucket. S3 Access Logs can be enabled and saved in another S3 bucket.

You can create a log ingestion into Amazon OpenSearch Service either by using the Centralized Logging with OpenSearch console or by deploying a standalone CloudFormation stack.

**Important**
The S3 Bucket Region must be the same as the Centralized Logging with OpenSearch solution Region.
The Amazon OpenSearch Service index is rotated on a daily basis by default, and you can adjust the index in the Additional Settings.

## Create log ingestion (OpenSearch Engine)
<a name="create-log-ingestion-opensearch-engine-1"></a>

### Using the Centralized Logging with OpenSearch Console
<a name="using-the-centralized-logging-with-opensearch-console-2"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose the Create a log ingestion button.

1. In the **AWS Services** section, choose **Amazon S3**.

1. Choose **Next**.

1. Under **Specify settings**, choose **Automatic** or **Manual** for **Amazon S3 Access Log enabling**. The automatic mode will enable the Amazon S3 Access Log and save the logs to a centralized S3 bucket if logging is not enabled yet.
   + For **Automatic mode**, choose the S3 bucket from the dropdown list.
   + For Manual mode, enter the Bucket Name and Amazon S3 Access Log location.
   + (Optional) If you are ingesting Amazon S3 logs from another account, select a [linked account](cross-account-ingestion.md#add-a-member-account) from the **Account** dropdown list first.

1. Choose **Next**.

1. In the Specify OpenSearch domain section, select an imported domain for the Amazon OpenSearch Service domain.

1. Choose **Yes** for **Sample dashboard** if you want to ingest an associated built-in Amazon OpenSearch Service dashboard.

1. You can change the **Index Prefix** of the target Amazon OpenSearch Service index if needed. The default prefix is your bucket name.

1. In the **Log Lifecycle** section, enter the number of days to manage the Amazon OpenSearch Service index lifecycle. The Centralized Logging with OpenSearch will create the associated [Index State Management (ISM)](https://opensearch.org/docs/latest/im-plugin/ism/index/) policy automatically for this pipeline.

1. Choose **Next**.

1. Add tags if needed.

1. Choose **Create**.

### Using the CloudFormation Stack
<a name="using-the-cloudformation-stack-2"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - Amazon S3 Access Log Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/S3AccessLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/S3AccessLog.template)  |
| AWS China Regions |  ![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/S3AccessLog.template)  |

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
  <tr><td>Log Bucket Name</td><td> {{&lt;Requires input&gt;}} </td><td>The S3 bucket name which stores the logs.</td></tr>
  <tr><td>Log Bucket Prefix</td><td> {{&lt;Requires input&gt;}} </td><td>The S3 bucket path prefix which stores the logs.</td></tr>
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
  <tr><td>EnableS3Notification</td><td> <code>True</code> </td><td>An option to enable or disable notifications for Amazon S3 buckets. The default option is recommended for most cases.</td></tr>
  <tr><td>LogProcessorRoleName</td><td> <i>Optional input</i> </td><td>Specify a role name for the log processor. The name should NOT duplicate an existing role name. If no name is specified, a random name is generated.</td></tr>
  <tr><td>QueueName</td><td> <i>Optional input</i> </td><td>Specify a queue name for an Amazon SQS queue. The name should NOT duplicate an existing queue name. If no name is given, a random name will be generated.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-2"></a>

The dashboard includes the following visualizations.

| Visualization Name | Source Field | Description |
| --- | --- | --- |
| Total Requests | \* log event | A visualization showing the total number of requests made to the Amazon S3 bucket, including all types of operations (for example, GET, PUT, DELETE). |
| Unique Visitors | \* log event | This visualization displays the count of unique visitors accessing the Amazon S3 bucket, identified by their IP addresses. |
| Access History | \* log event | Provides a chronological log of all access events made to the Amazon S3 bucket, including details about the operations and their outcomes. |
| Request By Operation | \* operation | This visualization categorizes and shows the distribution of requests based on different operations (for example, GET, PUT, DELETE). |
| Status Code | \* http\_status | Displays the count of requests made to the Amazon S3 bucket, grouped by HTTP status codes returned by the server (for example, 200, 404, 403). |
| Status Code History | \* http\_status | Shows the historical trend of HTTP status codes returned by the Amazon S3 server over a specific period of time. |
| Status Code Pie | \* http\_status | Represents the distribution of requests based on different HTTP status codes using a pie chart. |
| Average Time | \* total\_time | This visualization calculates and presents the average time taken for various operations in the Amazon S3 bucket (for example, average time for GET, PUT requests). |
| Average Turn Around Time | \* turn\_around\_time | Shows the average turnaround time for different operations, which is the time between receiving a request and sending the response back to the client. |
| Data Transfer | \* bytes\_sent \* object\_size \* operation | Provides insights into data transfer activities, including the total bytes transferred, object sizes, and different operations involved. |
| Top Client IPs | \* remote\_ip | Displays the top client IP addresses with the highest number of requests made to the Amazon S3 bucket. |
| Top Request Keys | \* key \* object\_size | Shows the top requested keys in the Amazon S3 bucket along with the corresponding object sizes. |
| Delete Events | \* operation \* key \* version\_id \* object\_size \* remote\_ip \* http\_status \* error\_code | Focuses on delete events, including the operation, key, version ID, object size, client IP, HTTP status, and error code associated with the delete requests. |
| Access Failures | \* operation \* key \* version\_id \* object\_size \* remote\_ip \* http\_status \* error\_code | Highlights access failures, showing the details of the failed requests, including operation, key, version ID, object size, client IP, HTTP status, and error code. |

You can access the built-in dashboard in Amazon OpenSearch Service to view log data. For more information, see the [Access Dashboard](getting-started.md#step-4-access-the-dashboard).

 **Amazon S3 logs sample dashboard.**

![image34](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image34.png)
