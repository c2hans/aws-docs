---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_quick_protection_plan_config.html
---

# (Optional) Enable protection plans for existing member accounts
<a name="guardduty_quick_protection_plan_config"></a>

The following procedure includes steps to enable protection plans for existing member accounts by using the **Accounts** page. For steps to do this by using API or AWS CLI, see documents related to the specific protection plan.

You can enable protection plans for individual accounts through the **Accounts** page.

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Use the delegated GuardDuty administrator account credentials.

1. In the navigation pane, choose **Accounts**.

1. Select one or more accounts for which you want to configure a protection plan. Repeat the following steps for each protection plan that you want to configure:

   1. Choose **Edit Protection Plans**.

   1. From the list of protection plans, choose one protection plan that you want to configure.

   1. Choose one of the actions that you want to perform for this protection plan, and then choose **Confirm**.

   1. For the selected account, the column corresponding to the configured protection plan will show the updated configuration as **Enabled** or **Not enabled**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
