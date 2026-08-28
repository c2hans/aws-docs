---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/settings.html
---

# Manage Demand Plan settings
<a name="settings"></a>

You can update the Demand Planning settings at any time to make sure that your forecasts are more accurate and take effect when the forecast is successfully generated.

**Note**
Your prior forecast versions will be unavailable when you modify the *Time Interval* and *Hierarchy levels* on the **Demand Plan** page, because those prior versions will no longer align with the new forecast settings.
When you modify the *Time interval* or *Hierarchy* configuration and when you regenerate the forecast, the accuracy metrics will not be displayed since the accuracy metric values are not relevant.

1. In the left navigation pane on the Supply Chain dashboard, choose the **Settings** icon.

1. Under **Organization**, choose **Demand Planning**.

   The **Demand Planning Setting** page appears.

   Use the steps in [Create your first demand plan](onboarding.md) to edit the Demand Planning configuration settings.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
