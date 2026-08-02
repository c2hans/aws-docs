---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

This section describes the components and AWS services that make up this solution and the architecture details on how these components work together.

## AWS services in this solution
<a name="aws-services-in-this-solution"></a>

The following AWS services are included in this solution:

| AWS service | Description |
| --- | --- |
|  [Amazon API Gateway](https://aws.amazon.com/api-gateway/)  |  **Core.** Used for internal API management. |
|  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)  |  **Core.** Used to deploy the solution. |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  |  **Core.** Used for monitoring and logs. |
|  [Amazon Cognito](https://aws.amazon.com/cognito/)  |  **Core.** Used for user management. |
|  [AWS Identity and Access Management](https://aws.amazon.com/iam/)  |  **Core.** Used for user role and permissions management. |
|  [AWS Key Management Service](https://aws.amazon.com/kms/)  |  **Core.** Used for encryption. |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  **Core.** Provides logic for chatbot interactions and provides extension capabilities for Amazon Translate before and after interaction with Amazon Lex. |
|  [Amazon Lex](https://aws.amazon.com/lex/)  |  **Core.** Provides the advanced deep learning functionalities of ASR for converting speech to text, and NLU to recognize the intent of the text. |
|  [Amazon OpenSearch Service](https://aws.amazon.com/elasticsearch-service/)  |  **Core.** Provides question bank, metrics, feedback indices, and provides OpenSearch Dashboards for chatbot usage. |
|  [Amazon SNS](https://aws.amazon.com/pm/sns/)  |  **Core.** Used for notifications, such as feedback. |
|  [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose)  |  **Supporting.** Delivers logs and metrics data to an Amazon S3 bucket. |
|  [Amazon Polly](https://aws.amazon.com/polly/)  |  **Supporting.** Used for Interactive Voice Response systems. It provides text to speech capabilities to relay the response back in the voice of choice. |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  **Supporting.** Provides object storage for content designer UI data and logs and metrics data. |
|  [AWS Systems Manager Parameter Store](https://aws.amazon.com/systems-manager/features/#Parameter_Store)  |  **Supporting.** Provides secure, hierarchical storage for configuration data management and secrets management. |
|  [Amazon Translate](https://aws.amazon.com/translate/)  |  **Supporting.** Provides multi-language support to your customer’s bot interactions. You can maintain question and answer banks in a single language while still offering support to customers who interact with the bot in other languages through the use of Amazon Translate. |
|  [Amazon Bedrock](https://aws.amazon.com/bedrock/)  |  **Optional.** This solution utilizes Bedrock for embedding models, LLM models, knowledge base, and guardrails. |
|  [Amazon Connect](https://aws.amazon.com/connect/)  |  **Optional.** Provides an omnichannel cloud contact center. If you implement this component, you can create personalized experiences for your customers. For example, you can dynamically offer chat and voice contact, based on such factors as customer preference and estimated wait times. Agents, meanwhile, conveniently handle all customers from just one interface. For example, they can chat with customers, and create or respond to tasks as they are routed to them. |
|  [Amazon Kendra](https://aws.amazon.com/kendra/)  |  **Optional.** Hosts unstructured datasets hosted in an index. You can also use Amazon Kendra to provide semantic search capabilities to your question bank through the use of Amazon Kendra FAQs. |

## Amazon Lex web client
<a name="amazon-lex-web-client"></a>

Amazon Lex allows conversational interfaces to be integrated into applications such as the Amazon Lex web client. An Amazon Lex chatbot uses *intents* to encapsulate the purpose of an interaction, and *slots* to capture elements of information from the interaction. Since QnABot on AWS has a single purpose, to answer a user’s question, it defines just one intent. This intent has a single slot which is trained to capture the text of the question. QnABot on AWS also uses `AMAZON.FallBackIntent` to ensure that all user input is processed. To learn more about how Amazon Lex bots work, and to understand the concepts of intents, slots, sample values, fulfillment functions, see the [Amazon Lex Developer Guide](https://docs.aws.amazon.com/lex/latest/dg/what-is.html).

The QnABot on AWS Amazon Lex web client is deployed to an Amazon S3 bucket in your account, and accessed via Amazon API Gateway.

## Amazon Alexa devices
<a name="amazon-alexa-devices"></a>

Amazon Alexa devices interact with QnABot on AWS using an Alexa skill. Like an Amazon Lex chatbot, an Alexa skill also uses *intents* to encapsulate the purpose of an interaction, and *slots* to capture elements of information from the interaction.

The Alexa QnABot on AWS skill uses the same `Bot fulfillment` Lambda function as the Amazon Lex chatbot. When you ask a question, for example, ` "Alexa, ask Q and A, How can I include pictures in Q and A Bot answers?" `, your Alexa device interacts with the skill you created, which in turn invokes the `Bot fulfillment` Lambda function in your AWS account, passing the transcribed question as a parameter.

## Content designer UI
<a name="content-designer-ui"></a>

The QnABot on AWS content designer UI, like the Amazon Lex web client, is also deployed to an Amazon S3 bucket and accessed via Amazon API Gateway, and it too retrieves configuration from an API Gateway endpoint. The content designer UI requires the user to sign in with credentials defined in a Cognito user pool.

Using temporary AWS credentials from Cognito, the content designer UI interacts with secure API Gateway endpoints backed by the content designer Lambda functions. All interactions with Amazon OpenSearch Service and Amazon Lex are handled by these Lambda functions.
