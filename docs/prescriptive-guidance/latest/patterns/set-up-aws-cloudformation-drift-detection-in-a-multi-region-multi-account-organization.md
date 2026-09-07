---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-aws-cloudformation-drift-detection-in-a-multi-region-multi-account-organization.html
---

# Set up CloudFormation drift detection in a multi-Region, multi-account organization
<a name="set-up-aws-cloudformation-drift-detection-in-a-multi-region-multi-account-organization"></a>

*Ram Kandaswamy, Amazon Web Services*

## Summary
<a name="set-up-aws-cloudformation-drift-detection-in-a-multi-region-multi-account-organization-summary"></a>

Amazon Web Services (AWS) users often look for an efficient way to detect resource configuration mismatches, including drift in AWS CloudFormation stacks, and fix them as soon as possible. This is especially the case when AWS Control Tower is used.

This pattern provides a prescriptive solution that efficiently solves the problem by using consolidated resource configuration changes and acting on those changes to generate results. The solution is designed for scenarios where there are several CloudFormation stacks created in more than one AWS Region, or in more than one account, or a combination of both. The goals of the solution are the following:
+ Simplify the drift detection process
+ Set up notification and alerting
+ Set up consolidated reporting

## Prerequisites and limitations
<a name="set-up-aws-cloudformation-drift-detection-in-a-multi-region-multi-account-organization-prereqs"></a>

**Prerequisites **
+ AWS Config enabled in all the Regions and accounts that must be monitored

**Limitations **
+ The report generated supports only the comma-separated values (CSV) and JSON output formats.

## Architecture
<a name="set-up-aws-cloudformation-drift-detection-in-a-multi-region-multi-account-organization-architecture"></a>

The following diagram shows AWS Organizations set up with multiple accounts. AWS Config rules communicate between the accounts.

![Five-step process for monitoring stacks in two AWS Organizations accounts.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/735d0987-b953-47f8-a9bc-b02a88957ee5/images/340cee9a-5a4e-49ea-bd73-d37dcea5e098.png)

 The workflow includes the following steps:

1. The AWS Config rule detects drift.

1. Drift detection results that are found in other accounts are sent to the management account.

1. The Amazon CloudWatch rule calls an AWS Lambda function.

1. The Lambda function queries the AWS Config rule for aggregated results.

1. The Lambda function notifies Amazon Simple Notification Service (Amazon SNS), which sends email notification of the drift.

**Automation and scale**

The solution presented here can scale for both additional Regions and accounts.

## Tools
<a name="set-up-aws-cloudformation-drift-detection-in-a-multi-region-multi-account-organization-tools"></a>

**AWS services**
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) provides a detailed view of the configuration of AWS resources in your AWS account. This includes how the resources are related to one another and how they were configured in the past so that you can see how the configurations and relationships change over time.
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications you run on AWS in real time.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.

## Epics
<a name="set-up-aws-cloudformation-drift-detection-in-a-multi-region-multi-account-organization-epics"></a>

### Automate drift detection for CloudFormation
<a name="automate-drift-detection-for-cfn"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the aggregator. | 1. Sign in to the AWS Management Console and open the AWS Config console at [https://console.aws.amazon.com/config]().<br />2. Create an aggregator in the management account.<br />3. Ensure that data replication is turned on so that AWS Config can fetch data from the source accounts.<br />4. Select all applicable Regions and accounts. You can select accounts based on AWS Organizations. We recommend this approach because new accounts in the organization are automatically part of the aggregator. | Cloud architect |
| Create an AWS managed rule. | Add the `cloudformation-stack-drift-detection-check` AWS** **managed rule. The rule needs one parameter value: `cloudformationArn`. <br />Enter the IAM role Amazon Resource Name (ARN) that has permissions to detect stack drift. The role must have a trust policy that enables AWS Config to assume the role. | Cloud architect |
| Create the advanced query section of the aggregator. | To fetch drifted stacks from multiple sources, create the following query:<pre>SELECT resourceId, configuration.driftInformation.stackDriftStatus WHERE resourceType = 'AWS::CloudFormation::Stack'  AND configuration.driftInformation.stackDriftStatus IN ('DRIFTED')</pre> | Cloud architect, Developer |
| Automate running the query and publish. | 1. Create a Lambda function by using the code that is attached. Lambda will publish the results to an SNS topic that is provided as an environment variable in the Lambda function.<br />2. To receive alerts, create an email subscription to the SNS topic. | Cloud architect, Developer |
| Create a CloudWatch rule. | Create a schedule-based CloudWatch rule to call the Lambda function, which is responsible for alerting. | Cloud architect |

## Related resources
<a name="set-up-aws-cloudformation-drift-detection-in-a-multi-region-multi-account-organization-resources"></a>

**Resources**
+ [What Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
+ [Multi-account multi-Region data aggregation](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html)
+ [Detecting unmanaged configuration changes to stacks and resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html)
+ [IAM: Pass an IAM role to a specific AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam-passrole-service.html)
+ [What is Amazon SNS?](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)

## Additional information
<a name="set-up-aws-cloudformation-drift-detection-in-a-multi-region-multi-account-organization-additional"></a>

**Considerations**

We recommend using the solution presented in this pattern instead of using custom solutions that involve API calls at specific intervals to initiate drift detection on each CloudFormation stack or stack set. Custom solutions that use API calls at specific intervals can lead to a large number API calls and affect performance. Because of the number of API calls, throttling can occur. Another potential issue is a delay in detection if resource changes are identified based on schedule only.

Because stack sets are made of stacks, you can use this solution. Stack instance details are also available as part of the solution.

## Attachments
<a name="attachments-735d0987-b953-47f8-a9bc-b02a88957ee5"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/735d0987-b953-47f8-a9bc-b02a88957ee5/attachments/attachment.zip)
