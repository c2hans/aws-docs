---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iac-edp-combo-approach/blind-spot-scenario.html
---

# Blind spot scenario
<a name="blind-spot-scenario"></a>

This section provides an example of a scenario where an engineering team can make an IT decision that results in a blind spot that has unintentional consequences that can harm their organization. The hypothetical scenario assumes that an [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) storage volume is created in the AWS Cloud by using [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) as part of an IaC approach.

For this example, assume that an engineering team writes and then deploys a fully-tested program that generates an automated response if the capacity of a utilized volume crosses 80 percent (an arbitrary number for this example). The program responds to the threshold event by calling APIs to increase the volume size. The engineering team expects that the volume will continue to grow over time but not lead to a production outage. The engineering team has solved the storage space problem, but another subtle and often neglected problem emerges unintentionally—drift.

**Note**
This is just an example and other scenarios are possible. For instance, you could replace the EBS volume with a security group where the engineering team creates an ingress rule that allows traffic from a dynamic IP address based on an event.

## Unintentional consequences
<a name="unintentional-consequences"></a>

[Drift ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html#what-is-drift)occurs when you change the properties of the resources outside of the IaC system. In this scenario, that means the resources that are provisioned by CloudFormation. Engineers in this scenario use an API to increase the size of an EBS volume. The drift introduced by using the API instead of CloudFormation has a ripple effect that leads to additional problems. The issue is also magnified with the update deployment of the same stack in a DevOps process.

Because the volume size changed on the resource outside the code repository, the CloudFormation template isn't aware of the change. Therefore, any deployment will fail until the volume size increase is incorporated in the CloudFormation template. More importantly, if the engineers aren't aware of the volume resource changes, then their templates won't have the necessary updates. Volumes are particularly vulnerable to drift. After you increase volume storage size, you can't decrease volume storage size. Therefore, the CloudFormation template not only fails to update but also fails to roll back because the value of the size parameter can't be applied.

## Problematic approach
<a name="problematic-approach"></a>

The following diagram shows a problematic solution to the example scenario. The user, as part of the workflow, follows an IaC approach and provisions an EBS volume by using a CloudFormation template. The production monitoring team uses an EDP automation approach and creates an [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) rule. This rule is configured to invoke an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function when the EBS volume reaches a specific storage threshold. Then, the Lambda function calls the API to increase the EBS volume size.

![Problematic scenario with EBS volume](http://docs.aws.amazon.com/prescriptive-guidance/latest/iac-edp-combo-approach/images/guide-img/1c2f9dce-c146-4233-a850-fc07cab4966b/images/8a32b708-f6a6-4fdc-82dc-71c0af73d4d8.png)

## Recommended approach
<a name="recommended-approach"></a>

The following diagram shows a recommended approach that aligns with the best practices covered in the *Best practices* section of this guide. This approach involves greater complexity and more AWS services, including [Amazon Simple Notification Service (Amazon SNS) ](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)for sending notifications, [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) for source control, [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) for automated code deployment, and [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) for serverless workflow orchestration. In this approach, CodePipeline adds the EBS volume size to [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) (a capability of [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)) initially, and then Step Functions makes any subsequent updates.

You can use Parameter Store to see a history of the values and use it for values that change. Parameter Store also integrates with multiple services, such as CloudFormation and Lambda. The Lambda function in this scenario doesn't directly interact with the EBS volume to increase volume size. Instead, the Lambda function interacts with CloudFormation to update the API. As a result, CloudFormation stacks are safeguarded from drift. Finally, this approach relies on CloudFormation as the single source for performing updates.

![Recommended scenario with EBS volume](http://docs.aws.amazon.com/prescriptive-guidance/latest/iac-edp-combo-approach/images/guide-img/1c2f9dce-c146-4233-a850-fc07cab4966b/images/02d49e50-00a7-476f-b1fc-31a2bf843339.png)
