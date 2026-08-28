---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/sharing-remove.html
---

# Delete shared access in AWS Well-Architected Tool
<a name="sharing-remove"></a>

You can delete a workload invitation. Deleting a workload invitation removes shared access to the workload.

**To delete shared access to a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select the workload in one of the following ways:
   + Choose the name of the workload.
   + Select the workload and choose **View details**.

1. Choose **Shares**.

1. Select the workload invitation to delete and choose **Delete**.

1. Choose **Delete** to confirm.

If a user and the user's AWS account have workload invitations, you must delete both workload invitations to remove the user's permission to the workload.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
