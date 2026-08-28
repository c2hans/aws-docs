---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/about-mapping-destinations.html
---

# About mapping destinations in Connect Customer
<a name="about-mapping-destinations"></a>

A mapping destination is your mapping from a source to a standard definition that is already defined in Connect Customer.

The following table lists the supported mapping destinations.

| Source object | Destination: Customer, Product, Order, Case |
| --- | --- |
| S3 | Any |
| Salesforce-Account | Customer |
| Salesforce-Contact | Customer |
| Salesforce-Asset | Product |
| Zendesk-users | Customer |
| Marketo-leads | Customer |
| Servicenow-sys\_user | Customer |
| Segment-Identify | Customer |
| Segment-Customer | Customer |
| Shopify-Customer | Customer |
| Shopify-DraftOrder | Order |
| Zendesk-tickets | Case |
| Servicenow-task | Case |
| Servicenow-incident | Case |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
