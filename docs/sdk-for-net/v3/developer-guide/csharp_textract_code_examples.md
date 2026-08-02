---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/csharp_textract_code_examples.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

# Amazon Textract examples using SDK for .NET
<a name="csharp_textract_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for .NET with Amazon Textract.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Scenarios](#scenarios)

## Scenarios
<a name="scenarios"></a>

### Create an application to analyze customer feedback
<a name="cross_FSA_csharp_topic"></a>

The following code example shows how to create an application that analyzes customer comment cards, translates them from their original language, determines their sentiment, and generates an audio file from the translated text.

**SDK for .NET**
 This example application analyzes and stores customer feedback cards. Specifically, it fulfills the need of a fictitious hotel in New York City. The hotel receives feedback from guests in various languages in the form of physical comment cards. That feedback is uploaded into the app through a web client. After an image of a comment card is uploaded, the following steps occur:
+ Text is extracted from the image using Amazon Textract.
+ Amazon Comprehend determines the sentiment of the extracted text and its language.
+ The extracted text is translated to English using Amazon Translate.
+ Amazon Polly synthesizes an audio file from the extracted text.
 The full app can be deployed with the AWS CDK. For source code and deployment instructions, see the project in [ GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/cross-service/FeedbackSentimentAnalyzer).

**Services used in this example**
+ Amazon Comprehend
+ Lambda
+ Amazon Polly
+ Amazon Textract
+ Amazon Translate
