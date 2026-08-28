---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-considerations-gen-ai/journey.html
---

# Data strategy
<a name="journey"></a>

A well-defined data strategy is essential for the successful adoption of generative AI. This section examines how data strategy plays a critical role at each stage of the generative AI adoption journey. It also outlines key considerations across various dimensions of implementation. For more information about the stages of the generative AI journey, see [Maturity model for adopting generative AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-maturity-model/introduction.html) on AWS Prescriptive Guidance.

The generative AI adoption journey is a structured progression through four key stages:
+ **Envision** – Organizations explore generative AI concepts, build awareness, and identify potential use cases.
+ **Experiment** – Organizations validate generative AI's potential through structured pilot projects and proofs of concepts, while building core technical capabilities and foundational frameworks for implementation.
+ **Launch **– Organizations systematically deploy production-ready generative AI solutions with robust governance, monitoring, and support mechanisms to deliver consistent value and operational excellence while maintaining security and compliance standards.
+ **Scale **– Organizations establish enterprise-wide generative AI capabilities through reusable components, standardized patterns, and self-service platforms to accelerate adoption while maintaining automated governance and fostering innovation.

Across all stages, AWS emphasizes a holistic approach, aligning strategy with infrastructure investments, governance policies, security frameworks, and operational best practices to promote responsible and scalable AI deployment. Each stage requires alignment across six foundational [pillars of adoption](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-maturity-model/overview-aspects.html#overview-aspects-pillars): Business, People, Governance, Platform, Security, and Operations. These pillars align with and extend the [AWS Cloud Adoption Framework (AWS CAF)](https://aws.amazon.com/cloud-adoption-framework/) to address generative AI needs.

**This section discusses the following maturity model stages in more detail:**
+ [Level 1: Envision](#journey-envision)
+ [Level 2: Experiment](#journey-experiment)
+ [Level 3: Launch](#journey-launch)
+ [Level 4: Scale](#journey-scale)

## Level 1: Envision
<a name="journey-envision"></a>

In the Envision stage, organizations focus on planning by identifying suitable use cases, mapping the necessary data sources for implementation, and establishing the foundational security and data access requirements for the upcoming experimentation phase.

At this stage, the following are the alignment criteria for the pillars of adoption:
+ **Business** – Identify strategic use cases for generative AI that align with enterprise goals. Assess where high-value data resides and its accessibility.
+ **People** – Foster a data-driven culture by educating leadership and stakeholders on the importance of data in generative AI adoption.
+ **Governance** – Conduct an initial data audit to evaluate compliance, privacy concerns, and potential ethical risks. Develop early policies on AI transparency and accountability.
+ **Platform** – Assess existing data infrastructure, catalog internal and external data sources, and evaluate data quality for generative AI feasibility.
+ **Security** – Begin implementing access controls and least-privilege principles for data access. Make sure that generative AI models can only retrieve information that the user is authorized to access.
+ **Operations** – Define a structured approach to collecting, cleaning, and labeling data for generative AI experiments. Establish initial feedback loops for data monitoring.

## Level 2: Experiment
<a name="journey-experiment"></a>

During the Experiment phase, organizations validate the availability and suitability of the required data to support the implementation of identified use cases. In parallel, establish a minimum viable data governance framework to support the use of real data in proofs of concept. You can fine-tune a selected foundation model or use an off-the-shelf model in combination with a Retrieval Augmented Generation (RAG) approach.

At this stage, the following are the alignment criteria for the pillars of adoption:
+ **Business** – Define clear success criteria for pilot projects, and make sure that data availability meets the needs of each use case.
+ **People** – Form a cross-functional team that includes data engineers, AI specialists, and domain experts. This team is responsible for validating data quality and model alignment with business requirements.
+ **Governance** – Draft a framework for generative AI data governance. At a minimum, the framework should discuss regulatory compliance and responsible AI guidelines.
+ **Platform** – Implement early-stage data integration efforts, including structured and unstructured data pipelines. Set up vector databases for RAG experiments.
+ **Security** – Enforce strict data permissions and compliance checks. Make sure that PII or other sensitive information is masked or anonymized before model training.
+ **Operations** – To prepare for production release, establish quality metrics to identify gaps.

## Level 3: Launch
<a name="journey-launch"></a>

In the Launch stage, generative AI solutions move from experimentation to full-scale deployment. At this point, integrations are fully implemented, and robust monitoring frameworks are established to track performance, model behavior, and data quality. Comprehensive security and compliance measures are enforced to support data privacy, safety, and regulatory adherence.

At this stage, the following are the alignment criteria for the pillars of adoption:
+ **Business** – Measure operational efficiency and business value. Optimize operational costs and resource use.
+ **People** – Train operational teams on generative AI model management and monitoring. Use proper data curation processes.
+ **Governance** – Refine the framework for generative AI data governance. Address regulatory compliance, model biases, and responsible AI guidelines. Establish continuous auditing of generative AI data pipelines in order to validate compliance with evolving regulations.
+ **Platform** – Optimize scalable infrastructure to support real-time data ingestion, vector search, and fine-tuning where necessary.
+ **Security** – Deploy encryption, role-based access control (RBAC), and least-privilege access models. You can use Amazon Q Business to control data access and make sure that the generative AI solution retrieves only data that the user is authorized to access.
+ **Operations** – Establish data observability practices. Track data lineage, provenance, and quality metrics to identify gaps before scaling.

## Level 4: Scale
<a name="journey-scale"></a>

In the Scale stage, the focus shifts to automation, standardization, and enterprise-wide adoption. Organizations establish reusable data pipelines, implement scalable governance frameworks, and enforce robust policies to support data accessibility, security, and compliance. This phase democratizes** **data products. This helps teams across the organization to seamlessly develop and deploy new generative AI solutions while maintaining consistency, quality, and control.

At this stage, the following are the alignment criteria for the pillars of adoption:
+ **Business** – Align generative AI projects with long-term business goals. Focus on revenue growth, cost reduction, and customer satisfaction.
+ **People** – Develop enterprise-wide AI literacy programs and embed AI adoption within business functions through AI Centers of Excellence (CoEs).
+ **Governance** – Standardize AI governance policies across departments to promote consistency in AI decision-making.
+ **Platform** – Invest in scalable AI data platforms that use cloud-native solutions for federated data access and processing.
+ **Security** – Implement automated compliance monitoring, robust data loss prevention (DLP), and continuous threat assessments.
+ **Operations** – Establish an AI observability framework. Integrate feedback loops, anomaly detection, and model performance analytics at scale.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
