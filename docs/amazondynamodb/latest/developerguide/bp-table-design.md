---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-table-design.html
---

# Best practices for DynamoDB table design
<a name="bp-table-design"></a>

General design principles in Amazon DynamoDB recommend that you keep the number of tables you use to a minimum. In the majority of cases, we recommend that you consider using a single table. However if a single or small number of tables are not viable, these guidelines might be of use.
+ The per account limit cannot be increased above 10,000 tables per account. If your application requires more tables, plan for distributing the tables across multiple accounts. For more information see [ service, account, and table quotas in Amazon DynamoDB.](ServiceQuotas.html#limits-tables)
+ Consider control plane limits for concurrent control plane operations that might impact your table management.
+ Work with AWS solution architects to validate your design patterns for multi-tenant designs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
