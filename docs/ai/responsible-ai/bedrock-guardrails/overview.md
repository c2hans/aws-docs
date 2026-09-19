---
source_url: https://docs.aws.amazon.com/ai/responsible-ai/bedrock-guardrails/overview.html
---

# Amazon Bedrock Guardrails
<a name="overview"></a>

![Banner background image](https://docs.aws.amazon.com/ai/responsible-ai/bedrock-guardrails/images/card-background.jpg)

An AWS AI Service Card explains the use cases for which the service is intended, how machine learning (ML) is used by the service, and key considerations in the responsible design and use of the service. A Service Card will evolve as AWS receives customer feedback, and as the service progresses through its lifecycle. AWS recommends that customers assess the performance of any AI service on their own content for each use case they need to solve. For more information, please see [AWS Responsible Use of AI Guide](https://d1.awsstatic.com/products/generative-ai/responsbile-ai/AWS-Responsible-Use-of-AI-Guide-Final.pdf) and the references at the end. Please also be sure to review the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/), [AWS Acceptable Use Policy](https://aws.amazon.com/aup/), and [AWS Service Terms](https://aws.amazon.com/service-terms/) for the services you plan to use.

This Service Card applies to the release of Amazon Bedrock Guardrails that is current as of September 15, 2026.

## Overview
<a name="overview-section"></a>

Amazon Bedrock Guardrails provides configurable safeguards that help customers implement responsible AI policies for safety, privacy, and veracity in generative AI applications. Customers apply safeguards to text, code and image content where supported on inputs, outputs, or both, either with foundation models on Amazon Bedrock or independently through the standalone API. Bedrock Guardrails is a managed service. For current capabilities and integration options, see [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) and [How Amazon Bedrock Guardrails works](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html).

Customers define their own responsible AI policies and implement each by configuring the corresponding safeguards and validating behavior on their own content. For current configuration controls, see [Create your guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html).

Bedrock Guardrails detects policy violations using ML-based classifiers, pattern matching, or formal logic (Automated Reasoning checks). Regardless of approach, each safeguard must overcome issues of intrinsic and confounding variation. Intrinsic variation refers to features of the input to which a guardrail should attend, such as whether a question actually seeks financial advice. Confounding variation refers to features the guardrail should ignore, such as differences in wording that do not change meaning. Real-world inputs include many such variations in language, style, format, image quality, and errors.

## Intended use cases and limitations
<a name="use-cases-limitations"></a>

Bedrock Guardrails provides a layer of defense for AI applications that allows customers to experiment with different application components (such as different foundation models), while keeping uniform standards for safety, privacy and veracity. Protection comes from two layers: customer-defined policies configured in Bedrock Guardrails and the native safety controls of the foundation model. Customers translate each responsible AI policy into one or more configured safeguards and apply them to the relevant inputs, outputs, or both. Because policies are expressed at an abstract level, customers should verify that the configured safeguards align with their intended policy on representative content.

For current safeguard types, content categories, configuration options, actions, limits, and supported modalities, see [Guardrail components](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html). For current language and code support, see [Supported languages](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-supported-languages.html) and [Code domain support](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-code-domain.html).

**Guarded AI application performance**: In choosing and configuring guardrails, customers must evaluate the overall performance of the resulting Guarded AI application because adding or changing a guardrail can affect other responsible AI outcomes, such as fairness.

**Asynchronous mode for streaming:** Customers should use the default synchronous mode for streaming responses unless latency requirements outweigh content moderation. In asynchronous mode, response chunks are returned to end users before the guardrail finishes evaluating them, so harmful content or unmasked sensitive information can reach end users before intervention occurs, and masking of sensitive information is not supported. Asynchronous mode is not appropriate for applications that handle sensitive information or serve vulnerable users. See [Configure streaming response behavior](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-streaming.html).

**RAI coverage:** Like other AI-powered content moderation tools, Bedrock Guardrails may not by itself suffice to implement all customer responsible AI policies. Customers should consider their full range of options, including using system prompts to constrain foundation model behavior and blocking sensitive content in the knowledge base of the RAG system.

When assessing Bedrock Guardrails for a particular AI application and use case, we encourage customers to define the use case narrowly, i.e., by considering at least the following factors: the business problem being solved; the stakeholders in the business problem and the deployment process; the workflow that solves the business problem, with the Bedrock Guardrails service and human oversight as components; key application inputs and outputs; the expected intrinsic and confounding variation; and the types of errors possible and the relative impact of each.

Example use case: Consider a bank implementing safety and veracity policies for a customer chatbot. The goal is to provide accurate information while adhering to the bank's content safety policies. Stakeholders are the bank's customers, who want accurate information, and the bank, which wants safe, non-hallucinated responses. The workflow is 1/ the bank sets up a RAG system or customized foundation model as the chatbot, 2/ tests it for safety and veracity without guardrails, 3/ configures and tests multiple guardrail versions, 4/ deploys the most effective version, 5/ updates versions as needed, and 6/ monitors performance periodically. Inputs are customer questions; outputs are chatbot answers or guardrail intervention messages. Prompts vary in language, detail, accuracy, spelling, and abbreviations. Error types, ranked by impact, are a/ outputs that violate the bank's policies, b/ acceptable outputs incorrectly blocked, c/ irrelevant responses, and d/ poor-quality writing.

The bank should test representative prompts and completions, including benign, policy-violating, ambiguous, and adversarial inputs. For example, a benign account-balance question grounded in the bank's reference content should be allowed, while a request for prohibited investment advice should be blocked. The bank should review both missed and unnecessary interventions, define acceptance criteria based on the impact of each error type, validate results with human judgment, and retest after changes. See [Test a guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-test.html) and [Amazon Bedrock Prompt Management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html).

## Design of Bedrock Guardrails
<a name="design"></a>

****Machine learning****
Bedrock Guardrails detects policy violations using ML-based classifiers, pattern matching, or formal logic (Automated Reasoning checks). ML-based safeguards are probabilistic: they can miss violations or flag acceptable content, and their behavior depends on how well the configured policy matches the customer's intent. For how guardrails are applied to inputs and outputs, see [How Amazon Bedrock Guardrails works](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html).

****Controllability****
We design each guardrail with configuration controls, such as filter strength, topic definitions, word lists, and confidence thresholds, and refine training data and rules so that guardrail behavior aligns with our design goals and responds predictably to those controls. Customers use these controls to align guardrails with their own policies; because misconfiguration can cause over- or under-filtering, customers should version and test configurations before deployment. For current controls, see [Create your guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html).

****Performance expectations****
Guardrail effectiveness varies by application because inputs, content variation, and policy interpretation differ. Two applications with similar use cases can have different error rates even when correctly deployed. Customers should evaluate guardrails on their own content rather than rely on general results.

****Test-driven methodology****
We evaluate individual guardrails and their impact on guarded applications using multiple datasets, because no single dataset covers all use cases, content variation, and policy interpretations. We test representative, challenging, and perturbed content across relevant groups and use the findings to guide iterative improvements. Because outcomes depend on configuration, workflow, and content, customers should test their own content, calibrate settings, and validate results with human review.

### Evaluation Methodology for Guardrails
<a name="evaluation-methodology-guardrails"></a>

This section describes how we evaluate, and govern Bedrock Guardrails itself against AWS Responsible AI dimensions. It covers fairness, robustness, privacy, and the transparency, explainability, and governance practices that support responsible use. It explains our methodology and known limitations.

****Fairness (text and image)****
We evaluate whether the guardrail's decisions are consistent across different groups. We evaluate on datasets with human-validated labels. Disparities can still occur for groups, languages, or dialects underrepresented in our evaluations, so customers should assess fairness for the groups relevant to their use case.

****Robustness (text and image)****
We evaluate whether the guardrail's decisions stay consistent when inputs change in ways that should not affect the outcome. We apply perturbations, semantic-preserving text edits and natural image degradations, to labeled samples and measure worst-case predictions across perturbation types. Novel or adversarial inputs can still bypass guardrails, so customers should test the variations and attack patterns expected in their application.

****Privacy****
Amazon Bedrock is a managed service and AWS does not use inputs or outputs generated through the Amazon Bedrock service to train Amazon Bedrock models, including Guardrails. Customers control what content is submitted; evaluated content can appear in customer-enabled invocation logs. See [AWS Service Terms](https://aws.amazon.com/service-terms/), [Data protection in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html), and [model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html). For service-specific privacy information, see the Privacy and Security section of the [Amazon Bedrock FAQs](https://aws.amazon.com/bedrock/faqs/) documentation.

****Security****
Bedrock Guardrails inherits Amazon Bedrock's security controls, including encryption in transit and at rest, IAM-based access control, and CloudTrail logging. Security is a shared responsibility: Guardrails evaluates content but does not replace application-level controls such as authentication, authorization, or input validation. Customers should apply least-privilege permissions to guardrail configuration and invocation, use immutable guardrail versions in production, and be aware that evaluated and blocked content can appear in customer-enabled invocation logs. See [Security in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security.html) and [model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html).

****Transparency****
Information about Guardrails is available through this Service Card, the [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html), AWS educational channels, and guardrail traces in the Console and API responses. We accept feedback through the Console and [AWS Support](https://aws.amazon.com/contact-us/). Customers should consider disclosing their use of ML to end users, providing a feedback mechanism, and referencing this Service Card in their own documentation.

****Explainability****
Guardrails return the actions and interventions for each enabled safeguard so customers can review and verify how content was handled. This indicates what was flagged but does not fully explain why the model reached a given decision. For trace details, see [View information about your guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-view.html).

****Governance****
We incorporate responsible AI throughout product development through reviews by dedicated Responsible AI experts, routine testing, customer reviews, and best-practice development and training. Customers remain responsible for governing how guardrails are configured, versioned, monitored, and updated within their own applications. See [Deploy a guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-deploy.html).

### Evaluation Methodology for AI Applications Using Guardrails
<a name="evaluation-methodology-applications"></a>

This section describes how we evaluate whether Guardrails helps customers meet responsible AI goals in their own applications: safety (filtering harmful content without over-blocking benign content), privacy (detecting and masking sensitive information), and veracity (identifying responses that are ungrounded or inconsistent with defined policies). These evaluations reflect common customer configurations; customers should validate effectiveness on their own content and use cases.

****Safety (text and image)****
+ *Toxicity:* Views on what is toxic vary widely, so we evaluate configurations that reflect common customer anti-toxicity policies. For text, we combine content filters at high strength with denied topics matching each dataset's harm categories, and evaluate them separately and together on datasets containing unsafe content across multiple risk categories and unambiguously safe content. For images, we evaluate content filters at high strength on manually curated and AI-generated images across unsafe categories. Findings drive targeted data curation and continued evaluation. Novel attacks or content outside expected distributions can still be missed, so customers should test their own policies and content. For available categories and strengths, see [Content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters-overview.html) and [Denied topics](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-denied-topics.html).
+ *Harmlessness:* Over-detecting harmful content can block benign content. We evaluate safety guardrails at high strength on datasets of harmless prompts and completions to measure unnecessary interventions and use the findings to reduce over-blocking while maintaining protection. The right balance depends on the use case, so customers should evaluate both missed and unnecessary interventions against their own acceptance criteria.

****Privacy (text)****
We evaluate whether detected entities are correct and whether present entities are detected, using synthetic domain-specific documents and data for names, addresses, and phone numbers across genders, countries, and locales. Findings drive targeted data curation and continued evaluation. Detection can be less reliable for unusual formats, encodings, or content embedded in code and structured data, so customers should test representative formats and use custom patterns where needed. See [Sensitive information filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html).

****Veracity (text)****
We evaluate contextual grounding checks on multi-hop fact-verification datasets to assess whether they distinguish responses supported by provided sources from those that are not, and Automated Reasoning checks on curated and synthetic customer use cases and conditional-reasoning question-answering datasets to assess whether they identify responses consistent with formal policies. Guardrails reduce but do not eliminate hallucinations, and customers should not rely on them as the sole control for factual accuracy. Grounding checks evaluate consistency with the source the application provides, not truth in general: they cannot correct inaccurate or incomplete sources, and can miss hallucinations involving tables and structured data, long contexts, numerical or multi-step reasoning, or content that is plausible but unsupported. Automated Reasoning checks depend on the completeness and correctness of the customer's policy. Customers should validate source quality, calibrate thresholds on their own content, and keep human review for outputs that affect consequential decisions. See [Contextual grounding checks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-contextual-grounding-check.html) and [Automated Reasoning checks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html).

## Deployment and performance optimization best practices
<a name="deployment-performance-optimization-best-practices"></a>

AWS publishes guidance on building and operating AI applications responsibly, and on configuring, testing, versioning, and deploying Bedrock Guardrails, including threshold calibration, input tagging, streaming modes, and latency trade-offs. See the [AWS Responsible Use of AI Guide](https://d1.awsstatic.com/products/generative-ai/responsbile-ai/AWS-Responsible-Use-of-AI-Guide-Final.pdf), [Build safe generative AI applications like a pro: best practices with Amazon Bedrock Guardrails](https://aws.amazon.com/blogs/machine-learning/build-safe-generative-ai-applications-like-a-pro-best-practices-with-amazon-bedrock-guardrails/), and the [Amazon Bedrock Guardrails User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html).

Customers should still define effectiveness criteria for their own use case, test guardrail configurations on representative content before deployment, incorporate human review for high-risk or sensitive decisions such as those affecting an individual's rights or access to essential services, and retest periodically because changes in prompts or in the service can change results.

## Further information
<a name="further-info"></a>
+ For service documentation, see [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/), [Amazon Bedrock Guardrails User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html), [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/), [Amazon Bedrock Security Compliance](https://aws.amazon.com/bedrock/security-compliance/), [Amazon Bedrock Studio](https://docs.aws.amazon.com/bedrock/latest/studio-ug/what-is-bedrock-studio.html), and [Amazon Bedrock Prompt Management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html?icmpid=docs_bedrock_help_panel_prompt_management).
+ For details on privacy and other legal considerations, see the following AWS policies: [Acceptable Use](https://aws.amazon.com/aup/), [Responsible AI](https://aws.amazon.com/ai/responsible-ai/policy/), [Legal](https://aws.amazon.com/legal/), [Compliance](https://aws.amazon.com/compliance/), and [Privacy](https://aws.amazon.com/privacy/).
+ For help optimizing workflows, see [Generative AI Innovation Center](https://aws.amazon.com/ai/generative-ai/innovation-center/), [AWS Customer Support](https://aws.amazon.com/contact-us/), [AWS Professional Services](https://aws.amazon.com/professional-services/), [Ground Truth Plus](https://aws.amazon.com/sagemaker/groundtruth/), and [Amazon Augmented AI](https://aws.amazon.com/augmented-ai/).
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
