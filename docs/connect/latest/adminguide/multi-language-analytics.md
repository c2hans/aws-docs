---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/multi-language-analytics.html
---

# Analyze contacts in more than one language using conversational analytics

In some calls, the customer and the agent speak more than one language. For example, a customer starts the call in English and then switches to Spanish. If you choose only one language, Connect Customer conversational analytics transcribes all the speech in that language.

You can choose up to five languages for a voice contact. Conversational analytics then does the following:

1. Identifies the language of each segment of the conversation.

1. Transcribes each segment in its language.

1. Applies each analytics feature to the segments whose language supports the feature.

**Topics**
+ [Things to know](#multi-language-analytics-things-to-know)
+ [How conversational analytics features work with more than one language](#multi-language-analytics-features)
+ [Choose the languages in the flow block](#multi-language-analytics-flow-block)
+ [Get the languages at run time](#multi-language-analytics-dynamic)
+ [Where to find the languages of a contact](#multi-language-analytics-where-to-find)
+ [Choose the languages by using the Flow language](#multi-language-analytics-flow-language)

## Things to know
<a name="multi-language-analytics-things-to-know"></a>

Keep the following in mind when you analyze voice contacts in more than one language, including the automated interaction with an interactive voice response (IVR) system. Chat and email contacts use one language.
+ You can choose up to five languages in the [Set recording, analytics, and processing behavior](set-recording-analytics-processing-behavior.md) flow block.
+ You can choose only one dialect of each language. For example, you can choose English (United States) or English (United Kingdom), but not both.
+ The order of the languages matters. Conversational analytics uses the first language that you choose as the preferred language for transcription, and stores it in the `LanguageLocale` field of the contact record. Put the language that you expect participants to speak most first.
+ If a participant speaks a language that you didn't choose, the transcript of that segment might be inaccurate.
+ Features such as sentiment analysis and redaction apply only to segments in languages that support them. The rest of the contact is still analyzed.
+ If you turn on redaction for post-call analytics, at least one language that you choose must support redaction. Conversational analytics redacts the entire segment if its language doesn't support redaction.
+ Summaries are generated in the most spoken language among the languages you choose that support summaries.

For supported languages, see [Languages supported by Connect Customer features](supported-languages.md#supported-languages-contact-lens). Analysis in more than one language has no additional charge beyond the standard conversational analytics pricing (see [Connect Customer pricing](https://aws.amazon.com/connect/pricing/)), and is available in the same AWS Regions as analysis in one language (see [Availability of Connect Customer features by Region](regions.md)). Languages marked with an asterisk (\*) in the supported languages table aren't available in Africa (Cape Town) or AWS GovCloud (US-West).

## How conversational analytics features work with more than one language
<a name="multi-language-analytics-features"></a>

The following table describes how each conversational analytics feature works when you choose more than one language for a contact.

**Conversational analytics features for contacts with more than one language**

| Feature | What conversational analytics does |
| --- | --- |
| Transcript | Transcribes each segment in its language. In the output file and in the real-time API, the `LanguageCode` field of each segment contains the language code of the segment. |
| Redaction | For post-call analytics, redacts sensitive data in the segments whose language supports redaction. If the language of a segment doesn't support redaction, conversational analytics redacts the entire segment, as follows:+  In the redacted transcript, in both the output file and the **Contact details** page, the text of the segment is `[Content Removed - <language code> redaction is not supported]`, for example, `[Content Removed - pl-PL redaction is not supported]`. <br />+  In the redacted audio, the segment is silent. <br />+  In the output file, the `Redaction` object of the segment contains `"Unsupported": true`.  If you turn on redaction for post-call analytics, at least one language that you choose must support redaction. To check which languages support redaction, see [Languages supported by Connect Customer features](supported-languages.md#supported-languages-contact-lens).  |
| Sentiment analysis | Analyzes the sentiment of each segment whose language supports sentiment analysis. Segments in languages that don't support sentiment analysis don't get a sentiment value. In the output file, these segments have no `Sentiment` field.<br />Conversational analytics provides contact-level sentiment scores (overall sentiment and sentiment trend) only if all the languages that you choose support sentiment analysis. If at least one of the languages doesn't support sentiment analysis, the contact has no contact-level sentiment scores. |
| Post-contact summary | Writes the summary in the most spoken language among the languages that you choose that support summaries. If none of the languages that you choose support summaries, conversational analytics doesn't write a summary. |
| Summary during After Contact Work (ACW) (real-time) | Writes the summary in the most spoken language among the languages that you choose that support summaries. If none of the languages that you choose support summaries, conversational analytics doesn't write a summary. |
| Custom vocabularies | Applies the default custom vocabulary of each language that you choose. |
| Rules | Checks the transcript in all languages for exact match and pattern match conditions. Enter the words of the rule in each language that you expect the participants to speak. |

## Choose the languages in the flow block
<a name="multi-language-analytics-flow-block"></a>

Use the following procedures to turn on analytics and choose the languages of a voice contact in the flow designer.

**To turn on recording and analytics**

1. In the flow designer, add a **Set recording, analytics, and processing behavior** block, or open an existing one.

1. For **Select action**, choose **Set recording and analytics behavior**.

1. For **Select channel**, choose **Voice**.

1. Turn on **Agent and customer interaction recording**.

1. (Optional) To analyze the automated interaction (IVR), under **Automated interaction recording**, select **Enable automated interaction**. You need this setting to use **Automated interaction analytics**.

1. Expand **Enable conversational analytics**, and then select the **Enable conversational analytics** check box.

**To choose the analytics options and the languages**

1. Under **Enable conversational analytics**, choose **Enable agent and customer interaction analytics**.

1. Choose **Post-contact analytics** or **Real-time and post-contact analytics**.

1. (Optional) To analyze the automated interaction (IVR), select **Automated interaction analytics**.

1. For **Analytics Languages**, choose up to five languages. Put the language that you expect the participants to speak most first in the list.

1. Under **Configure conversational analytics**, choose the other features that you want, such as **Conversational analytics redaction**, **Sentiment analysis**, **Agent interaction summary**, and **Automated interaction summary**.

   If one or more languages don't support a feature that you choose, a warning lists these languages. The warning doesn't prevent you from publishing the flow. Conversational analytics doesn't apply the feature to segments in those languages. For redaction, it replaces the text of those segments in the redacted transcript and silences them in the redacted audio.

   The following image shows English (United States) and Finnish (Finland) selected. Finnish doesn't support redaction or sentiment analysis, so a warning appears for each feature.
![The conversational analytics settings with English and Finnish selected as analytics languages, redaction options with a warning that Finnish isn't supported, and AI analytics options including sentiment analysis.](https://docs.aws.amazon.com/connect/latest/adminguide/images/multi-language-analytics-choose-languages.png)

1. Choose **Save**.

1. Choose **Publish**.

## Get the languages at run time
<a name="multi-language-analytics-dynamic"></a>

You can get the list of languages at run time, for example, from a Lambda function or a data table.

**Prerequisite:** If you get the languages from a Lambda function, open the **AWS Lambda function** block, and for **Response validation**, choose **JSON**. A `STRING_MAP` response can't contain a list.

**To get the languages at run time**

1. In the **Set recording, analytics, and processing behavior** block, for **Analytics Languages**, choose **Set dynamically**.

1. Choose the **Namespace** and the **Key** of the list:
   + **Lambda function** – For **Namespace**, choose **Lambda invocation**. For **Key**, choose **Result data**, and then enter `languages`. The block saves the value as `$.LambdaInvocation.ResultData.languages`.
   + **Data table** – For **Namespace**, choose **Data tables**. For **Key**, choose the query and an attribute that contains a list of text values. The block saves the value as `$.DataTables.{{query name}}.{{attribute name}}`.

1. Choose **Save**.

1. Choose **Publish**.

The following image shows **Analytics Languages** set dynamically.

![The conversational analytics settings with Analytics Languages set dynamically by using a namespace, redaction turned on with manual setup for PII data, and sentiment analysis turned on.](https://docs.aws.amazon.com/connect/latest/adminguide/images/multi-language-analytics-set-dynamically.png)

At run time, the value must be a list of one to five language codes. The first language in the list is the preferred language. The following example shows a Lambda response that returns two languages.

```json
{
    "languages": ["en-US", "es-US"]
}
```

Each entry of the list can be a language code or a JSON path, for example, `["en-US", "$.Attributes.lang"]`.

**Note**
When you publish the flow, the block can't validate dynamic languages. Instead, a warning under each feature reminds you to make sure that the languages support the feature. At run time, the block takes the **Error** branch if the list isn't valid. The list isn't valid in the following cases:
The list is empty or has more than five items.
The list contains a language more than once.
The list contains more than one dialect of a language.
The list contains an unknown language code.
Redaction is turned on, and no language in the list supports redaction.

## Where to find the languages of a contact
<a name="multi-language-analytics-where-to-find"></a>

The following table lists the fields that contain the languages of a contact.

**Fields that contain the languages of a contact**

| Where | Field | Value |
| --- | --- | --- |
| Contact record | `ContactLens.ConversationalAnalytics.Configuration.LanguageLocales` | All the languages that you set in the flow, in the order that you set them. |
| Contact record | `ContactLens.ConversationalAnalytics.Configuration.LanguageLocale` | The first language in the list (the preferred language). |
| Contact events | `contactLens.conversationalAnalytics.configuration.languageLocales` | The same values as in the contact record. |
| DescribeContact API | `Contact.ContactLens.ConversationalAnalytics.Configuration.LanguageLocales` | The same values as in the contact record. |
| Output file | `LanguageCode` at the file root | The most spoken language. |
| Output file | `LanguageCodes` at the file root | Only the languages that the participants spoke, from the languages that you choose. For voice contacts, the output file always contains this field. |
| Output file | `Configuration.LanguageLocales` | All the languages that you set in the flow, in the order that you set them. |
| Output file, real-time API, segment stream | `LanguageCode` of each transcript segment | The language of the segment. |

**Note**
The top-level `LanguageCode` of the output file is the most spoken language. The top-level `LanguageCode` of each segment stream event is the first language in the list (the preferred language). This is the same value as `LanguageLocale` in the contact record. The automated interaction and the agent conversation of the same contact can have a different most spoken language (`LanguageCode`).

## Choose the languages by using the Flow language
<a name="multi-language-analytics-flow-language"></a>

In the Flow language, use the `AnalyticsLanguages` parameter of the [UpdateContactRecordingAndAnalyticsBehavior](https://docs.aws.amazon.com/connect/latest/devguide/contact-actions-updatecontactrecordingandanalyticsbehavior.html) action. The following example turns on post-call analytics in US English and US Spanish. US English is the preferred language.

```json
"VoiceAnalyticsBehavior": {
    "Enabled": "True",
    "AnalyticsModes": ["PostContact"],
    "AnalyticsLanguages": ["en-US", "es-US"]
}
```

**Note**
Don't specify both `AnalyticsLanguage` and `AnalyticsLanguages` in the same block.
