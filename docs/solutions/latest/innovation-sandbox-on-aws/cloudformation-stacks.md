---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/cloudformation-stacks.html
---

# CloudFormation stacks
<a name="cloudformation-stacks"></a>

The solution is composed of several CloudFormation templates that are deployed into these accounts:
+ The AWS Organizations management account
+ The account containing the organizations' AWS IAM Identity Center instance
+ A designated Hub account for the solution to be deployed into.

Sandbox accounts have a CloudFormation StackSets instance deployed in the account, managed by AWS Organizations.

## Stack dependencies
<a name="stack-dependencies"></a>

![Diagram showing the deployment order of the AccountPool IDC Data and Compute stacks and their dependencies](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/diagrams/stack-dependencies.drawio.png)

**Solution stack dependencies**
This diagram shows the order in which the stacks should be deployed. Some stacks depend on resources created by another stack to successfully deploy, so it is critical to deploy the stacks in the correct order for a successful deployment.

1. Deploy the **AccountPool** and **IDC** stacks as they do not depend on each other. The **SandboxAccount** stack is created as a service-managed StackSet resource. The StackSet instances will be deployed in the SandboxAccount when the accounts are moved into the AccountPool OU.

1. Deploy the **Data** stack, as it requires the **AccountPool** stack.

1. Deploy the **Compute** stack as it requires all other stacks to be deployed before it is deployed.

As part of the deployment, the solution deploys these CloudFormation stacks.

![Diagram showing the relationships between the ISB CloudFormation stacks and the accounts they deploy into](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/diagrams/stack-relationships.drawio.png)

**ISB CloudFormation stacks**
+ The **AccountPool** stack, deployed into the AWS Organizations management account, is used to manage the lifecycle on sandbox accounts controlled by the solution. This stack contains three major types of resources:
  +  **Organizational Units** (OUs) representing the lifecycle of the sandbox accounts (available, active, frozen, cleanup, quarantine, entry, exit),
  +  **Service Control Policies** (SCPs) that limit what actions can be taken in accounts in each OU and by what principals, and
  + An **IAM** role. The permissions on this role are least privileged to only allow read actions from Cost Explorer, read actions on the account pool OUs, and move account actions on the account pool OUs. The trust policy on the role only allows for a single Intermediate IAM role from the Compute stack to assume into it.
  + In addition to account management, a **Spoke** role in this account is used to read the account cost data from the Cost Explorer service API.
+ The **IAM Identity Center** (IDC) stack deployed into the AWS Account containing the organizations AWS IAM Identity Center instance, is used to manage the solution web UI and sandbox account access. This stack initializes user groups and corresponding permission sets in the instance that administrators can manually add users to. The IDC stack also contains an IAM Role. The permissions on this role are least privileged to only allow the actions required by the solution. The trust policy on the role only allows for a single Intermediate IAM role from the Compute stack to assume into it.
+ The **Data** stack is deployed into the account containing the core of the solution (Hub account). It contains Amazon DynamoDB tables containing the stateful data of the solution, including records for sandbox accounts, lease templates, leases, and global configurations.
+ The **Compute** stack is deployed into the account containing the core of the solution (Hub account). This stack contains all of the stateless (compute) resources used by the solution. The stack contains these two parts:
  + The **web application** is composed of the Amazon CloudFront distribution that serves the static assets of the UI, an Amazon API Gateway REST API with IAM authorization, and AWS Lambda function handlers for each of the API resources.
  + The **event infrastructure** is composed of producers and consumers on an Amazon EventBridge event bus. Producers consist of AWS Lambda functions running on EventBridge schedules and API-initiated events. Event consumers consist of Lambda functions handling account lifecycle, sending emails via Amazon SES, the blueprint deployment and assignment processing AWS Step Functions workflows, and the account cleaner durable Lambda. The account cleaner durable Lambda orchestrates a CodeBuild project that uses a custom public image containing the AWS Nuke binary.

**Note**
The **SandboxAccount** stack is automatically configured as a service-managed CloudFormation StackSet resource in the AccountPool stack using the **AccountPool OU** as the deployment target. The stack contains a single spoke role that is assumed into by compute resources in the compute stack to run the account cleanup job. SCPs established in the AccountPool stack protect the deletion of the role as well as the StackSet instance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
