---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/solution-overview.html
---

# Create a custom question and answer chatbot
<a name="solution-overview"></a>

The QnABot on AWS solution is a generative AI-enabled multi-channel, multi-language conversational chatbot that responds to your customer’s questions, answers, and feedback. It is built on [Amazon Lex](https://aws.amazon.com/lex/), [Amazon Polly](https://aws.amazon.com/polly/), [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/), [Amazon Translate](https://aws.amazon.com/translate/), [Amazon Comprehend](https://aws.amazon.com/comprehend/), [Amazon Kendra](https://aws.amazon.com/kendra/), and [Amazon Bedrock](https://aws.amazon.com/bedrock/). This solution helps you to quickly deploy self-service conversational artificial intelligence (AI) on multiple channels, including your contact centers, websites, social media channels, SMS text messaging, or Amazon Alexa without programming.

This implementation guide provides an overview of the QnABot on AWS solution, its reference architecture and components, considerations for planning the deployment, configuration steps for deploying the solution to the Amazon Web Services (AWS) Cloud. It also includes a user’s guide with prescriptive guidance for using QnABot on AWS.

Use this navigation table to quickly find answers to these questions:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this solution |  [Cost](cost.md)  |
| Understand the security considerations for this solution |  [Security](security-1.md)  |
| Know how to plan for quotas for this solution |  [Quotas](quotas.md)  |
| Know which AWS Regions are supported for this solution |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
| View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution |  [AWS CloudFormation template](aws-cloudformation-template.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) (AWS CDK) to deploy the solution |  [GitHub repository](https://github.com/aws-solutions/qnabot-on-aws)  |

## Use cases
<a name="use-cases"></a>

 **Contact centers - How can I help?**

Virtual agents to automatically help resolve customer questions or guide customers to the right agent.

 **Informational bots - Can I answer your question?**

Chatbots for everyday requests and frequently asked questions.

 **Enterprise productivity bots - Can I help you get more done**?

Streamline internal enterprise work activities and enhance productivity.

## Features and benefits
<a name="features-and-benefits"></a>

With the solution’s content management environment and the Contact Center Integration wizard, you can set up and customize an environment that provides the following benefits:
+ Enhance your customer’s experience by providing personalized tutorials and question and answer support with intelligent multi-part interaction.
+ Uncover insights and business trends.
+ Reduce call center wait times by automating customer support workflows.
+ Expand existing channels and grow new ones.
+ Implement the latest machine learning (ML) technology to create engaging, human-like interactions for chatbots.
+ Reduce customer support costs.

QnABot on AWS provides the following features:

 **High quality speech recognition and natural language understanding (NLU)**

This solution uses automatic speech recognition (ASR) and NLU technologies to create a Speech Language Understanding (SLU) system with Amazon Lex. Amazon Lex uses the same proven technology that powers Alexa. Amazon Lex is able to learn the multiple ways users can express their intent based on a few sample utterances provided by the developer. The SLU system takes natural language speech and text input, understands the intent behind the input, and fulfills the user intent by invoking the appropriate response.

 **Context management**

As the conversation develops, being able to accurately classify utterances requires managing context across multi-turn conversations. Amazon Lex supports [context management](https://docs.aws.amazon.com/lexv2/latest/dg/conversation-contexts.html) natively, so you can manage the context directly without the need for custom code. As the initial prerequisite intents are filled, you can create `"contexts"` to invoke related intents. This simplifies bot design and expedites the creation of conversational experiences.

 **Generative responses**

Integration with the various large language models (LLMs) hosted on Amazon Bedrock allows QnABot to:
+ Disambiguate customer questions by considering conversational context
+ Dynamically generate answers from relevant FAQs, Amazon Kendra search results, and Amazon Bedrock knowledge bases
+ Ask questions and summarize data from a single uploaded document

Generated responses reduce the number of FAQs you must maintain because the solution synthesizes concise answers from existing documents. You can customize responses to be short, concise, and suitable for voice channel contact center bots as well as website text bots. Text generation is fully compatible with this solution’s multi-language support, allowing users to interact in their chosen languages and receive generated answers in the same language.

**Note**
By choosing to use the generative responses features, you acknowledge that QnABot on AWS engages third-party generative AI models that AWS does not own or otherwise has any control over (`"Third-Party Generative AI Models"`). Your use of the Third-Party Generative AI Models is governed by the terms provided to you by the Third-Party Generative AI Model providers when you acquired your license to use them (for example, their terms of service, license agreement, acceptable use policy, and privacy policy).
You are responsible for ensuring that your use of the Third-Party Generative AI Models comply with the terms governing them, and any laws, rules, regulations, policies, or standards that apply to you.
You are also responsible for making your own independent assessment of the Third-Party Generative AI Models that you use, including their outputs and how Third-Party Generative AI Model providers use any data that may be transmitted to them based on your deployment configuration.
AWS does not make any representations, warranties, or guarantees regarding the Third-Party Generative AI Models, which are `"Third-Party Content"` under your agreement with AWS. QnABot on AWS is offered to you as `"AWS Content"` under your agreement with AWS.

 **8 kHz telephony audio support**

This solution uses high fidelity with telephone speech interactions, such as through a contact center application or helpdesk. This feature leverages the Amazon Lex speech recognition engine, which has been trained on telephony audio (8 kHz sampling rate).

 **Multi-turn dialog**

After the solution identifies an intent, it prompts users for information that is required for the intent to be fulfilled (for example, if `"Book hotel"` is the intent, then the user is prompted for the location, check-in date, number of nights, etc.). QnABot on AWS gives you an easy way to build multi-turn conversations for your chatbots. You simply list the slots/parameters you want to collect from your bot users, as well as the corresponding prompts, and the Amazon Lex component takes care of orchestrating the dialogue by prompting for the appropriate slot.

 **Early implementation of intent and slot matching**

This new capability supports creating dedicated custom Intents for a QnABot Item ID. You can extend QnABot to support one or more related intents. For example, you might create an intent that makes a car reservation, or assists an agent during a live chat or call (via [Amazon Connect](https://aws.amazon.com/connect/)). For more details, see the [Intent and slot matching](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/docs/intent_slot_matching/README.md) section in the GitHub repository.

 **Custom domain names in QnABot content designer and QnABot client**

This solution supports using custom domain names for QnABot content designer and client interfaces. For more details, see the [Set up custom domain name for QnABot content designer and client](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/docs/custom_domain_name_setup/README.md) section in the GitHub repository.

 **Importing and exporting questions and answers using CLI**

You can import and export questions and answers using the AWS QnABot Command Line Interface (CLI) command line. For more details, see the [AWS QnABot Command Line Interface (CLI)](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/docs/qnabot_cli/README.md) section in the GitHub repository.

 **Support for the Amazon Kendra Redirect feature**

With the Amazon Kendra Redirect feature, you can now include an Amazon Kendra query within an Item ID. For more details, see the [Amazon Kendra Redirect](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/docs/kendra_redirect/README.md) section in the GitHub repository.

 **Enhanced functionality for Excel**

This solution supports importing QnABot questions and answers from an Excel file when uploaded to the [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) data folder, as well as support for importing session attributes via Excel.

## Concepts and definitions
<a name="concepts-and-definitions"></a>

The following terms are specific to this document:

 **fulfillment**

The process of performing actions based on user requests. It involves taking the information gathered during the conversation and performing relevant tasks or providing appropriate responses. For instance, Alexa uses fulfillment processes to run tasks such as setting reminders, playing music, or providing weather updates.

 **intent**

An action in response to user input in natural language. An intent represents the main purpose or goal behind a user’s query. It captures what the user is trying to accomplish when interacting with a chatbot. Intents are the building blocks that empower chatbots to understand and respond effectively to user queries. For instance, if a user asks, ` "Show me the weather in Houston, Texas," ` the intent behind their query is to "get the weather information". If the user says, ` "Is it going to rain today?" ` or ` "What’s the weather like today?" `, the chatbot should be able to understand that both these *utterances* have the same *intent*, which is to get the weather information.

 **slot**

Slots are placeholders for specific pieces of information. For example, in the query ` "Book a flight from New York to Los Angeles," ` the slots are ` "departure city" ` (New York) and ` "destination city" ` (Los Angeles). The slots are the specific input data extracted from the user’s utterance and needed to fulfill the intent. Slot filling helps extract relevant entities from the user’s input.

 **token**

A token is the smallest unit into which text data can be broken down for an AI model to process. It is similar to how we might break sentences into words or characters. For AI, especially in the context of language models, tokens can represent a character, a word, or even larger chunks of text, such as phrases, depending on the model and its configuration. Tokens are used to characterize different models. For example, the more questions a user asks the chat bot, the more it will cost because more tokens are processed.

 **utterance**

Utterances are simply anything a user says to a chatbot or virtual assistant. These could be in the form of text input, voice commands, or any other form of user input. For instance, if a user types ` "Show me the weather in Houston, Texas" ` the entire sentence is the utterance.

**Note**
For a general reference of AWS terms, see the [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html).
