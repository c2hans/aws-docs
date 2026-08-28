---
source_url: https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/the-developer-experience.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# The developer experience
<a name="the-developer-experience"></a>

 As a general architectural principle, developers typically attempt to introduce layers or frameworks that centralize and abstract away horizontal aspects of their applications. The goal here is to centralize and standardize policies and tenant resolution strategies. You might, for example, introduce a data access layer that would inject tenant context into data access requests. This would simplify development and limit a developer’s awareness of how tenant identity flows through the system.

 Having this layer in place also provides you with more options for policies and strategies that might vary on a tenant-by-tenant basis. It also creates a natural opportunity to centralize configuration and tracking of storage activity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
