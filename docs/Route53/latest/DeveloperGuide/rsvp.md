---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rsvp.html
---

# .rsvp
<a name="rsvp"></a>

Used for events and reservations, from weddings to fundraisers to business bookings.

[Return to index](registrar-tld-list.md#index)

**Lease period for registration and renewal **
One to ten years.

**Restrictions**
HTTPS is required for all websites on this TLD. For the domain to work properly in browsers, you must configure HTTPS for your website. For more information about configuring HTTPS with AWS, including resources to obtain an SSL certificate, see [What Is AWS Certificate Manager?](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html).

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
