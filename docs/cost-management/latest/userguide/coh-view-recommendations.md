---
source_url: https://docs.aws.amazon.com/cost-management/latest/userguide/coh-view-recommendations.html
---

# Viewing recommended actions and estimated savings
<a name="coh-view-recommendations"></a>

Use the following procedure to view a recommended action and estimated savings for a specific resource ID.

1. On the **Savings opportunities** page, under **Resources with estimated savings**, choose a row in the table.

   This opens a split-view panel with a recommended action and estimated savings for your chosen resource.

   The recommended action includes the following information:
   + **Usage:** The usage based on a 14-day lookback period.
   + **Estimated cost (before discounts):** The savings estimate using AWS public (On-Demand) pricing without incorporating any discounts.
   + **Estimated other discounts:** Estimated other discounts include all discounts that are not itemized, which includes Free Tier. Itemized discounts include Savings Plans and Reserved Instances.
   + **Estimated cost (after discounts):** The savings estimate incorporating all discounts with AWS, such as Reserved Instances and Savings Plans.
   + **Estimated unused net amortized commitments:** The net amortized Savings Plans and Reserved Instances costs included in the cost of the current instance but can't be used for the recommended instance.
   + **Estimated monthly savings:** The estimated monthly savings amount for the recommendation.
   + **Estimated savings percentage:** The estimated savings percentage relative to the total cost.

1. Based on the recommended action, you can choose to view the recommendation in the AWS Billing and Cost Management console, or you can open it in AWS Compute Optimizer or the relevant console.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
