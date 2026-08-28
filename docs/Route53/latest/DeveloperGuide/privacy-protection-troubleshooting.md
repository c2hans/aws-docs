---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/privacy-protection-troubleshooting.html
---

# Troubleshooting privacy protection issues
<a name="privacy-protection-troubleshooting"></a>

Privacy protection option is not available in the console
This indicates that your domain's TLD does not support privacy protection. Your contact information will be publicly visible in WHOIS queries. This is normal behavior for certain TLDs due to registry policies or local regulations.
To verify whether your TLD supports privacy protection, check the individual TLD page in [Domains that you can register with Amazon Route 53](registrar-tld-list.md) or see [TLDs that don't support privacy protection](privacy-protection-tld-support.md).

Contact information is still visible after enabling privacy protection
Some registries maintain their own WHOIS databases and might continue to show contact information even when privacy protection is enabled with Route 53. This is controlled by the TLD registry, not by Route 53.
Additionally, some TLD registries intentionally maintain limited privacy protection or redaction services for their domains.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
