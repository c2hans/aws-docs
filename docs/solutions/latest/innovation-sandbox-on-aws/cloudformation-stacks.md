---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/cloudformation-stacks.html
---

# CloudFormation stacks

The solution is composed of several CloudFormation templates that are deployed into these accounts:
+ The AWS Organizations management account
+ The account containing the organizations' AWS IAM Identity Center instance
+ A designated Hub account for the solution to be deployed into.

Sandbox accounts have a CloudFormation StackSets instance deployed in the account, managed by AWS Organizations. A second service-managed StackSet, which the **Compute** stack creates, links each sandbox account to an Amazon CloudWatch observability sink in the Hub account.

## Stack dependencies
<a name="stack-dependencies"></a>

![Diagram showing the deployment order of the AccountPool IDC Data and Compute stacks and their dependencies](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/diagrams/stack-dependencies.drawio.png)

**Solution stack dependencies**
This diagram shows the order in which the stacks should be deployed. Some stacks depend on resources created by another stack to successfully deploy, so it is critical to deploy the stacks in the correct order for a successful deployment.

1. Deploy the **AccountPool** and **IDC** stacks as they do not depend on each other. The **SandboxAccount** stack is created as a service-managed StackSet resource. The StackSet instances will be deployed in the SandboxAccount when the accounts are moved into the AccountPool OU.

1. Deploy the **Data** stack, as it requires the **AccountPool** stack.

1. Deploy the **Compute** stack as it requires all other stacks to be deployed before it is deployed.

As part of the deployment, the solution deploys these CloudFormation stacks.

![Diagram showing the relationships between the ISB CloudFormation stacks and the accounts they deploy into](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/diagrams/stack-relationships.drawio.png)

**ISB CloudFormation stacks**
+ The **AccountPool** stack, deployed into the AWS Organizations management account, is used to manage the lifecycle on sandbox accounts controlled by the solution. This stack contains three major types of resources:
  +  **Organizational Units** (OUs) representing the lifecycle of the sandbox accounts (available, active, frozen, cleanup, quarantine, entry, exit),
  +  **Service Control Policies** (SCPs) that limit what actions can be taken in accounts in each OU and by what principals, and
  + An **IAM** role. The permissions on this role are least privileged to only allow read actions from Cost Explorer, read actions on the account pool OUs, and move account actions on the account pool OUs. The trust policy on the role only allows for a single Intermediate IAM role from the Compute stack to assume into it.
  + In addition to account management, a **Spoke** role in this account is used to read the account cost data from the Cost Explorer service API.
+ The **IAM Identity Center** (IDC) stack deployed into the AWS Account containing the organizations AWS IAM Identity Center instance, is used to manage the solution web UI and sandbox account access. This stack initializes user groups and corresponding permission sets in the instance that administrators can manually add users to. The IDC stack also contains an IAM Role. The permissions on this role are least privileged to only allow the actions required by the solution. The trust policy on the role only allows for a single Intermediate IAM role from the Compute stack to assume into it. The role also has read access to permission sets, including their inline policies, managed policies, and permissions boundaries. Sandbox Spaces uses this access to build the session policy of the agent.
+ The **Data** stack is deployed into the account containing the core of the solution (Hub account). It contains Amazon DynamoDB tables that store the solution’s persisted state, and the Amazon Cognito user pool with its app clients, including the app client for the MCP server.
+ The **Compute** stack is deployed into the account containing the core of the solution (Hub account). This stack contains all of the stateless (compute) resources used by the solution. The stack contains these three parts:
  + The **web application** is composed of the Amazon CloudFront distribution that serves the static assets of the UI, an Amazon API Gateway REST API with IAM authorization, and AWS Lambda function handlers for each of the API resources.
  + The **event infrastructure** is composed of producers and consumers on an Amazon EventBridge event bus. Producers consist of AWS Lambda functions running on EventBridge schedules and API-initiated events. Event consumers consist of Lambda functions handling account lifecycle, sending notifications through Amazon SES and an Amazon SNS integration topic, the blueprint deployment and assignment processing AWS Step Functions workflows, and the account cleaner durable Lambda. The account cleaner durable Lambda orchestrates a CodeBuild project that uses a custom public image containing the AWS Nuke binary.
  + The **Sandbox Spaces and MCP server** components are composed of an Amazon API Gateway WebSocket API, an Amazon SQS FIFO queue with a dead-letter queue, and Lambda functions that connect users, run the Worker, and clean up memory. They also include an Amazon Bedrock AgentCore Runtime that hosts the agent container, an AgentCore Memory store, an Amazon Bedrock guardrail, and an AgentCore Gateway with a Cedar policy engine. The Compute stack also creates the CloudWatch observability sinks in the Hub account and the StackSet that links sandbox accounts to them. For more information, see [Sandbox Spaces](sandbox-spaces-architecture.md) and [MCP server](mcp-server-architecture.md).

**Note**
The **SandboxAccount** stack is automatically configured as a service-managed CloudFormation StackSet resource in the AccountPool stack using the **AccountPool OU** as the deployment target. The stack contains a spoke role that is assumed into by compute resources in the compute stack to run the account cleanup job. SCPs established in the AccountPool stack protect the deletion of the role as well as the StackSet instance. The stack also contains a second role, `SandboxAgentRole-<namespace>`, which the Sandbox Spaces agent assumes through the Intermediate role in the Hub account. The trust policy of the role accepts only the Intermediate role and requires a non-empty source identity. The SCPs deny sandbox users, and the agent itself, any action on this role.
