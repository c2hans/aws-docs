---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-the-setup-of-inter-region-peering-with-aws-transit-gateway.html
---

# Automate the setup of inter-Region peering with AWS Transit Gateway
<a name="automate-the-setup-of-inter-region-peering-with-aws-transit-gateway"></a>

*Ram Kandaswamy, Amazon Web Services*

## Summary
<a name="automate-the-setup-of-inter-region-peering-with-aws-transit-gateway-summary"></a>

[AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) connects virtual private clouds (VPCs) and on-premises networks through a central hub. Transit Gateway traffic doesn't traverse the public internet, which reduces threat vectors, such as common exploits and distributed denial of service (DDoS) attacks.

If you need to communicate between two or more AWS Regions, you can use inter-Region Transit Gateway peering to establish peering connections between transit gateways in different Regions. However, manually configuring inter-Region peering with Transit Gateway can be a complex and time-consuming. This pattern provides guidance for using infrastructure as code (IaC) to set up peering. You can use this approach if you have to repeatedly configure several Regions and AWS accounts for a multi-Region organization setup.

This pattern sets up an [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)stack that includes an AWS Step Functions [workflow](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-statemachines.html), AWS Lambda [functions](https://docs.aws.amazon.com/lambda/latest/dg/concepts-basics.html#gettingstarted-concepts-function), AWS Identity and Access Management (IAM) [roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html), and [log groups](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in Amazon CloudWatch Logs. You then run the Step Functions workflow to create the inter-Region peering connection for your transit gateways.

## Prerequisites and limitations
<a name="automate-the-setup-of-inter-region-peering-with-aws-transit-gateway-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ An IDE that has code-generation capability, such as [Kiro](https://kiro.dev/#what-is-kiro).
+ An Amazon Simple Storage Service (Amazon S3) bucket and permissions to upload objects to it.
+ Transit gateways created in the requesting and accepting Regions.
+ VPCs created in the requesting and accepting Regions. Tag the VPCs with an `addToTransitGateway` key with a value of `true`.
+ [Security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) configured for your VPCs according to your requirements.
+ [Network access control lists (ACLs)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) configured for your VPCs according to your requirements.

**Limitations**
+ Only some AWS Regions support inter-Region peering. For a full list of Regions that support inter-Region peering, see the [AWS Transit Gateway FAQs](https://aws.amazon.com/transit-gateway/faqs/).

## Architecture
<a name="automate-the-setup-of-inter-region-peering-with-aws-transit-gateway-architecture"></a>

 The agentic AI development approach described in this pattern involves the following steps:

1. **Define the automation prompt** – Kiro receives a natural language prompt that details the peering requirements.

1. **Generate automation script** – Kiro generates the CloudFormation and Lambda scripts based on the provided prompt.

1. **Deploy the stack** – Kiro uses CloudFormation to deploy the required resources.

1. **Set up peering** – Kiro runs the Step Functions workflow, which calls Lambda functions to create peering connections and modify route tables.

The following diagram shows the Step Functions workflow:

![Step Functions workflow to call Lambda function to modify route tables for transit gateway peering.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/b678bb87-c7b9-4f7b-b26e-eaac650e5d1b/images/2f235f47-5d68-492c-b954-7dc170939cae.png)

The workflow contains the following steps:

1. The Step Functions workflow calls the Lambda function for the Transit Gateway peering.

1. The workflow waits for one minute.

1. The workflow retrieves the peering status and sends it to the condition block. The block is responsible for the looping.

1. If the success condition is not met, the workflow is coded to enter the timer stage.

1. If the success condition is met, a Lambda function modifies the route tables.

1. The Step Functions workflow ends.

## Tools
<a name="automate-the-setup-of-inter-region-peering-with-aws-transit-gateway-tools"></a>
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so you can monitor them and archive them securely.
+ [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)[ (](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)[IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)[)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Kiro](https://kiro.dev/#what-is-kiro) is an agentic AI development tool that helps you build production-ready applications through spec-driven development.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications.

## Epics
<a name="automate-the-setup-of-inter-region-peering-with-aws-transit-gateway-epics"></a>

### Generate Lambda and Step Functions code
<a name="generate-lam-and-sfn-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Filling prompt placeholders with specific details | 1. Update the following prompt by replacing the AWS Regions and bucket names:<pre>- Active region: ACTIVE_REGION<br />- Passive region: PASSIVE_REGION<br />- S3_BUCKET : my-lambda-packages-bucket <br />- STACK_NAME : transit-gateway-peering <br />- All Lambda functions use two boto3 EC2 clients at module level (one per region), each with signature_version v4 and retries max_attempts=1 mode=standard.<br />- Print all API responses for CloudWatch logging.</pre><br />2. Save this as a markdown file.<br />3. Add this markdown file to your Kiro project for context.Alternatively, you can add this as an inline prompt that references the above variables without attaching the file for context. | General AWS, Network administrator |
| Create a Lambda function that creates the peering attachments. | 1. In your Kiro project, enter the following prompt:<pre>Write a Python Lambda that creates a transit gateway peering attachment from active region  to passive region. Both of these regions will be read as environment variables of the Lambda function. Use two boto3 EC2 clients at the module level, one per Region. The handler should describe available transit gateways in both Regions. Then check if a peering attachment already exists on the active side by filtering describe_transit_gateway_attachments for resource-type "peering" and states: available, initiatingRequest, modifying, pendingAcceptance, pending, rejected, and rejecting. Only if zero results, create the peering attachment with tags for both Transit Gateway IDs, then wait 60 seconds (AWS needs this before the passive side can accept), then call accept_transit_gateway_peering_attachment on the passive client. Print all API responses.</pre><br />2. Save and name this file `peer-transit-gateway.py`. | General AWS, Network administrator, Prompt engineering |
| Create a Lambda function that polls the peering attachment status. | 1. In your Kiro project, enter the following prompt:<pre>Using the shared context above, write a Python Lambda that polls peering attachment status. Describe available transit gateways in both regions, then call describe_transit_gateway_attachments on the active client filtered by the active Transit Gateway ID only (no resource-type filter). Return exactly `{'status': status}` where status is the State field from the first attachment. Do not return statusCode or body — the Step Function Choice state reads `$.Payload.status` and compares to "available".</pre><br />2. Save and name this file `get-transit-gateway-peering-status.py`. | General AWS, Network administrator, Prompt engineering |
| Create a Lambda function that adds static routes to both Regions. | 1. In your Kiro project, enter the following prompt:<pre>Using the shared context, write a Python Lambda that adds static routes to both regions' TGW route tables. Describe available transit gateways in both Regions, extract each transit gateway's AssociationDefaultRouteTableId. Discover routable VPCs by filtering describe_vpcs with tag `addtotransitgateway=true` in each region, collecting their CIDRs. Get the peering attachment ID from the active side by filtering on the active route table ID. For each passive CIDR, search the active route table using `route-search.exact-match` — only create the route if none found. For each active CIDR, search the passive route table using `route-search.supernet-of-match` (not exact-match — passive side may have supernet routes) — only create if none found. Both sides use the same peering attachment ID.</pre><br />2. Save and name this file as `modify-transit-gateway-routes.py`. | General AWS, Network administrator |
| Create the CloudFormation template. | 1. Enter the following orchestration prompt, which creates a CloudFormation template:<pre>Write a CloudFormation JSON template that deploys: three Lambda functions (peer-transit-gateway with 600s timeout, get-transit-gateway-peering-status with 30s timeout, modify-transit-gateway-routes with 600s timeout), Lambda code from an S3 bucket parameter (no default value — user must supply the bucket name at deploy time), a Step Functions state machine, and CloudWatch log groups with 90-day retention. The state machine flow is:<br /><br />1. Invoke peer-transit-gateway<br />2. Wait 20 seconds (attachment needs time after the Lambda's internal 20s sleep + acceptance)<br />3. Invoke get-transit-gateway-peering-status<br />4. Choice: if `$.Payload.status` equals "available" → go to step 5, otherwise loop back to step 2<br />5. Invoke modify-transit-gateway-routes → End<br /><br />Use `Fn::Sub` with Lambda ARN references like `${PeerTransitGateways.Arn}` in the DefinitionString. The polling loop has no max retry — it loops until "available" (typically 3-5 minutes total).</pre><br />2. Save and name the file `transit-gateway-peering.json`. | AWS DevOps, General AWS, Prompt engineering |

### Deploy the AWS resources
<a name="deploy-the-aws-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the CloudFormation stack by using prompts. | Enter the following prompt:<pre>Using the outputs from Prompts 1-4, package and deploy the full stack. Steps:<br /><br />1. For each of the three Python files from Prompts 1-3, create a zip named after the file (e.g. peer-transit-gateway.zip that contains peer-transit-gateway.py).<br />2. Upload all three zips to S3_BUCKET.<br />3. Deploy the CloudFormation template from Prompt 4 to ACTIVE_REGION with S3BucketName=S3_BUCKET and CAPABILITY_NAMED_IAM.<br />4. Initiate the Step Function from the deployed stack.<br /><br />Zip file names must match the S3Key values in the template exactly.</pre> | AWS DevOps, Cloud administrator, General AWS, Prompt engineering |
| Validate deployment. | 1. Monitor the Step Functions workflow for successful completion. For instructions, see the [Step Functions documentation](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-view-execution-details.html).<br />2. Verify that the Transit Gateway attachment peering status is available. For instructions, see the [Transit Gateway documentation](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html). | General AWS |

## Related resources
<a name="automate-the-setup-of-inter-region-peering-with-aws-transit-gateway-resources"></a>
+ [Starting state machine executions in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-executions.html)
+ [Transit Gateway peering attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html)
+ [Interconnecting VPCs across AWS Regions using AWS Transit Gateway](https://www.youtube.com/watch?v=cj1rQqLxXU8) (video)
