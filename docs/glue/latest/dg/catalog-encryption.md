---
source_url: https://docs.aws.amazon.com/glue/latest/dg/catalog-encryption.html
---

# Encrypting your Data Catalog
<a name="catalog-encryption"></a>

 You can protect your metadata stored in the AWS Glue Data Catalog at rest using encryption keys managed by AWS Key Management Service (AWS KMS). You can enable Data Catalog encryption for new Data Catalog, by using the **Data Catalog settings**. You can enable or disable encryption for existing Data Catalog as needed. When enabled, AWS Glue encrypts all new metadata written to the catalog, while existing metadata remains unencrypted.

For detailed information about encrypting your Data Catalog, see [Encrypting your Data Catalog](encrypt-glue-data-catalog.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
