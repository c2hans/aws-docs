---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/verify-that-elb-load-balancers-require-tls-termination.html
---

# Verify that ELB load balancers require TLS termination
<a name="verify-that-elb-load-balancers-require-tls-termination"></a>

*Priyanka Chaudhary, Amazon Web Services*

## Summary
<a name="verify-that-elb-load-balancers-require-tls-termination-summary"></a>

On the Amazon Web Services (AWS) Cloud, Elastic Load Balancing (ELB) automatically distributes incoming application traffic across multiple targets, such as Amazon Elastic Compute Cloud (Amazon EC2) instances, containers, IP addresses, and AWS Lambda functions. The load balancers use listeners to define the ports and protocols that the load balancer uses to accept traffic from users. Application Load Balancers make routing decisions at the application layer and use the HTTP/HTTPS protocols. Classic Load Balancers make routing decisions at either the transport layer, by using TCP or Secure Sockets Layer (SSL) protocols, or at the application layer, by using HTTP/HTTPS.

This pattern provides a security control that examines multiple event types for Application Load Balancers and Classic Load Balancers. When the function is invoked, AWS Lambda inspects the event and ensures that the load balancer is compliant.

The function initiates an Amazon CloudWatch Events event on the following API calls: [CreateLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLoadBalancer.html), [CreateLoadBalancerListeners](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLoadBalancerListeners.html), [DeleteLoadBalancerListeners](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DeleteLoadBalancerListeners.html), [CreateLoadBalancerPolicy](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLoadBalancerPolicy.html), [SetLoadBalancerPoliciesOfListener](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_SetLoadBalancerPoliciesOfListener.html), [CreateListener](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateListener.html), [DeleteListener](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeleteListener.html), and [ModifyListener](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyListener.html). When the event detects one of these APIs, it calls AWS Lambda, which runs a Python script. The Python script evaluates to see if the listener contains an SSL certificate, and if the policy that is applied is using Transport Layer Security (TLS). If the SSL policy is determined to be anything other than TLS, the function sends an Amazon Simple Notification Service (Amazon SNS) notification to the user with the relevant information.

## Prerequisites and limitations
<a name="verify-that-elb-load-balancers-require-tls-termination-prereqs"></a>

**Prerequisites **
+ An active AWS account

**Limitations **
+ This security control does not check for existing load balancers, unless an update is made to the load balancer listeners.
+ This security control is regional. You must deploy it in each AWS Region you want to monitor.

## Architecture
<a name="verify-that-elb-load-balancers-require-tls-termination-architecture"></a>

**Target architecture**

![Ensuring that load balancers require TLS termination.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/da99cda2-ac34-4791-a2bd-d37264d8d3d9/images/af92b3c8-32bb-45eb-a2a8-d8276fb3e824.png)

**Automation and scale**
+ If you are using [AWS Organizations](https://aws.amazon.com/organizations/), you can use [AWS Cloudformation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) to deploy this template in multiple accounts that you want to monitor.

## Tools
<a name="verify-that-elb-load-balancers-require-tls-termination-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) – AWS CloudFormation helps you model and set up your AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle. You can use a template to describe your resources and their dependencies, and launch and configure them together as a stack, instead of managing resources individually.
+ [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) – Amazon CloudWatch Events delivers a near real-time stream of system events that describe changes in AWS resources.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – AWS Lambda is a compute service that supports running code without provisioning or managing servers.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is a highly scalable object storage service that can be used for a wide range of storage solutions, including websites, mobile applications, backups, and data lakes.
+ [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) – Amazon Simple Notification Service (Amazon SNS) coordinates and manages the delivery or sending of messages between publishers and clients, including web servers and email addresses. Subscribers receive all messages published to the topics to which they subscribe, and all subscribers to a topic receive the same messages.

**Code**

This pattern includes the following attachments:
+ `ELBRequirestlstermination.zip` – The Lambda code for the security control.
+ `ELBRequirestlstermination.yml` – The CloudFormation template that sets up the event and Lambda function.

## Epics
<a name="verify-that-elb-load-balancers-require-tls-termination-epics"></a>

### Set up the S3 bucket
<a name="set-up-the-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Define the S3 bucket. | On the [Amazon S3 console](https://console.aws.amazon.com/s3/), choose or create an S3 bucket to host the Lambda code .zip file. This S3 bucket must be in the same AWS Region as the load balancer that you want to evaluate. An S3 bucket name is globally unique, and the namespace is shared by all AWS accounts. The S3 bucket name cannot include leading slashes. | Cloud architect |
| Upload the Lambda code. | Upload the Lambda code (`ELBRequirestlstermination.zip` file) that's provided in the *Attachments *section to the S3 bucket. | Cloud architect |

### Deploy the CloudFormation template
<a name="deploy-the-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch the AWS CloudFormation template. | Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/) in the same AWS Region as your S3 bucket and deploy the attached template `ELBRequirestlstermination.yml`. For more information about deploying AWS CloudFormation templates, see [Creating a stack on the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the CloudFormation documentation. | Cloud architect |
| Complete the parameters in the template. | When you launch the template, you'll be prompted for the following information:+ **S3 bucket:** Specify the bucket that you created or selected in the first epic. This is where you uploaded the attached Lambda code (`ELBRequirestlstermination.zip` file).<br />+ **S3 key:** Specify the location of the Lambda .zip file in your S3 bucket (for example, `ELBRequirestlstermination.zip` or `controls/ELBRequirestlstermination.zip`). Do not include leading slashes.<br />+ **Notification email:** Provide an active email address where you want to receive Amazon SNS notifications.<br />+ **Lambda logging level:** Specify the logging level and frequency for the Lambda function. Use **Info** to log detailed informational messages on progress, **Error** for error events that would still allow the deployment to continue, and **Warning** for potentially harmful situations. | Cloud architect |

### Confirm the subscription
<a name="confirm-the-subscription"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Confirm the subscription. | When the CloudFormation template deploys successfully, it sends a subscription email to the email address you provided. You must confirm this email subscription to start receiving violation notifications. | Cloud architect |

## Related resources
<a name="verify-that-elb-load-balancers-require-tls-termination-resources"></a>
+ [Creating a stack on the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) (AWS CloudFormation documentation)
+ [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) (AWS Lambda documentation)
+ [What is a Classic Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/introduction.html) (ELB documentation)
+ [What is an Application Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) (ELB documentation)

## Attachments
<a name="attachments-da99cda2-ac34-4791-a2bd-d37264d8d3d9"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/da99cda2-ac34-4791-a2bd-d37264d8d3d9/attachments/attachment.zip)
