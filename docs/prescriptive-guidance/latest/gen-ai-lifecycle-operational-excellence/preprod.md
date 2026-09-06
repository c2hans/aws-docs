---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/preprod.html
---

# GLOE stage 2: Preproduction, validation, and staging for generative AI applications
<a name="preprod"></a>

The preproduction stage is a pivotal phase in the GenAIOps lifecycle. It bridges the gap between a controlled experiment and a full-scale production deployment. This stage moves beyond the lab and into a controlled, near-production environment with a select group of internal or beta users. This allows teams to gather crucial feedback, harden the system, and build a final, data-driven business case for a full release.

The preproduction stage is defined by a fundamental shift in objective, from proving technical feasibility to validating business viability. While a PoC validates that the technology works, preproduction must answer far more critical business questions, such as "Is this solution valuable, reliable, secure, and scalable enough for enterprise use?"  This requires moving beyond a simple technology experiment to a project with clear *production intent*, which is a commitment to building a solution that the business genuinely plans to deploy to solve a worthwhile problem.  Success is now measured by the systematic mitigation of business, operational, and security risks.

This transition is where most generative AI projects stall, falling into the massive gap between a prototype and a production-ready system. PoCs create a dangerous illusion of completeness because they are often built under ideal conditions with clean data and manual processes. They ignore the work required for a real-world application.  This includes building scalable infrastructure, establishing feedback loops for continuous improvement, integrating seamlessly with the user experience, implementing continuous monitoring, and fortifying the application with enterprise-grade security. For more information, see [Is Your AI Project Ready for Production? A Practical Guide from PoC to Real-World Impact](https://medium.com/data-science-collective/how-to-make-ai-work-from-poc-to-production-a-practical-guide-for-modern-decision-makers-275b6c3f3a64) (Medium blog post).

Key failure points that emerge during this transition include but are not limited to the following:
+ **Lack of observability** – The non-deterministic nature of LLMs means that they can excel in a demo and then break completely in real-world use. Without detailed tracing and observability, it is impossible to debug why it failed, not just what failed.
+ **Missing evaluation frameworks** – PoCs are often judged subjectively. Production systems require automated, objective evaluation frameworks to continuously measure quality and detect regressions.
+ **Absent governance and guardrails** – PoCs rarely include the necessary compliance controls, security guardrails, and data privacy measures that are non-negotiable for enterprise deployment.
+ **No clear path to ROI** – Without a clear framework for measuring costs, such as token usage and infrastructure, and business impact, the project cannot demonstrate its value. This can lead to a withdrawal of funding and support.

Beyond these key failure points, there are additional ones, such as difficulty of use or challenges securing a high level of SME supervision or validation. The solution is to assemble a cross-functional production team from the early stage of the lifecycle. Involving stakeholders from IT, security, data science, and platform engineering during the PoC validation and at the start of preproduction is critical to prevent late-stage tech stack misalignment. It also helps you validate that the application is enterprise-ready. This early and continuous collaboration confirms alignment on critical technology choices, such as the foundational LLMs, vector databases, cloud platforms, and orchestration frameworks, before you invest significant development effort.

This chapter is organized into the following main sections to help you overcome the challenges of the preproduction stage:
+ [Architecting generative AI applications for production](preprod-architecting.md) – This section focuses on architecting generative AI applications for production. It includes information about decomposing monoliths into microservices, designing data and prompt flows, implementing AI gateways, and optimizing for performance and cost.
+ [Hardening the generative AI application through a GenAIOps framework](preprod-hardening.md) – This section describes how to harden generative AI applications through testing, security, and continuous improvement. It helps you implement CI/CD pipelines, observability, and feedback loops to prepare for production.

When you have finished architecting and hardening your application, use the recommendations in the [Advancing your generative AI application to production](preprod-advancing.md) section to determine whether to progress to the next stage.
