---
source_url: https://docs.aws.amazon.com//solutions/cost-optimizer-for-amazon-workspaces//index.html
---

# Cost Optimizer for Amazon WorkSpaces

Monitor Amazon WorkSpaces usage and optimize costs

- **Version**: 2.9.7
- **Released**: 7/2026
- **Author**: AWS
- **Est. deployment time**: 5-15 mins
- **Estimated cost**: [See details](/solutions/latest/cost-optimizer-for-workspaces/cost.html)

## Overview

Cost Optimizer for Amazon WorkSpaces analyzes all of your Amazon WorkSpaces usage data and automatically converts the WorkSpace to the most cost-effective billing option (hourly or monthly), depending on your individual usage. You can use this AWS Solution with a single account—or with AWS Organizations across multiple accounts—to help you monitor your WorkSpace usage and optimize costs. This solution calculates hourly WorkSpace usage once per day, just before midnight GMT. If the WorkSpace exceeds the hourly usage threshold, the solution will convert the WorkSpace from hourly to monthly billing. If usage exceeds the threshold after the nightly calculation, the WorkSpace will not be converted until usage is calculated the following night. You can manually change the billing model at any time using the WorkSpaces console. If you want to change the threshold for when each Workspace converts from hourly to monthly billing, the solution’s AWS CloudFormation template includes parameters that will execute these conversions. For more information, review [Billing model conversion](/solutions/latest/cost-optimizer-for-workspaces/overview.html) in the implementation guide.

## Benefits

### Automatic WorkSpaces conversion

Automatically convert your WorkSpaces to the most cost-effective billing option (hourly or monthly), depending on your individual usage. If desired, you can apply a resource tag to individual WorkSpaces to exclude them from automatic conversions.

### Monitor your WorkSpaces usage

Monitor your WorkSpace usage and optimize costs by using AWS CloudFormation to automatically provision and configure the necessary AWS services to convert individual WorkSpaces.

### Secure one-click deployment

Provide a secure one-click deployment with a CloudFormation template developed using the AWS Well-Architected Framework.

## How it works

You can automatically deploy this architecture using the implementation guide and the AWS CloudFormation template.

[View implementation guide](/solutions/latest/cost-optimizer-for-workspaces)

![Architecture diagram](/images/solutions/cost-optimizer-for-amazon-workspaces/images/cost-optimizer-for-amazon-workspaces-1.png)

1. **Step 1**: The spoke template creates a custom resource that invokes an AWS Lambda function to register the account as a spoke account in an Amazon DynamoDB table in the hub account.
1. **Step 2**: The hub template creates an Amazon EventBridge rule that invokes an Amazon ECS task every 24 hours.
1. **Step 3**: The Amazon ECS task assumes an AWS Identity and Access Management (IAM) role in each spoke account to manage WorkSpaces.
1. **Step 4**: The Amazon ECS task polls AWS Directory Service to gather a list of all directories registered for Amazon WorkSpaces in a specific AWS Region. The task then checks the total usage for each WorkSpace that is on an hourly billing model. If a WorkSpace has met the monthly usage threshold, the solution will convert the individual WorkSpace to monthly billing.
## Deploy with confidence

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Open guide](/solutions/latest/cost-optimizer-for-workspaces/cost-optimizer-for-workspaces.pdf)

- **Let's make it happen**: Ready to deploy? Open the CloudFormation template in the AWS Console to begin setting up the infrastructure you need. You'll be prompted to access your AWS account if you haven't yet logged in.

[Go to the AWS Console](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?&templateURL=https:%2F%2Fsolutions-reference.s3.amazonaws.com%2Fcost-optimizer-for-amazon-workspaces%2Flatest%2Fcost-optimizer-for-amazon-workspaces.template&redirectId=SolutionWeb)

## Deployment options

- **CloudFormation template**: View or modify the CloudFormation template to customize your deployment.

[Download template](/solutions/latest/cost-optimizer-for-workspaces/templates.html)

- **Source code**: The source code for this AWS Solution is available in GitHub.

[Go to GitHub](https://github.com/aws-solutions/cost-optimizer-for-amazon-workspaces)

- **Implementation guide**: Follow the implementation guide for step-by-step actions to deploy this AWS Solution.

[Download guide](/solutions/latest/cost-optimizer-for-workspaces/cost-optimizer-for-workspaces.pdf)

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/cost-optimizer-for-workspaces/contact-aws-support.html)

## RSS Feed

- [Subscribe now to get updates on the latest release.](https://solutions-reference.s3.us-east-1.amazonaws.com/cost-optimizer-for-amazon-workspaces/latest/rss.xml)
