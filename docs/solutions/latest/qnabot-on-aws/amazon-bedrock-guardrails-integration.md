---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/amazon-bedrock-guardrails-integration.html
---

# Amazon Bedrock Guardrails Integration
<a name="amazon-bedrock-guardrails-integration"></a>

QnABot on AWS implements a comprehensive guardrail system that includes preprocessing, LLM integration, and postprocessing guardrails. This multi-layer approach provides enhanced content control and broader security for your chatbot application.

## Multi-Layer Guardrail System
<a name="multi-layer-guardrail-system"></a>

QnABot on AWS implements a comprehensive guardrail system that includes three distinct layers of protection:
+  **Preprocessing Guardrail**: Validate and block harmful inputs before they are processed by the QnABot application
+  **Bedrock LLM Guardrail**: Control model behavior during inference using Amazon Bedrock’s guardrail system
+  **Postprocessing Guardrail**: Filter and validate final responses before delivering to the chat user

This multi-layer approach provides enhanced content control and comprehensive security for your chatbot application. Each optional layer can be configured independently using different guardrails:
+  **Preprocessing**: Configure input validation rules, prompt attack and PII detection
+  **Bedrock LLM Guardrail**: Apply pre-configured Bedrock Guardrail Identifier and Version
+  **Postprocessing**: Set up response filtering and content moderation rules

The system leverages Amazon Bedrock’s [Guardrails](https://aws.amazon.com/bedrock/guardrails/) capabilities while extending protection to both incoming and outgoing content, increasing end-to-end conversation safety and reliability. To learn more about Guardrails for Amazon Bedrock, please see [How Guardrails for Amazon Bedrock works](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html).

## Key Benefits
<a name="key-benefits"></a>

### Security & Control
<a name="security-control"></a>
+  **Comprehensive Protection**: Multi-layer security across all flows
+  **Flexible Configuration**: Independent, customizable guardrails and policies
+  **PII Protection**: Multiple security checkpoints
+  **Content Control**: Fine-grained input, output and LLM inference control

### Performance & Cost
<a name="performance-cost"></a>
+  **Early Filtering**: Blocks harmful content before processing for embeddings, LLM and chat history storage
+  **Efficient Processing**:
  + Pre-process Guardrail: Initial question/utterance screening
  + Bedrock Guardrail: Only invoked for LLM requests
  + Post-process Guardrail: Final response validation
+  **Cost Control**: Ability to customize guardrail policies at each layer and reduces token usage

### Operations
<a name="operations"></a>
+  **Coverage**: Supports LLM and non-LLM flows
+  **Monitoring**: Logs guardrail response in Fulfillment Lambda logs and records answer source OpenSearch Dashboards

## Comparison
<a name="comparison"></a>

| Feature | Pre-process Guardrail | Bedrock LLM Guardrail | Post-process Guardrail |
| --- | --- | --- | --- |
| Guard Scope | Before processing user’s input (First) *Applies to all flows*  | During LLM response generation *LLM flows only*  | After processing response (Last) *Applies to all flows*  |
| Focus | User Input Protection | LLM Inference Control | Response Sanitization |
| Capabilities | \* Prompt Attack Prevention \* PII Rejection \* Content Filtering \* Profanity and Word Filtering \* Denied Topics | \* Contextual Grounding \* Relevance Check \* Content Filtering \* Profanity and Word Filtering \* Denied Topics | \* PII Redaction and Rejection \* Content Filtering \* Profanity and Word Filtering \* Denied Topics |
| Actions | BLOCK | BLOCK, MASK (PII) | BLOCK, MASK (PII) |
| Blocked Response | Guardrail Blocked Message | Guardrail Blocked Message *Can be overriden using LLM\_NO\_HITS\_REGEX*  | Guardrail Blocked Message |
| API Integration | ApplyGuardrail *All request types*  | \* Converse \* ConverseStream \* RetrieveGenerate \* RetrieveAndGenerateStream *LLM requests only*  | ApplyGuardrail *All response types*  |

### Guardrails for Amazon Bedrock Quick Setup:
<a name="guardrails-for-amazon-bedrock-quick-setup"></a>

1. Prerequisites for using guardrails:

   1. Please verify [supported regions for Guardrails for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-supported.html).

   1. If using guardrails for Bedrock LLM and KnowledgeBase Integration:
      + The provided guardrail identifier and version will be applied to the requests made to the models specified in `LLMBedrockModelId` and `BedrockKnowledgeBaseModel`. Please verify the models you have specified in cloudformation parameter `LLMBedrockModelId` and `BedrockKnowledgeBaseModel` are [supported models for Guardrails for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-supported.html)
      + Please verify the models you have specified [have access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) for the same models in Bedrock console.

1. Create a Guardrail using Amazon Bedrock console in your AWS account:

   1. To configure QnABot to use Guardrails for Amazon Bedrock, you will first need to [create a guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html). Below is a quick step by step guide to get started:
      + Step 1: Provide guardrail details : ** *TIP:* ** For Bedrock Guardrails, you can leave the default message unchanged `Sorry, the model cannot answer this question` as it is a pattern defined in `LLM_QA_NO_HITS_REGEX`. When a Guardrail has intervened, QnaBot will respond with ([Custom Don’t Know](https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/using-keyword-filters-for.html#custom-dont-know-answers)) answers that you have defined, similar to when QnABot can’t find an answer. For pre-processing and post-processing guardrails, the default message from Amazon Bedrock Guardrail will be processed.

**Provide Guardrail detail**
 ![provide guardrail detail](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/provide_guardrail_detail.png)
      + Step 2: Configure content filters (optional) - Configure content filters by adjusting the degree of filtering to detect and block harmful user inputs and model responses that violate your usage policies.

**Note**
Please carefully note the strength of each of these filters. When they are low, content classified as harmful with HIGH confidence will be blocked while content classified as harmful with NONE, LOW, or MEDIUM confidence will be allowed. Please adjust the filters as per your requirements.

**Content filters**
 ![content filters](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/content_filters.png)
+ Step 3: Add denied topics (optional)
+ Step 4: Add word filters (optional)
+ Step 5: Add sensitive information filters (optional)
+ Step 6: Contextual grounding check (optional) - From 7.0.0 of QnABot, this feature is supported only for Bedrock Guardrails and shouldn’t be configured for pre-processing and post-processing guardrails.
+ Step 7: Review and create guardrail

  1. Once you have created a guardrail, you can test it with your testing data. After you have tested the guardrail, you can create a version. Once you have a version created, you can copy it and alongwith ID shown in the below screenshot. .Test Guardrail ![test guardrail](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/test_guardrail.png)

     1. Input the Guardrail configured in the previous section into the Content Designer’s settings page:

Finally, input the copied ID and the copied version number from section B.2 in the QnaBot Content Designer settings : Amazon Bedrock Guardrails Integration fields. To do this navigate to the Content Designer - select the tools menu ( ☰ ) in top left corner, then select Settings - General Settings - Text Generation using LLMs - General Settings and update the settings as shown in the below screenshot. Then click Save.

**Update settings**
 ![update settings](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/update_settings.png)

### Settings for Guardrail in QnABot on AWS:
<a name="settings-for-guardrail-in-qnabot-on-aws"></a>

Below are the available settings to configure Guardrail in the Content Designer’s settings page.
+  **BEDROCK\_GUARDRAIL\_IDENTIFIER:** Enter a pre-configured Amazon Bedrock Guardrail Identifier (e.g. 4ojm24q0yada) that you want to be applied to the requests made to the LLM models configured in the CloudFormation parameters `LLMBedrockModelId` and `BedrockKnowledgeBaseModel`. If you don’t provide a value, no guardrail is applied to the LLM invocation. If you provide a guardrail identifier, you must also provide a `BEDROCK_GUARDRAIL_VERSION` otherwise no guardrail will be applied.
+  **BEDROCK\_GUARDRAIL\_VERSION:** Enter the version (e.g. 1 or DRAFT) of the Bedrock Guardrail specified in `BEDROCK_GUARDRAIL_IDENTIFIER`.
+  **PREPROCESS\_GUARDRAIL\_IDENTIFIER:** Enter a pre-configured Amazon Bedrock Guardrail Identifier (e.g. 4ojm24q0yada) that you want to be applied to the input query to block harmful content or detected PII entities before pre-processing (PREPROCESS) user’s utterance in the fulfillment. If you don’t provide a value, no guardrail is applied in the preprocessing step. If you provide a identifier, you must also provide a `PREPROCESS_GUARDRAIL_VERSION`.
+  **PREPROCESS\_GUARDRAIL\_VERSION:** Enter the version (e.g. 1 or DRAFT) of the Bedrock Guardrail specified in `PREPROCESS_GUARDRAIL_IDENTIFIER`.
+  **POSTPROCESS\_GUARDRAIL\_IDENTIFIER:** Enter a pre-configured Amazon Bedrock Guardrail Identifier (e.g. 4ojm24q0yada) that you want to be applied to the final answer after processing of the user’s utterance has completed in the post-processing (POSTPROCESS) step of fulfillment. If you don’t provide a value, no guardrail is applied in the postprocessing step. If you provide a identifier, you must also provide a `POSTPROCESS_GUARDRAIL_VERSION`.
+  **POSTPROCESS\_GUARDRAIL\_VERSION:** Enter the version (e.g. 1 or DRAFT) of the Bedrock Guardrail specified in `POSTPROCESS_GUARDRAIL_IDENTIFIER`.
