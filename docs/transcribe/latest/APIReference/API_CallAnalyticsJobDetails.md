---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CallAnalyticsJobDetails.html
---

# CallAnalyticsJobDetails
<a name="API_CallAnalyticsJobDetails"></a>

Contains details about a call analytics job, including information about skipped analytics features.

## Contents
<a name="API_CallAnalyticsJobDetails_Contents"></a>

 ** Skipped **   <a name="transcribe-Type-CallAnalyticsJobDetails-Skipped"></a>
Contains information about any skipped analytics features during the analysis of a call analytics job.
This array lists all the analytics features that were skipped, along with their corresponding reason code and message.
Type: Array of [CallAnalyticsSkippedFeature](API_CallAnalyticsSkippedFeature.md) objects
Required: No

## See Also
<a name="API_CallAnalyticsJobDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/CallAnalyticsJobDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/CallAnalyticsJobDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/CallAnalyticsJobDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Transcribe. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transcribe` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
