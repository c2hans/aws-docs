---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/reference.html
---

# Reference
<a name="reference"></a>

This section includes information about an optional feature for [collecting unique metrics](#anonymized-data-collection) for this guidance, [pointers to related resources](#related-aws-documentation), and a [list of builders](#contributors) who contributed to this guidance.

## Anonymized data collection
<a name="anonymized-data-collection"></a>

This guidance includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this guidance and related services and products. When invoked, the following information is collected and sent to AWS:
+  **Solution ID** - The AWS solution identifier
+  **Unique ID (UUID)** - Randomly generated, unique identifier for each guidance deployment
+  **Timestamp** - The UTC formatted timestamp of when the event occurred
+  **Data** - The Region where the stack launched, request type (whether the stack was created, updated, or deleted), and details about the option chosen (for example, language, OpenSearch node count, OpenSearch EBS volume size, LLM API, etc.) For example:

```
{'InstallLexResponseBots': 'true', 'EmbeddingsBedrockModelId': 'amazon.titan-embed-text-v1', 'PublicOrPrivate': 'PRIVATE', 'LLMApi': 'BEDROCK', 'OpenSearchEBSVolumeSize': '10', 'LexBotVersion': 'LexV2 Only', 'EmbeddingsApi': 'BEDROCK', 'Language': 'English', 'Version': 'v6.1.0', 'OpenSearchNodeCount': '1', OpenSearchFineGrainAccessControl: 'TRUE', EnableStreaming': 'FALSE', 'LLMBedrockModelId': 'anthropic.claude-instant-v1', 'Region': 'us-east-1', 'OpenSearchInstanceType': 'm6g.large.search', 'FulfillmentConcurrency': '1', 'RequestType': 'Delete', 'BEDROCK_GUARDRAIL_ENABLE': 'false','PREPROCESS_GUARDRAIL_ENABLE': 'false', 'POSTPROCESS_GUARDRAIL_ENABLE': 'false',  'ENABLE_MULTI_LANGUAGE_SUPPORT': 'false', 'LLM_GENERATE_QUERY_ENABLE': 'true', 'KNOWLEDGE_BASE_SEARCH_TYPE': 'DEFAULT', 'PII_REJECTION_ENABLED': 'false', 'EMBEDDINGS_ENABLE': 'true', 'LLM_QA_ENABLE': 'true', 'ENABLE_REDACTING': 'false', 'ENABLE_REDACTING_WITH_COMPREHEND': 'false', 'KNOWLEDGE_BASE_METADATA_FILTERS_ENABLE': 'false' }
```

Or

```
{ 'event': 'UPDATE_SETTINGS', 'BEDROCK_GUARDRAIL_ENABLE': 'false'. 'ENABLE_MULTI_LANGUAGE_SUPPORT': 'false', 'LLM_GENERATE_QUERY_ENABLE': 'true','KNOWLEDGE_BASE_SEARCH_TYPE': 'DEFAULT', 'PII_REJECTION_ENABLED': 'false', 'EMBEDDINGS_ENABLE': 'true', 'LLM_QA_ENABLE': 'true' }
```

AWS owns the data gathered through this survey. Data collection is subject to the Privacy Notice. To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

1. Download the `qnabot-on-aws-main.template`[AWS CloudFormation](aws-cloudformation-template.md) template to your local hard drive.

1. Open the AWS CloudFormation template with a text editor.

1. Search for `SO0189` and modify the AWS CloudFormation template description field to remove the solution ID. The template should be modified from:

   ```
   SolutionHelperAnonymizedData:
       SendAnonymizedData:
         Data: Yes
   ```

   to:

   ```
   SolutionHelperAnonymizedData:
       SendAnonymizedData:
         Data: No
   ```

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. Select **Create stack**.

1. On the **Create stack** page, **Specify template** section, select **Upload a template file**.

1. Under **Upload a template file**, choose **Choose file** and select the edited template from your local drive.

1. Choose **Next** and follow the steps in Launch the stack for the relevant deployment option in the [Deploy the guidance](deploy-the-solution.md) section of this guide.

## Related AWS documentation
<a name="related-aws-documentation"></a>

### Blog posts
<a name="blog-posts"></a>
+  [Create a Question and Answer Bot with Amazon Lex and Amazon Alexa](https://aws.amazon.com/blogs/machine-learning/creating-a-question-and-answer-bot-with-amazon-lex-and-amazon-alexa/)
+  [Create a questionnaire bot with Amazon Lex and Amazon Alexa](https://aws.amazon.com/blogs/machine-learning/create-a-questionnaire-bot-with-amazon-lex-and-amazon-alexa/)
+  [Creating virtual guided navigation using a Question and Answer Bot with Amazon Lex and Amazon Alexa](https://aws.amazon.com/blogs/machine-learning/creating-virtual-guided-navigation-using-a-question-and-answer-bot-with-amazon-lex-and-amazon-alexa/)
+ Deploy a Web UI for [Your](https://aws.amazon.com/blogs/machine-learning/deploy-a-web-ui-for-your-chatbot/) Chatbot
+  [Building a multilingual question and answer bot with Amazon Lex](https://aws.amazon.com/blogs/machine-learning/building-a-multilingual-question-and-answer-bot-with-amazon-lex/)
+  [Delight your customers with great conversational experiences via QnABot, a generative AI chatbot](https://aws.amazon.com/blogs/machine-learning/delight-your-customers-with-great-conversational-experiences-via-qnabot-a-generative-ai-chatbot/)

### Workshop
<a name="workshop"></a>
+  [QnABot Workshop](https://qnabot.workshop.aws/)

### YouTube demo
<a name="youtube-demo"></a>
+  [Multi-lingual FAQ bots with agent transfer using Amazon Lex, Amazon Kendra, Amazon Connect, and open source AWS QnABot](https://www.youtube.com/watch?v=4Wxu775i5yM)

## Contributors
<a name="contributors"></a>

The following individuals contributed to this document:
+ Tim Mekari
+ Michael Lin
+ Abhishek Patil
+ Fabien Houeto
+ Abhay Joshi
+ Ajay Swami
+ Manish Jangid
+ Morris Estepa
+ Marc Burnie
+ Ibrahim Mohamed
+ Tarek Abdunabi
+ Alireza Assadzadeh
+ Bob Strahan
+ Bob Potterveld
+ Chris Lott
+ John Calhoun
+ Karl Thomas
+ Raj Chary
+ Mohsen Ansari
