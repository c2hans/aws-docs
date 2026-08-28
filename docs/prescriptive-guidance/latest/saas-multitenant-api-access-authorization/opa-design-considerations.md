---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/opa-design-considerations.html
---

# OPA multi-tenant design considerations
<a name="opa-design-considerations"></a>

The Open Policy Agent (OPA) is a flexible service that can be applied to numerous use cases where applications are required to make policy and authorization decisions. Using OPA with multi-tenant SaaS applications requires the consideration of unique criteria to ensure that key SaaS best practices such as tenant isolation remain a part of OPA's implementation. These criteria include OPA deployment patterns, tenant isolation and the OPA document model, and tenant onboarding. Each of these affects the optimal design for OPA as it pertains to multi-tenant applications.

Although the discussion in this section focuses on OPA, the general concepts are rooted in the [isolation mindset](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/pool-isolation.html) and the guidance it provides. SaaS applications must always consider tenant isolation as part of their design, and this general principle of isolation extends to including OPA in a SaaS application. OPA, if used appropriately, can be a key part of how isolation is enforced in SaaS applications. This section also references core SaaS isolation models such as the [siloed SaaS model](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/silo-isolation.html) and the [pooled SaaS model](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/pool-isolation.html). For additional information, see the [core isolation concepts](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/core-isolation-concepts.html) in the AWS Well-Architected Framework, SaaS Lens.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
