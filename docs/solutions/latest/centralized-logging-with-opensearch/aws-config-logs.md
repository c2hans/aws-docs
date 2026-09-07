---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-config-logs.html
---

# AWS Config logs
<a name="aws-config-logs"></a>

By default, AWS Config delivers configuration history and snapshot files to your Amazon S3 bucket.

You can create a log ingestion into Amazon OpenSearch Service either by using the Centralized Logging with OpenSearch console or by deploying a standalone CloudFormation stack.

**Important**
AWS Config must be enabled in the same Region as the Centralized Logging with OpenSearch solution.
The Amazon S3 bucket Region must be the same as the Centralized Logging with OpenSearch solution.
The Amazon OpenSearch Service index is rotated on a daily basis by default, and you can adjust the index in the Additional Settings.

## Create log ingestion (OpenSearch Engine)
<a name="create-log-ingestion-opensearch-engine-8"></a>

### Using the Centralized Logging with OpenSearch Console
<a name="using-the-centralized-logging-with-opensearch-console-14"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose the Create a log ingestion button.

1. In the AWS Services section, choose AWS Config Logs.

1. Choose **Next**.

1. Under Specify settings, choose Automatic or Manual for Log creation.
   + For **Automatic mode**, make sure that the S3 bucket location is correct, and enter the **AWS Config Name**.
   + For Manual mode, enter the AWS Config Name and Log location.
   + (Optional) If you are ingesting VPC Flow Logs from another account, select a [linked account](cross-account-ingestion.md) from the **Account** dropdown list first.

1. Choose **Next**.

1. In the Specify OpenSearch domain section, select an imported domain for the Amazon OpenSearch Service domain.

1. Choose **Yes** for **Sample dashboard** if you want to ingest an associated built-in Amazon OpenSearch Service dashboard.

1. You can change the **Index Prefix** of the target Amazon OpenSearch Service index if needed. The default prefix is your VPC name.

1. In the **Log Lifecycle** section, enter the number of days to manage the Amazon OpenSearch Service index lifecycle. The Centralized Logging with OpenSearch will create the associated [Index State Management (ISM)](https://opensearch.org/docs/latest/im-plugin/ism/index/) policy automatically for this pipeline.

1. Choose **Next**.

1. Add tags if needed.

1. Choose **Create**.

### Using the CloudFormation Stack
<a name="using-the-cloudformation-stack-14"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - AWS Config Log Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Standard Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/ConfigLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/ConfigLog.template)  |
| AWS China Regions |  [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/ConfigLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/ConfigLog.template)  |

1. Log in to the AWS Management Console and select the preceding button to launch the AWS CloudFormation template. You can also download the template as a starting point for your own implementation.

1. To launch the stack in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-config-logs.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-14"></a>

The dashboard includes the following visualizations.

| Visualization Name | Source Field | Description |
| --- | --- | --- |
| Global Filters | awsAccountId awsRegion resourceType resourceId resourceName | The charts are filtered according to Account ID, Region, Resource Type, and other conditions. |
| Total Change Events | log event | Shows the number of configuration changes detected across all AWS resources during a selected time period. |
| Top Resource Types | resourceType | Displays the breakdown of configuration changes by the most frequently modified AWS resource types during a selected time period. |
| Config History | log event | Presents a bar chart that displays the distribution of events over time. |
| Total Delete Events | log event | Shows the number of AWS resource deletion events detected by AWS Config during a selected time period. |
| Config Status | configurationItemStatus | Displays the operational state of the AWS Config service across monitored Regions and accounts. |
| Top S3 Changes | resourceName | Displays the Amazon S3 buckets undergoing the highest number of configuration changes during a selected time period. |
| Top Changed Resources | resourceName resourceId resourceType | Displays the individual AWS resources undergoing the highest number of configuration changes during a selected time period. |
| Top VPC Changes | resourceId | Presents a bar chart that Displays the Amazon VPCs undergoing the highest number of configuration changes during a selected time period. |
| Top Subnet Changes | resourceId | Delivers targeted visibility into the subnets undergoing the most transformation for governance, security, and stability. |
| Top Network Interface Changes | resourceId | Spotlights the Amazon VPC network interfaces seeing the most configuration changes during a selected period. |
| Top Security Group Changes | resourceId | Top 10 changed groups rank by total modification count. |
| EC2 Config | @timestamp awsAccountId awsRegion resourceId configurationItemStatus | Allows reconstructing the incremental changes applied to EC2 configurations over time for auditing. |
| RDS Config | @timestamp awsAccountId awsRegion resourceId resourceName configurationItemStatus | Shows the configuration history and changes detected by AWS Config for RDS database resources |
| Latest Config Changes | @timestamp awsAccountId awsRegion resourceType resourceId resourceName relationships configurationItemStatus | Offers an at-a-glance overview of infrastructure modifications. |

You can access the built-in dashboard in Amazon OpenSearch Service to view log data. For more information, see the [Access Dashboard](getting-started.md#step-4-access-the-dashboard).

 **AWS Config logs sample dashboard.**

![image46](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image46.png)
