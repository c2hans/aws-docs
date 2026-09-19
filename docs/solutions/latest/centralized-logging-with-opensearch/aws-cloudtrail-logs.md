---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-cloudtrail-logs.html
---

# AWS CloudTrail logs
<a name="aws-cloudtrail-logs"></a>

AWS CloudTrail monitors and records account activity across your AWS infrastructure. It outputs all the data to the specified S3 bucket or a CloudWatch Log Group.

You can create a log analytics pipeline either by using the Centralized Logging with OpenSearch console or by deploying a standalone CloudFormation stack.

**Important**
The CloudTrail logging bucket must be in the same Region as the Centralized Logging with OpenSearch solution.
The Amazon OpenSearch Service index is rotated on a daily basis by default, and you can adjust the index in the Additional Settings.

## Create log ingestion (OpenSearch Engine)
<a name="create-log-ingestion-opensearch-engine"></a>

### Using the Centralized Logging with OpenSearch console
<a name="using-the-centralized-logging-with-opensearch-console"></a>

1. Sign in to the Centralized Logging with OpenSearch console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose **Create a log ingestion**.

1. In the AWS Services section, choose AWS CloudTrail.

1. Choose **Next**.

1. Under Specify settings, choose Automatic or Manual.
   + For **Automatic** mode, choose a CloudTrail in the dropdown list.
   + For **Manual** mode, enter the CloudTrail name.
   + (Optional) If you are ingesting CloudTrail logs from another account, select a [linked account](cross-account-ingestion.md) from the **Account** dropdown list first.

1. Under **Log Source**, Select **Amazon S3** or **CloudWatch** as the log source.

1. Choose **Next**.

1. In **the Specify OpenSearch domain** section, select an imported domain for the Amazon OpenSearch Service domain.

1. Choose **Yes** for **Sample dashboard** if you want to ingest an associated built-in Amazon OpenSearch Service dashboard.

1. You can change the **Index Prefix** of the target Amazon OpenSearch Service index if needed. The default prefix is your trail name.

1. In the **Log Lifecycle** section, enter the number of days to manage the Amazon OpenSearch Service index lifecycle. Centralized Logging with OpenSearch will create the associated [Index State Management (ISM)](https://opensearch.org/docs/latest/im-plugin/ism/index/) policy automatically for this pipeline.

1. In the **Select log processor** section, choose the log processor.

   1. When selecting Lambda as a log processor, you can configure the Lambda concurrency if needed.

   1. (Optional) OSI as log processor is now supported in these [Regions](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-opensearch-service-ingestion/). When OSI is selected, type in the minimum and maximum number of OCU. See more information [here](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion.html#ingestion-scaling).

1. Choose **Next**.

1. Add tags if needed.

1. Choose **Create**.

### Using the CloudFormation Stack
<a name="using-the-cloudformation-stack"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - CloudTrail Log Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CloudTrailLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CloudTrailLog.template)  |
| AWS China Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CloudTrailLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CloudTrailLog.template)  |

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
  <tr><td>Log Source Account ID</td><td>&lt;Optional&gt;</td><td>The AWS Account ID of the S3 bucket. Required for cross-account log ingestion (<a href="cross-account-ingestion.md">add a member account</a> first). By default, the Account ID you logged in at <b>Step 1</b> will be used.</td></tr>
  <tr><td>Log Source Region</td><td> <i>Optional input</i> </td><td>The AWS Region of the S3 bucket. By default, the Region you selected at <b>Step 2</b> will be used.</td></tr>
  <tr><td>Log Source Account Assume Role</td><td> <i>Optional input</i> </td><td>The IAM Role ARN used for cross-account log ingestion. Required for cross-account log ingestion (<a href="cross-account-ingestion.md">add a member account</a> first).</td></tr>
  <tr><td>KMS-CMK ARN</td><td> <i>Optional input</i> </td><td>The KMS-CMK ARN for encryption. Leave it blank to create a new AWS KMS key.</td></tr>
  <tr><td>Enable OpenSearch Ingestion as processor</td><td> <i>Optional input</i> </td><td>Ingestion table ARN. Leave empty if you do not use OSI as Processor.</td></tr>
  <tr><td>Amazon S3 Backup Bucket</td><td> {{&lt;Requires input&gt;}} </td><td>The Amazon S3 backup bucket name to store the failed ingestion logs.</td></tr>
  <tr><td>Engine Type</td><td> <code>OpenSearch</code> </td><td>The engine type of the OpenSearch.</td></tr>
  <tr><td>OpenSearch Domain Name</td><td> {{&lt;Requires input&gt;}} </td><td>The domain name of the Amazon OpenSearch Service cluster.</td></tr>
  <tr><td>OpenSearch Endpoint</td><td> {{&lt;Requires input&gt;}} </td><td>The OpenSearch endpoint URL. For example, <code>vpc-your_opensearch_domain_name-xcvgw6uu2o6zafsiefxubwuohe.us-east-1.es.amazonaws.com</code> </td></tr>
  <tr><td>Index Prefix</td><td> {{&lt;Requires input&gt;}} </td><td>The common prefix of OpenSearch index for the log. The index name will be <code>&lt;Index Prefix&gt;-&lt;Log Type&gt;-&lt;Other Suffix&gt;</code>.</td></tr>
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
  <tr><td>Index Suffix</td><td> <code>yyyy-MM-dd</code> </td><td>The common suffix format of OpenSearch index for the log (Example: yyyy-MM-dd, yyyy-MM-dd-HH). The index name will be <code>&lt;Index Prefix&gt;-&lt;Log Type&gt;-&lt;Index Suffix&gt;-000001</code>.</td></tr>
  <tr><td>Compression type</td><td> <code>best_compression</code> </td><td>The compression type to use to compress stored data. Available values are best_compression and default.</td></tr>
  <tr><td>Refresh Interval</td><td> <code>1s</code> </td><td>How often the index should refresh, which publishes its most recent changes and makes them available for searching. Can be set to -1 to disable refreshing. The default is 1s.</td></tr>
  <tr><td>EnableS3Notification</td><td> <code>True</code> </td><td>An option to enable or disable notifications for Amazon S3 buckets. The default option is recommended for most cases.</td></tr>
  <tr><td>LogProcessorRoleName</td><td> <i>Optional input</i> </td><td>Specify a role name for the log processor. The name should NOT duplicate an existing role name. If no name is specified, a random name is generated.</td></tr>
  <tr><td>QueueName</td><td> <i>Optional input</i> </td><td>Specify a queue name for an Amazon SQS queue. The name should NOT duplicate an existing queue name. If no name is given, a random name will be generated.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard"></a>

The dashboard includes the following visualizations.

| Visualization Name | Source Field | Description |
| --- | --- | --- |
| Global Control | awsRegion | Provides users with the ability to drill down data by Region. |
| Event History | log event | Presents a bar chart that displays the distribution of events over time. |
| Event by Account ID | userIdentity.accountId | Breaks down events based on the AWS account ID, enabling you to analyze activity patterns across different accounts within your organization. |
| Top Event Names | eventName | Shows the most frequently occurring event names, helping you identify common activities or potential anomalies. |
| Top Event Sources | eventSource | Highlights the top sources generating events, providing insights into the services or resources that are most active or experiencing the highest event volume. |
| Event Category | eventCategory | Categorizes events into different types or classifications, facilitating analysis and understanding of event distribution across categories. |
| Top Users | \* userIdentity.sessionContext.sessionIssuer.userName \* userIdentity.sessionContext.sessionIssuer.arn \* userIdentity.accountId \* userIdentity.sessionContext.sessionIssuer.type | Identifies the users or IAM roles associated with the highest number of events, aiding in user activity monitoring and access management. |
| Top Source IPs | sourceIPAddress | Lists the source IP addresses associated with events, enabling you to identify and investigate potentially suspicious or unauthorized activities. |
| Amazon S3 Access Denied | \* eventSource: s3\* \* errorCode: AccessDenied | Displays events where access to Amazon S3 resources was denied, helping you identify and troubleshoot permission issues or potential security breaches. |
| S3 Buckets | requestParameters.bucketName | Provides a summary of S3 bucket activity, including create, delete, and modify operations, allowing you to monitor changes and access patterns. |
| Top Amazon S3 Change Events | \* eventName \* requestParameters.bucketName | Presents the most common types of changes made to Amazon S3 resources, such as object uploads, deletions, or modifications, aiding in change tracking and auditing. |
| EC2 Change Event Count | \* eventSource: ec2\* \* eventName: (RunInstances or TerminateInstances or RunInstances or StopInstances) | Shows the total count of EC2-related change events, giving an overview of the volume and frequency of changes made to EC2 instances and resources. |
| EC2 Changed By | userIdentity.sessionContext.sessionIssuer.userName | Identifies the users or IAM roles responsible for changes to EC2 resources, assisting in accountability and tracking of modifications. |
| Top EC2 Change Events | eventName | Highlights the most common types of changes made to EC2 instances or related resources, allowing you to focus on the most significant or frequent changes. |
| Error Events | \* awsRegion \* errorCode \* errorMessage \* eventName \* eventSource \* sourceIPAddress \* userAgent \* userIdentity.accountId \* userIdentity.sessionContext.sessionIssuer.accountId \* userIdentity.sessionContext.sessionIssuer.arn \* userIdentity.sessionContext.sessionIssuer.type \* userIdentity.sessionContext.sessionIssuer.userName | Displays events that resulted in errors or failures, helping you identify and troubleshoot issues related to API calls or resource operations. |

You can access the built-in dashboard in Amazon OpenSearch Service to view log data. For more information, see the [Access Dashboard](getting-started.md#step-4-access-the-dashboard).

You can choose the following image to view the high-resolution sample dashboard.

 **CloudTrail logs sample dashboard.**

![image32](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image32.png)

## Create log ingestion (Light Engine)
<a name="create-log-ingestion-light-engine"></a>

### Using the Centralized Logging with OpenSearch console
<a name="using-the-centralized-logging-with-opensearch-console-1"></a>

1. Sign in to the Centralized Logging with OpenSearch console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose **Create a log ingestion**.

1. In the **AWS Services** section, choose AWS CloudTrail.

1. Choose **Next**.

1. Under Specify settings, choose Automatic or Manual.
   + For **Automatic** mode, choose a CloudTrail in the dropdown list.
   + For **Manual** mode, enter the CloudTrail name.
   + (Optional) If you are ingesting CloudTrail logs from another account, select a [linked account](cross-account-ingestion.md) from the **Account** dropdown list first.

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
<a name="using-the-cloudformation-stack-1"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - CloudTrail Log Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesCloudTrailPipeline.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesCloudTrailPipeline.template)  |
| AWS China Regions |  ![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesCloudTrailPipeline.template)  |

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
  <tr><td>Staging Bucket Prefix</td><td> <code>AWSLogs/CloudTrailLogs</code> </td><td>The storage directory for logs in the temporary storage area should ensure the uniqueness and non-overlapping of the Prefix for different pipelines.</td></tr>
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
  <tr><td>Centralized Table Name</td><td> <code>CloudTrail</code> </td><td>Table name for writing data to the centralized database. You can modify it if needed.</td></tr>
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
  <tr><td>Grafana URL</td><td> {{&lt;Requires input&gt;}} </td><td>Grafana access URL for example: https://alb-72277319.us-west-2.elb.amazonaws.com.</td></tr>
  <tr><td>Grafana Service Account Token</td><td> {{&lt;Requires input&gt;}} </td><td>Grafana Service Account Token: Service Account Token created in Grafana.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-1"></a>

 **CloudTrail log sample dashboard**

![image33](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image33.png)
