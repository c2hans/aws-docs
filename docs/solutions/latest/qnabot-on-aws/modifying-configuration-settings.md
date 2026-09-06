---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/modifying-configuration-settings.html
---

# Modifying configuration settings
<a name="modifying-configuration-settings"></a>

The guidance uses a DynamoDB Table to hold default and custom configuration settings. You can view and edit these settings using the Settings menu in the content designer.

Explore the available configuration settings and override the defaults. You can configure custom keyword filtering, answer field scoring, messages, and redaction from logs and metrics (**ENABLE\_REDACTING** and **REDACTING\_REGEX**), and more. You can also enable debug mode (**ENABLE\_DEBUG\_RESPONSES** and **ENABLE\_DEBUG\_LOGGING**). Additionally, you can initiate fuzzy matching (**ES\_USE\_FUZZY\_MATCH**) and experiment with score boosting for exact phrase matches (**ES\_PHRASE\_BOOST**). The following are examples of frequently used settings. For more complete information on the settings, see [QnABot Settings](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/docs/settings.md) in the GitHub repository.

**Note**
Custom settings are kept when you upgrade the guidance.

## Configure keyword filters feature
<a name="configure-keyword-filters-feature"></a>

1. Sign in to the content designer, select the tools menu ( ☰ ), and then choose **Settings**.

1. Change the value of the **ES\_USE\_KEYWORD\_FILTERS** setting from `true` to `false`.

1. Scroll to the bottom and select **Save**. This turns off the new keyword filters feature.

You can further customize how the keyword filters feature works by changing the following settings:
+  **ES\_KEYWORD\_SYNTAX\_TYPES** - A list of [tokens](https://docs.aws.amazon.com/comprehend/latest/dg/how-syntax.html) representing parts of speech identified by Amazon Comprehend.
+ \*ES\_MINIMUM\_SHOULD\_MATCH \* - A [query rule](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-minimum-should-match.html) used to determine how many keywords must match an item question in a valid answer.

## Configure words and phrases replacement in user questions
<a name="configure-words-and-phrases-replacement-in-user-questions"></a>

If you want to replace words or phrases in user questions, for example, you want *Thumbs up* rewritten to be a direct match by question ID, you can use the

 **SEARCH\_REPLACE\_QUESTION\_SUBSTRINGS** setting.

1. Sign in to the content designer, select the tools menu ( ☰ ), and then choose **Settings**.

1. Change the value of the **SEARCH\_REPLACE\_QUESTION\_SUBSTRINGS** setting to a JSON object, such as `{"Thumbs Down": "QID::Feedback.001", "Thumbs Up": "QID::Feedback.002"}`. You can add additional pairs separated by commas.

1. Scroll to the bottom and select **Save**. This will now rewrite all input matching `"Thumbs Down"` to `"QID::Feedback.001"`.

## Configure pre-processing and post-processing Lambda hooks
<a name="configure-pre-processing-and-post-processing-lambda-hooks"></a>

The content designer enables you to dynamically generate answers by letting you specify your own [Lambda hook](https://github.com/aws-solutions/qnabot-on-aws/tree/main/source/docs/lambda_hooks) function for any item/question defined in the content designer (hook). In addition, a Lambda hook can be called as the first step in the fulfillment pipeline (PREPROCESS) or after processing has completed (POSTPROCESS ) and before the userInfo is saved to DynamoDB and the result has been sent back to the client.

You can add pre-processing and post-processing Lambda hooks (that run before preprocessing and after every question is run) via the Settings page.

1. Sign in to the content designer, select the tools menu ( ☰ ), and then choose **Settings**.

1. Find the **LAMBDA\_PREPROCESS\_HOOK** setting and set its value to your hook name. The name of the Lambda must start with qna- or QNA- to comply with the permissions of the role attached to the Fulfillment Lambda, for example, QNA-ExampleJSLambdahook.

1. Scroll to the bottom and select **Save**. The Lambda function specified will now be run before each question is processed\_.\_

**Note**
For more information on Lambda hooks, see the [Extending QnABot with Lambda hook functions](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/docs/lambda_hooks/README.md) and the [QnABot Settings](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/docs/settings.md) sections in the GitHub repository.

## Configure multi-language support
<a name="configure-multi-language-support"></a>

QnABot on AWS supports both voice and text interactions in multiple languages. QnABot can detect the predominant language in an interaction by using Amazon Comprehend, a NLP service that uses machine learning to find insights and relationships in text. The bot then uses Amazon Translate, a neural machine translation service to convert questions and answers across languages from a single shared set of FAQs and documents.

By default the multi-language feature is disabled. QnABot on AWS uses a property named **ENABLE\_MULTI\_LANGUAGE\_SUPPORT** with a default value of `false`. You can change this setting using the content designer **Settings** page. Set it to `true` to enable multi-language support.

QnABot on AWS uses Amazon Translate to convert the question posed by the user to your core language that was chosen during your deployment. It performs a lookup of the answer in Amazon OpenSearch Service just as it normally does, using the native language translation of the question.

Searches are done in the language you have selected for your deployment only since QnABot on AWS documents are indexed using the language analyzer and their corresponding text analyzer for example, stemming and stop words. Once it finds the question, QnABot serves up the configured answer.

When you are in multi-language mode, consider letting the user choose their preferred language at the beginning of the chat and then have the whole conversation session from that point on to be only in the preferred language. Use Handlebars to do this. For details, see [Integrating Handlebars templates](integrating-handlebars-templates.md).

You must enter a question into the QnA question bank with an utterance that is the name of the language that you are trying to set as preference, such as Spanish, coupled with the `\#setLang` Handlebar in the answer of that utterance. This utterance or question must be invoked at the point where you want to set the conversation to the preferred language. For example, you can import the **Language / Multiple Language Support** sample or extension from the QnABot **Import** menu option. This adds two questions to the system: `Language.000` and `Language.001`. The first question allows the end user to set their preferred language explicitly to a list of supported languages; the latter resets the preferred language and allows QnABot to choose the locale based on the automatically detected predominant language.

**Note**
Button values in the response cards are still displayed with their original value as input in the chat conversation.

When you deploy the QnABot on AWS guidance (version 5.5.0 and higher) CloudFormation template, a **Language** parameter lets you select one of 33 languages. This **Language** parameter is used as the core language for your QnABot on AWS deployment. The Language Analyzer for your OpenSearch index setting uses the language that you have specified in this parameter. In the case that your input has a low confidence rate, it defaults to English since that is the backup language.
+ Custom terminology also supports your `NATIVE_LANGUAGE`.
+ If using the thumbs up and down feature, you should translate *thumbs up* and *thumbs down* into your native language and put that phrase in the `PROTECTED_UTTERANCES` setting. This is to prevent it from being treated as a question by the guidance. To do this, complete the following steps:

  1. Use the AWS translate API to translate *thumbs up* and *thumbs down* to your deployment language, if it is not English.

  1. Add the translation of *thumbs up* and *thumbs down* in the website client config file inside your QnABot on AWS code and deploy.

  1. Add the translation of the *thumbs up* and *thumbs down* as a question in your QnABot deployment.

  1. Go to the content designer, navigate to the top left and select **Settings**.

  1. Find the `PROTECTED_UTTERANCES` variable and insert that phrase in by adding a comma, and then enter the translation.
+ PII redaction will still be for English, since that is still accurate with other languages.
+ Changing the `NATIVE_LANGUAGE` should always be done from the CloudFormation stack by changing the **Language** parameter.

When creating an Amazon Kendra web crawling data source from the **QnABot** UI, it will be created in the native language specified in your CloudFormation parameters. If the specified native language is not supported by Amazon Kendra, English will be used as the default language.

When querying within your Amazon Kendra data source, the following logic will be applied to determine the language used for querying:

1. The algorithm will determine the user’s locale and use the `shouldUseOriginalLanguageQuery()` function to decide whether to query in the user’s native language or the locale’s language.

1. Based on the result from `shouldUseOriginalLanguageQuery()`, it will either:
   + Use the locale’s language if it is supported by Amazon Kendra.
   + If the locale’s language is not supported, it will check if the native language (the language chosen in the CloudFormation parameters) is supported by Amazon Kendra.

1. If neither the locale’s language nor the native language is supported by Amazon Kendra, English will be used as the default language for querying.

In summary, the algorithm tries to use the user’s preferred language (either the locale or the native language specified in the CloudFormation parameters) if it is supported by Amazon Kendra. If neither language is supported, English is used as the fallback language for querying the Amazon Kendra data source.

For more information, see the [MultiLanguage Support](https://github.com/aws-solutions/qnabot-on-aws/tree/main/source/docs/multilanguage_support) section in the GitHub repository or the [Multi Language](https://catalog.us-east-1.prod.workshops.aws/workshops/20c56f9e-9c0a-4174-a661-9f40d9f063ac/en-US/deployment/optional-configurations/multi-language) section in the QnABot Workshop.

## Using automatic translation
<a name="using-automatic-translation"></a>

This guidance supports automatic translation to the end user’s language using [Amazon Translate](https://aws.amazon.com/translate/).

1. Turn on multiple-language support by setting: **ENABLE\_MULTI\_LANGUAGE\_SUPPORT** to `TRUE`*0*

1. In the web UI, ask: \_Qu’est-ce que q et a bot? \_

1. The chatbot replies to you in French.

The guidance also supports speech recognition and voice interaction in multiple languages. When you install or update QnABot on AWS, specify the languages using the **LexV2BotLocaleIds** CloudFormation parameter. The default languages are US English, US Spanish, and Canadian French, but you can customize the list to use any of the [languages supported by Amazon LexV2](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).

Use the **ENABLE\_DEBUG\_RESPONSES** setting to see how local language questions are translated to English by QnABot on AWS. Use this translation to tune the content as needed to ensure that QnABot on AWS finds the best answer to a non-English question.

The guidance also supports Amazon Translate [custom terminology](https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html) to provide additional control over the translation of entities and phrases. Custom terminology supports the language that you are deploying with. For more information on how to use the Import Custom Terminology tool in the content designer, see the [Using Custom Terminologies with Amazon Translate](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/docs/custom_terminology_guide/README.md) section in the GitHub repository.

## Configure personally identifiable information (PII) rejection and redaction
<a name="configure-personally-identifiable-information-pii-rejection-and-redaction"></a>

QnABot on AWS can detect and redact personally identifiable information (PII) using Amazon Comprehend and regular expressions.

If **ENABLE\_REDACTING** is set to `true`, the Comprehend detected PII entities will also be redacted from Amazon CloudWatch logs and OpenSearch Service logs.

 **PII rejection and redaction**

![image25](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image25.png)

For more information, see [Personally Identifiable Information (PII) Rejection and Redaction](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/docs/PII_Detection_And_Redaction/README.md) in the GitHub repository.
