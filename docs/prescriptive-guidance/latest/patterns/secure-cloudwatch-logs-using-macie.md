---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/secure-cloudwatch-logs-using-macie.html
---

# Secure sensitive data in CloudWatch Logs by using Amazon Macie
<a name="secure-cloudwatch-logs-using-macie"></a>

*Anisha Salunkhe, Omar Franco, and David Guardiola, Amazon Web Services*

## Summary
<a name="secure-cloudwatch-logs-using-macie-summary"></a>

This pattern shows you how to use Amazon Macie to automatically detect sensitive data in an Amazon CloudWatch Logs log group by implementing a comprehensive security monitoring workflow. The solution uses Amazon Data Firehose to stream CloudWatch Logs entries to Amazon Simple Storage Service (Amazon S3). Macie periodically scans this bucket for personally identifiable information (PII), financial data, and other sensitive content. The infrastructure is deployed through a AWS CloudFormation template that provisions all necessary AWS services and configurations.

CloudWatch Logs often contains application data that can inadvertently include sensitive user information. This can create compliance and security risks. Traditional log monitoring approaches lack automated sensitive data detection capabilities. This can make it difficult to identify and respond to potential data exposures in real-time.

This pattern helps security teams and compliance officers maintain data confidentiality by providing automated detection and alerting for sensitive data in logging systems. This solution enables proactive incident response through Amazon Simple Notification Service (Amazon SNS) notifications, and it automatically isolates sensitive data to a secure Amazon S3 bucket. You can customize the detection patterns and integrate the workflow with your existing security operations processes.

## Prerequisites and limitations
<a name="secure-cloudwatch-logs-using-macie-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Permissions to create a CloudFormation stack
+ A CloudWatch Logs log group that you want to monitor
+ An active email address to receive notifications from Amazon SNS
+ Access to [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html)
+ (Optional) Access to the AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

**Limitations**
+ Macie is subject to service quotas. For more information, see [Quotas for Macie](https://docs.aws.amazon.com/macie/latest/user/macie-quotas.html) in the Macie documentation.

## Architecture
<a name="secure-cloudwatch-logs-using-macie-architecture"></a>

**Target architecture**

The following diagram shows the workflow for using Macie to examine CloudWatch Logs log entries for sensitive data.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c9979070-09ab-4331-b969-5eff26fb2baa/images/d02f34ce-a7d1-4f96-a430-22975224eb9d.png)

The workflow shows the following steps:

1. The CloudWatch Logs log group generates the logs, which are subject to the subscription filter.

1. The subscription filter forwards the logs to Amazon Data Firehose.

1. The logs are encrypted with an AWS Key Management Service (AWS KMS) key when they pass through the Amazon Data Firehose delivery stream.

1. The delivery stream delivers the logs to the exported logs bucket in Amazon S3.

1. At 4 AM each day, Amazon EventBridge initiates an AWS Lambda function that starts a Macie scan for sensitive data in the exported logs bucket.

1. If Macie identifies sensitive data in the bucket, a Lambda function removes the log from the exported logs bucket and encrypts it with an AWS KMS key.

1. The Lambda function isolates the logs that contain sensitive data in the data isolation bucket.

1. The identification of sensitive data initiates an Amazon SNS topic.

1. Amazon SNS sends an email notification to an email address that you configure with information about the logs that contain sensitive data.

**Deployed resources**

The CloudFormation template deploys the following resources in your target AWS account and AWS Region:
+ Two Amazon S3 [buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html#BasicsBucket):
  + An exported logs bucket for storing the CloudWatch Logs data
  + A data isolation bucket to store the sensitive information
+ An Amazon EventBridge [rule](https://docs.aws.amazon.com/macie/latest/user/findings-monitor-events-eventbridge.html) that responds to Macie findings
+ AWS Lambda [functions](https://docs.aws.amazon.com/lambda/latest/dg/concepts-basics.html#gettingstarted-concepts-function) that initiate events and export logs to Amazon S3 buckets
+ An Amazon SNS [topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html) and [subscription](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html)
+ An Amazon Data Firehose [stream](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html#key-concepts)
+ A Macie [session](https://docs.aws.amazon.com/macie/latest/user/macie-terms.html#macie-terms-session)
+ A Macie [custom data identifier](https://docs.aws.amazon.com/macie/latest/user/macie-terms.html#macie-terms-cdi)
+ A CloudWatch Logs [subscription filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html)
+ AWS KMS [keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) to encrypt the logs stored in the buckets
+ The necessary AWS Identity and Access Management (IAM) [roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) and [policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) for the solution

## Tools
<a name="secure-cloudwatch-logs-using-macie-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so you can monitor them and archive them securely.
+ [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) helps you deliver real-time streaming data to other AWS services, custom HTTP endpoints, and HTTP endpoints owned by supported third-party service providers.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, sources such as AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) helps you discover sensitive data, provides visibility into data security risks, and enables automated protection against those risks.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Code repository**

The code for this pattern is available in the GitHub [sample-macie-for-securing-cloudwatch-logs](https://github.com/aws-samples/sample-macie-for-securing-cloudwatch-logs) repository.

## Best practices
<a name="secure-cloudwatch-logs-using-macie-best-practices"></a>

Follow the [CloudFormation best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html) in the CloudFormation documentation.

## Epics
<a name="secure-cloudwatch-logs-using-macie-epics"></a>

### Deploy the solution
<a name="deploy-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the code repository. | Enter the following command to clone the repository to your local workstation:<pre>git clone https://github.com/aws-samples/sample-macie-for-securing-cloudwatch-logs</pre> | App developer |
| (Optional) Edit the CloudFormation template. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/secure-cloudwatch-logs-using-macie.html) | App developer |
| Option 1 – Deploy using script with command-line parameters. | Enter the following command to deploy the solution by using command line parameters, where the value for `enable-macie` is `true` only if Amazon Macie is not already enabled:<pre>./scripts/test-macie-solution.sh --deploy-stack \<br />  --stack-name <stack name> \<br />  --email <email address> \<br />  --enable-macie <true or false> \<br />  --region <region> \<br />  --resource-name <prefix for all resources> \<br />  --bucket-name <bucket name></pre> | General AWS |
| Option 2 – Deploy using script with environment variables. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/secure-cloudwatch-logs-using-macie.html) | General AWS |
| Option 3 – Deploy using the AWS CLI. | Enter the following command to deploy the solution by using the AWS CLI, where the value for `EnableMacie` is `true` only if Amazon Macie is not already enabled:<pre>aws cloudformation create-stack \<br />  --region us-east-1 \<br />  --stack-name macie-for-securing-cloudwatch-logs \<br />  --template-body file://app/main.yml \<br />  --capabilities CAPABILITY_IAM \<br />  --parameters \<br />    ParameterKey=ResourceName,ParameterValue=<prefix for all resources> \<br />    ParameterKey=BucketName,ParameterValue=<bucket name> \<br />    ParameterKey=LogGroupName,ParameterValue=<path for log group> \<br />    ParameterKey=SNSTopicEndpointEmail,ParameterValue=<email address> \<br />    ParameterKey=EnableMacie,ParameterValue=<true or false></pre> |  |
| Option 4 – Deploy through the AWS Management Console. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/secure-cloudwatch-logs-using-macie.html) | General AWS |
| Monitor the deployment status and confirm deployment. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/secure-cloudwatch-logs-using-macie.html) | General AWS |
| Confirm the Amazon SNS subscription. | Follow the instructions in [Confirm your Amazon SNS subscription](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.confirm.html) in the Amazon SNS documentation to confirm your Amazon SNS subscription. | App developer |

### Test the solution
<a name="test-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Option 1 – Test with automated reporting. | If you used the default stack name, enter the following command to test the solution:<pre>./scripts/test-macie-solution.sh \<br />   --full-test</pre><br />If you used a custom stack name, enter the following command to test the solution:<pre>./scripts/test-macie-solution.sh \<br />   --full-test \<br />   --stack-name <stack name></pre><br />If you used a custom stack name and custom parameters, enter the following command to test the solution:<pre>./scripts/test-macie-solution.sh --full-test \<br />  --stack-name <stack name> \<br />  --region <region> \<br />  --log-group <log group path></pre> | General AWS |
| Option 2 – Test with targeted validation. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/secure-cloudwatch-logs-using-macie.html) | General AWS |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Option 1 – Perform automated cleanup. | If you used the default stack name, enter the following command to delete the stack:<pre>./scripts/cleanup-macie-solution.sh \<br />  --full-cleanup</pre><br />If you used a custom stack name, enter the following command to delete the stack:<pre>./scripts/cleanup-macie-solution.sh \<br />  --full-cleanup \<br />  --stack-name <stack name></pre><br />If you used a custom stack name and custom parameters, enter the following command to delete the stack:<pre>./scripts/cleanup-macie-solution.sh \<br />  --full-cleanup \<br />  --stack-name <stack name> \<br />  --region <region> \<br />  --disable-macie <true or false></pre> | General AWS |
| Option 2 – Perform step-by-step cleanup. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/secure-cloudwatch-logs-using-macie.html) | General AWS |
| Verify clean up. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/secure-cloudwatch-logs-using-macie.html) | General AWS |

## Troubleshooting
<a name="secure-cloudwatch-logs-using-macie-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| CloudFormation stack status shows **CREATE\_FAILED**. | The CloudFormation template is configured to publish logs to CloudWatch Logs. You can view the logs in the AWS Management Console so that you don't have to connect to your Amazon EC2 instance. For more information, see [View CloudFormation logs in the console](https://aws.amazon.com/blogs/devops/view-cloudformation-logs-in-the-console/) (AWS blog post). |
| CloudFormation `delete-stack` command fails. | Some resources must be empty before they can be deleted. For example, you must delete all objects in an Amazon S3 bucket or remove all instances in an Amazon EC2 security group before you can delete the bucket or security group. For more information, see [Delete stack fails](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-delete-stack-fails) in the Amazon S3 documentation. |
| Error when parsing a parameter. | When you use the AWS CLI or the CloudFormation console to pass in a value, add the quotation marks. |

## Related resources
<a name="secure-cloudwatch-logs-using-macie-resources"></a>
+ [Architecture best practices for storage](https://aws.amazon.com/architecture/storage/?docs3_bp1&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all) (AWS website)
+ [Filter pattern syntax for metric filters, subscription filters, filter log events, and Live Tail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html) (CloudWatch Logs documentation)
+ [Designing and implementing logging and monitoring with Amazon CloudWatch](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/welcome.html) (AWS Prescriptive Guidance)
+ [Troubleshooting CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html) (CloudFormation documentation)
