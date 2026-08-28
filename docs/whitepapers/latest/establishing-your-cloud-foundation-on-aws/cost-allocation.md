---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/cost-allocation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Cost allocation
<a name="cost-allocation"></a>

Leveraging metadata across your environment, helps you to accurately allocate cost for workloads and applications. Using a showback approach you can identify the costs incurred by a business unit, product, or team. However, material spends, may not be accounted for due to the lack of enforcing tagging mechanisms. Grouping your different resource and establishing boundaries between them can help you identify how those groups of resources are using the budget assigned to a specific business unit or across different stages software development lifecycle of a workload.

Creating categories to consolidate groups of resources based on your business needs (some examples of categories would include: Business Unit, Product Line, Environment). Once these categories are established and set up, you can use them to monitor cost and usage information within these categories. Additionally, you can retrieve meaningful information from these groups of resources leveraging multiple dimensions (such as, who created a resource). For example, the Line of Business where a resource belongs.

Leveraging infrastructure as code to deploy infrastructure and resources for your workloads will allow you to consistently apply tags from your tagging dictionary, avoid untagged resources, and enforce your tagging policy to ensure the cloud financial management capability allows you to allocate costs for your infrastructure when needed.

With the appropriate mechanisms in place, the Cost Allocation methods allow you to carve out material cloud charges, including commitment purchases, standalone, and shared resources. For example, networking, log retention and archival, security tools, and operational tools charges. Establishing chargeback mechanisms will allow you to report costs incurred by different business units, products, and teams.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
