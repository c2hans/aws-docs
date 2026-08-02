---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/artificial-intelligence-and-machine-learning-with-.net.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Artificial Intelligence and Machine Learning with .NET
<a name="artificial-intelligence-and-machine-learning-with-.net"></a>

Artificial Intelligence (AI) and Machine Learning (ML) are increasingly used to solve new types of problems, and are becoming fundamental parts of many modern applications.

AWS provides a rich set of services that aim to put AI and ML in the hands of every developer. You can either choose from a set of pre-trained AI services, including computer vision, language, recommendations, and forecasting, or you can build, train and deploy custom models with support for all the popular open-source frameworks.

[Amazon Rekognition](https://aws.amazon.com/rekognition/) allows you to add image and video analysis to your applications, and can identify objects, text, and activities, and can also be used for facial recognition.

There are a number of services for working with language, allowing you to easily add intelligence and process natural language in your .NET applications. [Amazon Transcribe](https://aws.amazon.com/transcribe/) automatically converts speech to text, making it simple to enable speech in your applications. [Amazon Textract](https://aws.amazon.com/textract/) extracts text from scanned documents, after which you can use [Amazon Comprehend](https://aws.amazon.com/comprehend/) to find insights or relationships in text, helping you to extract key phrases, classify text, or analyze sentiment. [Amazon Translate](https://aws.amazon.com/translate/) enables you to translate text between more than 25 languages, and helps you build .NET applications that can localize content.

[Amazon Polly](https://aws.amazon.com/polly/) turns text into lifelike speech, and [Amazon Lex](https://aws.amazon.com/lex/) enables you to build conversational interfaces and chatbots into any application using voice and text. Amazon Lex can recognize the intent from a piece of text, enabling you to orchestrate a conversation and build applications with highly engaging user experiences.

[Amazon Personalize](https://aws.amazon.com/personalize/) enables you to enhance your applications with real-time personalization and recommendations, by working with an activity stream from your application, identifying what is meaningful, and helping you serve personalized content to users.

Finally, [Amazon Forecast](https://aws.amazon.com/forecast/) is an accurate time-series forecasting service, allowing your application to process historical time-series data and to produce meaningful forecasts based on trends in the data.

Although the pre-trained AI services enable you to enhance your .NET applications with a rich set of capabilities, you can also build your own machine learning models. [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) is a managed service that enables developers and data scientists to quickly build, train, and deploy machine learning models. Using the AWS .NET SDK, you can set up, configure, and execute Amazon SageMaker AI jobs, enabling you to push new ML boundaries.

Access from .NET applications to all the pre-trained services and to Amazon SageMaker AI is available through the [AWS SDK for .NET](https://aws.amazon.com/sdk-for-net/).
