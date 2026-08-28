---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/recommendations-preferences.html
---

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Strategy Recommendations preferences
<a name="recommendations-preferences"></a>

This section describes how to view and edit Migration Hub Strategy Recommendations preferences in the Migration Hub console.

You choose your recommendation preferences when you first set up Strategy Recommendations as described in [Step 5: Get recommendations](getting-started-get-recommendations.md). You can edit these preferences.

**To edit recommendation preferences**

1. Using the AWS account that you created in [Setting up Strategy Recommendations](setting-up.md), sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/).

1. In the Migration Hub console navigation pane, choose **Strategy** and then choose **Recommendations**.

1. On the **Recommendations** page, choose the **Preferences** tab.

1. Under **Prioritized business goals**, you can drag and drop the business goals to rearrange them.

1. Choose the **Application preferences** and **Database preferences** that you want, and then choose **Save changes**.

If you change your preferences, a banner is displayed to remind you to choose **Reanalyze data**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
