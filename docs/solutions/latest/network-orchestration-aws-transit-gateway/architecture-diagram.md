---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/architecture-diagram.html
---

# Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters deploys the following components in your AWS account.

 **Architecture diagram of AWS resources deployed to automate managing Transit Gateway attachments.**

![network orchestration aws transit gateway architecture](http://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/images/network-orchestration-aws-transit-gateway-architecture.png)

**Note**
CloudFormation resources are created from AWS Cloud Development Kit (AWS CDK) constructs.

1. This template deploys an [Amazon EventBridge](https://aws.amazon.com/eventbridge/) rule that monitors specific VPC and subnet tag changes.
**Note**
To identify the VPCs (spoke accounts) for the solution to manage, [tag the VPCs](step-5-add-tags.md) and the selected subnets within those VPCs.

1. An EventBridge rule in the spoke account sends the tags to the EventBridge bus in the hub account.

1. The rules associated with the EventBridge bus invoke an [AWS Lambda function](https://aws.amazon.com/lambda/) to start the solution workflow. For more information about workflows, refer to [Architecture details](architecture-details.md).
**Note**
Wait for the hub stack launch to complete before you launch spoke templates. The spoke accounts depend on the EventBridge bus that’s created during the hub stack launch.

1.  [AWS Step Functions](https://aws.amazon.com/step-functions/) (solution [state machine](concepts-and-definitions.md)) processes network requests from the spoke accounts.

1. The state machine workflow attaches a VPC to the transit gateway.

1. The state machine workflow updates the VPC route table associated with the tagged subnet.

1. The state machine workflow updates the transit gateway route table with association and propagation changes.
**Note**
This workflow only updates the transit gateway route table defined in the VPC tags.

1. (Optional) The state machine workflow updates the attachment name with the VPC name and the Organizational Unit (OU) name for the spoke account (retrieved from the Org Management account).
**Note**
This occurs only if you provide your Organizations ARN for the **Account List or AWS Organizations ARN** template parameter. For more information, see [Step 3: Launch the hub stack](step-3-launch-the-hub-stack.md).

1. The solution updates [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) with the information extracted from the event and resources created, updated, or deleted in the workflow.

Users can view tagging event details and the history of network requests from different accounts, and monitor their status in the web UI. Administrators can accept or reject requests when manual approval is required.
