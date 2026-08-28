---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/cloudwatch-container-insights-iam-permissions.html
---

# IAM permissions for Container Insights
<a name="cloudwatch-container-insights-iam-permissions"></a>

To enable or change Container Insights on a compute environment, AWS Batch requires the `ecs:UpdateCluster` permission. How you provide this permission depends on your compute environment's service role configuration.

Using the AWS Batch service-linked role (recommended)
If your compute environment uses the *AWSServiceRoleForBatch* service-linked role, the `ecs:UpdateCluster` permission is included automatically. No action is required.
For more information, see [Using service-linked roles for AWS Batch](using-service-linked-roles.md).

Using a custom service role
If your compute environment uses a custom service role, you must add the `ecs:UpdateCluster` permission to that role. Without this permission, updating Container Insights settings causes the compute environment to go to an `INVALID` state.
Add the following statement to your custom service role's policy:

```
{
    "Effect": "Allow",
    "Action": "ecs:UpdateCluster",
    "Resource": "arn:aws:ecs:*:*:cluster/*"
}
```

**Note**
If updating Container Insights fails because of missing permissions, the compute environment status changes to `INVALID` with a status reason explaining the error. After you correct the permissions, submit any `UpdateComputeEnvironment` request to trigger a retry. AWS Batch automatically reconciles the Container Insights setting on the next update workflow.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
