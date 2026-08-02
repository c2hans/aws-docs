---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/text-generation-and-query-disambiguation-using-llms.html
---

# Text generation and query disambiguation using LLMs
<a name="text-generation-and-query-disambiguation-using-llms"></a>

**Note**
These are optional features available as of v5.4.0. We encourage you to try it out on non-production instances initially to validate expected accuracy improvements and to test for any regression issues. See the [Cost](cost.md) section to see estimates of how these features affect pricing.

QnABot on AWS can leverage LLMs to provide a richer, more conversational chat experience. The goal of these features is to minimize the amount of individually curated answers administrators are required to maintain, to improve question matching accuracy by providing query disambiguation, and to enable the solution to provide more concise answers to users, especially when using the Amazon Bedrock knowledge base or [Amazon Kendra fallback features](integrating-amazon-kendra.md).

These benefits are provided through these primary features:
+  **Text Generation**
  +  **Generate answers to questions from text passages** - In the content designer web interface, administrators can store full text passages for QnABot on AWS to use. When a question gets asked that matches against this passage, the solution can leverage LLMs to answer the user’s question based on information found within the passage.
  +  **Retrieval augmentation generation (RAG) from your data sources** - By integrating with the Amazon Bedrock knowledge base or Amazon Kendra index, QnABot on AWS can use an LLMs to generate concise answers to user’s questions from your data source. This prevents the need for users to sift through larger text passages to find the answer.
+  **Query Disambiguation** - By leveraging an LLM, QnABot can take the user’s chat history and generate a standalone question for the current utterance. This enables users to ask follow up questions which on their own may not be answerable without context of the conversation.

**Note**
The ability to answer follow up questions is similar to what [QnABot Topics](using-topics-to-support-follow-up-questions-and-contextual-user-journeys.md) aims to solve. Consider that as an option if you’re unable to use the LLM features.

These features (together with [embeddings](semantic-question-matching-using-text-embeddings-llm.md)) enable QnABot on AWS to serve end users with a more conversational chat experience using various AI and NLP techniques. To enable the use of these features, you must deploy the solution with the LLM selection of your choice. You can choose to use any of the following LLM providers:
+ Select LLM models or inference profiles provided by Amazon Bedrock and specify your Amazon Bedrock Knowledge Base ID (preferred)
+ Any other LLM model through a user provided custom Lambda function

**Note**
By choosing to use the generative responses features, you acknowledge that QnABot on AWS engages third-party generative AI models that AWS does not own or otherwise has any control over ("Third-Party Generative AI Models"). Your use of the Third-Party Generative AI Models is governed by the terms provided to you by the Third-Party Generative AI Model providers when you acquired your license to use them (for example, their terms of service, license agreement, acceptable use policy, and privacy policy).
You are responsible for ensuring that your use of the Third-Party Generative AI Models comply with the terms governing them, and any laws, rules, regulations, policies, or standards that apply to you.
You are also responsible for making your own independent assessment of the Third-Party Generative AI Models that you use, including their outputs and how Third-Party Generative AI Model providers use any data that may be transmitted to them based on your deployment configuration.
AWS does not make any representations, warranties, or guarantees regarding the Third-Party Generative AI Models, which are "Third-Party Content" under your agreement with AWS. QnABot on AWS is offered to you as "AWS Content" under your agreement with AWS.

## Enabling LLM support
<a name="enabling-llm-support"></a>

### Amazon Bedrock (preferred)
<a name="amazon-bedrock-preferred"></a>

**Note**
Cross-region inference profiles are not supported when deploying QnABot via VPC template
Access to all Amazon Bedrock foundation models is enabled by default. However selecting Anthropic models requires customer to submit use case details [once per account](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) in the Amazon Bedrock console.

Utilizes one of the Amazon Bedrock foundation models or inference profiles to generate text. QnABot supports any valid Bedrock foundation model ID or inference profile ID. For the complete list of supported models and their availability by region, see:
+  [Bedrock Supported Foundation Models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)
+  [Bedrock Inference Profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)

**Note**
Access to all Amazon Bedrock foundation models is enabled by default. However selecting Anthropic models requires customer to submit use case details [once per account](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) in the Amazon Bedrock console.

 **Configuring Amazon Bedrock**

From the CloudFormation console, set the following parameters:
+ Set **LLMApi** to `BEDROCK`.
+ Set **LLMBedrockModelId** to a valid Amazon Bedrock model ID or inference profile ID.

 **QnABot on AWS Amazon Bedrock models.**

![image32](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image32.png)

### Using a custom Lambda Function
<a name="using-a-custom-lambda-function-1"></a>

If the pre-built options don’t work for your use case, or you want to experiment with other LLMs, you can build a custom Lambda function to integrate with the LLM of your choice. The provided Lambda function takes as input the prompt, model parameters, and the QnABot settings object. Your Lambda function can invoke any LLM you choose, and return the prediction in a JSON object containing the key **generated\_text**. You provide the ARN for your Lambda function when you deploy or update the solution.

**Note**
If integrating your Lambda with external resources, evaluate the security implications of sharing data outside of AWS.

To deploy the stack using a custom Lambda function:
+ Set **LLMApi** to `LAMBDA` **0**
+ Set **LLMLambdaArn** to the ARN of your Lambda function.
+ If using the Amazon Kendra fallback:
  + Set the **AltSearchAmazon KendraIndexes** CloudFormation parameter to the index ID of your existing Amazon Kendra index containing ingested documents.
+ If using text passages:
  + Enable text embeddings by setting **EmbeddingsApi** to the mechanism of your choice. For options, see [Semantic question matching using text embeddings LLM](semantic-question-matching-using-text-embeddings-llm.md).

 **LLM LAMBDA integration**

![image34](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image34.png)

Your Lambda function is passed as an event:

```
{
  // prompt for the LLM
  "prompt": "string",

  // object containing key/value pairs for the model parameters
  // these parameters are defined on the QnABot settings page
  "parameters":{"temperature":0,...},

  // settings object containing all default and custom QnAbot settings
  "settings":{"key1":"value1",...}
}
```

The Lambda function returns a JSON structure:

```
{"generated_text":"string"}
```

An example of a minimal Lambda function for testing, which you must extend to invoke your LLM:

```
def lambda_handler(event, context):
    print(event)
    prompt = event["prompt"]
    model_params = event["parameters"]
    settings = event["settings"]

    # REPLACE BELOW WITH YOUR LLM INFERENCE API CALL
    generated_text = f"This is the prompt: {prompt}"

    return {
        'generated_text': generated_text
    }
```

## Query disambiguation and conversation retrieval
<a name="query-disambiguation-and-conversation-retrieval"></a>

Query disambiguation is the process of taking an *ambiguous* question (having multiple meanings) and transforming it into an unambiguous, standalone question.

The new disambiguated question can then be used as a search query to retrieve the best FAQ, passage, or Amazon Kendra match.

For example, with the new LLM disambiguation feature enabled, given the chat history context:

```
[{"Human":"Who was Little Bo Peep?"},{"AI":"She is a character from a nursery rhyme who lost her sheep."}]
```

A follow up question:

```
Did she find them again?
```

The solution can rewrite (" *disambiguate* ") that question to provide all the context required to search for the relevant FAQ or passage:

```
Did Little Bo Peep find her sheep again?
```

## Text generation for question answering
<a name="text-generation-for-question-answering"></a>

Generate answers to questions from context provided by Amazon Kendra search results, or from text passages created or imported directly into QnAbot. Some of the benefits include:
+ Generated answers allow you to reduce the number of FAQs you must maintain since you can now synthesize concise answers from your existing documents in an Amazon Kendra index, or from document passages stored in QnABot as **text** items.
+ Generated answers can be short, concise, and suitable for voice channel contact center bots and website and text bots.
+ Generated answers are compatible with the solution’s multi-language support - users can interact in their chosen languages and receive generated answers in the same language.
+ With QnABot you can use three different data sources to generate responses from:
  +  **Text passages within the content designer UI** - Create your own text passages to generate answers from using the content designer. We highly recommend you use this option with [Semantic question matching using text embeddings LLM](semantic-question-matching-using-text-embeddings-llm.md). It also requires an LLM. In the content designer, choose **Add**, select the text, enter an Item ID and a passage, and choose **Create**. You can also import your passages from a JSON file using the content designer **Import** feature. From the tools menu (☰), choose **Import**, open **Examples/Extensions**, and choose the **LOAD** button next to **TextPassage-NurseryRhymeExamples** to import two nursery rhyme text items.
  +  **Amazon Bedrock knowledge bases** - You can also create your own knowledge base from files stored in an S3 bucket. Amazon Bedrock knowledge bases do not require an LLM or embeddings model to function, since the embeddings and generative response are already provided by the knowledge base. Choose this option if you prefer not to manage and configure an Amazon Kendra index or LLM models. To enable this option, create an [Amazon Bedrock knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html) and copy your knowledge base ID into the **BedrockKnowledgeBaseId** CloudFormation parameter. For more information, please refer to [Retrieval Augmentation Generation (RAG) using Amazon Bedrock Knowledge Base](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/docs/bedrock_knowledgebase_rag/README.md). For more information, refer to [Retrieval Augmentation Generation (RAG) using Amazon Bedrock Knowledge Base.](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/docs/bedrock_knowledgebase_rag/README.md)
**Important**
If you want to enable S3 presigned URLs, S3 bucket names must start with `qna`, for example, `qnabot-mydocs`, otherwise make sure IAM Role **FulfillmentLambdaRole** has been granted **S3:GetObject** access to the Bedrock knowledge base bucket (otherwise the signed URLS will not have access). In addition, you can encrypt the transient messages using your own AWS KMS key; ensure that when creating the AWS KMS key that the IAM Role **FulfillmentLambdaRole** is a key user.
  +  **Amazon Kendra** - Generates responses from the webpages that you’ve crawled or documents that you’ve ingested using an Amazon Kendra data source connector. If you’re not sure how to load documents into Amazon Kendra, see [Ingesting Documents through the Amazon Kendra S3 Connector](https://catalog.us-east-1.prod.workshops.aws/workshops/df64824d-abbe-4b0d-8b31-8752bceabade/en-US/200-ingesting-documents/230-using-the-s3-connector/231-ingesting-documents) in the Amazon Kendra Essentials Workshop.
**Note**

    ```
    You can only use either Amazon Kendra or Amazon Bedrock knowledge bases as a fallback data source, and not both. When *AltSearchKendraIndexes* is not empty (an index is provided) Amazon Kendra will be the default data source even if a Bedrock knowledge base is configured.
    ```

For example, with these LLM QA features enabled, QnABot on AWS can answer questions from the AWS Whitepapers such as:
+  *"What is DynamoDB?"* → **Amazon’s Highly Available Key-value Store.**
+  *"What frameworks does AWS have to help people design good architectures?"* → **Well-Architected Framework.**

 **RAG based text generation using Amazon Kendra fallback.**

![image35](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image35.png)

It can even generate answers to yes or no questions, like:
+  *"Is Lambda a database service?"* → **No, Lambda is not a database service.**

  Likewise, it can also answer questions with Context and Signed URLs with Amazon Bedrock knowledge base, such as:
+  *"What services are available in AWS for container orchestration?"*
+  *"Are there any upfront fees with ECS?"*

   **RAG based text generation using Amazon Bedrock knowledge base.**
![image36](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image36.png)

Even if you aren’t using Amazon Kendra or Amazon Bedrock knowledge base, QnABot on AWS can answer questions based on passages created or imported into the content designer, such as:
+  *"Where did Humpty Dumpty sit?"* → **On the wall.**
+  *"Did Humpty Dumpty sit on the wall?"* → **Yes.**
+  *"Were the king’s horses able to fix Humpty Dumpty?"* → **No.**

all from a text passage item that contains the nursery rhyme.

 **LLM response from a passage within content designer UI.**

![image37](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image37.png)

You can use disambiguation and generative question answering together:

 **Disambiguation and generative question answering.**

![image38](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image38.png)

## Settings available for text generation LLMs configuration
<a name="settings-available-for-text-generation-llms-configuration"></a>

CloudFormation stack parameters:
+  **LLMApi** - Optionally enable QnABot on AWS question disambiguation and generative question answering using an LLM. Selecting the `LAMBDA` option allows for configuration with other LLMs.
+  **LLMBedrockModelId** - Required when **LLMApi** is `BEDROCK`. Ensure you have [requested access to the LLMs in Bedrock console](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html), before deploying.
+  **LLMLambdaArn** - Required if **LLMApi** is `LAMBDA`. Provide the ARN for a Lambda function that takes JSON `{"prompt":"string", "settings":{key:value,..}}` and returns JSON `{"generated_text":"string"}`.
+  **BedrockKnowledgeBaseId** - ID of an existing Amazon Bedrock knowledge base. This setting enables the use of Amazon Bedrock knowledge bases as a fallback mechanism when a match is not found in OpenSearch.
+  **BedrockKnowledgeBaseModel** - Required if **BedrockKnowledgeBaseId** is not empty. Sets the preferred LLM model to use with the Amazon Bedrock knowledge base. Ensure that you have requested access to the LLMs in the Amazon Bedrock console.
+  **AltSearchAmazon KendraIndexes** - Set to the ID (not the name) of your Amazon Kendra index where you have ingested documents of web pages that you want to use as source passages for generative answers. If you plan to use only text passage items instead of Amazon Kendra, leave this parameter blank.

**Note**
It is only possible to use Amazon Kendra or Amazon Bedrock knowledge bases as a fallback data source, and not both. When **AltSearchKendraIndexes** is not empty (an index is provided) Amazon Kendra will be the default data source even if a Amazon Bedrock knowledge base is configured.

When the QnABot stack is installed, open the content designer **Settings** page and configure the following settings:
+  **ENABLE\_DEBUG\_RESPONSES** - Set to `TRUE` to add additional debug information to the solution’s response, including any language translations (if using multi language mode), question disambiguation (before and after), and inference times for your LLM model(s).
+  **ES\_SCORE\_TEXT\_ITEM\_PASSAGES** - Should be `TRUE` to enable the new text passage items to be retrieved and used as input context for generative QA Summary answers.

**Note**
 `qna` items are queried first, and if none meet the score threshold, then the solution queries the text field of text items.
+  **EMBEDDINGS\_TEXT\_PASSAGE\_SCORE\_THRESHOLD** - Applies only when embeddings are enabled (recommended) and if **ES\_SCORE\_TEXT\_ITEM\_PASSAGES** is `TRUE`. If embedding similarity score on text item field is under threshold the match is rejected. Default threshold is 0.80.
+  **ALT\_SEARCH\_KENDRA\_MAX\_DOCUMENT\_COUNT** - The number of passages from Amazon Kendra to provide in the input context for the LLM.

Scroll to the bottom of the settings page and observe the new LLM settings:
+  **LLM\_API** - Set to `LAMBDA` - Based on the value chosen when you last deployed or updated the solution stack.
+  **LLM\_GENERATE\_QUERY\_ENABLE** - Set to `TRUE` or `FALSE` to enable or disable question disambiguation.
+  **LLM\_GENERATE\_QUERY\_PROMPT\_TEMPLATE** - The prompt template used to construct a prompt for the LLM to disambiguate a follow-up question. The template can use the following placeholders:
  +  `{history}` - Placeholder for the last **LLM\_CHAT\_HISTORY\_MAX\_MESSAGES** messages in the conversational history, to provide conversational context.
  +  `{input}` - Placeholder for the current user utterance or question.
+  **LLM\_GENERATE\_QUERY\_MODEL\_PARAMS** - Parameters sent to the LLM model when disambiguating follow-up questions. Default parameter: `{"temperature":0, "maxTokens":300, "topP":1}`. Check model documentation for additional values that your model provider accepts.
+  **LLM\_QA\_ENABLE** - Set to `TRUE` or `FALSE` to enable or disable generative answers from passages retrieved via embeddings or Amazon Kendra fallback (when no FAQ match is found).

**Note**
LLM based generative answers are not applied when an FAQ or QID matches the question.
+  **LLM\_QA\_PROMPT\_TEMPLATE** - The prompt template used to construct a prompt for the LLM to generate an answer from the context of a retrieved passage (from Amazon Kendra or embeddings). The template can use the following placeholders:
  +  `{context}` - Placeholder for passages retrieved from the search query - either a QnABot on AWS text item passage, or the top **ALT\_SEARCH\_KENDRA\_MAX\_DOCUMENT\_COUNT** Amazon Kendra passages.
  +  `{history}` - Placeholder for the last **LLM\_CHAT\_HISTORY\_MAX\_MESSAGES** messages in the conversational history, to provide conversational context.
  +  `{input}` - Placeholder for the current user utterance or question.
  +  `{query}` - Placeholder for the generated (disambiguated) query created by the generated query feature.
+  **LLM\_QA\_NO\_HITS\_REGEX** - When the pattern specified matches the response from the LLM. For example: *"Sorry, I don’t know"*, then the response is treated as no\_hits, and the default **EMPTYMESSAGE** or Custom Don’t Know (`no_hits`) item is returned instead. Disabled by default, since enabling it prevents easy debugging of LLM don’t know responses.
+  **LLM\_QA\_MODEL\_PARAMS** - Parameters sent to the LLM model when generating answers to questions. Default parameter: `{"temperature":0, "maxTokens":300, "topP":1}`. Check model documentation for additional values that your model provider accepts.
+  **LLM\_QA\_PREFIX\_MESSAGE** - Message use to prefix LLM generated answer. Can be empty.
+  **LLM\_QA\_SHOW\_CONTEXT\_TEXT** - Set to `TRUE` or `FALSE` to enable or disable inclusion of the passages (from Amazon Kendra or Embeddings) used as context for LLM generated answers.
+  **LLM\_QA\_SHOW\_SOURCE\_LINKS** - Set to `TRUE` or `FALSE` to enable or disable Amazon Kendra source links or passage refMarkdown links (doc references) in markdown answers.
+  **LLM\_CHAT\_HISTORY\_MAX\_MESSAGES** - The number of previous questions and answers (chat history) to maintain (in the DynamoDB `UserTable`). Chat history is necessary for the solution to disambiguate follow-up questions from previous question and answer context.
+  **KNOWLEDGE\_BASE\_PROMPT\_TEMPLATE** - The prompt template used to construct a prompt for the LLM specified in the BedrockKnowledgeModel which is sent to the model to generate an answer from the context of a retrieved results from Knowledge Bases for Amazon Bedrock. To opt out of sending a prompt to the Knowledge Base model, leave this field empty. The template can use the following placeholders:
  + $query$ - The user query sent to the knowledge base.
  + $search\_results$ - The retrieved results for the user query.
  + $output\_format\_instructions$ - The underlying instructions for formatting the response generation and citations. Differs by model. If you define your own formatting instructions, we suggest that you remove this placeholder. Without this placeholder, the response won’t contain citations.
  + $current\_time$ - The current time.

To learn more about prompt template and supported model for these placeholders, see **Knowledge base prompt template** in [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html#kb-test-config-prompt-template).
+  **KNOWLEDGE\_BASE\_MODEL\_PARAMS** - Parameters sent to the LLM specified in the `BedrockKnowledgeModel` CloudFormation parameter when generating answers from Knowledge Bases (For example, anthropic model parameters can be customized as `{"temperature":0.1}` or `{"temperature":0.3, "maxTokens": 262, "topP":0.9, "top_k": 240 }`). To learn more, see **Inference parameters** in [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html#:~:text=Query%20modifications-,Inference,-parameters).
+  **KNOWLEDGE\_BASE\_MAX\_NUMBER\_OF\_RETRIEVED\_RESULTS** - Sets the maximum number of retrieved result where each result corresponds to a source chunk. When you query a knowledge base, Amazon Bedrock returns up to five results by default. To learn more, see **Maximum number of retrieved results** in [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html#kb-test-config-prompt-template).
+  **KNOWLEDGE\_BASE\_SEARCH\_TYPE** - The search type defines how data sources in the knowledge base are queried. If you’re using an Amazon OpenSearch Serverless vector store that contains a filterable text field, you can specify whether to query the knowledge base with a HYBRID search using both vector embeddings and raw text, or SEMANTIC search using only vector embeddings. For other vector store configurations, only SEMANTIC search is available. To learn more, see **Search type** in [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html#kb-test-config-prompt-template).
+  **KNOWLEDGE\_BASE\_METADATA\_FILTERS** - Specifies the filters to use on the metadata in the Knowledge Base data sources before returning results. (For example, filters can be customized as `{"filter1": { "key": "string", "value": "string" }, "filter2": { "key": "string", "value": number }}`). For more information, see **Metadata and filtering** in [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html#kb-test-config-prompt-template).
+  **KNOWLEDGE\_BASE\_PREFIX\_MESSAGE** - Message to append in the chat client when the knowledge base generates a response
+  **KNOWLEDGE\_BASE\_SHOW\_REFERENCES** - Enables the knowledge base to provide full-text references to the sources the knowledge base generated text from.
+  **KNOWLEDGE\_BASE\_S3\_SIGNED\_URLS** - Enables the knowledge base to provide signed URLs for the knowledge base documents.
+  **KNOWLEDGE\_BASE\_S3\_SIGNED\_URL\_EXPIRE\_SECS** - The number of seconds the signed URL will be valid for.
