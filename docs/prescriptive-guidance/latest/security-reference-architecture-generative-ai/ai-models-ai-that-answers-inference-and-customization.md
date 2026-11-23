---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/ai-models-ai-that-answers-inference-and-customization.html
---

# AI Models (AI that answers) : inference and customization

Model inference sends a request to a model and returns its output. The AWS AI Security Framework describes this capability as **AI that answers**.

![AWS SRA of AI Security AWS OU and account structure with AWS service reference - Model Inference](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/images/guide-img/a349f18f-a9fd-43a3-9a48-27534bf6412a/images/bf08bcf4-e6f5-451c-85a5-9474318c7455.png)

Fig 3: ***AWS SRA of AI Security AWS OU and account structure with AWS service reference - Model Inference***

Choose your hosting path below. Add training controls when you train or customize a model.

|
|
| **Your model path** | **Start here** | **Add when needed** |
| --- |--- |--- |
| [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/endpoints.html) managed inference | [Bedrock model access](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/#amazon-bedrock-protect-managed-model-access) and [inference guardrails](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/#amazon-bedrock-configure-and-test-inference-guardrails) | [Bedrock customization](https://dp8l2mfblnx2f.cloudfront.net/answers/model-customization/#amazon-bedrock-isolate-managed-customization-jobs) if you adapt a model |
| [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-options.html) hosted inference | [SageMaker endpoints](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/#amazon-sagemaker-ai-protect-hosted-endpoints) and [input and output checks](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/#amazon-sagemaker-ai-integrate-input-and-output-checks) | [SageMaker training](https://dp8l2mfblnx2f.cloudfront.net/answers/model-customization/#amazon-sagemaker-ai-isolate-training-environments) if you train or adapt a model |
| A model on compute you operate | [Self-hosted compute controls](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/#shared-application-and-self-hosted-compute-controls) | Training and artifact controls for the components you operate |

Apply [application access controls](https://dp8l2mfblnx2f.cloudfront.net/answers/ai-applications/) to users, sessions, and results on each path.

## Security considerations
<a name="security-considerations"></a>
+ Broad invocation permissions can expose unapproved models and processing Regions.
+ Public or alternate API paths can bypass required network and content controls.
+ Retained prompts, responses, training data, and model artifacts can expose protected information.
+ Unauthorized inputs and unsafe model output can affect downstream application behavior.

Configure and test [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) on the model request paths that need content safeguards. An application that uses Amazon SageMaker AI must integrate guardrails explicitly through the [ApplyGuardrail API](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html).

## Design Consideration
<a name="design-consideration"></a>

Apply [data and knowledge bases](https://apg-library.amazonaws.com/edit/a349f18f-a9fd-43a3-9a48-27534bf6412a#contents?section=knowledge-bases-ai-that-connects) for retrieval and [agentic AI](https://apg-library.amazonaws.com/edit/a349f18f-a9fd-43a3-9a48-27534bf6412a#contents?section=agentic-ai-and-actions-ai-that-acts) for agent tool use, including read-only tools.
