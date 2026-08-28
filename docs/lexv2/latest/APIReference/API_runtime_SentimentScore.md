---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_SentimentScore.html
---

# SentimentScore
<a name="API_runtime_SentimentScore"></a>

The individual sentiment responses for the utterance.

## Contents
<a name="API_runtime_SentimentScore_Contents"></a>

 ** mixed **   <a name="lexv2-Type-runtime_SentimentScore-mixed"></a>
The level of confidence that Amazon Comprehend has in the accuracy of its detection of the `MIXED` sentiment.
Type: Double
Required: No

 ** negative **   <a name="lexv2-Type-runtime_SentimentScore-negative"></a>
The level of confidence that Amazon Comprehend has in the accuracy of its detection of the `NEGATIVE` sentiment.
Type: Double
Required: No

 ** neutral **   <a name="lexv2-Type-runtime_SentimentScore-neutral"></a>
The level of confidence that Amazon Comprehend has in the accuracy of its detection of the `NEUTRAL` sentiment.
Type: Double
Required: No

 ** positive **   <a name="lexv2-Type-runtime_SentimentScore-positive"></a>
The level of confidence that Amazon Comprehend has in the accuracy of its detection of the `POSITIVE` sentiment.
Type: Double
Required: No

## See Also
<a name="API_runtime_SentimentScore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/runtime.lex.v2-2020-08-07/SentimentScore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/runtime.lex.v2-2020-08-07/SentimentScore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/runtime.lex.v2-2020-08-07/SentimentScore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
