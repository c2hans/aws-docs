---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/preprod-hardening.html
---

# Hardening the generative AI application through a GenAIOps framework
<a name="preprod-hardening"></a>

The evolution of generative AI applications from PoC to production-ready systems requires a comprehensive hardening process that promotes reliability, security, and continuous improvement. Through the implementation of a GenAIOps framework, organizations can transform experimental prototypes into robust, enterprise-grade applications that meet stringent quality and compliance standards.

This transformation encompasses multiple key areas: formalizing the AI stack with rigorous versioning, implementing automated CI/CD pipelines, establishing deep observability, and creating multi-layered testing frameworks. These components work together to create a secure, governable system that can adapt and improve through carefully designed feedback loops.

**This section contains the following topics:**
+ [Formalizing the generative AI stack](#preprod-hardening-formalizing-stack)
+ [Automating deployment through CI/CD pipelines](#preprod-hardening-cicd-pipelines)
+ [Achieving deep observability](#preprod-hardening-observability)
+ [Establishing a multi-layered testing and evaluation framework](#preprod-hardening-testing-evaluation)
+ [Security controls for the preproduction stage](#preprod-security)
+ [Driving continuous improvement through data and feedback loops](#preprod-hardening-continuous-improvement)

## Formalizing the generative AI stack
<a name="preprod-hardening-formalizing-stack"></a>

The approach to versioning generative AI assets undergoes a transformation between the PoC and preproduction stages. In the PoC, versioning supports rapid, wide-ranging experimentation to discover what works. In preproduction, the focus shifts from discovery to stability. Versioning becomes a formal, rigorous process for managing a now well-defined application stack. In this stage, you treat all generative AI artifacts with the same discipline as production code to promote reproducibility and auditability and to prevent quality regressions. For more information about versioning generative AI applications, see [Version tracking for GenAI applications](https://mlflow.org/docs/3.1.3/genai/prompt-version-mgmt/version-tracking/) (MLflow).

The following are components that should be treated as versioned artifacts:
+ **Prompts and model configurations** – During the PoC stage, the prompt registry acted as a sandbox for testing dozens of prompt variations and model parameters. In preproduction, the most successful prompt candidates and their associated model configurations are promoted and locked in as stable, versioned artifacts. They are no longer experimental strings, and you should treat them as configuration as code, which focuses on application settings and parameters (unlike infrastructure as code, which manages computing resources). At this stage, changes should be small, targeted tweaks that are intended to fix a specific edge case or improve a performance metric. These changes must go through a formal review process, such as a pull request, and they must pass the full suite of automated evaluations in the CI/CD pipeline before being approved and promoted to production.
+ **Application code** – The application logic, which evolved from a simple script in the PoC to a collection of microservices, is managed in a version control system, such as Git. Every deployment, evaluation run, and logged trace must be linked back to a specific Git commit hash. This provides an immutable record of the application logic, and this is the standard practice to which all other generative AI artifacts must now adhere.
+ **Evaluation dataset** – This dataset is expanded with real-world examples, user-reported failures, and adversarial test cases that were discovered during early testing. It becomes the official benchmark against which all changes to the application stack are measured. Any modification to this dataset should be a versioned change. This makes sure that performance comparisons between different application versions are always fair and consistent.

This holistic approach to versioning means that a single application version is no longer just a Git commit. It is a complete, immutable snapshot of the entire stack: the specific code version, the prompt version, the model configuration, and the evaluation dataset version it was validated against. The application at this stage might also be open to internal user testing, which makes the online evaluation an important component in the lifecycle. For more information, see [Establishing a multi-layered testing and evaluation framework](#preprod-hardening-testing-evaluation) in this guide.

## Automating deployment through CI/CD pipelines
<a name="preprod-hardening-cicd-pipelines"></a>

The manual deployment processes of the PoC stage must be replaced by a fully automated continuous integration and continuous deployment (CI/CD) pipeline. This pipeline is the engine that enforces quality, security, and consistency for every change so that only validated and hardened code reaches production environments.

A mature CI/CD pipeline for a generative AI application includes the following automated stages:

1. **Trigger** – The pipeline is automatically initiated by a new commit to the main code branch or by the promotion of a new prompt version in the prompt registry.

1. **Build** – The pipeline builds and packages the application's microservices into container images.

1. **Unit test** – The pipeline runs traditional unit tests against the deterministic components of the application, such as its data processing tools and API integration logic, to catch functional bugs early.

1. **Evaluation** – This is a critical, generative AI-specific stage. The pipeline automatically runs the new application version against the versioned evaluation dataset. It can use the same LLM-as-a-judge evaluation metrics that were developed during PoC stage in order to score the outputs. The pipeline is configured to fail the build if the evaluation scores drop below a predefined threshold. In this way, the pipeline automatically detects and prevents quality regressions.

1. **Security scan** – The pipeline runs automated adversarial tests (*red teaming*) against the application to check for common vulnerabilities, such as prompt injection attacks, personally identifiable information (PII) exposure, or system prompt extraction. For more information, see [OWASP red teaming: A practical guide to getting started](https://www.promptfoo.dev/blog/owasp-red-teaming/) (Promptfoo).

1. **Deployment** – If all the preceding checks pass, the new version of the application is automatically deployed to a staging environment. This environment is a stable replica of production, used for final user acceptance testing, canary releases, or A/B testing.

## Achieving deep observability
<a name="preprod-hardening-observability"></a>

*Observability* is the practice of instrumenting a system to provide rich, detailed data about its internal state, allowing engineers to understand not just that a problem occurred, but why it occurred. The goals of observability evolve between the PoC and preproduction stages. The primary goal during PoC stage is debugging and validation. At the preproduction stage, the goal shifts to holistic system health and performance monitoring.

A robust observability strategy for generative AI requires the following three pillars of telemetry data, all collected and correlated in a centralized platform:
+ **Unified metrics, logs, and traces** – In addition to collecting standard application logs and infrastructure metrics, you must also collect generative AI-specific data. This includes the full prompt and response payloads, token counts for cost tracking, tool call parameters and outputs, and user feedback signals.
+ **End-to-end tracing** – For a compound AI system, a single user request can trigger a complex chain of events that  involves multiple LLM calls, tool executions, and database queries. It's essential that you use end-to-end tracing tools, such as [MLflow Tracing](https://mlflow.org/docs/3.3.0/genai/tracing/), [Langfuse](https://langfuse.com/docs), or platforms that use [OpenTelemetry](https://opentelemetry.io/). They capture the entire execution flow of a request, visualizing it as a *trace* that shows the inputs, outputs, and latency of each step. This is the single most powerful tool for debugging why an agent took an unexpected path or failed mid-execution.
+ **Performance, cost, and quality monitoring** – The observability platform should provide real-time dashboards to monitor key business and operational metrics. These dashboards track not only technical performance (such as latency and error rates) but also business-critical KPIs, such as the cost per request, token usage per user, and trends in quality evaluation scores and user feedback over time. This helps teams to proactively detect performance drift or escalating costs.

## Establishing a multi-layered testing and evaluation framework
<a name="preprod-hardening-testing-evaluation"></a>

The preproduction stage is where the application's quality and robustness are put to the test. Given the non-deterministic nature of generative AI, a traditional testing strategy is insufficient. A multi-layered approach is required, one that combines foundational software testing with novel techniques that are designed specifically to validate the behavior of LLM-based systems. This rigorous testing is essential for building the confidence needed to deploy the application to real users.

The following table shows the core layers and components of a testing and evaluation framework. It describes *foundational *tests, which are traditional software testing practices that have been adapted for generative AI. It also describes *quality assessment* tests, which are specific to generative AI applications. These quality assessments form a specialized evaluation framework that can assess the quality of non-deterministic outputs. This hybrid approach combines automated offline analysis, live online testing, and continuous human feedback in the preproduction stage.

|
|
| **Layer** | **Test** | **Recommended practices** |
| --- |--- |--- |
| Foundational | Unit testing | + Use mock and stub dependencies+ Aim for high coverage on the logic+ Test for edge cases+ Integrate with the CI/CD pipeline |
| Foundational | Integration testing | + Validate integration with the platform+ Validate the data flow+ Validate integration with external APIs |
| Foundational | End-to-end testing | + Focus on the workflow+ Use realistic data+ Automate the full flow from user interaction with the frontend to the entire backend system+ Test variable response times from external APIs+ Test asynchronicity from external APIs |
| Quality assessment | Offline evaluation | + Often uses LLM-as-a-judge approach+ Integrate with the CI/CD pipeline |
| Quality assessment | Online evaluation | + Use A/B testing+ Use canary releases |
| Quality assessment | Human-in-the-loop evaluation | + Collect explicit feedback+ Collect implicit feedback+ Close the loop |

### Unit testing
<a name="unit-testing.4dbcce31-e606-50d3-a400-b8f0b7b32c5c"></a>

*Unit testing*, in a generative AI context, concentrates on the individual, deterministic tools or components within the larger system. Each function, such as a data-retrieval script, an API client, or a data-transformation function, must have its own suite of unit tests to validate its logic in isolation. For more information, see [What is unit testing?](https://aws.amazon.com/what-is/unit-testing/)

A primary challenge of unit testing is handling dependencies on external services, such as LLM APIs. Unit tests must remain fast and isolated, which means they cannot make live network calls.

The following are recommended practices for unit testing:
+ **Mock and stub dependencies** – Use mocks and stubs to simulate the behavior of external services. For an LLM call, a mock can be configured to return a predefined, expected response. This helps you test how your code handles that specific output without calling the model.
+ **High coverage on business logic** – Aim for high test coverage on the critical, deterministic code paths that prepare data for the LLM or process its output.
+ **Edge case testing** – Actively test for extreme or invalid inputs (known as *edge cases*) to make sure that the component is resilient.
+ **CI/CD integration** – Unit tests must be integrated into the CI/CD pipeline and run automatically for every code change in order to provide rapid feedback.

### Integration testing
<a name="integration-testing.553ecc05-ccce-53b1-9aee-611f52b66d3e"></a>

*Integration testing* is the layer that verifies the interactions between the modular components of the generative AI application and its underlying platform. While unit tests confirm that each component works on its own, integration tests make sure that they fit together correctly within a realistic environment.

A principle of preproduction integration testing is to consider the deployment platform itself. Testing on a local machine is insufficient because it cannot replicate the complexities of a cloud-native environment, such as network policies, IAM roles, and service-specific configurations. The best practice is to establish a dedicated preproduction or staging environment that mirrors the production technology stack as closely as possible. Use containerization and orchestration tools, such as [Docker](https://www.docker.com/), to promote consistency.

The following are common enterprise integration scenarios that you should test:
+ **Data pipeline integrity** – For RAG systems, this is a top priority. Tests must validate the entire data flow, from the ingestion service that pulls data from a source system, through the processing and embedding service, and into the vector store. This catches issues that unit tests would miss, such as data format mismatches or errors in the ETL process.
+ **Agentic tool use and external APIs** – Tests must verify that an agent can correctly authenticate with and call external tools or enterprise APIs, parse their responses, and handle potential errors gracefully. For example, you might test integration with a customer relationship management (CRM) system or a booking system.
+ **Authentication and authorization flows** – Verify that the application correctly integrates with enterprise identity providers and that role-based access controls are properly enforced across service-to-service communication.

The following are recommended practices for integration testing:
+ **Isolate with service virtualization** – When a full production-mirror environment is too complex or expensive for every test run, use service virtualization to create mocks that simulate the behavior of dependent services. This allows you to test specific integration scenarios in isolation, such as how your application handles an error response from an external API.
+ **Adopt contract testing** – To avoid the brittleness of traditional integration tests, contract testing is a powerful shift-left strategy. Instead of testing live services together, this technique validates that each service adheres to a shared, version-controlled contract that defines the API's expected requests and responses. This allows teams to develop and deploy their services independently with high confidence that they will not break integrations. Contact-testing tools, such as [Pact](https://pactflow.io/difference-between-consumer-driven-contract-testing-and-bi-directional-contract-testing/), are the industry standard for implementing this consumer-driven approach.
+ **Automate in CI/CD pipelines** – All integration tests, especially fast-running contract tests, should be fully automated and integrated into the CI/CD pipeline. This helps you detect any integration failures with every code change.

### End-to-end testing
<a name="end-to-end-testing.0f68bc64-6df6-55a3-a817-a399f6f5966c"></a>

*End-to-end testing* validates the entire application workflow from the user's perspective. It makes sure that all the modular microservices work together correctly. This is crucial for catching integration issues that unit tests miss.

One of the key challenges for end-to-end testing is the non-deterministic nature of LLM responses. These make traditional end-to-end testing unreliable because traditional testing relies on exact-match assertions. Additionally, factors such as response latency and the complexity of multi-turn conversational flows add to the difficulty.

The following are recommended practices for end-to-end testing:
+ **Focus on workflow, not exact output** – Instead of asserting that the LLM produces a specific sentence, end-to-end tests should verify that the workflow completes successfully, that the response is structurally correct (such as valid JSON), and that its content is semantically relevant to the original query.
+ **Use realistic data** – End-to-end tests should mimic real-world user scenarios by using concrete and realistic test data, including edge cases and potential error conditions.
+ **Automate the full flow** – Use UI automation frameworks to simulate user interactions from the frontend through the entire backend stack.
+ **Handle asynchronicity and latency** – Tests must be designed to handle variable response times from LLM APIs. Include appropriate waits and timeouts to prevent flakiness.

### Offline evaluation
<a name="offline-evaluation.70ce0724-cb4e-5e7d-9ccc-0902d9a80c57"></a>

The offline evaluation process that began in the PoC stage is now formalized and scaled in preproduction. *Offline evaluation* is a method that allows you to assess the performance of an AI system by using historical data. The small high-quality dataset of prompts and ideal responses is expanded into a comprehensive, version-controlled evaluation dataset that includes common use cases, known edge cases, and adversarial inputs. This suite becomes the benchmark for automated quality assessment.

The most scalable approach for automated evaluation is using a powerful LLM as the judge. The judge is given the original prompt, the application's response, and a scoring rubric. It then returns a structured score and a rationale. If the same LLM judge has been used during PoC stage, the same LLM judgement instructions and prompts can be reused in the preproduction stage to provide the same level of evaluation metrics as the PoC stage. For more information, see [Evaluation strategies and metrics](dev-experimenting-quality.md#dev-experimenting-quality-metrics) in the PoC chapter of this guide.

Integrate offline evaluations into your CI/CD pipeline. These automated evaluations are a critical quality gate in the CI/CD pipeline. The pipeline is configured to fail the build if quality scores drop below a predefined threshold, which automatically prevents regressions. Available frameworks, such as [pytest-evals](https://github.com/AlmogBaku/pytest-evals) and the [LangSmith pytest](https://blog.langchain.com/pytest-and-vitest-for-langsmith-evals/) integration, are designed to bring this AI-centric evaluation into standard software engineering workflows.

### Online evaluation
<a name="online-evaluation.fb6bcd46-fe89-5a97-a697-40f6df76414a"></a>

*Online evaluations* are validations with real users. No matter how thorough offline evaluations are, the ultimate validation comes from real user interactions. Controlled rollouts are essential techniques for de-risking the final step into production by testing on live traffic.

The following are recommended techniques for offline evaluations, and you can use these techniques in both preproduction and production environments:
+ **A/B testing** – This technique is used to compare two or more versions of a specific component, typically a prompt or model configuration, on key business metrics. For example, a small percentage of users might receive responses generated by a new prompt while the rest use the stable version of the prompt. By analyzing metrics like user feedback scores, latency, and cost for each group, teams can make a data-driven decision about which version performs better. For more information, see [A/B testing of LLM prompts](https://langfuse.com/docs/prompt-management/features/a-b-testing) in the Langfuse documentation.
+ **Canary releases** – This is a broader strategy for deploying an entirely new version of the application. Initially, only a small fraction of traffic, such as 5%, is routed to the new version. The team closely monitors key metrics in real-time. If the performance remains stable, traffic is gradually increased. If issues arise, traffic is immediately rolled back to minimize the user impact. This makes canary testing an essential safety net for deploying unpredictable LLM updates. For more information, see [Canary testing for LLM apps](https://portkey.ai/blog/canary-testing-for-llm-apps/) (Portkey).

### Human-in-the-loop evaluation
<a name="human-in-the-loop-evaluation.8dc27cbd-c360-5357-a66a-cdf9c00279c3"></a>

The evaluation lifecycle is a continuous loop, not a one-time check. The feedback collected from real users during online testing is the fuel for this loop. Collecting feedback is a critical part of *human-in-the-loop* reviews. The application must be designed with mechanisms to collect both explicit feedback and implicit feedback. Examples of *implicit feedback* are thumbs up and thumbs down ratings and user comments. Examples of *explicit feedback* are user actions to copy the response or pose a rephrased query.

This feedback is not just for dashboards. The most valuable interactions, especially user-reported failures, should be triaged and converted into new test cases. These are then added to the version-controlled evaluation dataset, which continuously hardens the automated test suite against known, real-world failures. This creates a virtuous cycle where production usage directly improves the quality and robustness of future versions. For more information, see [Driving continuous improvement through data and feedback loops](#preprod-hardening-continuous-improvement) in this guide.

## Security controls for the preproduction stage
<a name="preprod-security"></a>

The preproduction stage represents a critical transition where security and governance must evolve from theoretical concepts to fully implemented, tested, and automated realities. This phase focuses on hardening applications through comprehensive testing and implementing production-ready security controls that bridge the gap between experimental PoC and enterprise deployment. With the intended system design now established, you can complete comprehensive [threat modelling](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_securely_operate_threat_model.html) to identify additional attack vectors and security requirements that might not have been apparent during the initial PoC stage.

Enhance guardrails beyond the basic protections that you established in development. Expand from simple prompt injection filters to include comprehensive content filtering, output validation, and context-aware guardrails that address identified threat modelling and business needs. For more information, see [Amazon Bedrock Guardrails enhances generative AI application safety with new capabilities](https://aws.amazon.com/blogs/aws/amazon-bedrock-guardrails-enhances-generative-ai-application-safety-with-new-capabilities/) (AWS blog post). Adopt immutable infrastructure patterns, where system components are replaced rather than modified in place. This reduces the risk of unauthorized changes and promotes consistent, reproducible deployments.

The preproduction stage introduces advanced security patterns that might have been too restrictive for PoC development, such as [Zero Trust principles](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-zero-trust-architecture/zero-trust-principles.html). Align organizational security and compliance standards during preproduction to reduce potential redevelopment work. For more information, see [Compliance validation for AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-compliance.html). It is also recommended that you evaluate against the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

In the preproduction stage, security and governance must transition from theoretical concerns to fully implemented, tested, and automated realities. For any enterprise, the deployment of a generative AI application is contingent on demonstrating that it is secure, compliant, and trustworthy. This requires a defense-in-depth approach that includes multi-layered guardrails, offensive security testing, and robust governance frameworks.

### Implementing multi-layered guardrails
<a name="implementing-multi-layered-guardrails.3ed744d0-c59b-5908-b8cd-8a536e4ef7bd"></a>

In the context of generative AI, *guardrails* are a system of programmatic controls that are designed to enforce policies on the inputs and outputs. They are essential for protecting data privacy, maintaining regulatory compliance, preventing misuse, and aligning the model's behaviour with the specific business context. Effective guardrails are not a single feature but an interlocking system of controls that operate at different points in the application's data flow. For example, you can use [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html) to detect and filter harmful content.

The following are the types of recommended guardrails:
+ **Input guardrails** – These controls scan and analyze user prompts before they are sent to the LLM. Their purpose is to detect and block malicious or inappropriate inputs. Key functions include the following:
  + **Detection of prompt injection attacks** – *Prompt injection attacks* involve manipulating prompts to influence LLM outputs, with the intent to introduce biases or harmful outcomes. For more information, see [Prompt engineering best practices to avoid prompt injection attacks on modern LLMs](https://docs.aws.amazon.com/prescriptive-guidance/latest/llm-prompt-engineering-best-practices/introduction.html) (AWS Prescriptive Guidance) and [Detect prompt attacks with Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prompt-attack.html) (Amazon Bedrock documentation).
  + **PII detection** – Scan for PII data (such as names, phone numbers and social security numbers) to prevent sensitive data from being processed by the LLM. For more information, see [Remove PII from conversations by using sensitive information filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html) in the Amazon Bedrock documentation.
  + **Denied topic filtering** – Block queries that fall into predefined restricted topics. For example, a customer service bot for a bank should be configured to refuse to give investment advice. For more information, see [Block denied topics to help remove harmful content](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-denied-topics.html) in the Amazon Bedrock documentation.
+ **Output guardrails** – These controls scan the LLM's response before it is sent back to the user. Their purpose is to make sure that the generated content is safe, accurate, and compliant. Key functions include the following:
  + **Guardrails to filter harmful content** – Detect and filter content related to hate speech, violence, or other toxic categories, based on configurable thresholds. For more information, see [Configure content filters for Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters-overview.html) in the Amazon Bedrock documentation.
  + **Contextual grounding checks** – For RAG applications, this guardrail compares the generated response against the source documents that were provided as context. If the response contains information that contradicts or is not supported by the source data, the guardrail can detect or block it. For more information, see [Use contextual grounding check to filter hallucinations in responses](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-contextual-grounding-check.html) in the Amazon Bedrock documentation.
  + **PII masking** – Masking acts as a final check to make sure that the LLM has not inadvertently included any sensitive information in its response. For more information, see [Remove PII from conversations by using sensitive information filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html) in the Amazon Bedrock documentation.

For consistency and manageability, these guardrails should be implemented centrally, often as a component within the AI gateway. This helps you apply policies uniformly across all applications and services. You can implement guardrails through policy-as-code frameworks (such as the [Open Policy Agent](https://www.openpolicyagent.org/)), specialized commercial or open source guardrail tools (such as [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) and [NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)), or custom-built logic for highly specific needs. For more information, see [GenAI Guardrails: Implementation & Best Practices](https://www.lasso.security/blog/genai-guardrails) (Lasso blog post).

When choosing a solution, organizations face a trade-off between commercial and open source guardrails. Commercial platforms generally offer faster implementation, access to specialized security expertise, and often come with compliance certifications. This makes them a good choice for enterprises that need to move quickly and need robust protection. Open source solutions provide maximum transparency and control, which is ideal for organizations with deep in-house security expertise and unique requirements. However, these solutions demand significant internal resources to implement, maintain, and continuously update against emerging threats. For more information, see [How we're thinking about Generative AI: Proprietary vs Open Source](https://medium.com/mantisnlp/how-were-thinking-about-generative-ai-proprietary-vs-open-source-3c8aff23a82b) (Medium blog post). In practice, some organizations adopt a hybrid solution of both commercial and open source guardrails to meet their requirements.

### Adversarial testing and red teaming
<a name="adversarial-testing-and-red-teaming.e978f1fe-efa8-59ef-ae2f-1e6c3de435e2"></a>

If guardrails are the defensive walls of the application, red teaming is the offensive force that is designed to test their strength. *Red teaming* is a form of ethical hacking where security professionals or automated tools simulate the attacks of a malicious actor to proactively discover vulnerabilities before they can be exploited in the production environment.

This process should not be random; it must be a systematic and repeatable effort that aligns with a recognized framework. The [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) (OWASP) has become the industry standard for categorizing the most critical security risks that face these systems. The preproduction red teaming effort should be structured to test for these specific vulnerabilities.

The following are key areas to test, based on OWASP top ten:
+ **LLM01: Prompt injection** – The red team should employ a variety of techniques (direct, indirect, and jailbreaking) to attempt to override the system's core instructions and cause it to perform unintended actions, such as ignoring previous commands or revealing confidential information.
+ **LLM02: Sensitive information disclosure** – Testers should craft prompts designed to trick the model into revealing sensitive data that may have been present in its training set or that exists in the current conversational context.
+ **LLM04: Data and model poisoning** – For RAG systems, this is a critical test. The red team should attempt to inject malicious or false information into the knowledge base, such as by uploading a compromised document, to see if they can *poison* the system and corrupt its future answers on that topic.
+ **LLM07: System prompt disclosure** – A common attack is to try to extract the system prompt itself because it often contains proprietary business logic, instructions, or context that the developers do not want exposed. The red team should test various extraction techniques.

This testing should be automated wherever possible by using tools such as [Promptfoo](https://www.promptfoo.dev/), which can run suites of adversarial tests. These automated scans should be integrated directly into the CI/CD pipeline to make sure that every new version of the application is tested for these critical vulnerabilities before deployment.

### Establishing governance and compliance
<a name="establishing-governance-and-compliance.6fc097d8-52a1-56ce-a944-d577ce414375"></a>

Finally, the application must be integrated into the enterprise's broader governance and compliance framework. Implement the following in your organization:
+ **Data governance** – All data handling processes, from ingestion into the RAG pipeline to the storage of conversation logs, must adhere to the organization's data governance policies and relevant regulations, such as [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) or [Health Insurance Portability and Accountability Act (HIPAA)](https://www.hhs.gov/hipaa/index.html). This includes policies for data classification, retention, and deletion. The AI gateway can play a role in enforcing data sovereignty by automatically routing requests from users in a specific geography to model endpoints that are hosted in a compliant AWS Region.
+ **Access control** – Robust role-based access control (RBAC) must be implemented. This makes sure that users and services can only access the data and functionalities for which they are explicitly authorized. The application's authentication and authorization system should be integrated with the enterprise's central identity provider to consistently enforce policies.
+ **Audit trails** – The observability system must be configured to provide a comprehensive and immutable audit trail. This log should capture all prompts, responses, tool calls, and actions taken by the agent. This detailed record is non-negotiable for compliance purposes and is invaluable for forensic investigation in the event of a security incident.

## Driving continuous improvement through data and feedback loops
<a name="preprod-hardening-continuous-improvement"></a>

A generative AI application is not a static artifact that is finished upon deployment. The real world is dynamic; new information becomes available, user expectations evolve, and new failure modes emerge. Without a mechanism to adapt to this changing environment, the quality and relevance of any generative AI application will inevitably degrade over time. The preproduction stage is where you must design and build a continuous learning architecture that learns from data and feedback loops.

The following diagram shows a feedback loop that drives continuous improvement.

![User feedback drives a continuous improvement loop for the generative AI application.](http://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/images/guide-img/5b6a3e4a-ff13-48e9-83d7-177629049c97/images/5b05dc8a-2cbd-4f15-aa28-67b92b296ddd.png)

The diagram shows the following continuous improvement cycle:

1. The user interacts with the generative AI application

1. The user provides implicit or explicit feedback through the generative AI application.

1. The application team analyzes the feedback, updates the evaluation dataset, and improves the prompt, system, or model.

1. The application team deploys the new version of the generative AI application.

To build this continuous improvement loop, you must design a robust feedback system, build a data collection pipeline for the user feedback, and then iterate the application based on that feedback.

### Designing robust feedback systems
<a name="designing-robust-feedback-systems.2bcef60d-fb55-5637-ba34-1c724e7da270"></a>

A robust feedback architecture captures signals from multiple sources as either explicit or implicit feedback.

*Explicit feedback* involves designing UI components that actively and directly solicit feedback from users. This is the most direct signal of quality. Common mechanisms include:
+ Thumbs up or down buttons for each generated response
+ A star rating system, such as 1-5 stars
+ A **report issue** button that opens a form where users can categorize the problem (such as *inaccurate*, *harmful*, or *irrelevant*) and provide a brief explanation of the issue

*Implicit feedback* involves capturing user behaviors that imply satisfaction or dissatisfaction, without requiring the user to take an explicit action. These signals can be noisy but are valuable at scale. Examples include:
+ (Positive signal) The user copies the generated response to their clipboard.
+ (Positive signal) In a conversational agent, the user ends the conversation after receiving an answer.
+ (Negative signal) The user immediately rephrases and resubmits their query after getting a response.
+ (Negative signal) The user ignores the generated response and continues scrolling or navigates away.

All of this feedback data, both explicit and implicit, must be logged. Critically, it must be tied back to the unique trace ID of the specific interaction that generated it. This allows engineers to correlate a piece of feedback directly with the full context of the request, including the prompt, the model's response, and the tools that were called.

### Architecting the feedback collection pipeline
<a name="architecting-the-feedback-collection-pipeline.d8c5abec-0273-5097-9b84-83adf9d560c5"></a>

Designing a robust feedback system involves meticulous planning of how feedback is collected, tracked, and stored. The following are common aspects in a feedback collection pipeline:
+ **Frontend integration and design** – The user interface, as the primary feedback channel, should minimize friction by offering simple tools such as rating buttons with optional comment fields. Feedback requests must appear at natural stopping points to avoid disrupting user flow. Responsible AI design also emphasizes that users should remain in control. AI involvement should be clearly disclosed. This means that users should know when content, suggestions, or responses are generated by AI rather than humans, and users should have the ability to dismiss or revert AI-generated content.
+ **Backend storage and request tracking** – All user interactions should be continuously collected, tracked, and logged. Linking feedback to unique request IDs enables detailed analysis by connecting user satisfaction to specific model outputs. Storing feedback with metadata, such as user ID and timestamp, is essential for thorough troubleshooting, performance monitoring, and extended evaluation.
+ **User behavior analytics** – Beyond explicit feedback, analyzing logs and using machine learning platforms can provide deeper insights into user patterns. It can also help you predict future trends, identify opportunities and risks, and drive continuous system improvement.

### Analyzing the feedback and improving the application
<a name="analyzing-the-feedback-and-improving-the-application.0e4d5dd3-2e26-5b71-93a1-88d4931bf7ed"></a>

Collecting feedback is useless if it sits dormant in a database. The final and most important part of the architecture is the automated workflow that closes the loop by turning raw feedback into concrete application improvements. This workflow typically involves the following stages:
+ **Collect and aggregate** – All feedback data is collected from the application logs and aggregated in a centralized data warehouse or analytics platform.
+ **Analyze and triage** – Dashboards and automated analysis are used to identify trends and patterns in the feedback. Which types of queries are receiving the most negative interactions? Is there a particular document in the RAG knowledge base that is frequently associated with responses marked as inaccurate?
+ **Curate for evaluation** – The most valuable pieces of feedback, especially user-reported failures with clear explanations, should be automatically triaged and converted into new test cases. These new prompt-and-expected-outcome pairs are added to the versioned evaluation dataset, hardening the test suite against known failures.
+ **Retrain or refine** – The aggregated feedback data provides a powerful signal for improvement. It can be used to guide prompt engineering efforts or to identify gaps in the RAG knowledge base that need to be filled. In more advanced scenarios, you can use it to create a preference dataset for fine-tuning the model by using techniques like [reinforcement learning from human feedback (RLHF)](https://aws.amazon.com/what-is/reinforcement-learning-from-human-feedback/). You might go back to the PoC stage with the extended datasets for evaluation or fine-tuning.
+ **Re-evaluate and deploy** – After a potential fix has been implemented, the improved version of the application is tested against the newly updated evaluation dataset. This confirms that the original issue has been resolved and that the change has not introduced any new regressions.

The quality of a generative AI application over its lifetime is a direct function of the quality and speed of its feedback loop. A system with no feedback loop is doomed to obsolescence. A system with a slow, manual feedback loop will struggle to keep pace with the changing world. A system with a fast, automated, and comprehensive feedback loop will continuously learn and adapt, maintaining or even improving its quality and value over time. Therefore, the feedback architecture is not a nice-to-have feature for post-launch improvement. It is a core architectural component that determines the long-term viability of the product. You must be designed built it with the same rigor as the core application logic during the preproduction stage.
