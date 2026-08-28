---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/name.html
---

# .name
<a name="name"></a>

Used by anyone who wants to create a personalized web presence.

[Return to index](registrar-tld-list.md#index)

**Lease period for registration and renewal**
One to ten years.

**Restrictions**
Verisign, the registry for .name TLDs, allows you to register both second-level domains (*name*.name) and third-level domains (*firstname*.*lastname*.name). Route 53 supports only second-level domains, both for registering domains and for transferring existing domains to Route 53.

**Privacy protection (applies to all contact types: person, company, association, and public body)**
All information is hidden except organization name.

**Domain locking to prevent unauthorized transfers**
Supported.

**Internationalized domain names**
Supported.

**Authorization code required for transfers**
Yes

**DNSSEC**
Supported for domain registration. For more information, see [Configuring DNSSEC for a domain](domain-configure-dnssec.md).

**Deadlines for renewing and restoring domains**
+ Renewal is possible: Until the expiration date
+ Late renewal with Route 53 is possible: Until 44 days after expiration
+ Domain is deleted from Route 53: 45 days after expiration
+ Restoration with the registry is possible: Between 45 days and 75 days after expiration
+ Domain is deleted from the registry: 75 days after expiration

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
