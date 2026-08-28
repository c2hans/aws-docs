---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-maturity-model/level-2.html
---

# Generative AI maturity model level 2: Experiment
<a name="level-2"></a>

Building upon the foundational awareness established in the previous level, the Experiment level marks a crucial transition from theoretical exploration to practical implementation of generative AI technologies. At this level, organizations move beyond conceptual understanding to engage in hands-on PoC projects and pilot programs. These PoC and pilot projects are designed to validate business value and build core competencies. This level is characterized by structured experimentation, where organizations form dedicated teams, establish governance frameworks, and begin developing internal technical expertise. Through carefully controlled pilot projects, organizations can test their hypotheses about generative AI's potential while minimizing risks and maximizing learning opportunities. This sets the stage for broader implementation and scaling of successful initiatives.

This section includes the following topics:
+ [Focus and criteria](#level-2-focus)
+ [Key activities](#level-2-activities)
+ [Transformation strategy to reach the next level](#level-2-transformation)

## Focus and criteria
<a name="level-2-focus"></a>

At this level, organizations transition from exploration to hands-on PoC experimentation and pilot projects with generative AI technologies. The focus is on validating business value through structured pilot programs and building core competencies. This level emphasizes practical learning, building internal capabilities and technical expertise, and establishing foundational and governance frameworks.

The following are the criteria for being at this level:
+ The organization has active pilot projects and proofs of concept in progress.
+ Dedicated, cross-functional teams are assigned to generative AI initiatives.
+ A structured internal training program is established.
+ The organizations has selected and validated AI models and tools.
+ The organization has defined its initial governance and data frameworks.

## Key activities
<a name="level-2-activities"></a>

The following table shows the key activities for each pillar of adoption.

|
|
| **Pillar of adoption** | **Activities** |
| --- |--- |
| Business | + Define and prioritize strategic use cases based on business value and feasibility.+ For PoCs, establish success metrics and frameworks for measuring the return on investment (ROI).+ Create value assessment scorecards for each PoC.+ Limit the scope of PoCs to a manageable scale with clear success metrics.+ For each PoC, measure the ROI and evaluate whether it achieved the success criteria. |
| People | + Implement structured training programs in prompt engineering, RAG, and model fine-tuning.+ Create generative AI certification paths and career progression frameworks.+ Hire generative AI and data science experts.+ Partner with external specialists, such as the AWS Generative AI Innovation Center or AWSProfessional Services, to co-build a PoC, provide support, and transfer knowledge.+ Establish AI certification paths and career-progression frameworks. |
| Governance | + Develop preliminary frameworks that encompass data governance for generative AI, such as the quality of content used for vector search.+ Establish model evaluation criteria and quality controls.+ Set up risk assessment protocols for generative AI projects.+ Set up guidelines for the ethical and responsible use of generative AI. Train developers, data scientists, and generative AI specialists to comply with these guidelines. |
| Platform | + Set up the foundation infrastructure for the PoC, such as an AWS [landing zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/understanding-landing-zones.html) and the [permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) that developers need.+ Set up an environment for generative AI experimentation and PoC development, such as an Amazon Bedrock [playground](https://docs.aws.amazon.com/bedrock/latest/userguide/playgrounds.html) or an Amazon SageMaker AI [JupyterLab space](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl.html) or [notebook instance](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html).+ Implement a RAG approach or an agentic workflow that developers can easily use. For a RAG approach, consider [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), and for an agentic workflow, consider [Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html).+ Set up frameworks or pipelines that manage prompts, models, and prompt evaluations. These resources should help developers quickly evaluate the results and performance of the PoC application.+ Implement early-stage data-integration efforts, including structured and unstructured data pipelines. Set up vector databases for RAG experiments.+ Evaluate foundation models based on cost, performance, and use case suitability. You can use Amazon Bedrock, Amazon SageMaker AI, and [Amazon SageMaker AI JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html). |
| Security | + Implement data access controls for training generative AI models, and make sure that they adhere to compliance requirements. [Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html) can simplify the implementation of RAG by enabling fine-grained controls that allow generative AI workloads to retrieve only the data that the user is authorized to access.+ Develop a strategy for protecting personally identifiable information (PII) in datasets that are used to train models. |
| Operations | + Create documentation and support processes for the following:PoC implementations and learningsBasic platform configurations and security controlsTesting and evaluation proceduresHand-over processes for successful PoCs that are moving to production |

## Transformation strategy
<a name="level-2-transformation"></a>

Organizations can transition to next maturity level by doing the following:
+ **Create production-grade** **infrastructure** **to support generative AI** – Use AWS services to implement CI/CD pipelines, standardized deployment patterns, and proper scaling mechanisms for production deployments.
+ **Implement governance** – Establish production-grade governance frameworks to manage ongoing generative AI usage and model updates.
+ **Implement observability** – Implement observability, monitoring, and logging practices that are specifically adapted for generative AI workloads. This includes model performance metrics, usage patterns, and response quality assessment.
+ **Focus on compliance** – Make sure that you comply with industry standards and regulations for data privacy and security.
+ **Build dedicated AI teams** – Set up a team that creates and maintains standardized paths to production for generative AI solutions.
+ **Implement operational excellence** – Create an incident response and escalation process. Establish service-level agreements (SLAs) and performance metrics. Implement cost optimization strategies.

By taking these actions, organizations can:
+ Validate that generative AI applications are stable, reliable, and continuously deliver value to the organization.
+ Support the growth of generative AI solutions as demand and usage increase across various departments.
+ Manage risks, maintain oversight, and align AI initiatives with regulatory standards as they become an integral part of business operations.
+ Provide continuous monitoring, improvement, and support for generative AI solutions. This reduces the reliance on ad-hoc or temporary project teams.
+ Prepare the organization to move from isolated projects to a strategic and cohesive approach, where AI becomes a core enabler of business processes. The organization is ready for further scale and broader adoption.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
