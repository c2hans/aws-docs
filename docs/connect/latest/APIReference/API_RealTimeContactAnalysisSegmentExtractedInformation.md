---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisSegmentExtractedInformation.html
---

# RealTimeContactAnalysisSegmentExtractedInformation
<a name="API_RealTimeContactAnalysisSegmentExtractedInformation"></a>

Segment containing information extracted from the conversation. Each segment represents the results for a single extraction definition.

## Contents
<a name="API_RealTimeContactAnalysisSegmentExtractedInformation_Contents"></a>

 ** ExtractionDefinitionId **   <a name="connect-Type-RealTimeContactAnalysisSegmentExtractedInformation-ExtractionDefinitionId"></a>
The identifier of the extraction definition that produced this result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ExtractionDefinitionName **   <a name="connect-Type-RealTimeContactAnalysisSegmentExtractedInformation-ExtractionDefinitionName"></a>
The name of the extraction definition that produced this result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** ExtractedValues **   <a name="connect-Type-RealTimeContactAnalysisSegmentExtractedInformation-ExtractedValues"></a>
The list of values extracted from the conversation for this extraction definition. This field is empty when a `FailureCode` is present.
Type: Array of [RealTimeContactAnalysisExtractedInformationValue](API_RealTimeContactAnalysisExtractedInformationValue.md) objects
Required: No

 ** ExtractionDefinitionDisplayLabel **   <a name="connect-Type-RealTimeContactAnalysisSegmentExtractedInformation-ExtractionDefinitionDisplayLabel"></a>
The display label of the extraction definition that produced this result.
Type: String
Length Constraints: Maximum length of 25.
Required: No

 ** FailureCode **   <a name="connect-Type-RealTimeContactAnalysisSegmentExtractedInformation-FailureCode"></a>
If the information failed to be extracted, one of the following failure codes occurs:
+  `QUOTA_EXCEEDED`: The number of concurrent analytics jobs reached your service quota.
+  `INSUFFICIENT_CONVERSATION_CONTENT`: Information extraction requires a conversation with at least one turn from each participant.
+  `FAILED_SAFETY_GUIDELINES`: The extracted information cannot be provided because it failed to meet system safety guidelines.
+  `INTERNAL_ERROR`: Internal system error.
+  `MAX_PACKAGE_FEATURE_ONLY`: Information extraction is only available in Amazon Connect Customer instances.
Type: String
Valid Values: `QUOTA_EXCEEDED | INSUFFICIENT_CONVERSATION_CONTENT | FAILED_SAFETY_GUIDELINES | INTERNAL_ERROR | MAX_PACKAGE_FEATURE_ONLY`
Required: No

## See Also
<a name="API_RealTimeContactAnalysisSegmentExtractedInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RealTimeContactAnalysisSegmentExtractedInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RealTimeContactAnalysisSegmentExtractedInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RealTimeContactAnalysisSegmentExtractedInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
