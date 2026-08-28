---
source_url: https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-rec-customizing.html
---

# Customizing Savings Plans recommendations
<a name="sp-rec-customizing"></a>

You can customize your Savings Plans recommendations using parameters shown on the **Recommendations** page.<a name="sp-rec-customize-howto"></a>

**To customize your Savings Plans recommendations**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Recommendations**.

1. For **Savings Plan type**, choose **Compute Savings Plans**, **Database Savings Plans**, **EC2 Instance Savings Plans**, or **SageMaker AI Savings Plans**.

1. Choose a **Savings Plans term**.

1. Choose a **Payment option**.

1. Choose the number of days for **Based on the past**.

1. (Management account level only) Choose the **Linked accounts** tab, and then select the account IDs you want the recommendations for.

1. (Optional) To purchase the plans, select the check box next to your desired plans, and choose **Add Savings Plans to cart**.

Your recommendations change as you customize your selections. You’ll see the most optimal option presented to you in the **Our recommendation** section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Savings Plans. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query savingsplans` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
