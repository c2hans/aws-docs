---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/architecture.html
---

# Architecture overview
<a name="architecture"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution.

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters deploys the following components in your AWS account.

**Note**
This solution includes both a \*hub account template \*(deployed first) for a central account to manage the WorkSpaces and provide a centralized report, and a \*spoke account template \*(deployed second) for each WorkSpace account that you want to monitor. The solution generates a report per directory and an aggregated report with information about WorkSpaces from all the directories combined.

 **Cost Optimizer for Amazon WorkSpaces architecture**

![workspaces cost optimizer architecture](http://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/images/workspaces-cost-optimizer-architecture.png)

1. The spoke template creates a [custom resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html) that invokes an [AWS Lambda](https://aws.amazon.com/lambda/) function to register the account as a spoke account in an [Amazon DynamoDB](https://aws.amazon.com/dynamodb) table in the hub account.

1. The hub template creates an [Amazon EventBridge](https://aws.amazon.com/eventbridge/) rule that invokes an [Amazon ECS](https://aws.amazon.com/ecs/) task every 24 hours.

1. The Amazon ECS task assumes an [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) role in each spoke account to manage WorkSpaces.

1. The Amazon ECS task polls [AWS Directory Service](https://aws.amazon.com/directoryservice/) to gather a list of all directories registered for Amazon WorkSpaces in a specific AWS Region. The task then checks the total usage for each WorkSpace that is on an hourly billing model. If a WorkSpace has met the monthly usage threshold, the solution will convert the individual WorkSpace to monthly billing.
**Note**
If a WorkSpace starts in monthly billing or the solution converts a WorkSpace from hourly to monthly billing, the solution will not convert the WorkSpace to hourly billing until the beginning of the next month if usage was below the threshold. However, you can manually change the billing model at any time using the Amazon WorkSpaces console. Also, you can change the threshold for when each WorkSpace converts from hourly to monthly billing. For more information, refer to [Automatic billing conversion](features-and-benefits.md#automatic-billing-conversion)

The solution also features a dry run mode (activated by default) that allows you to gain insight into how the recommended changes will affect your costs. For more information, refer to [Dry run mode](features-and-benefits.md#dry-run-mode).

\+

At the end of the month, the Amazon ECS task checks the total usage for each Workspace that is on a monthly billing model. If a WorkSpace has not met the monthly usage threshold, the solution will convert the individual WorkSpace from monthly to hourly billing at the start of the next month. . The Amazon ECS task writes the results of the execution to the DynamoDB usage table, session tables, and uploads them to an [Amazon Simple Cloud Storage (Amazon S3)](https://aws.amazon.com/s3/) bucket.

**Note**
Check your Amazon S3 bucket frequently to track the optimizer’s activity, and to view logs with error messages.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cost Optimizer for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
