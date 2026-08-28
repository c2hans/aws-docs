---
source_url: https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-pricing.html
---

# Pricing columns
<a name="table-dictionary-cur2-pricing"></a>

Pricing columns contain data about the pricing for a line item.

| Column name | Description | Data type |
| --- | --- | --- |
| pricing\_currency | The currency that the pricing data is shown in. | string |
| pricing\_lease\_contract\_length | The length of time that your RI is reserved for. | string |
| pricing\_offering\_class | The offering class of the Reserved Instance. | string |
| pricing\_public\_on\_demand\_cost | The total cost for the line item based on public On-Demand Instance rates. If you have SKUs with multiple On-Demand public costs, the equivalent cost for the highest tier is displayed. For example, services offering free-tiers or tiered pricing. | double |
| pricing\_public\_on\_demand\_rate | The public On-Demand Instance rate in this billing period for the specific line item of usage. If you have SKUs with multiple On-Demand public rates, the equivalent rate for the highest tier is displayed. For example, services offering free-tiers or tiered pricing. | string |
| pricing\_purchase\_option | How you chose to pay for this line item. Valid values are All Upfront, Partial Upfront, and No Upfront. | string |
| pricing\_rate\_code | A unique code for a product/offer/pricing-tier combination. The product and term combinations can have multiple price dimensions, such as a free tier, low-use tier, and high-use tier. | string |
| pricing\_rate\_id | The ID of the rate for a line item. | string |
| pricing\_term | Whether your AWS usage is Reserved or On-Demand. | string |
| pricing\_unit | The pricing unit AWS used to calculate your usage cost. For example, the pricing unit for Amazon EC2 instance usage is in hours. | string |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cur` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
