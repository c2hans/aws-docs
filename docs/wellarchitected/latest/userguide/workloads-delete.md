---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads-delete.html
---

# Delete a workload in AWS Well-Architected Tool
<a name="workloads-delete"></a>

You can delete a workload when it's no longer needed. Deleting a workload removes all data associated with the workload including any milestones and workload share invitations. Only the owner of a workload can delete it.

**Warning**
Deleting a workload cannot be undone. All data associated with the workload is permanently removed.

**To delete a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select the workload you want to delete and choose **Delete**.

1. In the **Delete** window, choose **Delete** to confirm the deletion of the workload and its milestones.

To prevent an entity from deleting workloads, attach a policy that denies `wellarchitected:DeleteWorkload` actions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
