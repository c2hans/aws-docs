---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-amazon-elasticache-clusters-for-at-rest-encryption.html
---

# Monitor Amazon ElastiCache clusters for at-rest encryption
<a name="monitor-amazon-elasticache-clusters-for-at-rest-encryption"></a>

*Abhishek Agawane, Amazon Web Services*

## Summary
<a name="monitor-amazon-elasticache-clusters-for-at-rest-encryption-summary"></a>

Amazon ElastiCache is an Amazon Web Services (AWS) service that provides a high-performance, scalable, and cost-effective caching solution for distributing an in-memory data store or cache environment in the cloud. It retrieves data from high-throughput and low-latency, in-memory data stores. This functionality makes it a popular choice for real-time use cases such as caching, session stores, gaming, geo-spatial services, real-time analytics, and queuing. ElastiCache offers Redis and Memcached data stores, both of which provide sub-millisecond response times.

Data encryption helps prevent unauthorized users from reading sensitive data available on your Redis clusters and their associated cache storage systems. This includes data saved to persistent media, known as *data at rest*, and data that can be intercepted as it travels through the network between clients and cache servers, known as *data in transit*.

You can enable at-rest encryption for ElastiCache (Redis OSS) when you create a replication group, by setting the `AtRestEncryptionEnabled`** **parameter to `true`. When this parameter is enabled, it encrypts the disk during sync, backup, and swap operations, and encrypts backups stored in Amazon Simple Storage Service (Amazon S3). You cannot enable at-rest encryption on an existing replication group. When you create a replication group, you can enable encryption at rest in these two ways:
+ By choosing the **Default **option, which uses service-managed encryption at rest.
+ By using a customer managed key and providing the key ID or Amazon Resource Name (ARN) from AWS Key Management Service (AWS KMS).

This pattern provides a security control that monitors for API calls and generates an Amazon EventBridge Events event on the `CreateReplicationGroup` operation. This event calls an AWS Lambda function, which runs a Python script. The function gets the replication group ID from the event JSON input, and performs the following checks to determine whether there's an unencrypted cluster:
+ Checks if the `AtRestEncryptionEnabled`** **key exists.
+ If `AtRestEncryptionEnabled`** **exists, checks the value to see if it is `true`.
+ If the `AtRestEncryptionEnabled`** **value is set to `false`, sets a variable that tracks violations and sends a violation message to an email address you provide, by using an Amazon Simple Notification Service (Amazon SNS) notification.

## Prerequisites and limitations
<a name="monitor-amazon-elasticache-clusters-for-at-rest-encryption-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ An S3 bucket to upload the provided Lambda code.
+ An email address where you would like to receive violation notifications.
+ ElastiCache logging enabled, for access to all the API logs.

**Limitations**
+ This detective control is regional and must be deployed in each AWS Region that you want to monitor.
+ The control supports replication groups that are running in a virtual private cloud (VPC).
+ The control supports replication groups that are running the following node types:
  + R7g, R6gd, R6g, R5, R4, R3
  + M7g, M6g, M5, M4, M3
  + T4g, T3, T2
  + C7gn

**Product versions**
+ Supports ElastiCache (Redis OSS) version 3.2.6 or later, and Valkey 7.2 or later

## Architecture
<a name="monitor-amazon-elasticache-clusters-for-at-rest-encryption-architecture"></a>

**Workflow architecture**

![Workflow for monitoring ElastiCache clusters.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2917ebc2-3cfe-4530-887d-2c7eb7085453/images/59a36936-e9a8-4f12-a49d-776ff7959053.png)

1. The user launches an ElastiCache replication group through the AWS Management Console, the AWS Command Line Interface (AWS CLI), or an API call.

1. ElastiCache generates EventBridge events when the `CreateReplicationGroup `API is called.

1. An EventBridge rule triggers and calls the Lambda function for compliance checking.

1. The Lambda function processes the event and checks if at-rest encryption is enabled on the ElastiCache cluster.

1. If encryption violation is detected, the Lambda function publishes a notification message to an SNS topic.

1. Amazon SNS delivers an email notification to administrators about the encryption compliance violation.

**Automation and scale**
+ If you are using AWS Organizations, you can use [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) to deploy this template in multiple accounts that you want to monitor.

## Tools
<a name="monitor-amazon-elasticache-clusters-for-at-rest-encryption-tools"></a>

**AWS services**
+ [Amazon ElastiCache](https://docs.aws.amazon.com/elasticache/) makes it easy to set up, manage, and scale distributed in-memory cache environments in the AWS Cloud. It provides a high performance, resizable, and cost-effective in-memory cache while removing complexity associated with deploying and managing a distributed cache environment. ElastiCache works with both the Redis and Memcached engines.
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/) helps you model and set up your AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle. You can use a template to describe your resources and their dependencies, and launch and configure them together as a stack, instead of managing resources individually. You can manage and provision stacks across multiple AWS accounts and AWS Regions.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/) delivers a near real-time stream of system events that describe changes in AWS resources. EventBridge becomes aware of operational changes as they occur and takes corrective action as necessary, by sending messages to respond to the environment, activating functions, making changes, and capturing state information.
+ [AWS Lambda](https://aws.amazon.com/lambda/) is a compute service that supports running code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically from a few requests per day to thousands per second. You pay only for the compute time that you consume—there is no charge when your code is not running.
+ [Amazon SNS](https://aws.amazon.com/sns/) coordinates and manages the sending of messages between publishers and clients, including web servers and email addresses. Subscribers receive all messages published to the topics to which they subscribe, and all subscribers to a topic receive the same messages.

**Code**

The code for this pattern is available in the GitHub [Monitor Amazon ElastiCache clusters for at-rest encryption](https://github.com/aws-samples/sample-Monitor_Amazon_ElastiCache_clusters_for_at-rest_encryption) repository. See the [Epics section](#monitor-amazon-elasticache-clusters-for-at-rest-encryption-epics) for information about how to use the files in the repository.

## Best practices
<a name="monitor-amazon-elasticache-clusters-for-at-rest-encryption-best-practices"></a>

**Deployment**
+ Make sure that AWS CloudTrail is logging ElastiCache API calls before you deploy this control.
+ This is a regional control; deploy the control in each AWS Region where you use ElastiCache.
+ Validate the solution in dev/test environments before you deploy it to production.

**Security**
+ For enhanced control over encryption keys, use customer managed KMS keys.
+ Review AWS Identity and Access Management (IAM) permissions to ensure least privilege access for the Lambda execution role.
+ Set up alerts for messages in the dead letter queue.

**Operations**
+ Set appropriate log retention to balance compliance needs with cost.
+ Tune the reserved concurrency of Lambda to adjust based on your ElastiCache creation frequency.
+ Subscribe multiple email addresses to Amazon SNS for team notifications.

**Monitoring**
+ Review Amazon CloudWatch alarms to make sure that alarm thresholds match your operational needs.
+ Monitor Lambda metrics execution duration and error rates regularly.
+ Audit violations regularly to review encryption compliance notifications.

## Epics
<a name="monitor-amazon-elasticache-clusters-for-at-rest-encryption-epics"></a>

### Deploy the security control
<a name="deploy-the-security-control"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the code from GitHub. | Clone or download the [code repository](https://github.com/aws-samples/sample-Monitor_Amazon_ElastiCache_clusters_for_at-rest_encryption) from GitHub. The repository contains the files  `index.py` and `elasticache_encryption_at_rest.yml`. | Cloud architect |
| Create Lambda deployment packages. | Create two .zip files from the Python code:+ Create `ElastiCache-EncryptionAtRest.zip`, which contains `index.py`.<br />+ Use the following command:<pre>zip ElastiCache-EncryptionAtRest.zip index.py</pre> | Cloud architect |
| Upload the code to an S3 bucket. | 1. Create a new S3 bucket or use an existing S3 bucket to upload the Lambda code. <br />2. Zip the Lambda code (`index.py`) and name it `ElastiCache-EncryptionAtRest.zip`. <br />3. Upload the .zip file to the S3 bucket. This bucket must be in the same AWS Region as the resources that you want to evaluate.  | Cloud architect  |
| Deploy the CloudFormation template. | Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/) in the same AWS Region as the S3 bucket, and deploy the `elasticache_encryption_at_rest.yml` file that's provided in the code repository. In the next epic, provide values for the template parameters. | Cloud architect  |

### Complete the parameters in the CloudFormation template
<a name="complete-the-parameters-in-the-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Provide the S3 bucket name. | Enter the name of the S3 bucket that you created or selected in the first epic. This S3 bucket contains the .zip file for the Lambda code and must be in the same AWS Region as the CloudFormation template and the resource that will be evaluated.  | Cloud architect |
| Provide the S3 key. | Provide the location of the Lambda code .zip file in your S3 bucket, without leading slashes (for example, `ElasticCache-EncryptionAtRest.zip` or `controls/ElasticCache-EncryptionAtRest.zip`). | Cloud architect  |
| Provide an email address. | Provide an active email address where you want to receive violation notifications.  | Cloud architect |
| Specify a logging level. | Specify the logging level and verbosity. + `Info` designates detailed informational messages on the application’s progress and should be used only for debugging. <br />+ `Error` designates error events that could still allow the application to continue running. <br />+ `Warning` designates potentially harmful situations. | Cloud architect  |

### Confirm the subscription
<a name="confirm-the-subscription"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Confirm the email subscription. | When the CloudFormation template deploys successfully, it sends a subscription message to the email address you provided. To receive notifications, you must confirm this email subscription. | Cloud architect |

## Troubleshooting
<a name="monitor-amazon-elasticache-clusters-for-at-rest-encryption-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| ** **Lambda function not triggered<br /> | **Symptom**: No logs in CloudWatch after you create or modify ElastiCache clusters.<br />**Solutions**:+ Verify EventBridge rule status: <pre>aws events describe-rule --name <rule-name></pre><br />+ Confirm that the Lambda resource-based policy allows EventBridge invocation.<br />+ Confirm that the EventBridge event pattern matches ElastiCache API calls. |
| No email notifications<br /> | **Symptom**: The Lambda function runs successfully, but you don’t receive any email notifications.<br />**Solutions**:+ Confirm your Amazon SNS subscription through the email confirmation link.<br />+ Check spam or junk folders for Amazon SNS emails.<br />+ Verify the Amazon Resource Name (ARN) for the Amazon SNS topic in the Lambda environment variable: `OUTBOUND_TOPIC_ARN`<br />+ Test Amazon SNS manually: <pre>aws sns publish --topic-arn <arn> --message "Test"</pre> |
| Permission issues | **Symptom**: *Access denied* errors in Lambda function CloudWatch logs.<br />**Solutions**:+ Verify that the Lambda execution role has the required ElastiCache read permissions.<br />+ Confirm that the AWS KMS key policy includes the Lambda execution role.<br />+ Make sure that the Amazon SNS topic policy allows Lambda to publish. |

## Related resources
<a name="monitor-amazon-elasticache-clusters-for-at-rest-encryption-resources"></a>
+ [Create a stack from the CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) (CloudFormation documentation)
+ [At-rest encryption in ElastiCache (Redis OSS)](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/at-rest-encryption.html) (ElastiCache documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
