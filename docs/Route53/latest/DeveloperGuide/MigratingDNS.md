---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html
---

# Making Amazon Route 53 the DNS service for an existing domain
<a name="MigratingDNS"></a>

If you're transferring one or more domain registrations to Route 53, and your current registrar doesn't provide paid DNS service, you need to migrate DNS service before you transfer the domain. Otherwise, the registrar will stop providing DNS service when you transfer your domains. The associated websites and web applications will become unavailable on the internet. (You can also migrate DNS service to another DNS service provider. You don't have to use Route 53 as the DNS service provider for domains registered with Route 53.)

The process depends on whether you're currently using the domain:
+ If the domain is currently getting traffic—for example, if your users are using the domain name to browse to a website or access a web application—see [Making Route 53 the DNS service for a domain that's in use](migrate-dns-domain-in-use.md).
+ If the domain isn't getting any traffic (or is getting very little traffic), see [Making Route 53 the DNS service for an inactive domain](migrate-dns-domain-inactive.md).

For both options, your domain should remain available during the entire migration process. However, in the unlikely event that there are issues, the first option lets you roll back quickly. With the second option, your domain could be unavailable for a couple of days.

If you want to connect with an expert at AWS, visit [Sales support](https://aws.amazon.com/contact-us/sales-support/?pg=ln&sec=hs).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
