---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/saas-identity.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# SaaS identity
<a name="saas-identity"></a>

 SaaS adds new considerations to your application’s identity model. As each user is authenticated, they must be connected to a specific tenant context. This tenant context provides essential information about your tenant that is used throughout your SaaS environment.

 This binding of tenants to users is often referred to as the *SaaS identity* of your application. As each user authenticates, your identity provider will typically yield a token that includes both the user identity and tenant identity.

 Connecting tenants to users represents a foundational aspect of your SaaS architecture that has many downstream implications. The token from this identity process flows into the microservices of your application and is used to create tenant aware logs, record metrics, meter billing, enforce tenant isolation, and so on.

 It’s essential that you avoid scenarios that rely on separate, standalone mechanisms that map users to tenants. This can undermine the security of your system, and often creates bottlenecks in your architecture.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
