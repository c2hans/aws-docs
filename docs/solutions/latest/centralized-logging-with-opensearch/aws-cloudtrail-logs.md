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
| AWS Regions |  [![Launch solution](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CloudTrailLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CloudTrailLog.template)  |
| AWS China Regions |  [![Launch solution](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CloudTrailLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CloudTrailLog.template)  |

1. Log in to the AWS Management Console and select the preceding button to launch the AWS CloudFormation template. You can also download the template as a starting point for your own implementation.

1. To launch the stack in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-cloudtrail-logs.html)

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

![image32](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image32.png)

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
| AWS Regions |  [![Launch solution](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesCloudTrailPipeline.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesCloudTrailPipeline.template)  |
| AWS China Regions |  ![Launch solution](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesCloudTrailPipeline.template)  |

1. Log in to the AWS Management Console and select the preceding button to launch the AWS CloudFormation template. You can also download the template as a starting point for your own implementation.

1. To launch the stack in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.

   1. Parameters for **Pipeline settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-cloudtrail-logs.html)

   1. Parameters for **Destination settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-cloudtrail-logs.html)

   1. Parameters for **Scheduler settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-cloudtrail-logs.html)

   1. Parameters for **Notification settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-cloudtrail-logs.html)

   1. Parameters for **Dashboard settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-cloudtrail-logs.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-1"></a>

 **CloudTrail log sample dashboard**

![image33](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image33.png)
