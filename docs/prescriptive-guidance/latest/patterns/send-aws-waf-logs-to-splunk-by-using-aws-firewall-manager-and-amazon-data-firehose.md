---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/send-aws-waf-logs-to-splunk-by-using-aws-firewall-manager-and-amazon-data-firehose.html
---

# Send AWS WAF logs to Splunk by using AWS Firewall Manager and Amazon Data Firehose
<a name="send-aws-waf-logs-to-splunk-by-using-aws-firewall-manager-and-amazon-data-firehose"></a>

*Michael Friedenthal, Aman Kaur Gandhi, and JJ Johnson, Amazon Web Services*

## Summary
<a name="send-aws-waf-logs-to-splunk-by-using-aws-firewall-manager-and-amazon-data-firehose-summary"></a>

Historically, there were two ways to move data into Splunk: a push or a pull architecture. A *pull architecture* offers delivery data guarantees through retries, but it requires dedicated resources in Splunk that poll data. Pull architectures usually are not real time because of the polling. A *push architecture* in typically has lower latency, is more scalable, and reduces operational complexity and costs. However, it doesn’t guarantee delivery and typically requires agents.

Splunk integration with Amazon Data Firehose delivers real-time streaming data to Splunk through an HTTP event collector (HEC). This integration provides the advantages of both push and pull architectures—it guarantees data delivery through retries, is near real-time, and is low latency and low complexity. The HEC quickly and efficiently sends data over HTTP or HTTPS directly to Splunk. HECs are token-based, which eliminates the need to hardcode credentials in an application or in supporting files.

In an AWS Firewall Manager policy, you can configure logging for all of the AWS WAF web ACL traffic in all of your accounts, and you can then use a Firehose delivery stream to send that log data to Splunk for monitoring, visualization, and analysis. This solution provides the following benefits:
+ Central management and logging for AWS WAF web ACL traffic in all of your accounts
+ Splunk integration with a single AWS account
+ Scalability
+ Near real-time delivery of log data
+ Cost optimization through the use of a serverless solution, so you don't have to pay for unused resources.

## Prerequisites and limitations
<a name="send-aws-waf-logs-to-splunk-by-using-aws-firewall-manager-and-amazon-data-firehose-prereqs"></a>

**Prerequisites **
+ An active AWS account that is part of an organization in AWS Organizations.
+ You must have the following permissions to enable logging with Firehose:
  + `iam:CreateServiceLinkedRole`
  + `firehose:ListDeliveryStreams`
  + `wafv2:PutLoggingConfiguration`
+ AWS WAF and its web ACLs must be configured. For instructions, see [Getting started with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html).
+ AWS Firewall Manager must be setup. For instructions, see [AWS Firewall Manager prerequisites](https://docs.aws.amazon.com/waf/latest/developerguide/fms-prereq.html).
+ The Firewall Manager security policies for AWS WAF must be configured. For instructions, see [Getting started with AWS Firewall ManagerAWS WAF policies](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms.html).
+ Splunk must be setup with a public HTTP endpoint that can be reached by Firehose.

**Limitations**
+ The AWS accounts must be managed in a single organization in AWS Organizations.
+ The web ACL must be in the same Region as the delivery stream. If you are capturing logs for Amazon CloudFront, create the Firehose delivery stream in the US East (N. Virginia) Region, `us-east-1`.
+ The Splunk add-on for Firehose is available for paid Splunk Cloud deployments, distributed Splunk Enterprise deployments, and single-instance Splunk Enterprise deployments. This add-on is not supported for free trial Splunk Cloud deployments.

## Architecture
<a name="send-aws-waf-logs-to-splunk-by-using-aws-firewall-manager-and-amazon-data-firehose-architecture"></a>

**Target technology stack**
+ Firewall Manager
+ Firehose
+ Amazon Simple Storage Service (Amazon S3)
+ AWS WAF
+ Splunk

**Target architecture **

The following image shows how you can use Firewall Manager to centrally log all AWS WAF data and send it to Splunk through Firehose.

![Architecture diagram showing sending AWS WAF log data to Splunk through Amazon Data Firehose](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/3dfeaae0-985a-42b8-91c4-ece081f0b51b/images/669169b1-caa4-419b-9988-19806ded54eb.png)

1. The AWS WAF web ACLs send firewall log data to Firewall Manager.

1. Firewall Manager sends the log data to Firehose.

1. The Firehose delivery stream forwards the log data to Splunk and to an S3 bucket. The S3 bucket acts as a backup in the event of an error with the Firehose delivery stream.

**Automation and scale**

This solution is designed to scale and accommodate all AWS WAF web ALCs within the organization. You can configure all web ACLs to use the same Firehose instance. However, if you want to set up and use multiple Firehose instances, you can.

## Tools
<a name="send-aws-waf-logs-to-splunk-by-using-aws-firewall-manager-and-amazon-data-firehose-tools"></a>

**AWS services**
+ [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) is a security management service that helps you to centrally configure and manage firewall rules across your accounts and applications in AWS Organizations.
+ [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) helps you deliver real-time [streaming data](http://aws.amazon.com/streaming-data/) to other AWS services, custom HTTP endpoints, and HTTP endpoints owned by supported third-party service providers, such as Splunk.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html) is a web application firewall that helps you monitor HTTP and HTTPS requests that are forwarded to your protected web application resources.

**Other tools**
+ [Splunk](https://docs.splunk.com/Documentation) helps you monitor, visualize, and analyze log data.

## Epics
<a name="send-aws-waf-logs-to-splunk-by-using-aws-firewall-manager-and-amazon-data-firehose-epics"></a>

### Configure Splunk
<a name="configure-splunk"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the Splunk App for AWS. | 1. Sign in to your Splunk heavy forwarder. The default URL is `http://<IP address>:8000`.<br />2. In the left navigation, next to **Apps**, choose the gear button.<br />3. Choose **Browse more apps**.<br />4. Search for **AWS**.<br />5. For **Splunk App for AWS**, choose **Install**.<br />6. Enter your Splunk.com sign-in credentials, accept the terms and conditions, and then choose **Login and Install**.<br />7. Choose **Done**. | Security administrator, Splunk administrator |
| Install the add-on for AWS WAF. | Repeat the previous instructions to install the **AWS Web Application Firewall Add-on** for Splunk. | Security administrator, Splunk administrator |
| Install and configure the Splunk add-on for Firehose. | 1. Install and configure the Splunk add-on for Firehose. As part of the installation and configuration, if necessary for your Splunk platform, you set up an HTTP Event Collector and prepare the infrastructure to send the log data to your indexers. See the instructions that correspond to your Splunk deployment:[Splunk Cloud deployment](https://docs.splunk.com/Documentation/AddOns/released/Firehose/InstallationstepsformanagedSplunkCloud) (Splunk documentation)[Distributed Splunk Enterprise deployment](https://docs.splunk.com/Documentation/AddOns/released/Firehose/InstallationstepsfordistributedSplunkEnterprise) (Splunk documentation)[Single-instance Splunk Enterprise deployment](https://docs.splunk.com/Documentation/AddOns/released/Firehose/InstallationstepsforsingleinstanceSplunkEnterprise) (Splunk documentation)Stop this procedure after you have installed and configured the Splunk add-on. Do not proceed with the instructions for configuring Firehose to send data to the Splunk platform.<br />2. Make note of the HTTP event collector token and the HTTP endpoint. You need this value later, when you configure the delivery stream. | Security administrator, Splunk administrator |

### Create the Firehose delivery stream
<a name="create-the-akf-delivery-stream"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Grant Firehose access to a Splunk destination. | Configure the access policy that permits Firehose to access a Splunk destination and back up the log data to an S3 bucket. For more information, see [Grant Firehose access to a Splunk destination](https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-splunk). | Security administrator |
| Create a Firehose delivery stream. | In the same account where you manage the web ACLs for AWS WAF, create a delivery stream in Firehose. You are required to have an IAM role when creating a delivery stream. Firehose assumes that IAM role and gains access to the specified S3 bucket. For instructions, see [Creating a delivery stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html). Note the following:+ The delivery stream name must start with `aws-waf-logs-`.<br />+ For the source, choose **Direct PUT**.<br />+ For **S3 backup mode**, choose **Backup all events**, and then choose an existing bucket or create a new one.<br />+ For the destination, follow the instructions in [Choose Splunk for your destination](https://docs.aws.amazon.com/firehose/latest/dev/create-destination.html#create-destination-splunk) in the Firehose documentation. For information about the values for Splunk endpoints and endpoint types, see [Configure Amazon Data Firehose](https://docs.splunk.com/Documentation/AddOns/released/Firehose/ConfigureFirehose) in the Splunk documentation.<br />Repeat this process for each token that you configured in the HTTP event collector. | Security administrator |
| Test the delivery stream. | Test the delivery stream to validate that it is properly configured. For instructions, see [Test using Splunk as the destination](https://docs.aws.amazon.com/firehose/latest/dev/test-drive-firehose.html#test-drive-destination-splunk) in the Firehose documentation. | Security administrator |

### Configure Firewall Manager to log data
<a name="configure-firewall-manager-to-log-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the Firewall Manager policies. | The Firewall Manager policies must be configured to enable logging and to forward logs to the correct Firehose delivery stream. For more information and instructions, see [Configuring logging for an AWS WAF policy](https://docs.aws.amazon.com/waf/latest/developerguide/waf-policies.html#waf-policies-logging-config). | Security administrator |

## Related resources
<a name="send-aws-waf-logs-to-splunk-by-using-aws-firewall-manager-and-amazon-data-firehose-resources"></a>

**AWS resources**
+ [Logging web ACL traffic](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html) (AWS WAF documentation)
+ [Configuring logging for an AWS WAF policy](https://docs.aws.amazon.com/waf/latest/developerguide/waf-policies.html#waf-policies-logging-config) (AWS WAF documentation)
+ [Tutorial: Sending VPC Flow Logs to Splunk Using Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/vpc-splunk-tutorial.html) (Firehose documentation)
+ [How do I push VPC flow logs to Splunk using Amazon Data Firehose?](https://aws.amazon.com/premiumsupport/knowledge-center/push-flow-logs-splunk-firehose/) (AWS Knowledge Center)
+ [Power data ingestion into Splunk using Amazon Data Firehose](https://aws.amazon.com/blogs/big-data/power-data-ingestion-into-splunk-using-amazon-kinesis-data-firehose/) (AWS blog post)

**Splunk documentation**
+ [Splunk Add-on for Amazon Data Firehose](https://docs.splunk.com/Documentation/AddOns/released/Firehose/About)
