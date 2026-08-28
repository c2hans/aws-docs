---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/lambda-hooks-view-logs.html
---

# View logs for the Lambda Hooks in your account
<a name="lambda-hooks-view-logs"></a>

When using a Lambda Hook, your validation output report log file can be found in the Lambda console.

## View Lambda Hook logs in the Lambda console
<a name="lambda-hooks-view-logs-console"></a>

**To view the Lambda Hook output log file**

1. Sign-in to the Lambda console.

1. On the navigation bar at the top of the screen, choose your AWS Region.

1. Choose **Functions**.

1. Choose desired Lambda function.

1. Choose the **Test** tab.

1. Choose **CloudWatch Logs Live Trail**

1. Choose the drop-down menu and select the log groups you want to view.

1. Choose **Start**. The log will display in the **CloudWatch Logs Live Trail** window. Choose **View in columns** or **View in plain text** depending on your preference.
   + You can add more filters to the results by adding them in the **Add filter pattern** field. This field allows you filter results to only include events that match the specified pattern.

For more information on viewing logs for Lambda functions, see [Viewing CloudWatch Logs for Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs-view.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
