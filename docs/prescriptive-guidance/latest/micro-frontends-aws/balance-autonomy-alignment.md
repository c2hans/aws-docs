---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/balance-autonomy-alignment.html
---

# Balancing autonomy with alignment
<a name="balance-autonomy-alignment"></a>

Micro-frontend architectures are strongly biased toward team autonomy. However, it's important to distinguish between areas that can support flexibility and diverse approaches to solve problems, and areas where standardization is necessary to achieve alignment. Senior leaders and architects must identify these areas early on and prioritize investments to balance security, performance, operational excellence, and reliability of micro-frontends. Finding this balance involves the following: micro-frontend creation, testing, release, and logging, monitoring, and alerting.

## Creating micro-frontends
<a name="create"></a>

Ideally, all teams are strongly aligned to maximize benefits in terms of end-user performance. In practice, this can be hard, and it might require more effort. We recommend starting with some written guidelines that multiple teams can contribute to through open and transparent debate. Teams can then gradually adopt the Cookiecutter software pattern, which supports creating tools that provide a unified way to scaffold a project.

Using this approach, you can bake in opinions and constraints. The downside is that these tools require significant investment for creation and maintenance, and to ensure that blockers are addressed quickly without affecting developer productivity.

## End-to-end testing for micro-frontends
<a name="testing"></a>

Unit testing can be left to owners. We recommend implementing a strategy early on to cross-test micro-frontends running on a unique shell. The strategy includes the capability to test applications before and after a production release. We recommend developing processes and documentation for technical and nontechnical people to test critical functionalities manually.

It's important to ensure that changes don't degrade either the functional or the nonfunctional customer experience. An ideal strategy is to gradually invest in automated testing, both for key features and for architecture characteristics such as security and performance.

## Releasing micro-frontends
<a name="release"></a>

Each team might have its own way to deploy their code, bake in opinions, and own infrastructure. The cost of complexity for maintaining such systems is usually a deterrent. Instead, we recommend investing early on to implement a shared strategy that can be enforced by shared tools.

Develop templates with the CI/CD platform of choice. Teams can then use the preapproved templates and shared infrastructure to release changes to production. You can begin investing in this development work early because these systems rarely need significant updates after an initial period of testing and consolidation.

## Logging and monitoring
<a name="logging"></a>

Each team can have different business and system metrics that they want to track for operational or analytics purposes. The Cookiecutter software pattern can be applied here as well. The delivery of events can be abstracted and made available as a library that multiple micro-frontends can consume. To balance flexibility and provide autonomy, develop tools for logging custom metrics and creating custom dashboards or reports. The reporting promotes close collaboration with product owners and reduces the end-customer feedback loop.

By standardizing the delivery, multiple teams can collaborate to track metrics. For example, an e-commerce website can track the user journey from the "Product details" micro-frontend to the "Cart" micro-frontend, to the "Purchase" micro-frontend to measure engagement, churn, and issues. If each micro-frontend logs events by using a single library, you can consume this data as whole, explore it holistically, and identify insightful trends.

## Alerting
<a name="alerting"></a>

Similar to logging and monitoring, alerting benefits from standardization with room for a degree of flexibility. Different teams might react differently to functional and non-functional alerts. However, if all teams have a consolidated way to initiate alerts based on metrics that are collected and analyzed on a shared platform, the business can identify cross-team issues. This capability is useful during incident-management events. For example, alerts can be initiated by the following:
+ Elevated number of JavaScript client-side exceptions on a particular browser version
+ Time to render significantly degraded over a given threshold
+ Elevated number of 5xx status codes when consuming a particular API

Depending on the maturity of your system, you can balance your efforts on different parts of your infrastructure, as shown in the following table.

|
|
| Adoption | Research and development | Ascent | Maturity |
| --- |--- |--- |--- |
| Create micro-frontends. | Experiment, document, and share learnings. | Invest in tooling to scaffold new micro-frontends. Evangelize adoption. | Consolidate tooling for scaffolding. Push for adoption. |
| Test micro-frontends end to end. | Implement mechanisms for manually testing all related micro-frontends. | Invest in tooling for automated security and performance testing. Investigate feature flags and service discovery. | Consolidate tooling for service discovery, testing in production, and automated end-to-end testing. |
| Release micro-frontends. | Invest in a shared CI/CD infrastructure and automated multiple-environment releases. Evangelize adoption. | Consolidate tooling for CI/CD infrastructure Implement manual rollback mechanisms. Push for adoption. | Create mechanisms to initiate automated rollbacks on top of system and business metrics and alerts. |
| Observe micro-frontend performance. | Invest in a shared monitoring infrastructure and library for consistent logging of system and business events. | Consolidate tooling for monitoring and alerting. Implement cross-team dashboards to monitor general health and improve incident management. | Standardize logging schemas. Optimize for cost. Implement alerting based on complex business metrics. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
