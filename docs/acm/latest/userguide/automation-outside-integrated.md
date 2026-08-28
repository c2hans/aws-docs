---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/automation-outside-integrated.html
---

# Automation outside integrated services
<a name="automation-outside-integrated"></a>

You can export an ACM issued certificate for use on any workload. Once exported, you get access to the certificate's private key that you can employ to securely terminate TLS traffic.

**Tip**
If you want to automate certificate issuance and renewal directly on your customer-managed infrastructure, we recommend ACME certificate automation for use with industry-standard, open source ACME clients (such as Certbot or cert-manager). See [ACME certificate automation](acm-acme.md). Alternatively, if you cannot use ACME, you can automate exportable certificates issued from ACM through [AWS Workload Credentials Provider](acm-certificate-automation.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
