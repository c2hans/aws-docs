---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/post-launch-settings-source.html
---

# Post-launch settings
<a name="post-launch-settings-source"></a>

Post-launch settings allow you to control and automate actions performed after a recovery instance has been launched for the source server in AWS. These settings are created automatically based on the **Default post-launch actions**.

**Activating the post-launch actions for a specific source server**:
+ Navigate to the **Source servers** page and select a source server.
+ Go to the **Post-launch settings** tab. If **Post launch action settings** has **Post launch actions** set to **Active**, click **Edit** for **Post launch action settings**.
+ You will be redirected to the **Edit post-launch settings** screen. Make sure the **Post-launch actions active** option is not checked and click **Save**.

 Alternatively, you can activate and deactivate post-launch actions for multiple servers by navigating to the **Source servers** page, selecting the servers you want to update and clicking **Actions > Edit post-launch action settings**. To activate, make sure the **Post-launch actions active** option is checked, and to deactivate, it should be unchecked. If you made a change, click **Save**.

**Topics**
+ [Adding custom actions with AWS DRS](post-launch-action-settings-adding-custom-source.md)
+ [Activating, deactivating, and editing predefined or custom actions](post-launch-action-settings-editing-source.md)
+ [Deleting custom actions](post-launch-action-settings-deleting-source.md)
+ [Predefined post-launch actions](predefined-post-launch-actions-source.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
