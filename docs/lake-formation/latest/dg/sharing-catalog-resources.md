---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/sharing-catalog-resources.html
---

# Sharing Data Catalog tables and databases across AWS Accounts
<a name="sharing-catalog-resources"></a>

You can share Data Catalog resources (databases and tables) with external AWS accounts by granting Lake Formation permissions on the resources to the external accounts. Users can then run queries and jobs that join and query tables across multiple accounts. With some restrictions, when you share a Data Catalog resource with another account, principals in that account can operate on that resource as if the resource were in their Data Catalog.

You don't share resources with specific principals in external AWS accounts—you share the resources with an AWS account or organization. When you share a resource with an AWS organization, you're sharing the resource with all accounts at all levels in that organization. The data lake administrator in each external account must then grant permissions on the shared resources to principals in their account.

For more information, see [Cross-account data sharing in Lake Formation](cross-account-permissions.md) and [Granting permissions on Data Catalog resources](granting-catalog-permissions.md).

**See Also:**
[Accessing and viewing shared Data Catalog tables and databases](viewing-shared-resources.md)
[Prerequisites](cross-account-prereqs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
