---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/amazon-bedrock.html
---

# Amazon Bedrock
<a name="amazon-bedrock"></a>

## Amazon Bedrock
<a name="amazon-bedrock.1502b2aa-fcd4-5bd7-861c-ae038b712a6f"></a>

[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed service that offers a choice of industry leading foundation models (FMs) along with a broad set of capabilities that you need to build generative AI applications and agents. Amazon Bedrock provides foundation model access, model customization, agent development, safety controls, and cost optimization — all behind a unified API. Since Amazon Bedrock is serverless, you don't have to manage any infrastructure, and you can securely integrate and deploy generative AI capabilities directly into your applications.

### Infrastructure management
<a name="infrastructure-management.eddcadcb-1c60-5195-9de8-eb39dfd4c08a"></a>

AWS manages the complete infrastructure lifecycle, including provisioning, scaling, and maintenance. This capability allows teams to focus on application development.

### Pricing model
<a name="pricing-model.ea0604fd-cdba-597a-ac27-01fba17b3cd7"></a>

Amazon Bedrock offers flexible pricing based on API consumption. Organizations pay for input and output tokens processed during on-demand usage, or they can use and scale [imported FMs](https://docs.aws.amazon.com/bedrock/latest/userguide/import-pre-trained-model.html) measured in capacity units.

Bedrock exposes four inference [service tiers](https://aws.amazon.com/bedrock/service-tiers/) — **Reserved**, **Priority**, **Standard**, and **Flex** — that let a workload trade off availability, latency, and cost without changing models or APIs. Three of them (Priority, Standard, Flex) are on-demand and share a single per-model quota; tier selection is just a request-time parameter. The fourth (Reserved) is a separate pool with its own SLA and minimum commitment. This sits alongside Bedrock's other capacity controls — [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) for custom and imported models, [batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html), and [cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) — and is usually the first lever to reach for on shared on-demand models.

### Model architecture support
<a name="model-architecture-support.4b71f944-969b-5a53-bb9e-5838e98d1cad"></a>

Amazon Bedrock provides access to hundreds of foundation models from leading AI companies. The catalog includes models from providers including OpenAI, Anthropic, Amazon, Meta, Mistral, and others. See [Bedrock Models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html).

Beyond pre-built models, Bedrock supports:
+ **Agent development**: Amazon Bedrock AgentCore is the end-to-end platform for building, connecting, and optimizing agents. Framework-agnostic and model-agnostic; no infrastructure management. Bedrock Managed Agents (powered by OpenAI for frontier models) are also available.
+ **Customization**: Knowledge Bases for RAG, Bedrock Data Automation for unstructured content, prompt engineering, fine-tuning.

### Automatic scaling
<a name="automatic-scaling.f3fb03ef-4120-5b4d-b8fe-8d524d1d1b72"></a>

AWS automatically adjusts capacity based on demand patterns, which helps to provide consistent performance during traffic fluctuations.

### Inference engine choice
<a name="inference-engine-choice.523bb073-3252-5a12-8d55-39b49c1a3df9"></a>

Amazon Bedrock provides a fully managed inference engine optimized for the supported model architectures, with AWS handling all engine configuration and optimization.

### Inference optimizations and configurations
<a name="inference-optimizations-and-configurations.b23e4d8d-fdf2-5f1e-b5cb-591dab87de73"></a>

You can control model behavior through model-specific request [parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-parameters.html). This capability allows customization of generation characteristics such as temperature, top-p sampling, and maximum token length for each inference request.

**Inference Features**

These features are available across the inference APIs:
+ **Structured output**: validated JSON results.
+ **Model reasoning**: extended thinking (where the model supports it).
+ **Inference parameters**: temperature, top-p, max tokens, and other model-specific knobs.
+ **Service tier selection**: `service_tier` request parameter accepting reserved, priority, default, or flex. Selects the capacity pool that serves the request. Resolved tier is reported back on the response, in CloudTrail, and as the ResolvedServiceTier CloudWatch dimension.

**Cost Optimization**
+ **Intelligent Prompt Routing**: automatically route to the most cost-effective model that meets quality requirements.
+ **Prompt caching**: reduce cost by reusing cached prompt prefixes.
+ **Real-time and batch processing**: choose the processing mode that fits the latency and cost requirements.
+ [**Advanced Prompt Optimization**](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompt-optimization-how.html): optimize prompts for any model on Amazon Bedrock, while comparing your original prompts to optimized prompts across up to 5 models simultaneously.

**Guardrails**

[Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) is the safeguard layer that provides six configurable filter types that operate on inputs, outputs, or both. Guardrails can block up to 88% of harmful content, and the Automated Reasoning checks can identify correct responses with up to 99% accuracy. Guardrails can be applied during a regular inference call or invoked independently via the ApplyGuardrail API to protect non-Bedrock model traffic.

### Supported clients and protocols
<a name="supported-clients-and-protocols.ef3c13af-adab-5093-905c-933cad4d3bdd"></a>

Applications can access models in Amazon Bedrock through the [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html), [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) API. Applications can also connect to Amazon Bedrock via model provider specific APIs [Responses API](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-mantle.html), Chat Completions API or [Messages API](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-messages-api.html). Further integration using the [AWS SDK](https://aws.amazon.com/what-is/sdk/) is also possible. These approaches provide straightforward integration paths for various application architectures. You can also use third-party open source libraries like [Strands Agents](https://strandsagents.com/docs/user-guide/concepts/model-providers/amazon-bedrock/) or [Crew AI](https://docs.crewai.com/en/concepts/llms#aws-bedrock) to interact with Amazon Bedrock. You can also integrate third-party applications like Claude Code and CoWork from Anthropic or Codex from OpenAI.

**Bedrock Endpoints**

Bedrock exposes inference through two endpoints:
+ **bedrock-mantle**: OpenAI Responses API, Anthropic Messages API.
+ **bedrock-runtime**: Invoke API, Converse API.

Additional features available across endpoints: structured output (validated JSON), model reasoning (extended thinking), latency-optimized inference, and standard inference parameters (temperature, top-p, max tokens).

#### Amazon Bedrock — Inference APIs
<a name="inference-ap-is"></a>

##### Bedrock exposes inference through two endpoints:
<a name="bedrock-exposes-inference-through-two-endpoints-.6cfd8b74-ad99-52c4-bb61-435181a5b127"></a>
+ **bedrock-mantle** — OpenAI Responses API, Anthropic Messages API.
+ **bedrock-runtime** — Invoke API, Converse API.

Additional features available across endpoints: structured output (validated JSON), model reasoning (extended thinking), latency-optimized inference, and standard inference parameters (temperature, top-p, max tokens).

##### API Summary
<a name="api-summary.dd979d73-52f6-5a13-a14e-9449da260d0d"></a>

|
|
| API | Endpoint | Shape |
| --- |--- |--- |
| Responses API | bedrock-mantle | OpenAI Responses |
| Chat Completions API | bedrock-runtime | OpenAI Chat Completions |
| Messages API | bedrock-mantle | Anthropic Messages |
| Invoke API | bedrock-runtime | Bedrock-native |
| Converse API | bedrock-runtime | Bedrock-native, model-agnostic |

##### Client and Tooling Compatibility
<a name="client-and-tooling-compatibility.9325670d-56fb-5b8f-adaf-1265106602a5"></a>

Because Bedrock exposes the OpenAI Responses and Anthropic Messages wire formats on the Mantle endpoint — alongside the native Converse and Invoke APIs on bedrock-runtime — many existing developer tools can route their inference through Bedrock with a configuration change rather than a code change. The qualifier matters: the client has to let you set the base URL (or have explicit Bedrock support) and accept Bedrock-issued credentials.

The operational consequence is what matters for procurement and security review: regardless of which API surface a client speaks, requests authenticate via *IAM*, can be reached over PrivateLink/VPC endpoints, are logged in CloudTrail, and are billed through the AWS account. Existing AWS controls — KMS, SCPs, Cost Explorer, Config — apply unchanged.

What this is **not**: Bedrock is not a drop-in replacement for OpenAI's or Anthropic's first-party APIs in every case. Feature-level coverage varies by model and by API (extended thinking, *service tiers*, structured output, prompt caching all have model-specific support matrices), and provider-specific endpoints outside the Responses / Chat Completions / Messages set are not part of the Bedrock surface. Validate the specific feature set your client depends on before migrating production traffic.

##### Inference Features
<a name="inference-features.196e93f2-d832-5bd9-9b34-0da2c664cdfe"></a>

These features are available across the inference APIs:
+ **Structured output** — validated JSON results.
+ **Model reasoning** — extended thinking (where the model supports it).
+ **Latency-optimized inference** — for time-critical workloads.
+ **Inference parameters** — temperature, top-p, max tokens, and other model-specific knobs.
+ **Service tier selection** — `service_tier` request parameter accepting reserved, priority, default, or flex. Selects the capacity pool that serves the request. Resolved tier is reported back on the response, in CloudTrail, and as the ResolvedServiceTier CloudWatch dimension.

#### Amazon Bedrock — Cross-Region Inference (CRIS)
<a name="cross-region-inference"></a>

##### Overview
<a name="overview.2ac8ab84-1dac-5a25-9f54-cb6510318852"></a>

Cross-region inference (CRIS) profiles let Bedrock route requests across AWS Regions to improve throughput. Two profile types — Geographic (within US/EU/APAC boundaries) and Global (any commercial Region) — trade data residency for cost and capacity. There is no additional routing cost; pricing follows the source Region.

##### Profile Types
<a name="profile-types.a019e9ba-aa8b-54c1-9d50-4dfc08df0f97"></a>

|
|
| Feature | Geographic | Global |
| --- |--- |--- |
| **Data residency** | Within geographic boundaries (US, EU, APAC) | Any supported AWS commercial Region worldwide |
| **Throughput** | Higher than single-region | Highest available |
| **Cost** | Standard pricing | \~10% savings vs. single-region |
| **Best suited for** | Organizations with data-residency regulations | Organizations prioritizing cost and performance |

##### Operational Details
<a name="operational-details.ec014e2f-76d2-5533-8b4c-d0e2a1993d8d"></a>
+ **No routing cost** — the request is priced based on the Region from which the inference profile is called.
+ **Account-level Region enablement is not required for routed Regions** — cross-region inference can route to Regions that have not been manually enabled in your account.
+ **Network path** — all data transmitted during cross-Region operations remains on the AWS network. Traffic never traverses the public internet.
+ **Encryption in transit** — data is encrypted between AWS Regions.
+ **CloudTrail logging** — all cross-Region inference requests are logged in CloudTrail in your source Region. The additionalEventData.inferenceRegion field shows where each request was actually processed.
+ **Provisioned Throughput** — not currently supported through inference profiles.

#### Amazon Bedrock — Guardrails
<a name="amazon-bedrock-guardrails"></a>

##### Overview
<a name="overview.4180fcdc-a23b-5127-932d-53bf8bf0a338"></a>

[Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) is the technical-safeguard layer that AWS Prescriptive Guidance recommends as part of an RAI program. It provides six configurable filter types that operate on inputs, outputs, or both. Guardrails can block up to 88% of harmful content, and the Automated Reasoning checks can identify correct responses with up to 99% accuracy. Guardrails can be applied during a regular inference call or invoked independently via the ApplyGuardrail API to protect non-Bedrock model traffic.

##### Six Filter Types
<a name="six-filter-types.4c5cdb5f-99ab-5577-8557-f7a434696637"></a>

##### 1. Content Filters
<a name="1.-content-filters.4d29d57d-6f22-5c64-8212-008e3405274b"></a>

Detect and filter harmful text or image content in inputs or responses.
+ **Predefined categories**: Hate, Insults, Sexual, Violence, Misconduct, Prompt Attack.
+ **Configurable filter strength** per category.

**Two tiers**:
+ **Classic** — base coverage.
+ **Standard** — extends detection to code elements (comments, variable and function names, string literals).

##### 2. Denied Topics
<a name="2.-denied-topics.83753799-08e0-53af-8126-c8cfff5a9c85"></a>

Define topics that are off-limits for the application. Blocks them in user queries or model responses. The Standard tier extends detection to code elements.

##### 3. Word Filters
<a name="3.-word-filters.adfe6cc6-99af-5641-a2da-36878049ee81"></a>

Block specific custom words or phrases (exact match). Includes a ready-to-use profanity option and supports custom word lists (e.g., competitor names).

##### 4. Sensitive Information Filters
<a name="4.-sensitive-information-filters.a9b2c363-c8ce-52a0-9e4e-9289d48e0861"></a>

Block or mask PII and sensitive data (SSN, date of birth, address, etc.). Detection is probabilistic. Custom regex patterns supported for organization-specific PII.

##### 5. Contextual Grounding Checks
<a name="5.-contextual-grounding-checks.e511a9fd-a055-5484-86f7-fe6e24bfaa00"></a>

Detect hallucinations in model responses that are not grounded in the provided source or are irrelevant to the user's query. Particularly useful for Retrieval Augmented Generation (RAG) applications.

##### 6. Automated Reasoning Checks
<a name="6.-automated-reasoning-checks.276da054-4a72-5930-89dc-3772af44c0bf"></a>

Validate the accuracy of FM responses against a set of logical rules. Can detect hallucinations, suggest corrections, and highlight unstated assumptions. Up to 99% accuracy for correct responses.

##### Customization
<a name="customization.99184733-e989-5884-bd27-d20b1020f0af"></a>

Customize the messages returned to users when a filter is violated.

##### Usage Patterns
<a name="usage-patterns.cfcbe732-6c20-5c75-8705-83c99aae24b9"></a>

Two ways to apply Guardrails:
+  **Inline during inference** — specify guardrail ID and version on the inference API call.
+ **Standalone** — call the ApplyGuardrail API independently, without invoking a foundation model. Useful for protecting non-Bedrock model traffic or running guardrails on cached content.

For RAG and conversational applications, you can selectively evaluate only certain sections of the input prompt using tags.

##### Where Guardrails Fit in RAI
<a name="where-guardrails-fit-in-rai.cd9ba72c-6af2-5a2c-9faa-fed77aa58e9e"></a>

Guardrails maps to the **technical safeguards** layer of the AWS Prescriptive Guidance RAI playbook (input validation, output filtering, PII sanitization). It complements but does not replace *model assessment, documentation, governance, and access controls*.

#### Amazon Bedrock — Service Tiers and Reservations
<a name="amazon-bedrock-service-tiers-and-reservations"></a>

##### Overview
<a name="overview.ad344b35-5d81-505a-a091-00679274f0b4"></a>

Bedrock exposes four inference [service tiers](https://aws.amazon.com/bedrock/service-tiers/) — **Reserved**, **Priority**, **Standard**, and **Flex** — that let a workload trade off availability, latency, and cost without changing models or APIs. Three of them (Priority, Standard, Flex) are on-demand and share a single per-model quota; tier selection is just a request-time parameter. The fourth (Reserved) is a separate pool with its own SLA and minimum commitment. This sits alongside Bedrock's other capacity controls — *Provisioned Throughput* for custom and imported models, *batch inference*, and *cross-region inference* — and is usually the first lever to reach for on shared on-demand models.

##### The Four Tiers
<a name="the-four-tiers.20dcd6dd-afed-5e4d-99de-748bbfc6d01f"></a>

|
|
| Tier | Reservation | Pricing model | Best for |
| --- |--- |--- |--- |
| **Reserved** | Pre-purchased | Fixed $/1K TPM, billed monthly, 1- or 3-month term | Mission-critical, steady, high-volume workloads that can't tolerate downtime |
| **Priority** | None | Premium over on-demand | Latency-sensitive customer-facing flows that don't justify 24x7 reservation |
| **Standard** | None | Standard on-demand | Default for everyday production traffic |
| **Flex** | None | Discounted on-demand | Tolerant of longer processing times — evaluations, summarization, agentic workflows |

##### Reserved Tier
<a name="reserved-tier.f721460a-131f-5e20-9ee9-8906ed049415"></a>

Pre-purchased capacity with a 99.5% uptime target. You separately size input and output tokens-per-minute (TPM) to match the workload, controlling cost without overprovisioning. Minimum reservations:
+ **Input TPM**: 100,000
+ **Output TPM**: 10,000

When demand exceeds the reservation, requests automatically **overflow to the Standard tier**, so applications keep running rather than getting throttled. Commitment terms are 1 month or 3 months, billed monthly at a fixed $/1K TPM. Access is gated — contact your AWS account team to enable it.

##### Priority Tier
<a name="priority-tier.c44e51e0-75c6-5bab-bc51-7638282fab74"></a>

Fastest response times at a per-token premium over Standard on-demand. No reservation required. Set `"service_tier": "priority"` on the request and that call jumps to the front of the on-demand queue, ahead of Standard and Flex traffic. Use it for the customer-facing path; pair with Flex for background jobs in the same application to balance the bill.

##### Standard Tier
<a name="standard-tier.49f63721-daf4-5d41-92e6-c76263a42d90"></a>

The default. Consistent performance for content generation, analysis, and routine document workloads. If service\_tier is omitted, requests resolve to Standard. You can also explicitly set `"service_tier": "default"`.

##### Flex Tier
<a name="flex-tier.20e36d4b-07eb-5685-abc3-f766bd923e01"></a>

Discounted on-demand pricing in exchange for tolerating longer processing times. Aligned with the docs' guidance, the right candidates are model evaluations, content summarization, and agentic workflows where extra seconds don't change the outcome. Set `"service_tier": "flex"` on the request.

##### How Tier Selection Works
<a name="how-tier-selection-works.212bbf84-6cd4-583a-8790-e1d9f54f83d5"></a>

Tier is a per-request parameter on the runtime API:

`"service_tier" : "reserved | priority | default | flex"`

**Observability:**
+ The chosen and resolved tier appear on the API response and in CloudTrail events.
+ CloudWatch Metrics expose ModelId, ServiceTier, and ResolvedServiceTier. ResolvedServiceTier reflects what actually served the request — useful when reservations overflow to Standard, or when the requested tier isn't supported by a given model.
+ Tier support is per-model; check the Models at a glance page for each model's supported tiers.
+  IAM policies can restrict which tiers a principal can request.
