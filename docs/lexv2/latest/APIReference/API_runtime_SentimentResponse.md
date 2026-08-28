---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_SentimentResponse.html
---

# SentimentResponse
<a name="API_runtime_SentimentResponse"></a>

Provides information about the sentiment expressed in a user's response in a conversation. Sentiments are determined using Amazon Comprehend. Sentiments are only returned if they are enabled for the bot.

For more information, see [ Determine Sentiment ](https://docs.aws.amazon.com/comprehend/latest/dg/how-sentiment.html) in the *Amazon Comprehend developer guide*.

## Contents
<a name="API_runtime_SentimentResponse_Contents"></a>

 ** sentiment **   <a name="lexv2-Type-runtime_SentimentResponse-sentiment"></a>
The overall sentiment expressed in the user's response. This is the sentiment most likely expressed by the user based on the analysis by Amazon Comprehend.
Type: String
Valid Values: `MIXED | NEGATIVE | NEUTRAL | POSITIVE`
Required: No

 ** sentimentScore **   <a name="lexv2-Type-runtime_SentimentResponse-sentimentScore"></a>
The individual sentiment responses for the utterance.
Type: [SentimentScore](API_runtime_SentimentScore.md) object
Required: No

## See Also
<a name="API_runtime_SentimentResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/runtime.lex.v2-2020-08-07/SentimentResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/runtime.lex.v2-2020-08-07/SentimentResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/runtime.lex.v2-2020-08-07/SentimentResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
