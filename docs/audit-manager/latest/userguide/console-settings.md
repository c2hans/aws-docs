---
source_url: https://docs.aws.amazon.com/audit-manager/latest/userguide/console-settings.html
---

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

# Reviewing and configuring your AWS Audit Manager settings
<a name="console-settings"></a>

You can review and configure your AWS Audit Manager settings at any time to ensure that they meet your specific needs.

This chapter takes you through the process of accessing, reviewing, and adjusting your Audit Manager settings step-by-step. By following along, you'll learn how to change your general settings, assessment settings, and evidence finder settings to align with your evolving compliance goals and business requirements.

## Procedure
<a name="settings-procedure"></a>

To get started, follow these steps to view your Audit Manager settings. You can view your Audit Manager settings using the Audit Manager console, the AWS Command Line Interface (AWS CLI), or the Audit Manager API.

**To view your settings**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the left navigation pane, choose **Settings**.

1. Choose the tab that meets your goal.
   + **General settings** - Choose this tab to review and update your general Audit Manager settings.
   + **Assessment settings** - Choose this tab to review and update the default settings for your assessments.
   + **Evidence finder settings** - Choose this tab to review and update your evidence finder settings.

## Next steps
<a name="settings-next-steps"></a>

To customize your Audit Manager settings for your use case, follow the procedures that are outlined here.
+ **General settings**
  + [Configuring your data encryption settings](settings-KMS.md)
  + [Adding a delegated administrator](add-delegated-admin.md)
  + [Changing a delegated administrator](change-delegated-admin.md)
  + [Removing a delegated administrator](remove-delegated-admin.md)
  + [Disabling AWS Audit Manager](disable.md)
+ **Assessment settings**
  + [Configuring your default audit owners](settings-default-audit-owner.md)
  + [Configuring your default assessment report destination](settings-destination.md)
  + [Configuring your Audit Manager notifications](settings-notifications.md)
+ **Evidence finder settings**
  + [Enabling evidence finder](evidence-finder-settings-enable.md)
  + [Confirming the status of evidence finder](confirm-status-of-evidence-finder.md)
  + [Configuring your default export destination for evidence finder](settings-export-destination.md)
  + [Disabling evidence finder](evidence-finder-settings-disable.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
