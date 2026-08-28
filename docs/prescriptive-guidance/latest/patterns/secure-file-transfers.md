---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/secure-file-transfers.html
---

# Secure file transfers by using Transfer Family, Amazon Cognito, and GuardDuty
<a name="secure-file-transfers"></a>

*Manoj Kumar, Amazon Web Services*

## Summary
<a name="secure-file-transfers-summary"></a>

This solution helps you securely transfer files through an SFTP server by using AWS Transfer Family. It includes automated malware scanning capabilities through [Malware Protection for S3](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-malware-protection-s3.html), a feature of Amazon GuardDuty. It is designed for organizations that need to securely exchange files with external parties and validate that all incoming files are scanned for malware before being processed.

The infrastructure as code (IaC) templates provided with this pattern help you deploy the following:
+ A secure SFTP server with Amazon Cognito authentication through AWS Lambda
+ Amazon Simple Storage Service (Amazon S3) buckets for uploads and incoming files that have been scanned for malware
+ A virtual private cloud (VPC)-based architecture with public and private subnets across multiple Availability Zones
+ IP-based access control for both ingress and egress traffic, with configurable allow and deny lists
+ Automated malware scanning through GuardDuty
+ Intelligent file routing based on scan results through Amazon EventBridge and Lambda
+ Real-time notifications for security incidents through Amazon Simple Notification Service (Amazon SNS)
+ Encryption for Amazon S3 buckets and Lambda environment variables through AWS Key Management Service (AWS KMS)
+ Amazon Virtual Private Cloud (Amazon VPC) endpoints for access without internet exposure
+ Comprehensive logging through Amazon CloudWatch integration

## Prerequisites and limitations
<a name="secure-file-transfers-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ Permissions in AWS Identity and Access Management (IAM) to perform the actions described in this pattern, including deploying AWS CloudFormation templates that provision IAM roles
+ GuardDuty, [enabled](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html) in the target account
+ Malware Protection for S3, [enabled](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-s3-get-started-independent.html) in the target account
+ Service quotas allow you to create the following in the target account:
  + One VPC
  + One private subnet
  + One public subnet
  + Three elastic IP addresses
  + Sufficient Lambda concurrency limits
+ A valid email address for security-related notifications
+ (Optional) A list of IP addresses or CIDR ranges that you want to allow or deny
+ (Optional) AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

**Limitations **
+ Malware Protection for S3 is subject to quotas, such as maximum file sizes. For more information, see [Quotas in Malware Protection for S3](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-s3-quotas-guardduty.html) and [Supportability of Amazon S3 features](https://docs.aws.amazon.com/guardduty/latest/ug/supported-s3-features-malware-protection-s3.html) in the GuardDuty documentation.
+ This solution uses Amazon Cognito username and password authentication only. Certificate-based or other authentication methods are not supported in this template. By default, this solution does not configure multi-factor authentication (MFA).
+ The solution implements IP-based access control through security groups only.

## Architecture
<a name="secure-file-transfers-architecture"></a>

The following architecture diagram shows the resources that are deployed in this pattern. This solution uses Amazon Cognito for user authentication and authorization. An AWS Transfer Family SFTP server is used for file uploads. Files are stored in Amazon S3 buckets, and Amazon GuardDuty scans the files for malware. Amazon SNS sends an email notification if malware is detected.

![Using GuardDuty and Cognito to securely transfer files to Amazon S3 buckets.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/39d98ebe-2844-4ccd-a497-9b796b7da5e8/images/05567010-e189-40e7-acab-74e77c4f8525.png)

The diagram shows the following workflow:

1. A user connects to the SFTP server endpoint in AWS Transfer Family. This initiates the authentication process with the Amazon Cognito user pool.

1. A Lambda function initiates the authentication and authorization process and validates the user’s credentials with Amazon Cognito.

1. The Lambda function returns the `UploadBucket` Amazon S3 bucket as the home directory. The user assumes the IAM role for the Transfer Family server, and the Lambda function notifies the user that they have been successfully authenticated.

1. The user uploads a file to the Transfer Family SFTP server. The file is stored in the `UploadBucket` Amazon S3 bucket.

1. GuardDuty scans the file for malware. The potential scan results are `NO_THREATS_FOUND`, `THREATS_FOUND`, `UNSUPPORTED`, `ACCESS_DENIED`, and `FAILED`. For sample results, see [S3 object scan result](https://docs.aws.amazon.com/guardduty/latest/ug/monitor-with-eventbridge-s3-malware-protection.html#s3-object-scan-status-malware-protection-s3-ev) in the GuardDuty documentation.

1. An EventBridge rule detects the scan result event.

1. EventBridge initiates the file-routing Lambda function.

1. The Lambda function processes the event and filters the files based on the scan results as follows:
   + Files that have a `NO_THREATS_FOUND` scan result are sent to the `CleanBucket` Amazon S3 bucket.
   + Files that have a `THREATS_FOUND` scan result are sent to the `MalwareBucket` Amazon S3 bucket.
   + Files that have an `UNSUPPORTED` scan result are sent to the `ErrorBucket` Amazon S3 bucket.
   + Files that have an `ACCESS_DENIED` scan result are sent to the `ErrorBucket` Amazon S3 bucket.
   + Files that have a `FAILED` scan result are sent to the `ErrorBucket` Amazon S3 bucket.

   All files are encrypted with an AWS KMS key.

1. If a file was sent to the `MalwareBucket` Amazon S3 bucket, the Lambda function initiates an Amazon SNS topic. The Amazon SNS topic sends an email notification to an email address that you configure.

## Tools
<a name="secure-file-transfers-tools"></a>

**AWS services**
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications you run on AWS in real time.
+ [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) provides authentication, authorization, and user management for web and mobile apps.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) is a continuous security monitoring service that analyzes and processes logs to identify unexpected and potentially unauthorized activity in your AWS environment.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html) helps you transfer files into and out of AWS storage services over the SFTP, FTPS, or FTP protocols.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

**Code repository**

The code for this pattern is available in the GitHub [AWS Transfer Family and GuardDuty Malware Scanning Solution](https://github.com/aws-samples/sample-secure-transfer-family-code) repository.

## Best practices
<a name="secure-file-transfers-best-practices"></a>

The CloudFormation template provided is designed to incorporate many AWS best practices, such as least-privilege permissions for IAM roles and policies, encryption at rest and in transit, and automatic key rotation. For production environments, consider implementing the following additional recommendations:
+ Enable [MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html) for Amazon Cognito users
+ Implement [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) for distributed denial of service (DDoS) protection
+ Configure [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) for continuous compliance monitoring
+ Implement [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) for comprehensive API logging
+ Set up [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) for threat detection beyond malware scanning
+ Implement [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html) for centralized security management
+ Use [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) for credential management
+ Implement network traffic monitoring with [Traffic Mirroring](https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html)
+ Configure [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) for sensitive data discovery and protection in Amazon S3
+ Implement regular security assessments and penetration testing
+ Establish a formal incident response plan
+ Implement automated patching for all components
+ Conduct regular security training for administrators
+ Set up [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) for multi-account security management

## Epics
<a name="secure-file-transfers-epics"></a>

### Deploy the resources
<a name="deploy-the-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | Enter the following command to clone the [AWS Transfer Family and GuardDuty malware scanning solution](https://github.com/aws-samples/sample-secure-transfer-family-code) repository to your local workstation:<pre>git clone https://github.com/aws-samples/sample-secure-transfer-family-code.git</pre> | App developer, DevOps engineer |
| Create the CloudFormation stack. | 1. Follow the instructions in the CloudFormation documentation to create a stack through the CloudFormation console or through the [AWS CLI](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/service_code_examples.html#create-stack-sdk). Configure the following parameters:`UploadBucketName` - Upload bucket name`CleanBucketName` - Clean files bucket name`MalwareBucketName` - Malware files bucket name`ErrorBucketName` - Error files bucket name`SecurityTeamEmail` - Email address for alerts`VpcCIDR` - CIDR range for VPC`PublicSubnet1CIDR` - CIDR range for public subnet 1`PublicSubnet2CIDR` - CIDR range for public subnet 2`PrivateSubnet1CIDR` - CIDR range for private subnet 1`PrivateSubnet2CIDR` - CIDR range for private subnet 2`AllowedIPAddresses` - Allowed IP addresses or CIDR ranges`EnableEgressRules` – If you want to enable egress rules for security groups, enter `true`. If you want disable the egress rules, enter `false`.<br />2. Wait for the stack deployment to complete.<br />3. In the stack creation outputs, make note of the SFTP server endpoint. You need this value later. | Cloud administrator, DevOps engineer |

### Configure the resources
<a name="configure-the-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Turn on malware protection. | 1. Sign in to the AWS Management Console and open the [GuardDuty console](https://console.aws.amazon.com/guardduty/).<br />2. In the navigation pane, choose **Malware Protection for S3**.<br />3. In the **Protected buckets** section, choose **Enable**.<br />4. Under **Enter S3 bucket details**, enter the **Amazon S3 bucket** name. Alternatively, choose **Browse S3** to select a bucket. Choose the `UploadBucket` Amazon S3 bucket.<br />5. Under **Prefix**, select **All the objects in the S3 bucket**.<br />6. Under **Tag scanned objects**, select **Tag objects**.<br />7. In the **Service access** section, choose **Create and use a new service role**.<br />8. Choose **Enable**. | Cloud administrator, AWS administrator |
| Add users to the user pool. | Add one or more users to the Amazon Cognito user pool. For instructions, see [Managing users in your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users.html) in the Amazon Cognito documentation. | Cloud administrator, AWS administrator |

### Test the SFTP server
<a name="test-the-sftp-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Connect to the SFTP server endpoint. | 1. Enter the following command to get the SFTP server endpoint, where `<stack-name>` is the name of your CloudFormation stack:<pre>TRANSFER_ENDPOINT=$(aws cloudformation describe-stacks \<br />  --stack-name <stack-name> \<br />  --query 'Stacks[0].Outputs[?OutputKey==`TransferServerEndpoint`].OutputValue' \<br />  --output text)</pre><br />2. Enter the following command to connect to the SFTP server:<pre>sftp user@company.com@$TRANSFER_ENDPOINT</pre><br />3. Validate that you receive the following prompt:<pre>sftp></pre><br />This indicates that you can now enter commands to perform file transfers. | App developer, Cloud administrator, Cloud architect, DevOps engineer |

## Troubleshooting
<a name="secure-file-transfers-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| User authentication fails | 1. Verify that the user exists in the Amazon Cognito user pool.<br />2. Validate that the user is confirmed and enabled.<br />3. Make sure the user is providing the correct password.<br />4. Check for errors in CloudWatch Logs.For a list of AWS CLI commands that can help you perform these troubleshooting steps, see *Useful commands for troubleshooting* in the [Additional information](#secure-file-transfers-additional) section. |
| SFTP authentication fails | 1. Verify that the user exists in the Amazon Cognito user pool.<br />2. Validate that the user is confirmed and enabled.<br />3. Make sure the user is providing the correct password.<br />4. Verify that the IP address is allowed in the security group for the AWS Transfer Family server.<br />5. Check for errors in the logs for the authentication Lambda function.<br />6. Verify that the IAM role for AWS Transfer Family has correct permissions.For a list of AWS CLI commands that can help you perform these troubleshooting steps, see *Useful commands for troubleshooting* in the [Additional information](#secure-file-transfers-additional) section. |
| File upload access denied | 1. Verify that the AWS KMS key permissions are properly configured.<br />2. Check the Amazon S3 bucket policies.<br />3. Confirm that the IAM role permissions are properly configured.<br />4. Verify that the VPC endpoints are properly configured<br />5. Verify that the IAM role for AWS Transfer Family has correct permissions.For a list of AWS CLI commands that can help you perform these troubleshooting steps, see *Useful commands for troubleshooting* in the [Additional information](#secure-file-transfers-additional) section. |
| No malware scanning | 1. Enable GuardDuty in your account.<br />2. Enable Malware Protection for S3.<br />3. Verify that the Amazon EventBridge rule is active.<br />4. Check for errors in the logs for the file-routing Lambda function.<br />5. Verify that notifications are configured correctly in Amazon SNS.For a list of AWS CLI commands that can help you perform these troubleshooting steps, see *Useful commands for troubleshooting* in the [Additional information](#secure-file-transfers-additional) section. |
| Lambda function errors | 1. Check the VPC configuration.<br />2. Verify that the VPC endpoints are properly configured.<br />3. Verify that the IAM role for AWS Transfer Family has correct permissions.<br />4. Check for errors in CloudWatch Logs.<br />5. Verify that the AWS KMS key permissions are properly configured.For a list of AWS CLI commands that can help you perform these troubleshooting steps, see *Useful commands for troubleshooting* in the [Additional information](#secure-file-transfers-additional) section. |

## Related resources
<a name="secure-file-transfers-resources"></a>
+ [Transfer Family web apps](https://docs.aws.amazon.com/transfer/latest/userguide/web-app.html) (Transfer Family documentation)

## Additional information
<a name="secure-file-transfers-additional"></a>

**Useful commands for troubleshooting**

Check the status of a CloudFormation stack:

```
aws cloudformation describe-stacks \
  --stack-name <STACK_NAME>
```

List all users in an Amazon Cognito user pool:

```
aws cognito-idp list-users \
  --user-pool-id <USER_POOL_ID>
```

View logs for Lambda functions:

```
aws logs describe-log-groups \
  --log-group-name-prefix /aws/lambda/
```

Check the status of GuardDuty:

```
aws guardduty list-detectors
```

Check security group rules:

```
aws ec2 describe-security-groups \
  --group-ids <SECURITY_GROUP_ID> \
  --output table
```

Check the status of the AWS Transfer Family server:

```
aws transfer describe-server \
  --server-id <SERVER_ID>
```

List all files in an Amazon S3 bucket:

```
aws s3 ls s3://<BUCKET_NAME>/ \
  --recursive
```

Check the status of an EventBridge rule:

```
aws events describe-rule \
  --name <RULE_NAME>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
