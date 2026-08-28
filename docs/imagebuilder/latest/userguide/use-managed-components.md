---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/userguide/use-managed-components.html
---

# Use managed components to customize your Image Builder image
<a name="use-managed-components"></a>

Managed components are created by AWS, sometimes in partnership with a third-party organization, such as the Center for Internet Security (CIS), for example. When you use managed components in your image or container recipes, Amazon provides the latest component versions that have patches and other updates applied. To get a list of components, or to get component information, see [List and view component details](component-details.md).

The following list of featured AWS managed components includes a component that's available for you to use when you subscribe to CIS hardened AMIs through the AWS Marketplace.

**Topics**
+ [Distributor package managed component application install for Image Builder Windows images](mgdcomponent-distributor-win.md)
+ [CIS hardening components](toe-cis.md)
+ [Amazon managed STIG hardening components for Image Builder](ib-stig.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
