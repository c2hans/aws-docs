---
source_url: https://docs.aws.amazon.com/privateca/latest/userguide/auto-export.html
---

# Automate export of a renewed certificate
<a name="auto-export"></a>

When you use AWS Private CA to create a CA, you can import that CA into AWS Certificate Manager and let ACM manage certificate issuance and renewal. If a certificate being renewed is associated with an [integrated service](https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html), the service seamlessly applies the new certificate. However, if the certificate was originally [exported](https://docs.aws.amazon.com/acm/latest/userguide/export-private.html) for use elsewhere in your PKI environment (for example, in an on-premises server or appliance), you need to export it again after renewal.

For a sample solution that automates the ACM export process using Amazon EventBridge and AWS Lambda, see [Automating export of renewed certificates](https://docs.aws.amazon.com/acm/latest/userguide/renew-private-cert.html#automating-export).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private Certificate Authority. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
