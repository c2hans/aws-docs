---
source_url: https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-create.html
---

# Create a deployment with CodeDeploy
<a name="deployments-create"></a>

You can use the CodeDeploy console, the AWS CLI, or the CodeDeploy APIs to create a deployment that installs application revisions you have already pushed to Amazon S3 or, if your deployment is to an EC2/On-Premises compute platform, GitHub, on the instances in a deployment group.

The process for creating a deployment depends on the compute platform used by your deployment.

**Topics**
+ [Deployment prerequisites](deployments-create-prerequisites.md)
+ [Create an Amazon ECS Compute Platform deployment (console)](deployments-create-console-ecs.md)
+ [Create an AWS Lambda Compute Platform deployment (console)](deployments-create-console-lambda.md)
+ [Create an EC2/On-Premises Compute Platform deployment (console)](deployments-create-console.md)
+ [Create an Amazon ECS Compute Platform deployment (CLI)](deployments-create-ecs-cli.md)
+ [Create an AWS Lambda Compute Platform deployment (CLI)](deployments-create-lambda-cli.md)
+ [Create an EC2/On-Premises Compute Platform deployment (CLI)](deployments-create-cli.md)
+ [Create an Amazon ECS blue/green deployment through CloudFormation](deployments-create-ecs-cfn.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
