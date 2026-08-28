---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/practice-cloud-financial-management-cfm.html
---

# Practice Cloud Financial Management (CFM)
<a name="practice-cloud-financial-management-cfm"></a>

Cloud Financial Management (CFM) allows finance, product, technology, and business organizations to manage, optimize, and plan costs as they grow their usage and scale on AWS. The primary goal of CFM is to allow customers to achieve their business outcomes in the most cost-efficient manner and accelerate economic and business value creation while finding the right balance between agility and control. AWS CFM offers a set of capabilities to manage, optimize, and plan for cloud costs while maintaining business agility. CFM is paramount not only to effectively manage costs, but also to verify that investments are driving expected business outcomes. The four pillars of the Cloud Financial Management Framework in the AWS Cloud are *see*, *save*, *plan*, and *run*. Each of these pillar areas has a set of activities and capabilities.

 Expand showback and chargeback taxonomies to include generative AI-specific tags or Cost Categories such as `model_name`, `model_family`, `token_in`, `token_out`, `vector_store_ops`, `embedding_jobs`, `kb_storage_gb`, `agent_name`, and `safety_filters_triggered`. This enhances visibility into which generative AI components are driving spend and supports more precise forecasting and accountability.

 Establish **model policy tiers** (for example, gold, silver, and bronze) that map business criticality to permitted models, context window sizes, and latency SLOs. Enforce these tiers through guardrails in CI/CD pipelines and API gateways to ensure cost discipline and consistent application of enterprise standards.

 Following the best practices in CFM is essential for managing costs in your financial services workloads.

 These Cloud Financial Management best practices help you establish cost transparency to control your resources and plan your spend to optimize your return on investments.

**Topics**
+ [FSICOST01: Is your cloud team educated on relevant technical and commercial optimization mechanisms?](fsicost01.md)
+ [FSICOST02: Do you apply the Pareto-principle (80/20 rule) to manage, optimize, and plan your cloud usage and spend?](fsicost02.md)
+ [FSICOST03: Do you use automation to drive scale for Cloud Financial Management practices?](fsicost03.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
