---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/deleting-profiles.html
---

# Deleting a profile from AWS WA Tool
<a name="deleting-profiles"></a>

If you created a profile, you can delete the profile from the list of profiles available in AWS WA Tool.

Deleting a profile from the **Profiles** page does not remove the profile from any associated workloads. You can continue using profiles that were shared and associated with a workload before deletion, however, no new workloads can be associated with a deleted profile. [Profile notifications](notifications.md#profiles-notifications) are sent to workload owners using deleted profiles.

**Disclaimer**
By sharing your profiles with other AWS accounts, you acknowledge that AWS will make your profiles available to those other accounts. Those other accounts may continue to access and use your shared profiles even if you delete the profile from your own AWS account or terminate your AWS account.

**To delete a profile from your list of profiles**

1. Select **Profiles** in the left navigation pane.

1. Select the name of the profile you want to remove.

1. Choose **Delete**.

1. To confirm removal, enter the profile name in the text input field.

1. Choose **Delete**.

If you want to keep a profile in your **Profiles** list, but remove it from a workload, see [Removing a profile from a workload in AWS WA Tool](removing-profiles-from-workloads.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
