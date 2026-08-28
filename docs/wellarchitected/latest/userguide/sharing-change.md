---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/sharing-change.html
---

# Modify shared access in AWS Well-Architected Tool
<a name="sharing-change"></a>

You can modify a pending or accepted workload invitation.

**To modify shared access to a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select a workload that you own in one of the following ways:
   + Choose the name of the workload.
   + Select the workload and choose **View details**.

1. Choose **Shares**.

1. Select the workload invitation to modify and choose **Edit**.

1. Choose the new permission that you want to grant to the AWS account or user.
**Read-Only**
Provides read-only access to the workload.
**Contributor**
Provides update access to answers and their notes, and read-only access to the rest of the workload.

1. Choose **Save**.

If the modified workload invitation is not accepted within seven days, it's automatically expired.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
