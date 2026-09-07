---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/understanding-gloe.html
---

# Understanding the GLOE framework for generative AI
<a name="understanding-gloe"></a>

Generative AI Lifecycle Operational Excellence (GLOE) is a structured, iterative framework that manages the complete lifecycle of generative AI applications, from ideation to deployment and monitoring. Its core objectives are to standardize processes, enable team collaboration, and promote operational excellence throughout the generative AI application lifecycle. It is designed to help organizations deliver reliable, ethical, and adaptable AI solutions.

The framework transforms unstructured development practices into a systematic methodology that is designed for the long-term evolution of generative AI applications. GLOE's value lies in building resilient, future-proof generative AI operations that can adapt to change and consistently deliver value in a rapidly evolving AI landscape. This section describes the GLOE framework, including the challenges it addresses, its guiding principles, how it benefits different technical audiences, and a description of its stages.

**This section contains the following topics:**
+ [Common generative AI challenges](#understanding-gloe-why)
+ [Guiding principles of the GLOE framework](#understanding-gloe-principles)
+ [Personas who benefit from GLOE](#understanding-gloe-personas)
+ [About the GLOE stages](#understanding-gloe-stages)

## Common generative AI challenges
<a name="understanding-gloe-why"></a>

The implementation of generative AI applications in enterprise environments presents a complex set of operational challenges that extend beyond conventional software development practices and traditional machine learning operations. The following common challenges collectively emphasize the necessity for the specialized GLOE framework:
+ **Managing non-deterministic outputs** – LLMs can demonstrate impressive capabilities in controlled demonstrations, but they often exhibit unpredictable behavior in real-world scenarios. This inherent non-determinism makes debugging and validating consistent quality particularly difficult.
+ **Dynamic evolution of prompts** – Prompts, which are central to generative AI application behavior, are not static elements. They are critical software artifacts that undergo continuous evolution. Their evolution demands rigorous lifecycle management, versioning, and proper decoupling from the application code itself.
+ **Bridging the prototype-to-production gap** – PoCs are often developed under ideal conditions with clean data and manual processes. This can cause developers to overlook the challenges of production applications, such as scalable infrastructure, continuous monitoring, enterprise-grade security, and real-world data variability.
+ **Lack of observability** – Without comprehensive tracing and observability mechanisms, it becomes difficult to determine why generative AI applications fail. This lack of deep insight hinders effective troubleshooting and continuous improvement.
+ **Missing evaluation frameworks** – Unlike PoCs, which may rely on subjective assessments, production systems necessitate automated, objective evaluation frameworks. These are crucial for continuously measuring quality, detecting performance regressions, and validating that the application consistently meets its objectives.
+ **Absent governance and guardrails** – PoCs typically do not incorporate the essential compliance controls, security guardrails, and data privacy measures that are non-negotiable for enterprise-level deployment. This oversight can lead to significant risks in production environments.
+ **No clear path to return on investment (ROI)** – Without a well-defined framework for measuring costs (such as token usage and infrastructure expenses) and demonstrating business impact, generative AI projects often struggle to prove their value and secure sustained funding and support.
+ **New threat landscape** – Generative AI applications introduce novel and sophisticated attack vectors, including prompt injection, jailbreaking, and data poisoning. These require specialized security strategies and proactive mitigation efforts beyond traditional cybersecurity measures.
+ **Rapidly evolving technical stacks** – The generative AI field is characterized by constant innovation, new tools, and rapid technical stack advancements. Traditional development frameworks often struggle to keep pace with these changes.

These challenges are deeply interconnected, making it ineffective to address them in isolation. The non-deterministic nature of LLMs requires robust evaluation and observability, and successful production deployment demands integrated governance, security, and scalability from the start. Organizations need a flexible framework that can quickly adapt to new developments and architectures, accommodate shorter development lifecycles, and integrate emerging capabilities while maintaining operational stability. GLOE addresses these interconnected challenges through a comprehensive, integrated framework that manages the entire lifecycle, offering a unique value proposition for organizations that are implementing generative AI solutions.

## Guiding principles of the GLOE framework
<a name="understanding-gloe-principles"></a>

GLOE is founded upon a set of core principles that are designed to promote the development and operation of robust, scalable, and responsible generative AI applications:
+ **Iterative and evidence-backed development** – GLOE promotes data-driven decision making through continuous experimentation and evaluation. Each development cycle builds upon validated learnings. This systematic approach makes sure that investments are backed by empirical evidence rather than assumptions.
+ **Continuous improvement and feedback loops** – GLOE operates on the fundamental principle that operationalizing a generative AI application is not a one-time event but an ongoing process of continuous improvement. This process is actively fueled by real-world usage and a robust feedback system. This includes the implementation of automated feedback loops, direct user feedback mechanisms, and strategic human-in-the-loop interventions.
+ **Holistic quality assurance** – To help address the inherent non-deterministic nature of generative AI outputs, GLOE mandates a multi-faceted evaluation strategy. This approach combines automated metric-based assessments, model-based evaluations (such as LLM-as-a-judge), and human evaluation to promote a comprehensive quality assessment.
+ **Security and governance by design** – In the GLOE framework, security, regulatory compliance, and responsible AI principles are deeply integrated throughout the entire application lifecycle, rather than being treated as afterthoughts. This encompasses multi-layered guardrails, proactive adversarial testing (red teaming), and robust, auditable trails.
+ **Modular and cloud-native architecture** – GLOE advocates for an architectural approach that involves decomposing complex generative AI applications into reusable microservices. This aligns with cloud-native principles, and it fosters enhanced scalability, resilience, and cost-effectiveness in deployed systems.
+ **Automation with human oversight** – GLOE promotes extensive automation through continuous integration and continuous delivery (CI/CD) pipelines for all generative AI artifacts. It also emphasizes the critical and irreplaceable role of human-in-the-loop interventions.

These guiding principles collectively reflect a mature engineering discipline applied to the field of generative AI. By systematically applying these principles, GLOE elevates generative AI development from ad-hoc scripting and experimental phases into a rigorous engineering practice. This disciplined approach enables more predictable outcomes and facilitates broader enterprise adoption.

## Personas who benefit from GLOE
<a name="understanding-gloe-personas"></a>

GLOE is designed to serve various roles and stakeholders who are actively involved across the generative AI application lifecycle. The framework provides tailored guidance and solutions for each persona to help foster a collaborative environment. The following are these personas:
+ **Generative AI application developers** – These individuals are responsible for building the core generative AI application logic, performing prompt engineering, and integrating with various LLMs. For this audience, GLOE provides structured workflows for effective prompt management, comprehensive evaluation, and streamlined deployment processes.
+ **Data scientists and AI engineers** – This group focuses on model selection, rigorous evaluation, and (if necessary) model fine-tuning. For this audience, GLOE offers robust mechanisms for experimentation tracking, comprehensive evaluation frameworks, and processes for validating data readiness.
+ **Platform engineers and DevOps engineers** – Tasked with constructing and maintaining the foundational infrastructure and deployment pipelines, these engineers benefit from GLOE's guidance on modular architectures, generative AI-specific CI/CD practices, deep observability, and scalable maintenance.
+ **Information security engineers (ISEs)** – Their primary concern is validating the security and compliance of generative AI systems. GLOE provides this persona with frameworks for implementing multi-layered guardrails, conducting adversarial testing (red teaming), and establishing auditability.
+ **Business leaders and product managers** – These stakeholders are focused on demonstrating tangible business value, effectively managing risks, and achieving a clear ROI. For this persona, GLOE offers structured proof of concept (PoC) validation processes, detailed cost modelling, and clear go/no-go decision criteria to support their strategic objectives.

The comprehensive coverage of these diverse personas within the GLOE framework inherently fosters cross-functional collaboration. The challenges identified previously (such as a lack of observability, absent governance, or an unclear ROI) frequently arise from communication breakdowns or misalignments between different functional teams. By explicitly addressing the unique needs and concerns of each persona within a unified framework, GLOE promotes a shared understanding and a more collaborative workflow. This collaborative environment is crucial for successfully moving generative AI projects from PoC to production.

## About the GLOE stages
<a name="understanding-gloe-stages"></a>

The GLOE framework provides a holistic and structured approach to managing the generative AI application development lifecycle. As shown in the following diagram, it operates as an iterative cycle that emphasizes continuous refinement based on data and feedback gathered from subsequent stages. This framework organizes the generative AI application lifecycle into three distinct yet interconnected stages: development (PoC and experimentation), preproduction (validation and staging), and production (deployment and continuous operations). Each stage is characterized by specific objectives, key activities, and operational considerations. All are designed to help you transition from an initial concept to a live, high-quality application., high-quality application. The following diagram shows the stages and key components of the GLOE framework.

![The stages in the GLOE framework: development, preproduction, and production.](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/images/guide-img/5b6a3e4a-ff13-48e9-83d7-177629049c97/images/8d81bb01-bb0c-4c29-a601-770340cce3e0.png)

### Development stage
<a name="development-stage.a891181e-f7da-5e22-bd72-8015ac686500"></a>

The development stage is also known as the *PoC and experimentation* stage. The purpose of this stage is to validate the core concept, establish foundational elements, and iteratively refine your prompts or model. The key activities in this stage include:
+ Manually or automatically optimizing prompts
+ Tracking and versioning experiments
+ Defining an evaluation dataset
+ Performing human labeling of a dataset
+ Evaluating through techniques such as LLM-as-a-judge
+ Creating CI/CD pipelines for development

### Preproduction
<a name="preproduction.ed00145a-1534-58da-9176-f9fc95114364"></a>

The preproduction stage is also known as the *validation and staging* stage. The purpose of this stage is to validate the application with internal or beta users, prepare for production deployment, and establish feedback systems. The key activities in this stage include:
+ Designing modular resources
+ Establishing a feedback system
+ Performing online validation
+ Performing unit, integration, and end-to-end testing
+ Establishing an AI gateway
+ Setting up tracing and logging systems
+ Defining a deployment strategy
+ Establishing guardrails and conducting adversarial testing

### Production
<a name="production.8900f238-c84f-5582-a4da-dfd7957d6258"></a>

The production stage is also known as the *deployment and continuous operations* stage. The purpose of this stage is to deliver value to the end users of the application. In this stage, you promote continuous performance, manage updates and changes, and maintain operational excellence. The key activities in this stage include:
+ Collecting feedback
+ Monitoring continuously
+ Performing shadow testing
+ Defining and following rollback strategies
+ Deploying iteratively
+ Managing governance and security risks
+ Tagging for cost allocation
+ Validating flexible scaling
+ Implementing CI/CD practices
