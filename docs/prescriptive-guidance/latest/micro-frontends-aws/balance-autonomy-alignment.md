---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/balance-autonomy-alignment.html
---

# Balancing autonomy with alignment

Micro-frontend architectures favor team autonomy. However, you should distinguish between areas that support flexibility and diverse approaches to problem solving, and areas where standardization is necessary to achieve alignment. Senior leaders and architects must identify these areas early and prioritize investments to balance the security, performance, operational excellence, and reliability of micro-frontends. To find this balance, focus on the following areas: creating, testing, and releasing micro-frontends; and logging, monitoring, and alerting.

## Creating micro-frontends
<a name="create"></a>

Ideally, all teams align on their approach to improve end-user performance. In practice, achieving this alignment can be difficult and can require additional effort. We recommend that you start with written guidelines that multiple teams contribute to through open and transparent discussion. Teams can then gradually adopt the Cookiecutter software pattern, which helps you create tools that provide a unified way to scaffold a project.

Using this approach, you can embed standard practices and constraints in your templates. However, these tools require significant investment to create and maintain. You must also address blockers quickly to avoid affecting developer productivity.

## End-to-end testing for micro-frontends
<a name="testing"></a>

Owners can handle unit testing. We recommend that you implement a strategy early to cross-test micro-frontends running on a unique shell. The strategy should include the capability to test applications before and after a production release. We also recommend that you develop processes and documentation so that technical and nontechnical people can manually test critical functionalities.

Ensure that changes don't degrade the functional or nonfunctional customer experience. An effective strategy is to gradually invest in automated testing for both key features and architectural characteristics, such as security and performance.

## Releasing micro-frontends
<a name="release"></a>

Each team might have its own way to deploy code, apply its own standards, and manage its own infrastructure. The complexity of maintaining such systems is often a deterrent. Instead, we recommend that you invest early in a shared strategy that shared tools enforce.

Develop templates with the CI/CD tools of your choice. Teams can then use the preapproved templates and shared infrastructure to release changes to production. You can begin investing in this development work early because these systems typically need few significant updates after an initial period of testing and consolidation.

## Logging and monitoring
<a name="logging"></a>

Each team can have different business and system metrics that they want to track for operational or analytics purposes. You can apply the Cookiecutter software pattern here as well. You can abstract the delivery of events into a library that multiple micro-frontends can consume. To balance flexibility and provide autonomy, develop tools for logging custom metrics and creating custom dashboards or reports. Reporting promotes close collaboration with product owners and shortens the end-customer feedback loop.

When you standardize the delivery, multiple teams can collaborate to track metrics. For example, an e-commerce website can track the user journey from the "Product details" micro-frontend to the "Cart" micro-frontend, and then to the "Purchase" micro-frontend to measure engagement, churn, and issues. If each micro-frontend logs events by using a single library, you can consume this data as a whole, explore it holistically, and identify trends.

## Alerting
<a name="alerting"></a>

Similar to logging and monitoring, alerting benefits from standardization with room for a degree of flexibility. Different teams might react differently to functional and non-functional alerts. However, if all teams have a consolidated way to initiate alerts based on metrics that they collect and analyze in a shared system, the business can identify cross-team issues. This capability is useful during incident-management events. For example, the following events can initiate alerts:
+ Elevated number of JavaScript client-side exceptions on a particular browser version
+ Time to render significantly degraded over a given threshold
+ Elevated number of 5xx status codes when consuming a particular API

Depending on the maturity of your system, you can balance your efforts on different parts of your infrastructure, as shown in the following table.

|
|
| Adoption | Research and development | Ascent | Maturity |
| --- |--- |--- |--- |
| Create micro-frontends. | Experiment, document, and share learnings. | Invest in tooling to scaffold new micro-frontends. Promote adoption. | Consolidate tooling for scaffolding. Promote adoption. |
| Test micro-frontends end to end. | Implement mechanisms for manually testing all related micro-frontends. | Invest in tooling for automated security and performance testing. Investigate feature flags and service discovery. | Consolidate tooling for service discovery, testing in production, and automated end-to-end testing. |
| Release micro-frontends. | Invest in a shared continuous integration and continuous delivery (CI/CD) infrastructure and automated multiple-environment releases. Promote adoption. | Consolidate tooling for CI/CD infrastructure. Implement manual rollback mechanisms. Promote adoption. | Create mechanisms to initiate automated rollbacks on top of system and business metrics and alerts. |
| Observe micro-frontend performance. | Invest in a shared monitoring infrastructure and library for consistent logging of system and business events. | Consolidate tooling for monitoring and alerting. Implement cross-team dashboards to monitor general health and improve incident management. | Standardize logging schemas. Optimize for cost. Implement alerting based on complex business metrics. |
