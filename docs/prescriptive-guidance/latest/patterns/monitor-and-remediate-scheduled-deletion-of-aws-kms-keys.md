---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-and-remediate-scheduled-deletion-of-aws-kms-keys.html
---

# Monitor and remediate scheduled deletion of AWS KMS keys
<a name="monitor-and-remediate-scheduled-deletion-of-aws-kms-keys"></a>

*Mikesh Khanal and Ramya Pulipaka, Amazon Web Services*

## Summary
<a name="monitor-and-remediate-scheduled-deletion-of-aws-kms-keys-summary"></a>

On the Amazon Web Services (AWS) Cloud, deleting an AWS Key Management Services (AWS KMS) key can result in data loss. Deletion removes the key material and all metadata associated with the AWS KMS key, and it is irreversible. After an AWS KMS key is deleted, you can no longer decrypt the data that were encrypted under that AWS KMS key, so that data cannot be recovered.

This pattern sets up monitoring, with notifications when an application or a user schedules an AWS KMS key for deletion. If you receive a notification, you might want to cancel deletion of the AWS KMS key and reconsider your decision to delete it. The pattern uses the AWS Systems Manager automation runbook [AWSConfigRemediation-CancelKeyDeletion](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-cancel-key-deletion.html) to facilitate canceling the deletion of an AWS KMS key.

**Note**
The pattern's CloudFormation template must be deployed in all AWS Regions where you want to monitor deletion of AWS KMS keys.

## Prerequisites and limitations
<a name="monitor-and-remediate-scheduled-deletion-of-aws-kms-keys-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ Understanding of the following AWS services:
  + Amazon EventBridge
  + AWS KMS
  + Amazon Simple Notification Service (Amazon SNS)
  + AWS Systems Manager

**Limitations **
+ Any customization of the solution requires knowledge of AWS CloudFormation templates and the AWS services used in this pattern.
+ Currently, this solution uses the default event bus, and it can be customized according to the requirements. For more information about the custom event bus, see the [AWS documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html).

## Architecture
<a name="monitor-and-remediate-scheduled-deletion-of-aws-kms-keys-architecture"></a>

**Target technology stack  **
+ Amazon EventBridge
+ AWS KMS
+ Amazon SNS
+ AWS Systems Manager
+ Automation using the following:
  + AWS Command Line Interface (AWS CLI) or AWS SDK
  + AWS CloudFormation stack

**Target architecture **

![Diagram of the five steps of the monitoring, alerting, and remediation process.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/56927ebc-bbf7-49cc-9ad2-b2e0dff1201c/images/32537a66-037a-45a1-af19-3bc7bc26eaa6.png)

1. Deletion of an AWS KMS key is scheduled.

1. The scheduled-deletion event is evaluated by an EventBridge rule.

1. The EventBridge rule engages the Amazon SNS topic.

1. The EventBridge rule initiates the Systems Manager automation and runbooks.

1. The runbooks cancel the deletion.

**Automation and scale**

The CloudFormation stack deploys all the necessary resources and services for this solution to work. The pattern can be run independently in a single account or run using AWS CloudFormation StackSets for multiple independent accounts or an organization.

```
aws cloudformation create-stack --stack-name  <stack-name>\
    --template-body file://<Full-Path-of-file> \
    --parameters ParameterKey=,ParameterValue= \
    --capabilities CAPABILITY_NAMED_IAM
```

## Tools
<a name="monitor-and-remediate-scheduled-deletion-of-aws-kms-keys-tools"></a>

**Tools**
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/) – AWS CloudFormation is a service that helps you model and set up your Amazon Web Services resources so that you can spend less time managing those resources and more time focusing on your applications that run on AWS. You can use a CloudFormation template to create stacks in an AWS account in an AWS Region. The template describes all the AWS resources that you want, and CloudFormation provisions and configures those resources for you.
+ [AWS CLI](https://docs.aws.amazon.com/cli/?id=docs_gateway) – The AWS Command Line Interface (AWS CLI) is an open source tool that you can use to interact with AWS services using commands in your command line shell.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html) – Amazon EventBridge is a serverless event bus service connecting your applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your own applications and AWS services, and it routes that data to targets such as AWS Lambda. EventBridge simplifies the process of building event-driven architectures.
+ [AWS KMS](https://aws.amazon.com/kms/) – AWS Key Management Service (AWS KMS) is a managed service for creating and controlling AWS KMS keys, the encryption keys used to encrypt your data.
+ [AWS SDKs](https://aws.amazon.com/tools/?id=docs_gateway) – AWS tools include SDKs so that you can develop and manage applications on AWS in the programming language of your choice.
+ [Amazon SNS](https://aws.amazon.com/sns/) – Amazon Simple Notification Service (Amazon SNS) is a managed service that provides message delivery from publishers to subscribers (also known as producers and consumers). Publishers communicate asynchronously with subscribers by sending messages to a topic, which is a logical access point and communication channel.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) – AWS Systems Manager is an AWS service that you can use to view and control your infrastructure on AWS. Using the Systems Manager console, you can automate operational tasks across your AWS resources. Systems Manager helps you maintain security and compliance by scanning your managed instances and reporting on (or taking corrective action on) any policy violations it detects.

**Code **
+ The `alerting_ct_logs.yaml` CloudFormation template for the project is attached.

## Epics
<a name="monitor-and-remediate-scheduled-deletion-of-aws-kms-keys-epics"></a>

### Prepare the AWS account
<a name="prepare-the-aws-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install and configure AWS CLI. | Install AWS CLI version 2. Then configure the security credentials settings for an identity, the default output format, and the default AWS Region that AWS CLI uses to interact with AWS.<br />The identity must have the required permissions to perform the tasks. | Developer, Security engineer |

### Deploy the AWS CloudFormation template
<a name="deploy-the-aws-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the CloudFormation template. | Download the attachment to a local path on your computer and extract the `alerting_ct_logs.yaml` template file. | Developer, Security engineer |
| Deploy the template. | In the terminal window where the AWS account profile has been configured, run the following command.<pre>aws cloudformation create-stack --stack-name <stack_name> \<br />--capabilities <Value>  \<br />--template-body file://<Full_Path> \<br /> --parameters ParameterKey=DestinationEmailAddress,ParameterValue=<Value> \<br />ParameterKey=SNSTopicName,ParameterValue=<Value> \<br />ParameterKey=EnableRemediation ,ParameterValue=<Value> \<br />ParameterKey=AutomationAssumeRole,ParameterValue=<Value></pre><br />In the next step, enter values for the template parameters. | Developer, Security engineer |
| Complete the template parameters. | Enter the required values for the parameters.+ `DestinationEmailAddress` – The email address to receive an alert when an AWS KMS key is scheduled for deletion.<br />+ `SNSTopicName` – The name of the Amazon SNS topic.<br />+ `EnableRemediation` – Cancellation of the scheduled key deletion using a Systems Manager runbook. Allowed values are `true` and `false`.<br />+ `AutomationAssumeRole` – The Amazon Resource Name (ARN) of the role that allows Systems Manager automation to perform the actions on your behalf. For more information, see the *Required IAM Permissions* section in the   [AWSConfigRemediation-CancelKeyDeletion](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-cancel-key-deletion.html) documentation. <br />+ `Capabilities` – For AWS CloudFormation to [create the stack](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack.html), you must explicitly acknowledge that your stack template contains certain capabilities. | Developer, Security engineer |

### Confirm the subscription
<a name="confirm-the-subscription"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Confirm the subscription. | Check your email inbox and choose **Confirm subscription** in the email message that you receive from Amazon SNS. A web browser window will open and display a subscription confirmation and your subscription ID.  | Developer, Security engineer |

## Related resources
<a name="monitor-and-remediate-scheduled-deletion-of-aws-kms-keys-resources"></a>

**References**
+ [Creating a rule for an AWS service](https://docs.aws.amazon.com/eventbridge/latest/userguide/create-eventbridge-rule.html)
+ [Creating an Amazon CloudWatch alarm to detect usage of an AWS KMS key that is pending deletion](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-creating-cloudwatch-alarm.html)

**Tutorials and videos **
+ [How to get started with Amazon EventBridge](https://www.youtube.com/watch?v=ea9SCYDJIm4)
+ [Deep dive on Amazon EventBridge](https://www.youtube.com/watch?v=28B4L1fnnGM) (AWS Online Tech Talks)

**AWS workshop **
+ [Working with EventBridge rules](https://event-driven-architecture.workshop.aws/2-event-bridge/2-rules/rules.html)

## Additional information
<a name="monitor-and-remediate-scheduled-deletion-of-aws-kms-keys-additional"></a>

The following code provides examples for extending the solution to monitor and notify you of any changes in any AWS service. The examples include predefined patterns and custom patterns. For more information, see [Events and event patterns in EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html).

```
EventPattern:
        source:
        - aws.kms
        detail-type:
        - AWS API Call via CloudTrail
        detail:
          eventSource:
          - kms.amazonaws.com
          eventName:
          - ScheduleKeyDeletion
```

## Attachments
<a name="attachments-56927ebc-bbf7-49cc-9ad2-b2e0dff1201c"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/56927ebc-bbf7-49cc-9ad2-b2e0dff1201c/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
