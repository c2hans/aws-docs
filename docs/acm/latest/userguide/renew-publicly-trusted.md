---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/renew-publicly-trusted.html
---

# Renew ACM public certificates
<a name="renew-publicly-trusted"></a>

When issuing a managed, publicly trusted certificate, AWS Certificate Manager requires you to prove that you are the domain owner. This happens by means of either [DNS validation](dns-validation.md) or [email validation](email-validation.md). When a certificate comes up for renewal, ACM uses the same method that you chose earlier to re-validate your ownership. The following topics describe how the renewal process works in each case.

**Topics**
+ [Renewal for domains validated by DNS](dns-renewal-validation.md)
+ [Renewal for email-validated domains](email-renewal-validation.md)
+ [Renewal for domains validated by HTTP](http-renewal-validation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
