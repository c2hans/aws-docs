---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/semantic-question-matching-using-text-embeddings-llm.html
---

# Semantic question matching using text embeddings LLM
<a name="semantic-question-matching-using-text-embeddings-llm"></a>

**Note**
This is an optional feature available as of v5.3.0. We encourage you to try it out on non-production instances initially to validate expected accuracy improvements and to test for any regression issues. See the [Cost](cost.md) section to see estimates of how this feature affects pricing.

QnABot on AWS can use text embeddings to provide semantic search capabilities by using LLMs. The goals of these features are to improve question matching accuracy while reducing the amount of tuning required when compared to the default OpenSearch keyword-based matching. Some of the benefits include:
+ Improved FAQ accuracy due to semantic matching compared to keyword matching (comparing the meaning of questions as opposed to comparing the individual words).
+ Fewer training utterances are required to match a diverse set of queries. This results in significantly less tuning to get and maintain good results.
+ Better multi-language support because translated utterances only need to match the original question’s meaning, not the exact wording.

For example, with semantic matching activated, ` "What’s the address of the Whitehouse?" ` matches to ` "Where does the president live?" ` and ` "How old are you?" ` would match with ` "What is your age?" `. These examples won’t match using the default keywords because they don’t share any of the same words.

To enable these expanded semantic search capabilities, QnABot can use:
+ Select from several embeddings models provided by Amazon Bedrock using the **EmbeddingsBedrockModelId** Cloudformation parameter. These models provide the best performance and operate on a pay-per-request model. To learn more about supported regions for Bedrock, please refer to [Bedrock Model support by AWS Region](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) in the Amazon Bedrock user guide.
+ Embeddings from a user provided custom Lambda function.

**Note**
By choosing to use the generative responses features, you acknowledge that QnABot on AWS engages third-party generative AI models that AWS does not own or otherwise has any control over ("Third-Party Generative AI Models"). Your use of the Third-Party Generative AI Models is governed by the terms provided to you by the Third-Party Generative AI Model providers when you acquired your license to use them (for example, their terms of service, license agreement, acceptable use policy, and privacy policy).
You are responsible for ensuring that your use of the Third-Party Generative AI Models comply with the terms governing them, and any laws, rules, regulations, policies, or standards that apply to you.
You are also responsible for making your own independent assessment of the Third-Party Generative AI Models that you use, including their outputs and how Third-Party Generative AI Model providers use any data that may be transmitted to them based on your deployment configuration.
AWS does not make any representations, warranties, or guarantees regarding the Third-Party Generative AI Models, which are "Third-Party Content" under your agreement with AWS. QnABot on AWS is offered to you as "AWS Content" under your agreement with AWS.

## Enabling embeddings support
<a name="enabling-embeddings-support"></a>

### Using Amazon Bedrock model (Preferred)
<a name="using-amazon-bedrock-model-preferred"></a>

Utilizes one of the Amazon Bedrock foundation models to generate text embeddings. Currently, the following embeddings models and inference profiles are supported by QnABot on AWS:

#### Foundation Models
<a name="foundation-models"></a>
+  [Amazon Titan embeddings G1](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/providers?model=amazon.titan-embed-text-v1)
+  [Amazon Titan Text Embeddings V2](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/providers%3Fmodel=amazon.titan-embed-text-v2:0)
+  [Amazon Nova Multimodal Embeddings](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/model-catalog/serverless/amazon.nova-2-multimodal-embeddings-v1:0)
+  [Cohere English](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/providers?model=cohere.embed-english-v3)
+  [Cohere Multilingual](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/providers?model=cohere.embed-multilingual-v3)

#### Inference Profiles
<a name="inference-profiles"></a>
+  [Global Cohere Embed V4](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/model-catalog/serverless/cohere.embed-v4:0)

**Note**
Cross-region inference profiles are not supported when deploying QnABot via VPC template
Access to all Amazon Bedrock foundation models is enabled by default. However selecting Anthropic models requires customer to submit use case details [once per account](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) in the Amazon Bedrock console.

From the CloudFormation console, set the following parameters:
+ Set **EmbeddingsAPI** to `BEDROCK`.
+ Set **EmbeddingsBedrockModelId** to one of the provided options.

 **Configure Amazon Bedrock embeddings.**

![image28](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image28.png)

### Using a custom Lambda function
<a name="using-a-custom-lambda-function"></a>

Users that want to explore alternate pre-trained or fine-tuned embeddings models can integrate a custom built Lambda function. By using a custom Lambda function, you can build your own embeddings model or even choose to connect to an external embeddings API.

**Note**
If integrating your Lambda function with external resources, evaluate the security implications of sharing data outside of AWS.

To begin, you must create a Lambda function. Your custom Lambda function should accept a JSON object containing the input string and return an array, which contains the embeddings. Record the length of your embeddings array because you need it to deploy the stack (this is also referred to as the *dimensions*).

Lambda event input:

```
{
  // inputtype has either a value of 'q' for question or 'a' for answer
  "inputType": "string",

  // inputtext is the string on which to generate your custom embeddings
  "inputText":"string"
}
```

Expected Lambda JSON return object:

```
{"embedding": [...] }
```

When your Lambda function is ready, you can deploy the stack. To activate your Lambda function for embeddings, deploy the stack with **EmbeddingsAPI** set to `LAMBDA`. You must also set **EmbeddingsLambdaArn** to the ARN of your Lambda function and **EmbeddingsLambdaDimensions** to the dimensions returned by your Lambda function.

 **Semantic search with Lambda function .**

![image30](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image30.png)

**Note**
You can’t change these settings through the content designer **Settings** page. To correctly reconfigure your deployment, update your CloudFormation stack to modify these values.

## Settings available for text embeddings
<a name="settings-available-for-text-embeddings"></a>

When your QnABot stack is installed with **EmbeddingsApi** enabled, you can manage several different settings through the content designer **Settings** page:
+  **EMBEDDINGS\_ENABLE** - To turn on and off use of semantic search using embeddings:
  + Set to `FALSE` to turn off the use of embeddings-based queries.
  + Set to `TRUE` to activate the use of embeddings-based queries after previously setting it to `FALSE`.

**Note**
Setting `TRUE` when the stack has **EmbeddingsAPI** set to `DISABLED` will cause failures since the QnABot on AWS stack isn’t provisioned to support generation of embeddings.
 **EMBEDDINGS\_ENABLE** will be set default to `TRUE`, if **EmbeddingsAPI** is provisioned to `LAMBDA`. If not provisioned, **EMBEDDINGS\_ENABLE** will be set default to `FALSE`.

If you disable embeddings, you will likely also want to re-enable keyword filters by setting **ES\_USE\_KEYWORD\_FILTERS** to `TRUE`.

If you add, modify, or import any items in the content designer when **EMBEDDINGS\_ENABLE** is set to `FALSE`, then embeddings won’t get created and you’ll need to re-import or re-save those items after re-enabling embeddings.

This setting allows you to toggle embeddings on and off, it does not manage the underlying infrastructure. If you choose to permanently turn off embeddings, update the stack as well.

**Important**
If you update or change your embeddings model, for example, from Amazon Titan Embeddings G1 to Cohere English, or change **EmbeddingsApi** the embedding dimensions need to be recalculated. QnABot on AWS will need to [export and re-import](importing-and-exporting-chatbot-answers.md) the Q&As in your content designer; however, we recommend backing up the Q&As using export before making this change. If any discrepancies occur, they can be addressed by import of exported Q&As.
+  **ES\_USE\_KEYWORD\_FILTERS** - This setting should now default to `FALSE`. Although you can use keyword filters with embeddings based semantic queries, they limit the power of semantic search by forcing keyword matches (preventing matches based on different words with similar meanings).
+  **ES\_SCORE\_ANSWER\_FIELD** - If set to `TRUE`, QnABot on AWS runs embedding vector searches on embeddings generated on answer field if no match is found on question fields. This allows QnABot to find matches based on the contents on the answer field as well as the questions. Only the plaintext answer field is used (not the Markdown or SSML alternatives). Tune the individual thresholds for questions and answers using the additional settings of:
  +  **EMBEDDINGS\_SCORE\_THRESHOLD**
  +  **EMBEDDINGS\_SCORE\_ANSWER\_THRESHOLD**
+  **EMBEDDINGS\_SCORE\_THRESHOLD** - Change this value to customize the score threshold on *question* fields. Unlike regular OpenSearch queries, embeddings queries always return scores between 0 and 1, so we can apply a threshold to separate good from bad results.
  + If no question has a similarity score above the threshold set, the match gets rejected and QnABot reverts to:

    1. Trying to find a match using the answer field (only if **ES\_SCORE\_ANSWER\_FIELD** is set to `TRUE`).

    1. Amazon Kendra fallback (only if enabled)

    1.  **no\_hits**

  The default threshold is 0.7 for `BEDROCK`, but you can modify this based on your embeddings model and your experiments.

**Tip**
Use the content designer **TEST** tab to see the hits ranked by score for your query results.
+  **EMBEDDINGS\_SCORE\_ANSWER\_THRESHOLD** - Change this value to customize the score threshold on *answer* fields. This setting is only used when **ES\_SCORE\_ANSWER\_FIELD** is set to `TRUE` and QnABot has failed to find a suitable response using the question field.
  + If no answer has a similarity score above the threshold set, the match gets rejected and QnABot reverts to:

    1. Amazon Kendra fallback (only if enabled)

    1.  **no\_hits**

  The default threshold is 0.8, but you can modify this based on your embeddings model and your experiments.

**Tip**
Use the content designer **TEST** tab and select the **Score on answer field** checkbox to see the hits ranked by score for your answer field query results.
+  **EMBEDDINGS\_TEXT\_PASSAGE\_SCORE\_THRESHOLD** - Change this value to customize the passage score threshold. This setting is only used if **ES\_SCORE\_TEXT\_ITEM\_PASSAGES** is `TRUE`.
  + If no answer has a similarity score above the threshold set, the match gets rejected and QnABot reverts to:

    1. Amazon Kendra fallback (only if enabled)

    1.  **no\_hits**

  The default threshold is 0.65 for `BEDROCK`, but you can modify this based on your embeddings model and your experiments.

**Tip**
Use the content designer **TEST** tab and select the **Score on answer field** checkbox to see the hits ranked by score for your answer field query results.

## Recommendations for tuning with LLMs
<a name="recommendations-for-tuning-with-llms"></a>

When using embeddings in QnABot, we recommend generalizing questions because more user utterances will match a general statement. For example, the embeddings model will cluster *checkings* and *savings* with *account*, so if you want to match both account types, just see *account* in your questions.

Similarly for the question and utterance of *transfer to an agent*, consider using *transfer to someone* as it will better match with *agent*, *representative*, *human*, *person*, etc.

In addition for LLMs, we recommend tuning the **EMBEDDINGS\_SCORE\_THRESHOLD**, **EMBEDDINGS\_SCORE\_ANSWER\_THRESHOLD**, and **EMBEDDINGS\_TEXT\_PASSAGE\_SCORE\_THRESHOLD** settings. The default values are generalized to all multiple models but you might need to modify this based on your embeddings model and your experiments.

## Test using example phrases
<a name="test-using-example-phrases"></a>

Add Q&As using the **QnABot** content designer

1. Choose **Add** to add a new question of QnA type with an Item ID: `EMBEDDINGS.WhiteHouse`

   1. Add a single example question/utterance: `What is the address of the White House?`

   1. Add an Answer: `The address is: 1600 Pennsylvania Avenue NW, Washington, DC 20500`

   1. Choose **CREATE** to save the item.

1. Add another question with an Item ID of `EMBEDDINGS.Agent`

   1. This time add a few questions/utterances:
      +  `I want to speak to an agent`
      +  `Representative`
      +  `Operator please`
      +  `Zero` (Zero handles when a customer presses "0" on their dial pad when integrated with a contact center)

   1. Add an answer: `Ok. Let me route you to a representative who can assist you. {{setSessionAttr 'nextAction' 'AGENT'}}`

      This Handlebars syntax will set a `nextAction` session attribute with the value `AGENT`.

   1. Choose **CREATE** to save the item.

1. Select the **TEST** tab in the content designer UI.

   1. Enter the question, `Where does the President live?` and choose **SEARCH**.

   1. Observe that the correct answer has the top ranked **score** (displayed on the left), even though it does not use any of the same words as the stored example utterance.

   1. Try some other variations, such as, `Where’s the Whitehouse?`, `Where’s the whitehousw?` (with a typo), or `Where is the President’s mansion?`

   1. To detect when a caller wants to speak with an agent, we entered only a few example phrases into QnABot. Try some tests where you ask for an agent in a variety of different ways.
