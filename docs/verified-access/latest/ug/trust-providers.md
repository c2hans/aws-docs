---
source_url: https://docs.aws.amazon.com/verified-access/latest/ug/trust-providers.html
---

# Trust providers for Verified Access
<a name="trust-providers"></a>

A trust provider is a service that sends information about users and devices to AWS Verified Access. This information is called trust context. It can include attributes based on user identity, such as an email address or membership in the "sales" organization, or device information such as installed security patches or anti-virus software version.

Verified Access supports the following categories of trust providers:
+ **User identity** – An identity provider (IdP) service that stores and manages digital identities for users.
+ **Device management** – A device management system for devices such as laptops, tablets, and smartphones.

**Topics**
+ [User-identity trust providers for Verified Access](user-trust.md)
+ [Device-based trust providers for Verified Access](device-trust.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Verified Access. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verified-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
