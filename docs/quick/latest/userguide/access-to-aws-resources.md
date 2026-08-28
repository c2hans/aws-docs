---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/access-to-aws-resources.html
---

# Configuring Amazon Quick Sight access to AWS data sources
<a name="access-to-aws-resources"></a>

Use this section to help you configure access to resources in other AWS services.

We recommend that you use SSL to secure Amazon Quick Sight connections to your data sources. To use SSL, you must have a certificate signed by a recognized certificate authority (CA). Amazon Quick doesn't accept certificates that are self-signed or issued from a nonpublic CA. For more information, see [Amazon Quick SSL and CA certificates](https://docs.aws.amazon.com/quicksuite/latest/userguide/configure-access.html#network-configuration-requirements).

**Topics**
+ [Required permissions](required-permissions.md)
+ [Network and database configuration requirements](configure-access.md)
+ [Allowing autodiscovery of AWS resources](autodiscover-aws-data-sources.md)
+ [Authorizing connections from Amazon Quick Sight to AWS data stores](enabling-access.md)
+ [Exploring your AWS data in Amazon Quick](explore-in-quicksight.md)
+ [AWS service action connectors](builtin-services-integration.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
