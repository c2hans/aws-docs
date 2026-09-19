---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-waf-logs.html
---

# AWS WAF logs
<a name="aws-waf-logs"></a>

 [AWS WAF Access Logs](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html) provide detailed information about traffic that is analyzed by your web ACL. Logged information includes the time that AWS WAF received a web request from your AWS resource, detailed information about the request, and details about the rules that the request matched.

You can create a log ingestion into Amazon OpenSearch Service either by using the Centralized Logging with OpenSearch console or by deploying a standalone CloudFormation stack.

**Important**
Deploy Centralized Logging with OpenSearch solution in the same Region as your Web ACLs, or you will not be able to create a AWS WAF pipeline. For example:
If your Web ACL is associated with Global CloudFront, you must deploy the solution in us-east-1.
If your Web ACL is associated with other resources in Regions like Ohio, your Centralized Logging with OpenSearch stack must also be deployed in that Region.
The AWS WAF logging bucket must be the same as the Centralized Logging with OpenSearch solution.
 [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) logs are not supported in Centralized Logging with OpenSearch. Learn more about [migrating rules from AWS WAF Classic to the new AWS WAF](https://aws.amazon.com/blogs/security/migrating-rules-from-aws-waf-classic-to-new-aws-waf/).
The Amazon OpenSearch Service index is rotated on a daily basis by default, and you can adjust the index in the Additional Settings.

## Create log ingestion (OpenSearch Engine)
<a name="create-log-ingestion-opensearch-engine-6"></a>

### Using the Centralized Logging with OpenSearch Console
<a name="using-the-centralized-logging-with-opensearch-console-10"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose the Create a log ingestion button.

1. In the **AWS Services** section, choose **AWS WAF**.

1. Choose **Next**.

1. Under Specify settings, choose Automatic or Manual.
   + For **Automatic** mode, choose a Web ACL in the dropdown list.
   + For **Manual** mode, enter the **Web ACL name**.
   + (Optional) If you are ingesting AWS WAF logs from another account, select a [linked account](cross-account-ingestion.md#add-a-member-account) from the **Account** dropdown list first.

1. Specify an Ingest Options. Choose between Sampled Request or Full Request.
   + For **Sampled Request**, enter how often you want to ingest sample requests in minutes.
   + For **Full Request**, if the Web ACL log is not enabled, choose **Enable** to enable the access log, or enter **Log location** in Manual mode. Note that Centralized Logging with OpenSearch will automatically enable logging with a Firehose stream as destination for your AWS WAF.

1. Choose **Next**.

1. In the Specify OpenSearch domain section, select an imported domain for the Amazon OpenSearch Service domain.

1. Choose **Yes** for **Sample dashboard** if you want to ingest an associated templated Amazon OpenSearch Service dashboard.

1. You can change the **Index Prefix** of the target Amazon OpenSearch Service index if needed. The default prefix is the Web ACL Name.

1. In the **Log Lifecycle** section, enter the number of days to manage the Amazon OpenSearch Service index lifecycle. The Centralized Logging with OpenSearch will create the associated [Index State Management (ISM)](https://opensearch.org/docs/latest/im-plugin/ism/index/) policy automatically for this pipeline.

1. In the **Select log processor** section, choose the log processor.

   1. When selecting Lambda as a log processor, you can configure the Lambda concurrency if needed.

   1. (Optional) OSI as log processor is now supported in these [Regions](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-opensearch-service-ingestion/). When OSI is selected, type in the minimum and maximum number of OCU. See more information [here](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion.html#ingestion-scaling).

1. Choose **Next**.

1. Add tags if needed.

1. Choose **Create**.

### Using the CloudFormation Stack
<a name="using-the-cloudformation-stack-10"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - AWS WAF Log Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Regions (Full Request) |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFLog.template)  |
| AWS China Regions (Full Request) |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFLog.template)  |
| AWS Regions (Sampled Request) |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFSampledLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFSampledLog.template)  |
| AWS China Regions (Sampled Request) |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFSampledLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFSampledLog.template)  |

1. Log in to the AWS Management Console and select the button to launch the AWS CloudFormation template. You can also download the template as a starting point for your own implementation.

1. To launch the stack in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.
   + Parameters for **Full Request** only

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Log Bucket Name</td><td> {{&lt;Requires input&gt;}} </td><td>The S3 bucket name that stores the logs.</td></tr>
  <tr><td>Log Bucket Prefix</td><td> {{&lt;Requires input&gt;}} </td><td>The S3 bucket path prefix that stores the logs.</td></tr>
</tbody>
</table>

   + Parameters for **Sampled Request** only

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>WebACL Names</td><td> {{&lt;Requires input&gt;}} </td><td>The list of Web ACL names, delimited by comma.</td></tr>
  <tr><td>Interval</td><td> <code>2</code> </td><td>The default interval (in minutes) to get sampled logs. The value must be greater or equal to 2, and less or equal to 180.</td></tr>
</tbody>
</table>

   + Common parameters

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th><th>Log Source Account ID</th><th> <i>Optional input</i> </th><th>The AWS Account ID of the S3 bucket. Required for cross-account log ingestion (<a href="cross-account-ingestion.md#add-a-member-account">add a member account</a> first). By default, the Account ID you logged in at <b>Step 1</b> will be used.</th></tr>
</thead>
<tbody>
  <tr><td>Log Source Region</td><td> <i>Optional input</i> </td><td>The AWS Region of the S3 bucket. By default, the Region you selected at <b>Step 2</b> will be used.</td><td>Log Source Account Assume Role</td><td> <i>Optional input</i> </td><td>The IAM Role ARN used for cross-account log ingestion. Required for cross-account log ingestion (<a href="cross-account-ingestion.md#add-a-member-account">add a member account</a> first).</td></tr>
  <tr><td>KMS-CMK ARN</td><td> <i>Optional input</i> </td><td>The KMS-CMK ARN for encryption. Leave it blank to create a new AWS KMS key.</td><td>Enable OpenSearch Ingestion as processor</td><td> <i>Optional input</i> </td><td>Ingestion table ARN. Leave empty if you do not use OSI as Processor.</td></tr>
  <tr><td>S3 Backup Bucket</td><td> {{&lt;Requires input&gt;}} </td><td>The S3 backup bucket name to store the failed ingestion logs.</td><td>Engine Type</td><td> <code>OpenSearch</code> </td><td>The engine type of the OpenSearch. Select OpenSearch or OpenSearch.</td></tr>
  <tr><td>OpenSearch Domain Name</td><td> {{&lt;Requires input&gt;}} </td><td>The domain name of the Amazon OpenSearch Service cluster.</td><td>OpenSearch Endpoint</td><td> {{&lt;Requires input&gt;}} </td><td>The OpenSearch endpoint URL. For example, vpc-your_opensearch_domain_name-xcvgw6uu2o6zafsiefxubwuohe.us-east-1.es.amazonaws.com</td></tr>
  <tr><td>Index Prefix</td><td> {{&lt;Requires input&gt;}} </td><td>The common prefix of OpenSearch index for the log. The index name will be &lt;Index Prefix&gt;-&lt;log-type&gt;-&lt;YYYY-MM-DD&gt;.</td><td>Create Sample Dashboard</td><td> <code>Yes</code> </td><td>Whether to create a sample OpenSearch dashboard.</td></tr>
  <tr><td>VPC ID</td><td> {{&lt;Requires input&gt;}} </td><td>Select a VPC that has access to the OpenSearch domain. The log processing Lambda will reside in the selected VPC.</td><td>Subnet IDs</td><td> {{&lt;Requires input&gt;}} </td><td>Select at least two subnets that have access to the OpenSearch domain. The log processing Lambda will reside in the subnets. Make sure that the subnets have access to the Amazon S3 service.</td></tr>
  <tr><td>Security Group ID</td><td> {{&lt;Requires input&gt;}} </td><td>Select a Security Group that will be associated with the log processing Lambda. Make sure that the Security Group has access to the OpenSearch domain.</td><td>Number Of Shards</td><td> <code>5</code> </td><td>Number of shards to distribute the index evenly across all data nodes. Keep the size of each shard between 10-50 GB.</td></tr>
  <tr><td>Number of Replicas</td><td> <code>1</code> </td><td>Number of replicas for OpenSearch Index. Each replica is a full copy of an index. If the OpenSearch option is set to <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html#managedomains-za-standby">Domain with standby</a>, you need to configure it to 2.</td><td>Age to Warm Storage</td><td> <code>0</code> </td><td>The number of days required to move the index into warm storage. This takes effect only when the value is larger than 0 and warm storage is enabled in OpenSearch.</td></tr>
  <tr><td>Age to Cold Storage</td><td> <code>0</code> </td><td>The number of days required to move the index into cold storage. This takes effect only when the value is larger than 0 and cold storage is enabled in OpenSearch.</td><td>Age to Retain</td><td> <code>0</code> </td><td>The total number of days to retain the index. If the value is 0, the index will not be deleted.</td></tr>
  <tr><td>Rollover Index Size</td><td> <i>Optional input</i> </td><td>The minimum size of the shard storage required to roll over the index (for example, 30GB).</td><td>Index Suffix</td><td> <code>yyyy-MM-dd</code> </td><td>The common suffix format of OpenSearch index for the log (for example, yyyy-MM-dd, yyyy-MM-dd-HH). The index name will be &lt;Index Prefix&gt;-&lt;Log Type&gt;-&lt;Index Suffix&gt;-000001.</td></tr>
  <tr><td>Compression type</td><td> <code>best_compression</code> </td><td>The compression type to use to compress stored data. Available values are best_compression and default.</td><td>Refresh Interval</td><td> <code>1s</code> </td><td>How often the index should refresh, which publishes its most recent changes and makes them available for searching. Can be set to -1 to disable refreshing. Default is 1s.</td></tr>
  <tr><td>Plugins</td><td> <i>Optional input</i> </td><td>List of plugins delimited by comma. Leave it blank if there are no available plugins to use. Valid inputs are user_agent, geo_ip.</td><td>EnableS3Notification</td><td> <code>True</code> </td><td>An option to enable or disable notifications for Amazon S3 buckets. The default option is recommended for most cases.</td></tr>
  <tr><td>LogProcessorRoleName</td><td> <i>Optional input</i> </td><td>Specify a role name for the log processor. The name should NOT duplicate an existing role name. If no name is specified, a random name is generated.</td><td>QueueName</td><td> <i>Optional input</i> </td><td>Specify a queue name for an Amazon SQS queue. The name should NOT duplicate an existing queue name. If no name is given, a random name will be generated.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-10"></a>

The dashboard includes the following visualizations.

| Visualization Name | Source Field | Description |
| --- | --- | --- |
| Filters | \* Filters | The following data can be filtered by query filter conditions. |
| Web ACLs | \* log event \* webaclName | Displays the count of requests made to the AWS WAF, grouped by Web ACL Names. |
| Total Requests | \* log event | Displays the total number of web requests. |
| Request Timeline | \* log event | Presents a bar chart that displays the distribution of events over time. |
| AWS WAF Rules | \* terminatingRuleId | Presents a pie chart that displays the distribution of events over the AWS WAF rules in the Web ACL. |
| Total Blocked Requests | \* log event | Displays the total number of blocked web requests. |
| Unique Client IPs | \* Request.ClientIP | Displays unique visitors identified by client IP. |
| Country or Region By Request | \* Request.Country | Displays the count of requests made to the Web ACL (grouped by the corresponding country or Region resolved by the client IP). |
| Http Methods | \* Request.HTTPMethod | Displays the count of requests made to the Web ACL using a pie chart, grouped by HTTP request method names (for example, POST, GET, HEAD). |
| Http Versions | \* Request.HTTPVersion | Displays the count of requests made to the Web ACL using a pie chart, grouped by HTTP protocol version (for example, HTTP/2.0, HTTP/1.1). |
| Top WebACLs | \* webaclName \* webaclId.keyword | The web requests view enables you to analyze the top web requests. |
| Top Hosts | \* host | Lists the source IP addresses associated with events, enabling you to identify and investigate potentially suspicious or unauthorized activities. |
| Top Request URIs | \* Request.URI | Top 10 request URIs. |
| Top Countries or Regions | \* Request.country | Top 10 countries with the Web ACL Access. |
| Top Rules | \* terminatingRuleId | Top 10 rules in the web ACL that matched the request. |
| Top Client IPs | \* Request.ClientIP | Provides the top 10 IP address. |
| Top User Agents | \* userAgent | Provides the top 10 user agents |
| Block Allow Host Uri | \* host \* Request.URI \* action | Provides blocked or allowed web requests. |
| Top Labels with Host, Uri | \* labels.name \* host \* Request.URI | Top 10 detailed logs by labels with host, URI |
| View by Matching Rule | \* sc-status | This visualization provides detailed logs by DQL "terminatingRuleId:\*". |
| View by httpRequest args,uri,path | \* sc-status | This visualization provides detailed logs by DQL. |

You can access the built-in dashboard in Amazon OpenSearch Service to view log data. For more information, see the [Access Dashboard](getting-started.md#step-4-access-the-dashboard).

 **AWS WAF logs sample dashboard.**

![image42](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image42.png)

## Create log ingestion (Light Engine)
<a name="create-log-ingestion-light-engine-4"></a>

### Using the Centralized Logging with OpenSearch Console
<a name="using-the-centralized-logging-with-opensearch-console-11"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose the Create a log ingestion button.

1. In the **AWS Services** section, choose **AWS WAF**.

1. Choose **Light Engine**, choose **Next**.

1. Under Specify settings, choose Automatic or Manual.
   + For **Automatic** mode, choose a Web ACL from the dropdown list.
   + For **Manual** mode, enter the Web ACL name.
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
<a name="using-the-cloudformation-stack-11"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - AWS WAF Log Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesWafPipeline.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesWafPipeline.template)  |
| AWS China Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesWafPipeline.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesWafPipeline.template)  |

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
  <tr><td>Staging Bucket Prefix</td><td> <code>AWSLogs/WAFLogs</code> </td><td>The storage directory for logs in the temporary storage area should ensure the uniqueness and non-overlapping of the Prefix for different pipelines.</td></tr>
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
  <tr><td>Centralized Table Name</td><td> <code>WAF</code> </td><td>Table name for writing data to the centralized database. You can modify it if needed.</td></tr>
</tbody>
</table>

   1. Parameters for **Scheduler settings**

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>LogProcessor Schedule Expression</td><td> <code>rate(5 minutes)</code> </td><td>Task scheduling expression for performing log processing, with a default value of executing the LogProcessor every 5 minutes. Configuration <a href="https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html">for reference</a>.</td></tr>
  <tr><td>LogMerger Schedule Expression</td><td> <code>cron(0 1 * _? )</code> </td><td>Task scheduling expression for performing log merging, with a default value of executing the LogMerger at 1 AM every day. Configuration <a href="https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html">for reference</a>.</td></tr>
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
  <tr><td>Recipients</td><td> {{&lt;Requires input&gt;}} </td><td>Alert notification: If the Notification Service is SNS, enter the SNS Topic ARN here so that you have the necessary permissions. If the Notification Service is SES, enter the email addresses separated by commas here, ensuring that the email addresses are already Verified Identities in SES. The adminEmail provided during the creation of the main stack will receive a verification email by default.</td></tr>
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
  <tr><td>Grafana Service Account Token</td><td> {{&lt;Requires input&gt;}} </td><td>Grafana Service Account Token：Service Account Token created in Grafana.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-11"></a>

The dashboard includes the following visualizations.

| Visualization Name | Source Field | Description |
| --- | --- | --- |
| Filters | Filters | The following data can be filtered by query filter conditions. |
| Total Requests | log event | Displays the total number of web requests. |
| Total Blocked Requests | log event | Displays the total number of blocked web requests. |
| Requests History | log event | Presents a bar chart that displays the distribution of events over time. |
| AWS WAF ACLs | log event webaclName | Displays the count of requests made to the AWS WAF, grouped by Web ACL Names. |
| AWS WAF Rules | terminatingRuleId | Presents a pie chart that displays the distribution of events over the AWS WAF rules in the Web ACL. |
| Sources | httpSourceId | Presents a pie chart that displays the distribution of events over the id of the associated resource. |
| HTTP Methods | httpRequest.HTTPMethod | Displays the count of requests made to the Web ACL using a pie chart, grouped by HTTP request method names (for example, POST, GET, HEAD). |
| Country or Region By Blocked Requests | HTTPRequest.Country | Displays the count of blocked web requests made to the Web ACL (grouped by the corresponding country or Region resolved by the client IP). |
| Top WebACLs | webaclName | The web requests view enables you to analyze the top web requests. |
| Top Sources | httpSourceId | Top 10 id of the associated resource. |
| Top Requests URIs | httpRequest.URI | Top 10 request URIs. |
| Top Countries or Regions | httpRequest.country | Top 10 countries with the Web ACL Access. |
| Top Rules | terminatingRuleId | Top 10 rules in the web ACL that matched the request. |
| Top Client IPs | httpRequest.ClientIP | Provides the top 10 IP addresses. |
| Top Blocked / Allowed Hosts URI | host httpRequest.URI action | Provides blocked or allowed web requests. |
| Top Labels with Host, URI | labels host httpRequest.URI | Top 10 detailed logs by labels with host, URI. |
| Metrics | webaclId webaclName terminatingRuleId terminatingRuleType httpSourceId httpRequest.HTTPMethod httpRequest.country httpRequest.ClientIP labels httpRequest.URI action | Provides a detailed list of log events, including timestamps, web ACL, and client IP. |

 **AWS WAF logs sample dashboard.**

![image43](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image43.jpeg)
