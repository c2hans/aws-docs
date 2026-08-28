---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/dns-renewal-validation.html
---

# Renewal for domains validated by DNS
<a name="dns-renewal-validation"></a>

Managed renewal is fully automated for ACM certificates that were originally issued using [DNS validation](dns-validation.md).

At 45 days prior to expiration, ACM checks for the following renewal criteria:

**Note**
Previously issued certificates with a 395-day validity period renew 60 days before expiration and receive a renewed validity period of 198 days. Certificates with a 198-day validity period renew 45 days before expiration.
+ The certificate is currently in use by an AWS service.
+ All required ACM-provided DNS CNAME records (one for each unique Subject Alternative Name) are present and accessible via public DNS.

If these criteria are met, ACM considers the domain names validated and renews the certificate.

ACM sends AWS Health events and Amazon EventBridge events if it can't automatically validate a domain during renewal. These events are sent at 30 days, 15 days, seven days, three days, and one day prior to expiration. For more information, see [Amazon EventBridge support for ACM](supported-events.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
