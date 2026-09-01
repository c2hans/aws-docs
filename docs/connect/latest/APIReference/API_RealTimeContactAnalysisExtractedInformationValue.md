---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisExtractedInformationValue.html
---

# RealTimeContactAnalysisExtractedInformationValue
<a name="API_RealTimeContactAnalysisExtractedInformationValue"></a>

An individual value extracted from the conversation, including its content and the locations where it was found.

## Contents
<a name="API_RealTimeContactAnalysisExtractedInformationValue_Contents"></a>

 ** Content **   <a name="connect-Type-RealTimeContactAnalysisExtractedInformationValue-Content"></a>
The text content of the extracted value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** PointsOfInterest **   <a name="connect-Type-RealTimeContactAnalysisExtractedInformationValue-PointsOfInterest"></a>
The sections in the conversation that indicate where the extracted value was found.
Type: Array of [RealTimeContactAnalysisTranscriptItemWithCharacterOffsets](API_RealTimeContactAnalysisTranscriptItemWithCharacterOffsets.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_RealTimeContactAnalysisExtractedInformationValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RealTimeContactAnalysisExtractedInformationValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RealTimeContactAnalysisExtractedInformationValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RealTimeContactAnalysisExtractedInformationValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
