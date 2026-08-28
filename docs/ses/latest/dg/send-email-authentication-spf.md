---
source_url: https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-spf.html
---

# Authenticating Email with SPF in Amazon SES
<a name="send-email-authentication-spf"></a>

*Sender Policy Framework* (SPF) is an email validation standard that's designed to prevent email spoofing. Domain owners use SPF to tell email providers which servers are allowed to send email from their domains. SPF is defined in [RFC 7208](https://tools.ietf.org/html/rfc7208).

Messages that you send through Amazon SES automatically use a subdomain of `amazonses.com` as the default MAIL FROM domain. SPF authentication successfully validates these messages because the default MAIL FROM domain matches the application that sent the email—in this case, SES. Therefore, in SES, SPF is implicitly set up for you.

However, if you don't want to use the SES default MAIL FROM domain, and would rather use a subdomain of a domain that you own, this is referred to in SES as using a *custom* MAIL FROM domain. To do this, it requires you to publish your own SPF record for your custom MAIL FROM domain. In addition, SES also requires you to set up an MX record so that your custom MAIL FROM domain can receive the bounce and complaint notifications that email providers send you.

**Learn how to set up SPF authentication**
Instructions are given for configuring your domain with SPF and how to publish the MX and SPF (type TXT) records in [Using a custom MAIL FROM domain](mail-from.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
