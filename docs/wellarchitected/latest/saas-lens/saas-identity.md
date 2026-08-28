---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/saas-identity.html
---

# SaaS Identity
<a name="saas-identity"></a>

 Most systems already rely on an identity provider for authentication. In the world of SaaS, we need to extend the notion of identity to incorporate tenancy into our definition of identity. This means that, after authenticating a user, we need to know who the user is as well as which tenant that user is associated with. This merging of the user identity with the tenant identity is referred to as a SaaS identity. This concept is a foundational element of a SaaS architecture, providing the tenant context that is used to implement the underlying multi-tenant policies and strategies that are part of a SaaS application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
