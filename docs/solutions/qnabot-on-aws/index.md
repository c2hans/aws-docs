---
source_url: https://docs.aws.amazon.com//solutions/qnabot-on-aws//index.html
---

---
title: 'Guidance for QnABot on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/qnabot-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for QnABot on AWS

## Overview

This Guidance demonstrates how to deploy a multi-channel, multi-language conversational AI chatbot powered by large language models that seamlessly integrates with telephony, Alexa, web apps, and mobile apps. Organizations can rapidly implement intelligent question-answering capabilities while maintaining full control over their deployment, enabling faster responses to business needs and fostering a collaborative development ecosystem that benefits the entire AWS community.

## Benefits

### Engage customers across channels

Deploy a conversational chatbot that reaches customers through web, voice, and contact center channels without building separate integrations. Reduce customer service costs by automating responses to frequently asked questions at scale.

### Serve global audiences instantly

Automatically detect and translate customer inquiries across multiple languages using built-in language detection and translation capabilities. Expand your customer support reach without hiring multilingual staff or rebuilding your chatbot for each language.

### Gain actionable chatbot insights

Visualize usage trends, unanswered questions, and customer sentiment through built-in analytics dashboards to continuously improve your self-service experience. Use these insights to identify content gaps and refine responses, helping your support team focus on higher-value interactions.

## How it works

This architecture diagram shows how to deploy a multi-channel, multi-language conversational interface (chatbot) that responds to your customer's questions, answers, and feedback, powered by large language models (LLMs). [Download the architecture diagram](downloads/qnabot-on-aws.pdf)

![Architecture diagram for QnABot on AWS](/images/solutions/qnabot-on-aws/images/qnabot-on-aws-1.png)

1. **Step 1**: The admin deploys the solution into their AWS account, opens the Content Designer UI or Amazon Lex web client, and uses Amazon Cognito to authenticate.
1. **Step 2**: After authentication, Amazon API Gateway and Amazon S3 deliver the contents of the Content Designer UI.
1. **Step 3**: The admin configures questions and answers in the Content Designer and the UI sends requests to Amazon API Gateway to save the questions and answers.
1. **Step 4**: The `Content Designer` AWS Lambda function saves the input in Amazon OpenSearch Service in a questions bank index. If using text embeddings, these requests will first pass through a LLM model hosted on Amazon Bedrock to generate embeddings before being saved into the question bank on OpenSearch. In addition, the `Content Designer` saves default and custom configuration settings in Amazon DynamoDB.
1. **Step 5**: Users of the chatbot interact with Amazon Lex via the web client UI, Amazon Alexa or Amazon Connect Customer.
1. **Step 6**: Amazon Lex forwards requests to the `Bot Fulfillment` AWS Lambda function. Users can also send requests to this Lambda function via Amazon Alexa devices. ***NOTE:*** When streaming is enabled, the chat client uses Amazon Lex sessionId to establish WebSocket connections through API Gateway V2.
1. **Step 7**: The user and chat information is stored in Amazon DynamoDB to disambiguate follow up questions from previous question and answer context.
1. **Step 8**: Amazon Comprehend and Amazon Translate (if necessary) are used by the `Bot Fulfillment` AWS Lambda function to translate non-native Language requests to the native Language selected by the user during the deployment and look up the answer in Amazon OpenSearch Service.
1. **Step 9**: If using LLM features such as text generation and text embeddings, these requests will first pass through various models or inference profiles hosted on Amazon Bedrock to generate the search query and embeddings to compare with those saved in the question bank on OpenSearch. 1. If pre-processing guardrails are enabled, they scan and block potentially harmful user inputs before they reach the QnABot application. This acts as the first line of defense to prevent malicious or inappropriate queries from being processed. 2. If using Bedrock guardrails for LLMs or Knowledge Base, it can apply contextual guarding and safety controls during LLM inference to ensure appropriate answer generation. 3. If post-processing guardrails are enabled, they scan, mask, or block potentially harmful content in the final responses before they are sent to the client through the fulfillment Lambda. This serves as the last line of defense to ensure that sensitive information (like PII) is properly masked and inappropriate content is blocked.
1. **Step 10**: If no match is returned from the OpenSearch question bank or text passages, then the Bot fulfillment Lambda function forwards the request as follows: 1. If an Amazon Kendra index is configured for fallback, then the `Bot Fulfillment` AWS Lambda function forwards the request to Kendra if no match is returned from the OpenSearch question bank. The text generation LLM can optionally be used to create the search query and to synthesize a response from the returned document excerpts. 2. If a Bedrock Knowledge Base ID is configured, then the `Bot Fulfillment` AWS Lambda function forwards the request to the Bedrock Knowledge Base. The `Bot Fulfillment` AWS Lambda function leverages the RetrieveAndGenerate or RetrieveAndGenerateStream APIs to fetch the relevant results for an user's query, augment the model's prompt and return the response.
1. **Step 11**: When streaming is enabled, RAG-enhanced LLM responses from text passages or external data sources is streamed via WebSocket connection using same Lex sessionId, while the final response is processed through the fulfillment Lambda.
1. **Step 12**: User interactions with the `Bot Fulfillment` function generate logs and metrics data, which is sent to Amazon Kinesis DataFirehose then to Amazon S3 for later data analysis. The OpenSearch Dashboards can be used to view usage history, logged utterances, no hits utterances, positive user feedback, and negative user feedback and also provides the ability to create custom reports.
1. **Step 13**: The OpenSearch Dashboards can be used to view usage history, logged utterances, no hits utterances, positive user feedback, and negative user feedback, and also provides the ability to create custom reports.
1. **Step 14**: Using Amazon CloudWatch, the admins can monitor service logs and use the CloudWatch dashboard created by QnABot to monitor deployment's operational health.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](/solutions/latest/qnabot-on-aws/welcome.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/qnabot-on-aws)

## Related content

- **Video**: Solving with AWS Solutions: QnABot on AWS

[Learn more](https://www.youtube.com/watch?v=44cz_lX07K8)

- **Automating Nonemergency Calls for PSAPs Using QnABot on AWS with Paragon**: Learn how AWS Partner Paragon Cloud Services automates nonemergency calls for overwhelmed 9-1-1 dispatch centers using QnABot on AWS.

[Learn more](https://aws.amazon.com/solutions/case-studies/paragon-qnabot/)

## Customer stories

### ResultsCX

"QnABot on AWS has empowered our SupportPredict platform to deliver fast, intuitive self-service experiences that reduce support costs and boost customer satisfaction. Its seamless integration with the broader AWS ecosystem positions us to scale effortlessly and innovate continuously as customer needs evolve."

**Ganesh Iyer, Chief Solutions Officer**

[Learn More](https://aws.amazon.com/solutions/case-studies/resultscx/)[Read usage guidelines](/solutions/guidance-disclaimers/)
