---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/vpc-flow-logs.html
---

# VPC Flow Logs
<a name="vpc-flow-logs"></a>

 [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) enable you to capture information about the IP traffic going to and from network interfaces in your VPC.

You can create a log ingestion into Amazon OpenSearch Service either by using the Centralized Logging with OpenSearch console or by deploying a standalone CloudFormation stack.

**Important**
Centralized Logging with OpenSearch supports VPCs who publish the flow log data to an Amazon S3 bucket or a CloudWatch log group. When publishing to Amazon S3, the S3 bucket Region must be the same as the Centralized Logging with OpenSearch solution Region.
The Amazon OpenSearch Service index is rotated on a daily basis by default, and you can adjust the index in the Additional Settings.

## Create log ingestion (OpenSearch Engine)
<a name="create-log-ingestion-opensearch-engine-7"></a>

### Using the Centralized Logging with OpenSearch Console
<a name="using-the-centralized-logging-with-opensearch-console-12"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose the Create a log ingestion button.

1. In the **AWS Services** section, choose **VPC Flow Logs**.

1. Choose **Next**.

1. Under **Specify settings**, choose **Automatic** or **Manual** for **VPC Flow Log enabling**. The automatic mode will enable the VPC Flow Log and save the logs to a centralized S3 bucket if logging is not enabled yet.
   + For **Automatic mode**, choose the VPC from the dropdown list.
   + For Manual mode, enter the VPC Name and VPC Flow Logs location.
   + (Optional) If you are ingesting VPC Flow Logs from another account, select a [linked account](cross-account-ingestion.md) from the **Account** dropdown list first.

1. Under **Log Source**, select **S3** or **CloudWatch** as the source.

1. Choose **Next**.

1. In the Specify OpenSearch domain section, select an imported domain for the Amazon OpenSearch Service domain.

1. Choose **Yes** for **Sample dashboard** if you want to ingest an associated built-in Amazon OpenSearch Service dashboard.

1. You can change the **Index Prefix** of the target Amazon OpenSearch Service index if needed. The default prefix is your VPC name.

1. In the **Log Lifecycle** section, enter the number of days to manage the Amazon OpenSearch Service index lifecycle. The Centralized Logging with OpenSearch will create the associated [Index State Management (ISM)](https://opensearch.org/docs/latest/im-plugin/ism/index/) policy automatically for this pipeline.

1. In the **Select log processor** section, choose the log processor.

   1. When selecting Lambda as a log processor, you can configure the Lambda concurrency if needed.

   1. (Optional) OSI as log processor is now supported in these [Regions](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-opensearch-service-ingestion/). When OSI is selected, please type in the minimum and maximum number of OCU. See more information [here](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion.html#ingestion-scaling).

1. Choose **Next**.

1. Add tags if needed.

1. Choose **Create**.

### Using the CloudFormation Stack
<a name="using-the-cloudformation-stack-12"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - VPC Flow Logs Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Standard Regions |  [https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/VPCFlowLog.template](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/VPCFlowLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/VPCFlowLog.template)  |
| AWS China Regions |  [https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/VPCFlowLog.template](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/VPCFlowLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/VPCFlowLog.template)  |

1. Log in to the AWS Management Console and select the preceding button to launch the AWS CloudFormation template. You can also download the template as a starting point for your own implementation.

1. To launch the stack in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/vpc-flow-logs.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-12"></a>

The dashboard includes the following visualizations.

| Visualization Name | Source Field | Description |
| --- | --- | --- |
| Global Filters | \* account-id \* Region \* vpc-id \* subnet-id \* action \* flow-direction \* log-status \* protocol-code \* type | The charts are filtered according to Account ID, Region, VPC ID, and other conditions. |
| Total Requests | \* log event | Shows the total number of network requests logged by VPC Flow Logs during a selected time period. |
| Request History | \* log event | Presents a bar chart that displays the distribution of events over time. |
| Requests By VPC ID | \* vpc-id | Displays the proportional breakdown of network requests by source VPC using a pie chart. |
| Total Requests By Action | \* action | Displays the total volume of requests segmented by action over time. |
| Total Bytes | \* bytes | Provides visibility into overall bandwidth usage and traffic patterns across the monitored VPCs, subnets, network interfaces, and security groups. |
| Total Packets | \* packets | Displays total logged packets over time to visualize trends, surges, and dips. |
| Bytes Metric | \* bytes \* flow-direction | Shows the distribution of incoming (Ingress) and outgoing (Egress) network traffic volumes in bytes across the range of flows logged by VPC Flow Logs over a time period. |
| Requests By Direction | \* flow-direction | Provides visibility into the proportional composition of incoming versus outgoing requests. |
| Requests By Direction | \* flow-direction | Displays the total number of network flows logged by VPC Flow Logs segmented by traffic direction - Ingress vs Egress. |
| Requests By Type | \* type | Shows the volume of flows for each type. This provides visibility into the protocol composition of network requests traversing the environment. |
| Top Source Bytes | \* srcaddr \* bytes | Displays the source IP addresses transmitting the highest outbound volume of data during the selected time period. |
| Top Destination Bytes | \* dstaddr \* bytes | Enables you to monitor and analyze outbound traffic from your VPC to external destinations. |
| Top Source Requests | \* srcaddr | Allows you to see which resources inside your VPC are initiating external requests. |
| Top Destination Requests | \* dstaddr | Allows you to see which external hosts are being contacted most by your VPC resources. |
| Requests by Protocol | \* protocol-code | Displays network flows logged by VPC Flow Logs segmented by traffic type - TCP, UDP, ICMP. |
| Requests by Status | \* log-status | Provides a breakdown of network flows by their traffic status - Accepted, Rejected, or Other. |
| Top Sources AWS Services | \* pkt-src-aws-service | Show the proportional distribution of flows originating from top AWS sources like Amazon S3, CloudFront, Lambda, etc. during the selected time period. |
| Top Destination AWS Services | \* pkt-dst-aws-service | Provide visibility into IP traffic going to and from AWS services located outside your VPC. By enabling flow logs on VPC subnets/interfaces and filtering on traffic with an ACCEPT action, you can view outbound flows from your VPC to various AWS services. |
| Network Flow | \* srcaddr \* dstaddr | Allows you to view information about the IP traffic going to and from network interfaces in your VPC. |
| Heat Map | \* srcaddr \* dstaddr | Offers a visual summary of connections between source and destination IPs in your flow log data. |
| Egress Traffic Path | \* traffic-path | Allows you to enable flow logging on VPC network interfaces to capture information about all IP traffic going to and from that interface. |
| Search | \* @timestamp \* account-id \* vpc-id \* flow-direction \* action \* protocol-code \* srcaddr \* scaport \* dstaddr \* dstport \* bytes \* packets \* log-status | Searching through the detailed flow log data allows pinpoint analysis of traffic around security events, network issues, changes in usage patterns, and more. |

You can access the built-in dashboard in Amazon OpenSearch Service to view log data. For more information, see the [Access Dashboard](getting-started.md#step-4-access-the-dashboard).

 **VPC Flow Logs sample dashboard.**

![image44](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image44.png)

## Create log ingestion (Light Engine)
<a name="create-log-ingestion-light-engine-5"></a>

### Using the Centralized Logging with OpenSearch Console
<a name="using-the-centralized-logging-with-opensearch-console-13"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose the Create a log ingestion button.

1. In the **AWS Services** section, choose **AWS VPC Flow**.

1. Choose **Light Engine**, choose **Next**.

1. Under **Specify settings**, choose **Automatic** or **Manual** for **CloudFront logs enabling**. The automatic mode will detect the CloudFront log location automatically.
   + For **Automatic** mode, choose the VPC Flow from the dropdown list.
   + For Standard Log, the solution will automatically detect the log location if logging is enabled.
   + For Manual mode, enter the VPC Flow ID and VPC Flow Log location.
   + (Optional) If you are ingesting CloudFront logs from another account, select a [linked account](cross-account-ingestion.md#add-a-member-account) from the **Account** dropdown list first.

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
<a name="using-the-cloudformation-stack-13"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - VpcFlow Standard Log Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Regions |  [https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesVpcFlowPipeline.template](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesVpcFlowPipeline.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesVpcFlowPipeline.template)  |
| AWS China Regions |  [https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesVpcFlowPipeline.template](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesVpcFlowPipeline.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesVpcFlowPipeline.template)  |

1. Log in to the AWS Management Console and select the preceding button to launch the AWS CloudFormation template. You can also download the template as a starting point for your own implementation.

1. To launch the stack in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.

   1. Parameters for **Pipeline settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/vpc-flow-logs.html)

   1. Parameters for **Destination settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/vpc-flow-logs.html)

   1. Parameters for **Scheduler settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/vpc-flow-logs.html)

   1. Parameters for **Notification settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/vpc-flow-logs.html)

   1. Parameters for **Dashboard settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/vpc-flow-logs.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-13"></a>

 **VPC Flow Logs sample dashboard.**

![image45](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image45.png)
