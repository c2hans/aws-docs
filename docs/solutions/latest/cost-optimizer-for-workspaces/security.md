---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/security.html
---

# Security
<a name="security"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared model](https://aws.amazon.com/compliance/shared-responsibility-model/) can reduce your operational burden as AWS operates, manages, and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the services operate. For more information about security on AWS, visit the [AWS Security Center](http://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

This solution creates IAM roles to control and isolate permissions, following the best practice of least privilege. The solution grants services the following permissions:

## Hub template
<a name="hub-template"></a>

 `RegisterSpokeAccountsFunctionLambdaRole`
+ Write permission to Amazon DynamoDB table where spoke accounts are registered

 `InvokeECSTaskRole`
+ Permission to create and run Amazon ECS tasks

 `CostOptimizerAdminRole`
+ Read permissions to an Amazon DynamoDB table where spoke accounts are registered
+ Assume role permissions to `WorkspacesManagementRole` in spoke accounts
+ Read only permissions to AWS Directory Service
+ Write permissions to Amazon CloudWatch Logs
+ Write permissions to Amazon S3
+ Read and write permissions to WorkSpaces

 `SolutionHelperRole`
+ Permisison to invoke an AWS Lambda function to generate a universally unique identifier (UUID) for solution metrics

## Spoke template
<a name="spoke-template"></a>

 `WorkSpacesManagementRole`
+ Read only permissions to AWS Directory Service
+ Write permissions to Amazon CloudWatch Logs
+ Write permissions to Amazon S3
+ Read/write permissions to WorkSpaces

 `AccountRegistrationProviderRole`
+ Invoke Lambda function to register spoke account with hub account stack

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cost Optimizer for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
