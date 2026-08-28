---
source_url: https://docs.aws.amazon.com/silk/latest/developerguide/ssl.html
---

# Learn about secure connections for Amazon Silk
<a name="ssl"></a>

Transport Layer Security (TLS) is a cryptographic protocol that provides security for online communications. Amazon Silk supports TLS communication between the device client on Fire devices and origin servers. For enhanced privacy and security, TLS traffic is not routed through Silk remote proxies in the Amazon Cloud, and we don't collect any metrics regarding web page resources downloaded using TLS connections. Amazon Silk currently supports up to TLS 1.2 for all Fire devices.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Silk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query silk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
