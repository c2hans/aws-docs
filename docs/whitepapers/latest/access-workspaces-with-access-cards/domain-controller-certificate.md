---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/domain-controller-certificate.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Domain controller certificate
<a name="domain-controller-certificate"></a>

Each domain controller that is going to authenticate smartcard users must have a domain controller certificate. Request and install a domain controller certificate on each domain controller.

If you install a Microsoft Enterprise CA in an AD forest, all domain controllers automatically enroll for a domain controller certificate.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
