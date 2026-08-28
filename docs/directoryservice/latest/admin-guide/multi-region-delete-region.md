---
source_url: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/multi-region-delete-region.html
---

# Deleting a replicated Region for AWS Managed Microsoft AD
<a name="multi-region-delete-region"></a>

Use the following procedure to delete a Region for your AWS Managed Microsoft AD directory. Before you delete a Region, make sure it does not have either of the following:
+ Authorized applications attached to it.
+ Shared directories associated with it.

**To delete a replicated Region**

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/) navigation pane, choose **Directories**.

1. From the navigation bar, choose the **Regions** selector and choose the region where your directory is stored.

1. On the **Directories** page, choose your directory ID.

1. On the **Directory details** page, under **Multi-Region replication** choose **Delete Region**.

1. In the **Delete Region** dialog box, review the information, and then enter in the Region name to confirm. Then choose **Delete**.
**Note**
You cannot make updates to the Region while it's being deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
