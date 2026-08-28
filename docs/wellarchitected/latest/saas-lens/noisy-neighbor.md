---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/noisy-neighbor.html
---

# Noisy Neighbor
<a name="noisy-neighbor"></a>

 Noisy neighbor is a term that is often applied to general architecture patterns and strategies. The idea behind noisy neighbor is that a user of a system could place load on the system’s resources that could have an adverse effect on other users of the system. The end result could be that one user could degrade the experience of another user.

 This concept has expanded relevance in a multi-tenant environment where tenants may be consuming shared resources. Adding to the complexity here is that workloads in a multi-tenant environment can be unpredictable. The combination heightens the need for SaaS architectures to employ their own strategies that can manage and minimize the potential impacts of noisy tenants.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
