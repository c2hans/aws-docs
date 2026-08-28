---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-selecting.html
---

# Determining which lens to upgrade in AWS WA Tool
<a name="lenses-selecting"></a>

You can find which workloads aren't using the most current lens version by viewing the **Notifications** page.

The following information is displayed on the **Notifications** page for each workload:

**Resource**
The name of the workload or review template.

**Resource type**
The type of resource. This can be either **Workload** or **Review template**.

**Associated resource**
The name of the lens.

**Notification type**
The type of upgrade notification.
+ **Not current** – The workload is using a version of the lens that is no longer current. Upgrade to the current lens version for better guidance.
+ **Deprecated** – The workload is using a version of the lens that no longer reflects best practices. Upgrade to the current lens version.
+ **Deleted** – The workload is using a lens that has been deleted by its owner.

**Version in use**
The lens version currently used for the workload.

**Current available version**
The lens version available for upgrade, or **None** if the lens has been deleted.

To upgrade the lens associated with a workload, select the workload and choose **Upgrade lens version**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
