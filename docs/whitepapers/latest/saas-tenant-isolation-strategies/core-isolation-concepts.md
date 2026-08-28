---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/core-isolation-concepts.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Core isolation concepts
<a name="core-isolation-concepts"></a>

 Part of the challenge of isolation is that there are multiple definitions of tenant isolation. For some, isolation is almost a business construct where they think about entire customers requiring their own environments. For others, isolation is more of an architectural construct that overlays the services and constructs of your multi-tenant environment. The sections below will explore the different types of isolation, and associate specific terminology with the varying isolation constructs.

**Topics**
+ [Silo isolation](silo-isolation.md)
+ [Pool isolation](pool-isolation.md)
+ [The bridge model](the-bridge-model.md)
+ [Tier-based isolation](tier-based-isolation.md)
+ [Identity and isolation](identity-and-isolation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
