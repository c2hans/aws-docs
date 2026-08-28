---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/catalog-integration-identity-propagation.html
---

# Identity propagation for data governance
<a name="catalog-integration-identity-propagation"></a>

In addition to the agentic experience and semantic inheritance, Quick supports identity propagation for applicable catalogs. When enabled, identity propagation enforces per-user data permissions at query time based on the user's identity in the upstream catalog.

For example, if John has access to US-Northeast region data and Mary has access to US-West region data, when each user views the same dashboard, they see only the data they are permitted to access. Permissions are enforced by the upstream catalog, not by manual Quick configuration.

**Important**
Identity propagation works only for DirectQuery datasets. If a dataset is switched to SPICE or has transformations applied, identity propagation does not apply.

**Important**
The agentic catalog experience (natural language discovery, bulk creation of datasets and topics, semantic inheritance) works with any supported authentication type. Identity propagation is not a prerequisite for the agentic experience. It is an optional, additive capability for customers who require per-user governance enforcement.

If you do not enable identity propagation, you can manage data permissions manually by using row-level security (RLS) and column-level security (CLS) rules in Quick.

The following identity propagation methods are available:
+ **AWS Glue Data Catalog** – Trusted identity propagation through AWS IAM Identity Center and Lake Formation. For setup instructions, see [Setting up trusted identity propagation for AWS Glue Data Catalog](catalog-integration-glue-tip.md).
+ **Databricks Unity Catalog** – OAuth 3LO (three-legged OAuth) with end-user identities. For setup instructions, see [Setting up identity enforcement with Databricks 3LO](catalog-integration-databricks-3lo.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
