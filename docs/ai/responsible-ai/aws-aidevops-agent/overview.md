---
source_url: https://docs.aws.amazon.com/ai/responsible-ai/aws-aidevops-agent/overview.html
---

# AWS DevOps Agent
<a name="overview"></a>

![Banner background image](https://docs.aws.amazon.com/ai/responsible-ai/aws-aidevops-agent/images/card-background.jpg)

An AWS AI Service Card explains the use cases for which the service is intended, how machine learning (ML) is used by the service, and key considerations in the responsible design and use of the service. A Service Card will evolve as AWS receives customer feedback, and as the service progresses through its lifecycle. AWS recommends that customers assess the performance of any AI service on their own content for each use case they need to solve. For more information, please see [AWS Responsible Use of AI Guide](https://d1.awsstatic.com/products/generative-ai/responsbile-ai/AWS-Responsible-Use-of-AI-Guide-Final.pdf) and the references at the end. Please also be sure to review the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/), [AWS Acceptable Use Policy](https://aws.amazon.com/aup/), and [AWS Service Terms](https://aws.amazon.com/service-terms/) for the services you plan to use.

This Service Card applies to the incident investigation, prevention recommendation, and on-demand SRE task capabilities of AWS DevOps Agent that are current as of September 30, 2026.

## Overview of AWS DevOps Agent
<a name="overview-section"></a>

AWS DevOps Agent is a generative artificial intelligence (GenAI) powered service that helps software engineering teams investigate production incidents, optimize operational health, and generate prevention recommendations based on historical incidents. The service uses AI agents to automatically analyze observability signals, correlate telemetry with code and deployment data, identify root causes of incidents, and provide actionable recommendations to resolve issues. AWS DevOps Agent operates within Agent Spaces: customer defined scoped environments that define what resources and services the AI agents can access. Each Agent Space maintains a topology—a knowledge graph of the application environment—serving as the foundation for intelligent incident investigation and analysis. The service integrates with observability tools, code repositories and CI/CD pipelines, and incident management tools. Customers can also extend AWS DevOps Agent by securely connecting to private or remote MCP (Model Context Protocol) servers. For more information, see the [AWS DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/).

We assess the quality of AWS DevOps Agent by measuring how well the agent's outputs align with ground-truth expectations defined for known incident scenarios. For incident investigations, we evaluate whether the agent correctly identifies the root cause of an incident by comparing investigation findings against known root causes. For prevention recommendations, we evaluate outputs across two levels. A recommendation is considered "valid" if it is assessed as meeting both safety criteria (following the recommendation would not worsen the operational situation) and correctness criteria (the proposed solution is technically sound). A recommendation is considered "high-value" if, in addition to being valid, it also demonstrates goal focus (targets the specific problem rather than generic advice), actionability (an engineer can execute the recommendation without ambiguity), and evidence quality (cites specific observability data from the customer's environment). AWS DevOps Agent does not provide a confidence score for its outputs; a customer's workflow must decide if an investigation finding or recommendation is effective using human judgment—for example, by reviewing the cited evidence and validating findings before taking remediation actions.

As is the case with more traditional ML solutions, AWS DevOps Agent must overcome issues of intrinsic and confounding variation. Intrinsic variation refers to features of the input environment to which the agent must attend—for example, different application architectures (monolithic vs. microservices), different root causes of incidents (code regression vs. configuration change vs. infrastructure failure vs. dependency issue), varying severity levels, and different resource relationships and dependencies within a customer's topology. Confounding variation refers to features that the agent should handle gracefully without impacting quality—for example, different types of incidents (latency degradation, error rate spikes, capacity exhaustion), different observability tool implementations, varying logging formats and verbosity levels, different naming conventions for resources and services, different CI/CD pipeline implementations, varying levels of observability coverage across an environment, and customer-specific runbook formatting. The full set of confounding variations also includes differences in how customers structure their cloud accounts, the complexity of cross-service dependencies, and the completeness of the application topology graph.

## Intended Use Cases and Limitations
<a name="use-cases-limitations"></a>

AWS DevOps Agent supports three key use cases: incident investigation and resolution, preventive recommendations, and on-demand Site Reliability Engineering (SRE) task handling.
+ **Incident investigation and resolution:** refers to the autonomous triage of production incidents, including root cause analysis, correlation of observability signals with code and deployment changes, and generation of actionable resolution steps.
+ **Prevention recommendations:** refers to the analysis of patterns across historical incidents to generate recommendations that strengthen observability, infrastructure configuration, deployment pipelines, and application resilience.
+ **On-demand SRE task handling:** refers to responding to natural language questions about application health, resource status, deployment history, and operational patterns—enabling operators to access insights from their operational data without writing queries.

When assessing AWS DevOps Agent for a particular use case, customers should consider: the completeness of observability coverage for the target application, the availability of code repository and CI/CD pipeline integrations, and the context the agent has about the application, its dependencies, and the operational environment. The agent performs best when investigating incidents in environments with rich observability signals (logs, metrics, traces) and relevant context about the application and its operational history.

Consider the following example use case: using AWS DevOps Agent to investigate production incidents for a microservices application. The business goal is to reduce mean time to resolution by providing on-call engineers with automated root cause analysis. The stakeholders include the on-call engineers who need fast, accurate root cause identification, and the engineering managers who want to reduce operational toil. The workflow is: 1/ a CloudWatch alarm fires due to elevated error rates, 2/ AWS DevOps Agent automatically begins investigating by correlating logs, metrics, traces, and recent code deployments, 3/ the agent generates a root cause summary with supporting evidence and recommended actions, 4/ the on-call engineer reviews the findings, validates the root cause by examining the cited evidence, and decides whether to proceed with remediation, 5/ the engineer provides feedback to indicate whether the investigation was effective. The inputs include alarm events, application logs, metrics, traces, deployment histories, code changes, and the application topology. The outputs are natural language investigation summaries with root cause identification, evidence citations, and recommended remediation steps.

Error types for each use case, ranked in estimated order of negative impact, are:

**Incident investigations:**

1. Incorrect root cause identification

1. Correct root cause but irrelevant or unhelpful recommended actions

1. Correct root cause but missing key evidence that would help the operator validate findings

1. Investigations that fail to reach a conclusion

**Prevention recommendations:**

1. Recommendations that could worsen the operational situation if followed

1. Technically incorrect recommendations that propose an invalid solution approach

1. Recommendations that do not address the actual problem identified during investigation

1. Recommendations that are too vague for an engineer to execute without ambiguity

1. Recommendations that lack supporting evidence from the customer's environment

**On-demand SRE tasks:**

1. Factually incorrect answers about the customer's environment or resources

1. Answers that reference resources or data not accessible within the configured Agent Space

1. Answers that are irrelevant to the question asked

1. Queries that fail to return results or time out

**Limitations:**
+ AWS DevOps Agent depends on large language models (LLMs) which can produce inaccurate content. Customers should evaluate outputs for accuracy and appropriateness for their use case, including by implementing appropriate human oversight, testing, and other use case-specific safeguards.
+ AWS DevOps Agent is designed for operational incident investigation and prevention in cloud environments. It is not designed for use cases unrelated to DevOps operations, such as general-purpose question answering, content creation, or software development tasks.
+ The agent's effectiveness depends on the completeness and quality of the observability data available. Environments with limited logging, metrics, tracing coverage, code repositories and CI/CD pipeline access may yield less accurate investigations.
+ AWS DevOps Agent operates based on the application topology and integrations configured within an Agent Space. Resources or services not included in the Agent Space, or not accessible via the IAM role policy configured for the Agent Space role, are not visible to the agent, which may result in incomplete or incorrect root cause analyses.
+ The agent is not designed to autonomously execute remediation actions that modify production infrastructure without human review and approval. Investigation findings and recommendations require human validation.
+ Customer-provided operational context (such as runbooks or steering instructions) influences the direction and output of the agents. Inaccurate or incomplete context may lead the agent toward incorrect conclusions.

## Design of AWS DevOps Agent
<a name="design"></a>

**Large language model**
AWS DevOps Agent uses large language models (LLMs) hosted on Amazon Bedrock (Amazon Bedrock) to power its agentic reasoning capabilities. The service operates through an agentic loop in which the AI agent: (1) receives an incident trigger or user prompt, (2) plans a sequence of investigation steps, (3) executes tool calls to query observability data, code repositories, deployment histories, and the application topology, (4) incorporates customer-provided context and knowledge (such as operational runbooks and findings from previous investigations) to guide its reasoning, (5) synthesizes findings across multiple data sources, and (6) generates natural language outputs including root cause summaries, evidence citations, and recommended actions. The agent iterates through this loop, refining its hypotheses as it gathers additional evidence. For prevention recommendations, the agent additionally analyzes patterns across historical investigations to identify systemic improvements. Amazon Bedrock Guardrails are applied to filter inputs for prompt attacks and enforce content safety policies.

**Performance expectations**
Individual and confounding variation will differ between customer environments. This means that performance will also differ between environments, even if they support the same use case. Consider two deployments A and B. Deployment A monitors a microservices application with comprehensive logging, distributed tracing, and well-defined resource relationships in the topology. Deployment B monitors a monolithic application with limited logging and partial observability coverage. Because A and B have differing levels of observability data and architectural complexity, they may have different root cause accuracy rates, even assuming each deployment is configured correctly. Customers are in the best position to assess the performance of AWS DevOps Agent on their own operational environment.

**Test-driven methodology**
We evaluate AWS DevOps Agent using structured scenarios that deploy real AWS infrastructure, inject known faults, and assess agent outputs against human-curated ground truths. The evaluation dataset spans diverse application architectures (serverless, containerized, and VM-based), multiple observability tool integrations, and various root cause categories (code regressions, infrastructure failures, configuration changes, capacity issues, and dependency problems). No single evaluation scenario provides a complete picture of performance because customer environments vary in architecture, observability coverage, and integration configurations.
Evaluation scenarios are developed by the AWS DevOps Agent engineering team in collaboration with applied scientists. Each ground truth is derived from expert knowledge of the injected failure mechanism and specifies the expected root cause, impacted resources, and relevant observability signals. The evaluation dataset currently spans multiple environment configurations across AWS-native and third-party observability integrations, and is continuously expanded as new failure patterns and integrations are supported.
To address uncertainty inherent in LLM-based evaluation, each scenario is evaluated across multiple independent iterations, and performance is monitored using aggregated daily metrics rather than individual run results.
No evaluation benchmark can fully capture the variability of customer environments, including differences in observability coverage, configured integrations, operational context supplied by customers, and application complexity. Customers should evaluate the agent on their own workloads.

**Controllability**
AWS DevOps Agent provides multiple mechanisms for customers to control the agent's behavior:
+ **Agent Spaces:** scope what resources and services the agent can access. Customers configure Agent Space boundaries and IAM role policies to restrict the agent's visibility.
+ **Controlled access to customer resources:** The agent currently operates in a read-only mode with respect to customer AWS resources. A mutative operations blocklist is designed to enforce this constraint at the tool layer. When remediation actions are proposed, they require explicit human approval before execution.
+ **Human-in-the-loop:** Investigation findings and recommendations are presented to human operators for review and decision-making. When mitigation actions are proposed, a human approval gate requires explicit operator confirmation before any action can proceed.
+ **Steering:** Operators can interact with ongoing investigations through a chat interface to provide additional context, redirect the investigation focus, or ask follow-up questions.
+ **Cancellation:** Operators can cancel an in-progress investigation at any time.
+ **Integration configuration:** Customers control which observability tools, code repositories, and communication channels are connected to the agent.

**Safety**
AWS DevOps Agent incorporates multiple layers of safety controls. The agent currently operates in a read-only mode with respect to customer AWS resources where a mutative operations blocklist is designed to enforce this constraint at the tool layer, preventing the agent from executing write operations on customer infrastructure without explicit human approval. Each sub-agent is designed to be restricted to a defined set of allowed tools, limiting the scope of actions any individual component can perform. For customer-provided MCP (Model Context Protocol) server integrations, tool specifications are designed to be validated at association time to ensure only explicitly allowlisted tools are exposed to the agent. The evaluation framework distinguishes between valid approaches that address the root cause and invalid approaches that could be counterproductive (for example, suppressing alarms rather than addressing the underlying issue, or scaling resources without resolving the actual bottleneck).

**Fairness**
AWS DevOps Agent uses the same system prompts and agent workflow uniformly across all customer environments. The service does not differentiate its behavior based on customer attributes, organization size, or workload characteristics. All customers receive the same quality of investigation and recommendation generation, subject to the observability data and integrations available in their environment.

**Explainability**
AWS DevOps Agent is designed to provide transparent, evidence-based outputs. Investigation findings include citations to specific observability data (log entries, metrics, traces, deployment events) that support the root cause analysis. Findings are classified by multiple evidence types (root cause, contributing cause, or hypothesis) to communicate the degree of certainty in each conclusion. Prevention recommendations cite the evidence from historical investigations that motivates the recommendation. This enables operators to independently verify the agent's reasoning by examining the referenced data.

**Privacy and security**
AWS DevOps Agent processes customer operational data (logs, metrics, traces, code, deployment data) within the scope of the customer's configured Agent Space. The service is designed to use IAM role-based access controls to prevent the agent from accessing resources other than those the customer has explicitly authorized. Amazon Bedrock Guardrails are deployed across all agent types with content filtering designed to detect and block prompt attacks in input. Customer data is encrypted at rest and in transit. Customer data processed by AWS DevOps Agent is not used to train or improve the underlying foundation models. When customers extend AWS DevOps Agent by connecting their own MCP servers, the security and trustworthiness of tool responses from those servers is the customers' responsibility. Customers select which tools are exposed to the agent during onboarding and are responsible for ensuring their MCP servers return trustworthy data. For more information, see Section 50.3 of the [AWS Service Terms](https://aws.amazon.com/service-terms/) and the [AWS Data Privacy FAQs](https://aws.amazon.com/compliance/data-privacy-faq/). For more information, see the [AWS DevOps Agent Security documentation](https://docs.aws.amazon.com/devopsagent/latest/userguide/aws-devops-agent-security.html).

**Veracity**
AWS DevOps Agent uses an agentic architecture that combines observability signal retrieval, topology-aware reasoning, and LLM-based synthesis to produce investigation findings that are grounded in the customer's operational data. However, agentic systems can still produce errors. We assess AWS DevOps Agent using structured ground truths that define the expected root cause, impacted resources, and relevant observability signals for each evaluation scenario.
Our evaluation suite covers a range of root-cause identification scenarios across multiple diverse application environments and multiple accounts, including a banking application with traditional compute and database components, a containerized application, and a distributed microservices application. We periodically inject real-world operational failures across these environments, spanning application, infrastructure, database, configuration, and service issues in AWS-native and selected third-party and multi-cloud configurations.
For incident investigations, we evaluate root cause accuracy by comparing the agent's identified root cause against known ground truths using an LLM-based semantic judge. We periodically validate the LLM-based evaluation through human review. Engineers independently assess a sample of automated judgments against the ground truth and relevant environment evidence using a defined rubric for successful investigations, agent failures, and test-harness issues. Any overrides are recorded and tracked to identify systematic disagreement and improve the evaluation process.
Each scenario is evaluated multiple times to account for variability in agent behavior. We summarize performance using three complementary measures. Pass@1 measures performance on a single attempt. Pass@3 measures whether the agent succeeds at least once across three attempts and reflects its ability to find the correct answer when multiple attempts are available. Pass^3 measures the fraction of scenarios in which the agent is accurate 3 times in a row, providing a stricter measure of consistency and reliability. We also report 95% confidence intervals for benchmark-level performance, computed over scenario-level results to quantify uncertainty arising from the finite evaluation set.
The agent is designed to validate its hypothesis against observed signals before they are presented as root causes. Findings are classified using structured confidence types (root cause, contributing cause, hypothesis) to communicate different levels of certainty. When insufficient data is available to reach a conclusion, the agent is designed to communicate this limitation rather than generating unsupported hypotheses.
For prevention recommendations, we evaluate outputs across two levels of strictness. A recommendation is considered "valid" if it passes both safety checks (following the recommendation would not worsen the operational situation) and correctness checks (the proposed solution is technically sound). A recommendation is considered "high-value" if, in addition to being valid, it also demonstrates goal focus (targets the specific problem rather than generic advice), actionability (an engineer can execute the recommendation without ambiguity), and evidence quality (cites specific observability data from the customer's environment).
We conduct daily offline evaluations using this methodology to monitor the quality of AWS DevOps Agent. We target a root-cause accuracy (Pass@1) of at least 95% for incident investigations and a high-value rate of at least 80% for prevention recommendations. Since the service is continuously improved, a single published point estimate may not remain representative of the production system. Instead, changes and new capabilities are evaluated against these predefined release criteria before deployment. To avoid regression in accuracy, changes and new capabilities are released only when the observed point estimates meet these targets; 95% bootstrap confidence intervals are reported alongside the point estimates to characterize uncertainty. For the current production release, these release criteria were met across the evaluated environments. Exact evaluation results are tracked internally as part of the service's release and quality-monitoring process, curated daily.
When performance does not consistently meet these targets, we investigate and take corrective action, which may include updating the agent or its configuration, or rolling back recent changes.
Customers should conduct veracity testing on their own operational environment and incident patterns.

**Robustness**
We measure robustness by evaluating root cause accuracy across multiple environment configurations that vary by cloud provider, observability, and third-party tool integration, testing whether the agent maintains consistent performance when the same class of incident is presented through different observability interfaces and infrastructure platforms. We additionally evaluate consistency of results across repeated attempts on the same scenario.
Individual and confounding variation will differ between customer environments, and customers are in the best position to assess the agent's performance on their own infrastructure and observability configuration.

**Transparency**
This AI Service Card is part of AWS's commitment to transparency about how AI services work. AWS DevOps Agent identifies itself as "AWS DevOps Agent" in its communications through integrated channels. The service provides customers with visibility into the investigation process through detailed investigation timelines, tool call histories, and evidence citations. Customers can observe what data the agent accessed and how it arrived at its conclusions. The Operator App console provides onboarding information describing the Agent Space boundary and agent capabilities.

**Governance**
AWS DevOps Agent supports customer governance requirements through IAM-based access controls, Agent Space scoping, and audit capabilities. Customers can configure who has access to the agent, what resources the agent can query, and review investigation histories for compliance and audit purposes. Foundation model versions are pinned to specific version identifiers, and updates are validated through an automated evaluation canary pipeline that runs multiple times daily and emits performance metrics (including root cause accuracy and time to resolution) with associated alarms. An A/B variant testing system enables controlled evaluation of model updates before production deployment.

## Deployment and performance optimization best practices
<a name="deployment-performance-optimization-best-practices"></a>

We encourage customers to build and operate their applications responsibly, as described in [AWS Responsible Use of AI Guide](https://d1.awsstatic.com/products/generative-ai/responsbile-ai/AWS-Responsible-Use-of-AI-Guide-Final.pdf). This includes implementing Responsible AI practices to address key dimensions including controllability, safety, fairness, veracity, robustness, explainability, privacy, security, transparency, and governance.

AWS DevOps Agent performance depends on the quality and completeness of the operational context available to the agent. Customers can optimize the effectiveness of the service by considering the following best practices:

**Agent Space configuration**
+ Define Agent Spaces with clear boundaries that align with application ownership and operational responsibility. A well-scoped Agent Space enables the agent to build an accurate topology and focus investigations on relevant resources.
+ Configure IAM role policies to grant the agent access to the observability data, code repositories, and deployment tools relevant to the applications being monitored. Overly restrictive permissions may limit the agent's ability to gather the evidence needed for accurate root cause identification.

**Observability coverage**
+ The agent's investigation quality correlates with the richness of available observability signals. Environments with comprehensive logging, metrics, and distributed tracing will generally yield more accurate and detailed root cause analyses than environments with limited observability.
+ Ensure that CloudWatch alarms, or equivalent alerts from third-party observability tools, are configured with appropriate thresholds to trigger investigations at the right time.

**Topology completeness**
+ The application topology (knowledge graph) serves as the foundation for the agent's understanding of resource relationships and dependencies. A more complete topology enables the agent to better trace the propagation of failures across components.
+ Onboard relevant AWS accounts and configure integrations to ensure all critical services and their dependencies are represented in the topology.

**Integration configuration**
+ Connect code repositories and CI/CD pipelines to enable code-to-cloud investigations. This allows the agent to correlate incidents with recent code deployments and identify code-level root causes.
+ Configure communication channel integrations (such as Slack or ticketing systems) to streamline the routing of investigation findings to the appropriate on-call teams.

**Runbooks and operational knowledge**
+ Provide customer-specific runbooks and operational knowledge to the agent by configuring custom instructions, creating investigation skills, and adding knowledge entries within the Agent Space. This enables the agent to incorporate organization-specific procedures and known failure patterns into its investigations and recommendations.

**Human oversight**
+ Review investigation findings and validate the cited evidence before acting on recommendations. The agent presents its reasoning and supporting data to enable informed decision-making.
+ Provide feedback (thumbs-up or thumbs-down) on investigation quality to help improve the service over time.
+ Steer ongoing investigations through the chat interface when additional context or a change in investigation direction is needed.

**Model updates**
+ AWS DevOps Agent uses foundation models that are updated periodically to improve quality and capabilities. Model updates may result in changes to investigation behavior or recommendation content. AWS evaluates model updates against quality benchmarks before deployment. Customers should periodically re-evaluate the agent's performance on their workloads following service updates.

**Testing and evaluation**
+ Customers are in the best position to assess the performance of AWS DevOps Agent for their specific operational environment. We recommend that customers evaluate investigation accuracy on their own incidents across a representative sample of their workload before relying on the agent for critical production use cases.
+ Consider starting with non-critical environments or lower-severity incidents to build confidence in the agent's findings before expanding to broader adoption.

## Further information
<a name="further-info"></a>

**Product documentation**
+ [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) — Product overview, features, pricing, and customer stories.
+ For service documentation, see [AWS DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/) — Technical documentation for configuring and operating the service.

**Responsible AI resources**
+ For details on privacy and other legal considerations, see the following AWS policies: [Acceptable Use](https://aws.amazon.com/aup/), [Responsible AI](https://aws.amazon.com/ai/responsible-ai/policy/), [Legal](https://aws.amazon.com/legal/), [Compliance](https://aws.amazon.com/compliance/), and [Privacy](https://aws.amazon.com/privacy/).
+ For help optimizing workflows, see [Generative AI Innovation Center](https://aws.amazon.com/ai/generative-ai/innovation-center/), [AWS Customer Support](https://aws.amazon.com/contact-us/), [AWS Professional Services](https://aws.amazon.com/professional-services/), [Ground Truth Plus](https://aws.amazon.com/sagemaker/groundtruth/), and [Amazon Augmented AI](https://aws.amazon.com/augmented-ai/).

**Related AWS services**
+ [Amazon Bedrock](https://aws.amazon.com/bedrock/) — The foundation model service used by AWS DevOps Agent for AI reasoning.
+ [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) — Content filtering and safety controls applied to AI model inputs and outputs.
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) — Monitoring and observability service integrated with AWS DevOps Agent.
+ [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) — Service for logging API activity, used in code-to-cloud investigations.
+ If you have any questions or feedback about AWS AI service cards, please complete [ this form](https://pages.awscloud.com/global-ln-gc-400-ai-service-cards-contact-us-registration.html).

## Glossary
<a name="glossary"></a>

 **Controllability: **Steering and monitoring AI system behavior.

 **Privacy & Security: **Appropriately obtaining, using and protecting data and models.

 **Safety: **Preventing harmful system output and misuse.

 **Fairness: **Considering impacts on different groups of stakeholders.

 **Explainability: **Understanding and evaluating system outputs.

 **Veracity & Robustness: **Achieving correct system outputs, even with unexpected or adversarial inputs.

 **Transparency: **Enabling stakeholders to make informed choices about their engagement with an AI system.

 **Governance: **Incorporating best practices into the AI supply chain, including providers and deployers.
