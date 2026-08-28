---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

 This section provides troubleshooting instructions for deploying and using the Guidance.

## Problem: Transfer workflow has not progressed after 14 hours
<a name="problem-transfer-workflow-has-not-progressed-after-14-hours"></a>

 Your transfer workflow has been launched for more than 14 hours, but the **Downloaded** count on the CloudWatch dashboard has not increased.

### Resolution
<a name="resolution"></a>

1.  Sign in to the [Step Functions console](https://console.aws.amazon.com/states).

1.  Under **State machines**, select the state machine called `OrchestratorStateMachine$CFN_ID` and choose **View Details**.

1.  Select the most recent execution and choose **View details**.

1.  Note failures. If the workflow is still running the **InventoryRetrieval** workflow, there might be an issue with the Amazon Glacier service generating the inventory file. Contact [Support](https://aws.amazon.com/premiumsupport) if you have an AWS Developer Support plan or above.

## Problem: Transfer workflow must be stopped
<a name="problem-transfer-workflow-must-be-stopped"></a>

 Your transfer workflow is ongoing, but you want to stop it.

### Resolution
<a name="resolution-1"></a>

1.  Follow steps 1–3 in [Problem: Transfer workflow has not progressed after 14 hours](#problem-transfer-workflow-has-not-progressed-after-14-hours).

1.  Under **Actions**, choose **Stop execution**.

1.  If you plan to [resume the transfer workflow later](step-3-resume-the-transfer-workflow.md), find the `workflow_run` value from the **Execution Input and** **Output** tab on this page. You need this value to resume the workflow.
**Note**
 After you stop the execution, no new archives are requested from the Amazon Glacier service. The archives that were already requested will download. These downloads take 4–8 hours to complete.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
