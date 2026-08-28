---
source_url: https://docs.aws.amazon.com/nova-act/latest/userguide/step-4-review-workflow-runs.html
---

# Step 4: Review your workflow runs in the Nova Act console
<a name="step-4-review-workflow-runs"></a>

The Nova Act AWS console provides visibility into your workflow execution with detailed traces and artifacts.

To review a workflow run:

1. Navigate to the [Nova Act AWS console](https://us-east-1.console.aws.amazon.com/nova-act/home).

1. From the workflow definitions list, select the workflow you want to review. Each workflow definition displays its name, creation date, and recent activity status.

1. Select a **Run ID** from the workflow runs list. Each entry shows the run ID, status (succeeded, failed, or in progress), when the run started and ended, and a link to download artifacts.

1. In the workflow run details page, you can see the run summary, execution timeline, selected model ID, and any artifacts generated during the workflow.

1. Use the **Step view** to drill down into specific sessions and act calls.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova Act. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova-act` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
