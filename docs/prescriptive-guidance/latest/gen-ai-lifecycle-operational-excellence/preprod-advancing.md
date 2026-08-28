---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/preprod-advancing.html
---

# Advancing your generative AI application to production
<a name="preprod-advancing"></a>

The culmination of the preproduction stage is a formal go or no-go decision for production deployment. This decision should not be based on gut feelings, stakeholder pressure, or looming deadlines. It must be a data-driven decision based on whether the application has met a predefined, objective, and comprehensive set of exit criteria. Successfully navigating the preproduction stage is the single most important factor in determining whether a generative AI project will deliver tangible business value or become another stalled statistic.

The journey requires architects to design for the harsh realities of production by embracing modular, cloud-native patterns and centralized governance. It requires engineers to build a robust GenAIOps framework that automates the entire application lifecycle, including full-stack versioning, deep observability, and CI/CD pipelines. To build confidence in a non-deterministic system, you need a multi-layered testing strategy that combines traditional methods with novel automated evaluations and controlled rollouts. And it requires an unwavering commitment to security, with implemented guardrails, offensive red teaming, and auditable governance. Finally, it requires a continuous improvement loop that improves the application based on explicit and implicit user feedback.

By establishing these capabilities and holding the project accountable to a strict set of metric-driven exit criteria, organizations can transform a fragile prototype into a resilient, scalable, and trustworthy enterprise application. A go decision at this stage signifies that the organization has high confidence in the solution's ability to deliver sustained value and that it is ready to commit the resources for a full production rollout.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
