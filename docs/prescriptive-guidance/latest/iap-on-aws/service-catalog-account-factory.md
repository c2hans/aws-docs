---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iap-on-aws/service-catalog-account-factory.html
---

# Service Catalog Factory
<a name="service-catalog-account-factory"></a>

Service Catalog Factory is another tool provided by AWS Labs. It is similar to AWS Control Tower―it generates accounts and calls Service Catalog (potentially through Puppet) to provision IaP within those accounts. It uses many of the same mechanisms as Service Catalog Puppet to implement its capabilities. Service Catalog Factory can call Service Catalog or Service Catalog Puppet to provision the infrastructure for products in an account. This tool also supports account generation in multiple AWS Regions and organizations. For more information, see the Service Catalog Factory [documentation](https://service-catalog-tools-workshop.com/tools/factory.html) and [GitHub repository](https://github.com/awslabs/aws-service-catalog-factory).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
