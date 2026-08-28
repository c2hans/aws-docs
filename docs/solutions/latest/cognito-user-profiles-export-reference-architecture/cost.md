---
source_url: https://docs.aws.amazon.com/solutions/latest/cognito-user-profiles-export-reference-architecture/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used while running this guidance. As of this revision, the cost for running this guidance in the North Virginia Region with the Tokyo Region as backup is approximately **$90.00 per month** for a user pool of 500,000 users (where each user is a member of one group) and a daily export frequency. Prices are subject to change. For full details, see the pricing webpage for each AWS service you will be using in this guidance.

| AWS Service | Total cost |
| --- | --- |
| Amazon DynamoDB | $86.00 |
| Amazon Step Functions | $1.00 |
| Amazon Simple Queue Service (Amazon SQS) | $1.00 |
| Amazon Simple Notification Service (Amazon SNS) | $1.00 |
| AWS Lambda | $1.00 |

 **IMPORTANT:** When the `ImportWorkflow` Step Functions workflow is run, it will create new users with the same profiles and group memberships in a new, empty user pool that you create. These new users will be treated by Cognito as additional monthly active users (MAU) when they are initially created by the guidance. Therefore, your Cognito cost could rise significantly during any month in which you run the `ImportWorkflow` Step Functions workflow. Refer to [Cognito’s Pricing Page](https://aws.amazon.com/cognito/pricing/) for more details on how Cognito MAUs are priced.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for User Profiles Export with Amazon Cognito. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
