---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/java_2_translate_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon Translate examples using SDK for Java 2.x
<a name="java_2_translate_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Java 2.x with Amazon Translate.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Scenarios](#scenarios)

## Scenarios
<a name="scenarios"></a>

### Building an Amazon Lex chatbot
<a name="cross_LexChatbotLanguages_java_2_topic"></a>

The following code example shows how to create a chatbot to engage your website visitors.

**SDK for Java 2.x**
 Shows how to use the Amazon Lex API to create a Chatbot within a web application to engage your web site visitors.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/usecases/creating_lex_chatbot).

**Services used in this example**
+ Amazon Comprehend
+ Amazon Lex
+ Amazon Translate

### Building an Amazon SNS application
<a name="cross_SnsPublishSubscription_java_2_topic"></a>

The following code example shows how to create an application that has subscription and publish functionality and translates messages.

**SDK for Java 2.x**
 Shows how to use the Amazon Simple Notification Service Java API to create a web application that has subscription and publish functionality. In addition, this example application also translates messages.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/usecases/creating_sns_sample_app).
 For complete source code and instructions on how to set up and run the example that uses the Java Async API, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/usecases/creating_sns_async).

**Services used in this example**
+ Amazon SNS
+ Amazon Translate

### Create an application to analyze customer feedback
<a name="cross_FSA_java_2_topic"></a>

The following code example shows how to create an application that analyzes customer comment cards, translates them from their original language, determines their sentiment, and generates an audio file from the translated text.

**SDK for Java 2.x**
 This example application analyzes and stores customer feedback cards. Specifically, it fulfills the need of a fictitious hotel in New York City. The hotel receives feedback from guests in various languages in the form of physical comment cards. That feedback is uploaded into the app through a web client. After an image of a comment card is uploaded, the following steps occur:
+ Text is extracted from the image using Amazon Textract.
+ Amazon Comprehend determines the sentiment of the extracted text and its language.
+ The extracted text is translated to English using Amazon Translate.
+ Amazon Polly synthesizes an audio file from the extracted text.
 The full app can be deployed with the AWS CDK. For source code and deployment instructions, see the project in [ GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/usecases/creating_fsa_app).

**Services used in this example**
+ Amazon Comprehend
+ Lambda
+ Amazon Polly
+ Amazon Textract
+ Amazon Translate
