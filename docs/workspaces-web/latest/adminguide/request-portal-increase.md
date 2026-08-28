---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/request-portal-increase.html
---

# Requesting a portal increase in Amazon WorkSpaces Secure Browser
<a name="request-portal-increase"></a>

A portal is the service’s foundational resource. Each portal is an association between your SAML 2.0 identity provider and your networking connection to the internet and any private web content. Each portal can have a separate portal browser policy and user settings, so administrators will commonly create multiple portals in the same region to address different use cases. For example, you can provide Group A with access to a specific website with restrictive policies (e.g., Clipboard and File transfer disabled), and Group B with access to the general internet without URL filtering. You can create a portal in any supported AWS Region. To view current service availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

To request a service quota increase

1. Open the [Service Quotas page](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/workspaces-web/quotas) in your desired region.

1. Choose **Number of Web Portals**.

1. Choose **Request an increase at account level**.

1. Under **Increase quota value**, enter in the total amount that you want the quota to be.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
