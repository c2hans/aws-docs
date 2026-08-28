---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-remove.html
---

# Removing a lens from a workload in AWS WA Tool
<a name="lenses-remove"></a>

If a lens is no longer relevant for your workload, you can remove it.

**To remove a lens from a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select the desired workload and choose **View details**.

1. Deselect the lens that you want to remove and choose **Save**.

   The AWS Well-Architected Framework Lens cannot be removed from a workload.

The data associated with the lens is retained. If the lens is added back to the workload, the data is restored.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
