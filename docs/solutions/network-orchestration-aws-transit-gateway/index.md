---
source_url: https://docs.aws.amazon.com//solutions/network-orchestration-aws-transit-gateway//index.html
---

# Network Orchestration for AWS Transit Gateway

Automate setting up and managing your transit networks with AWS Transit Gateway

- **Version**: 3.3.28
- **Released**: 8/2026
- **Author**: AWS
- **Est. deployment time**: 25 mins
- **Estimated cost**: [See details](https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/cost.html)

## Overview

The Network Orchestration for AWS Transit Gateway solution automates the process of setting up and managing transit networks in distributed AWS environments. This solution allows customers to visualize and monitor their global network from a single dashboard rather than toggling between Regions from the AWS Console. It creates a web interface to help control, audit, and approve transit network changes.

## Benefits

### Cross-account and cross-Region capability

Automate the process of setting up and managing transit networks in multi-account AWS environments.

### Change management

Use the web user interface to either accept or reject connectivity requests when manual approval is required.

### Web user interface

Deploy a web user interface to control, audit, and approve transit network changes.

### Compliance

Use rules to automatically accept or reject network changes based on the Organization Unit (OU).

## How it works

You can automatically deploy this architecture using the implementation guide and the accompanying AWS CloudFormation templates.

[View implementation guide](/solutions/latest/network-orchestration-aws-transit-gateway/solution-overview.html)

![Architecture diagram](/images/solutions/network-orchestration-aws-transit-gateway/images/network-orchestration-aws-transit-gateway-1.png)

1. **Step 1**: This template deploys an Amazon EventBridge rule that monitors specific VPC and subnet tag changes.
1. **Step 2**: An EventBridge rule in the spoke account sends the tags to the EventBridge bus in the hub account.
1. **Step 3**: The rules associated with the EventBridge bus invoke an AWS Lambda function to start the solution workflow. For more information about workflows, refer to [Architecture details](solutions/latest/network-orchestration-aws-transit-gateway/architecture-details.html).
1. **Step 4**: AWS Step Functions (solution state machine) processes network requests from the spoke accounts.
1. **Step 5**: The state machine workflow attaches a VPC to the transit gateway.
1. **Step 6**: The state machine workflow updates the VPC route table associated with the tagged subnet.
1. **Step 7**: The state machine workflow updates the transit gateway route table with association and propagation changes.
1. **Step 8**: (Optional) The state machine workflow updates the attachment name with the VPC name and the Organizational Unit (OU) name for the spoke account (retrieved from the Org Management account).
1. **Step 9**: The solution updates Amazon DynamoDB with the information extracted from the event and resources created, updated, or deleted in the workflow.
## Deploy with confidence

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.Open guide

[Open guide](/solutions/latest/network-orchestration-aws-transit-gateway/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Open the CloudFormation template in the AWS Console to begin setting up the infrastructure you need. You'll be prompted to access your AWS account if you haven't yet logged in.Launch in the AWS Console

[Launch in the AWS Console](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?&templateURL=https:%2F%2Fsolutions-reference.s3.amazonaws.com%2Fnetwork-orchestration-for-aws-transit-gateway%2Flatest%2Fnetwork-orchestration-hub.template&redirectId=SolutionWeb)

## Deployment options

- **Implementation guide**: Follow the implementation guide for step-by-step actions to deploy this AWS Solution.

[Download guide](/pdfs/solutions/latest/network-orchestration-aws-transit-gateway/network-orchestration-aws-transit-gateway.pdf#solution-overview)

- **Source code**: The source code for this AWS Solution is available in GitHub.

[Go to GitHub](https://github.com/aws-solutions/network-orchestration-for-aws-transit-gateway)

- **CloudFormation templates**: View or modify the CloudFormation template to customize your deployment.

[Download templates](/solutions/latest/network-orchestration-aws-transit-gateway/aws-cloudformation-templates.html?)

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/network-orchestration-aws-transit-gateway/contact-aws-support.html)

## RSS Feed

- [Subscribe now to get updates on the latest release.](https://solutions-reference.s3.us-east-1.amazonaws.com/network-orchestration-for-aws-transit-gateway/latest/rss.xml)
