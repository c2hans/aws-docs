---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/check-an-amazon-cloudfront-distribution-for-access-logging-https-and-tls-version.html
---

# Check an Amazon CloudFront distribution for access logging, HTTPS, and TLS version
<a name="check-an-amazon-cloudfront-distribution-for-access-logging-https-and-tls-version"></a>

*SaiJeevan Devireddy and Bijesh Bal, Amazon Web Services*

## Summary
<a name="check-an-amazon-cloudfront-distribution-for-access-logging-https-and-tls-version-summary"></a>

This pattern checks an Amazon CloudFront distribution to make sure that it uses HTTPS, uses Transport Layer Security (TLS) version 1.2 or later, and has access logging enabled. CloudFront is a service provided by Amazon Web Services (AWS) that speeds up the distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called *edge locations*. When a user requests content that you're serving with CloudFront, the request is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance.

This pattern provides an AWS Lambda function that is initiated when Amazon CloudWatch Events detects the CloudFront API call [CreateDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html), [CreateDistributionWithTags](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistributionWithTags.html), or [UpdateDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistribution.html). The custom logic in the Lambda function evaluates all CloudFront distributions that were created or updated in the AWS account. It sends a violation notification by using Amazon Simple Notification Service (Amazon SNS) if it detects the following violations:
+ Global checks:
  + Custom certificate doesn't use TLS version 1.2
  + Logging is disabled for distribution
+ Origin checks:
  + Origin isn't configured with TLS version 1.2
  + Communication with origin is allowed on a protocol other than HTTPS
+ Behavior checks:
  + Default behavior communication is allowed on a protocol other than HTTPS
  + Custom behavior communication is allowed on a protocol other than HTTPS

## Prerequisites and limitations
<a name="check-an-amazon-cloudfront-distribution-for-access-logging-https-and-tls-version-prerequisites-and-limitations"></a>

**Prerequisites **
+ An active AWS account
+ An email address where you want to receive the violation notifications

**Limitations **
+ This security control doesn't check for existing Cloudfront distributions unless an update has been made to the distribution.
+ CloudFront is considered a global service and isn't tied to a specific AWS Region. However, Amazon CloudWatch Logs and AWS Cloudtrail API logging for global services occur in the US East (N. Virginia) Region (`us-east-1`). Therefore, this security control for CloudFront must be deployed and maintained in `us-east-1`. This single deployment monitors all distributions for CloudFront. Do not deploy the security control in any other AWS Regions. (Deployment in other Regions will result in a failure to initiate CloudWatch Events and the Lambda function, and no SNS notifications.)
+ This solution has gone through extensive testing with CloudFront web content distributions. It does not cover real-time messaging protocol (RTMP) streaming distributions.

## Architecture
<a name="check-an-amazon-cloudfront-distribution-for-access-logging-https-and-tls-version-architecture"></a>

**Target technology stack  **
+ Lambda function
+ SNS topic
+ Amazon EventBridge rule

**Target architecture **

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/1ae60f8f-3eaf-40f5-b01f-06e30e5604ce/images/e1521c48-99f6-4ec6-9e53-8713f3cf5776.png)

**Automation and scale**
+ If you are using AWS Organizations, you can use [AWS Cloudformation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) to deploy the attached template across multiple accounts that you want to monitor.

## Tools
<a name="check-an-amazon-cloudfront-distribution-for-access-logging-https-and-tls-version-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) – CloudFormation is a service that helps you model and set up AWS resources by using infrastructure as code.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html) – EventBridge delivers a stream of real-time data from your own applications, software as a service (SaaS) applications, and AWS services, routing that data to targets such as Lambda functions.
+ [AWS Lambda ](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)– Lambda supports running code without provisioning or managing servers.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is a highly scalable object storage service that can be used for a wide range of storage solutions, including websites, mobile applications, backups, and data lakes.
+ [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) – Amazon SNS coordinates and manages the delivery or sending of messages between publishers and clients, including web servers and email addresses. Subscribers receive all messages published to the topics to which they subscribe, and all subscribers to a topic receive the same messages.

**Code**

The attached code includes:
+ A .zip file that contains the Lambda code (index.py)
+ A CloudFormation template (.yml file) that you run to deploy the Lambda code

## Epics
<a name="check-an-amazon-cloudfront-distribution-for-access-logging-https-and-tls-version-epics"></a>

### Upload the security control
<a name="upload-the-security-control"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the S3 bucket for the Lambda code. | On the Amazon S3 console, create a S3 bucket with an unique name that does not contain leading slashes. An S3 bucket name is globally unique, and the namespace is shared by all AWS accounts. Your S3 bucket must be in the Region where you are planning to deploy the Lambda code. | Cloud architect |
| Upload the Lambda code to the S3 bucket. | Upload the Lambda code (cloudfront\_ssl\_log\_lambda.zip file) that's provided in the *Attachments *section to the S3 bucket you created in the previous step. | Cloud architect |

### Deploy the CloudFormation template
<a name="deploy-the-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the CloudFormation template. | On the AWS CloudFormation console, in the same AWS Region as the S3 bucket, deploy the CloudFormation template (cloudfront-ssl-logging.yml) that's provided in the *Attachments *section.  | Cloud architect |
| Specify the S3 bucket name. | For the **S3 Bucket** parameter, specify the name of the S3 bucket that you created in the first epic. | Cloud architect |
| Specify the Amazon S3 key name for the Lambda file. | For the **S3 Key** parameter, specify the Amazon S3 location of the Lambda code .zip file in your S3 bucket. Do not include leading slashes (for example, you can enter lambda.zip or controls/lambda.zip). | Cloud architect |
| Provide a notification email address. | For the **Notification email** parameter, provide an email address where you would like to receive the violation notifications. | Cloud architect |
| Define the logging level. | For the **Lambda Logging level** parameter, define the logging level for your Lambda function. Choose one of the following values: [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/check-an-amazon-cloudfront-distribution-for-access-logging-https-and-tls-version.html) | Cloud architect |

### Confirm the subscription
<a name="confirm-the-subscription"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Confirm the subscription. | When the CloudFormation template has been deployed successfully, a new SNS topic is created and a subscription message is sent to the email address you provided. You must confirm this email subscription to receive violation notifications. | Cloud architect |

## Related resources
<a name="check-an-amazon-cloudfront-distribution-for-access-logging-https-and-tls-version-related-resources"></a>
+ [AWS CloudFormation information](https://aws.amazon.com/cloudformation/)
+ [Creating a stack on the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) (CloudFormation documentation)
+ [CloudFront logging](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/logging.html) (CloudFront documentation)
+ [Amazon S3 information](https://aws.amazon.com/s3/)
+ [AWS Lambda information](https://aws.amazon.com/lambda/)

## Attachments
<a name="attachments-1ae60f8f-3eaf-40f5-b01f-06e30e5604ce"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/1ae60f8f-3eaf-40f5-b01f-06e30e5604ce/attachments/attachment.zip)
