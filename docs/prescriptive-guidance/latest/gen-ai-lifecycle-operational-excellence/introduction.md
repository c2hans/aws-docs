---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/introduction.html
---

# Generative AI Lifecycle Operational Excellence framework on AWS
<a name="introduction"></a>

*Melanie Li, Alessandro Cerè, Derrick Choo, Deepak Dalakoti, Frank Huang, Dustin Liu, Faisal Masood, Nicholas Moore, Mahsa Paknezhad, James Schafer, Aaron Su, Eng-Hwa Tan, Tony Trinh, Romain Vivier, Vincent Wang, and Rafa XU, Amazon Web Services*

Generative AI is revolutionizing industries with unprecedented opportunities for innovation and efficiency. However, the transition from experimental proof-of-concepts (PoCs) to production-grade systems presents unique operational challenges that surpass traditional software development tactics. The Generative AI Lifecycle Operational Excellence (GLOE) framework is intended to address these challenges through best practices and a staged approach. It guides organizations through the entire lifecycle of generative AI application development and operations.

GLOE addresses the complexities of large language models (LLMs) by providing suggestions to help you manage non-deterministic outputs, dynamic prompt evolution, and continuous adaptation needs in real-world scenarios. The framework combines component-based architectures, risk-based governance, and specialized operational practices while emphasizing strategic value. This multifaceted approach helps organizations transform generative AI uncertainties into predictable business outcomes.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for engineers, developers, data scientists, project managers, and business leaders who are developing generative AI applications. For more detailed information, see [Personas who benefit from GLOE](understanding-gloe.md#understanding-gloe-personas) in this guide. To understand the concepts and recommendations in this guide, you should be familiar with the fundamentals of foundation models (FMs), including a basic understanding of LLMs. You should also be familiar with prompt engineering principles and have a basic understanding of AWS services, machine learning operations (MLOps) concepts, and DevOps concepts. This guide is intended for organizations that are starting generative AI PoCs or transitioning from experimental PoCs to production-grade generative AI systems.

## Objectives
<a name="objectives"></a>

The recommendations in this guide can help you achieve the following:
+ Convert prototypes into production-ready generative AI solutions that deliver measurable business value while reducing development time and costs.
+ Implement a structured approach to develop generative AI applications and manage their lifecycles.
+ Establish evaluation frameworks to handle non-deterministic AI outputs from generative AI applications.
+ Build trust through proper validation mechanisms, ethical use practices, and control systems that promote compliance and responsible AI deployment.
+ Monitor and maintain generative AI applications in production.
+ Transform AI prototypes into scalable, production-ready systems.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
