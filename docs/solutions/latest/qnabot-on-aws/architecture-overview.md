---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution.

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters deploys the following components in your AWS account (components with dotted line border are optional).

 **QnABot on AWS architecture on AWS**

![arch diagram](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/arch-diagram.png)

The high-level process flow for the solution components deployed with the AWS CloudFormation template is as follows:

1. The admin deploys the solution into their AWS account, opens the Content Designer UI or [Amazon Lex](https://aws.amazon.com/lex/) web client, and uses [Amazon Cognito](https://aws.amazon.com/cognito/) to authenticate.

1. After authentication, [Amazon API Gateway](http://aws.amazon.com/api-gateway/) and [Amazon S3](http://aws.amazon.com/s3/) deliver the contents of the Content Designer UI.

1. The admin configures questions and answers in the Content Designer and the UI sends requests to Amazon API Gateway to save the questions and answers.

1. The `Content Designer` [AWS Lambda](http://aws.amazon.com/lambda/) function saves the input in [Amazon OpenSearch Service](http://aws.amazon.com/opensearch-service/) in a questions bank index. If using [text embeddings](https://https://github.com/aws-solutions/qnabot-on-aws/tree/main/source/docs/semantic_matching_using_LLM_embeddings/README.md), these requests will first pass through a LLM model hosted on [Amazon Bedrock](https://aws.amazon.com/bedrock/) to generate embeddings before being saved into the question bank on OpenSearch. In addition, the `Content Designer` saves default and custom [configuration settings](https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/modifying-configuration-settings.html) in [Amazon DynamoDB](https://aws.amazon.com/dynamodb/).

1. Users of the chatbot interact with Amazon Lex via the web client UI, [Amazon Alexa](https://developer.amazon.com/en-US/alexa) or [Amazon Connect](https://aws.amazon.com/connect/).

1. Amazon Lex forwards requests to the `Bot Fulfillment` AWS Lambda function. Users can also send requests to this Lambda function via Amazon Alexa devices. ** *NOTE:* ** When streaming is enabled, the chat client uses Amazon Lex sessionId to establish WebSocket connections through API Gateway V2.

1. The user and chat information is stored in [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) to disambiguate follow up questions from previous question and answer context.

1.  [Amazon Comprehend](https://aws.amazon.com/comprehend/) and [Amazon Translate](https://aws.amazon.com/translate/) (if necessary) are used by the `Bot Fulfillment` AWS Lambda function to translate non-native Language requests to the native Language selected by the user during the deployment and look up the answer in Amazon OpenSearch Service.

1. If using LLM features such as [text generation](https://github.com/aws-solutions/qnabot-on-aws/tree/main/source/docs/LLM_Retrieval_and_generative_question_answering/README.md) and [text embeddings](https://github.com/aws-solutions/qnabot-on-aws/tree/main/source/docs/semantic_matching_using_LLM_embeddings/README.md), these requests will first pass through various models or inference profiles hosted on Amazon Bedrock to generate the search query and embeddings to compare with those saved in the question bank on OpenSearch.

   1. If pre-processing guardrails are enabled, they scan and block potentially harmful user inputs before they reach the QnABot application. This acts as the first line of defense to prevent malicious or inappropriate queries from being processed.

   1. If using Bedrock guardrails for LLMs or Knowledge Base, it can apply contextual guarding and safety controls during LLM inference to ensure appropriate answer generation.

   1. If post-processing guardrails are enabled, they scan, mask, or block potentially harmful content in the final responses before they are sent to the client through the fulfillment Lambda. This serves as the last line of defense to ensure that sensitive information (like PII) is properly masked and inappropriate content is blocked.

1. If no match is returned from the OpenSearch question bank or text passages, then the Bot fulfillment Lambda function forwards the request as follows:

   1. If an [Amazon Kendra](https://aws.amazon.com/kendra/) index is [configured for fallback](https://github.com/aws-solutions/qnabot-on-aws/tree/main/source/docs/Kendra_Fallback_README.md), then the `Bot Fulfillment` AWS Lambda function forwards the request to Kendra if no match is returned from the OpenSearch question bank. The text generation LLM can optionally be used to create the search query and to synthesize a response from the returned document excerpts.

   1. If a [Bedrock Knowledge Base](https://aws.amazon.com/bedrock/knowledge-bases/) ID is [configured](https://github.com/aws-solutions/qnabot-on-aws/tree/main/source/docs/LLM_Retrieval_and_generative_question_answering/README.md), then the `Bot Fulfillment` AWS Lambda function forwards the request to the Bedrock Knowledge Base. The `Bot Fulfillment` AWS Lambda function leverages the RetrieveAndGenerate or RetrieveAndGenerateStream APIs to fetch the relevant results for an user’s query, augment the model’s prompt and return the response.

1. When streaming is enabled, RAG-enhanced LLM responses from text passages or external data sources is streamed via WebSocket connection using same Lex sessionId, while the final response is processed through the fulfillment Lambda.

1. User interactions with the `Bot Fulfillment` function generate logs and metrics data, which is sent to [Amazon Kinesis DataFirehose](http://aws.amazon.com/kinesis/data-firehose/) then to Amazon S3 for later data analysis. The [OpenSearch Dashboards](https://github.com/aws-solutions/qnabot-on-aws/tree/main/source/docs/overview/images/image9.png) can be used to view usage history, logged utterances, no hits utterances, positive user feedback, and negative user feedback and also provides the ability to create custom reports.

1. The [OpenSearch Dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/dashboards.html) can be used to view usage history, logged utterances, no hits utterances, positive user feedback, and negative user feedback, and also provides the ability to create custom reports.

1. Using [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), the admins can monitor service logs and use the CloudWatch dashboard created by QnABot to monitor deployment’s operational health.
