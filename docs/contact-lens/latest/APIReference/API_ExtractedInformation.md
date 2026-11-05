---
source_url: https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_ExtractedInformation.html
---

# ExtractedInformation
<a name="API_connect-contact-lens_ExtractedInformation"></a>

Segment containing information extracted from the conversation. Each segment represents the results for a single extraction definition.

## Contents
<a name="API_connect-contact-lens_ExtractedInformation_Contents"></a>

 ** ExtractionDefinitionId **   <a name="connect-Type-connect-contact-lens_ExtractedInformation-ExtractionDefinitionId"></a>
The identifier of the extraction definition that produced this result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** ExtractionDefinitionName **   <a name="connect-Type-connect-contact-lens_ExtractedInformation-ExtractionDefinitionName"></a>
The name of the extraction definition that produced this result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `.*\S.*`
Required: Yes

 ** ExtractedValues **   <a name="connect-Type-connect-contact-lens_ExtractedInformation-ExtractedValues"></a>
The list of values extracted from the conversation for this extraction definition. This field is empty when a `FailureCode` is present.
Type: Array of [ExtractedInformationValue](API_connect-contact-lens_ExtractedInformationValue.md) objects
Required: No

 ** ExtractionDefinitionDisplayLabel **   <a name="connect-Type-connect-contact-lens_ExtractedInformation-ExtractionDefinitionDisplayLabel"></a>
The display label of the extraction definition that produced this result.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 25.
Required: No

 ** FailureCode **   <a name="connect-Type-connect-contact-lens_ExtractedInformation-FailureCode"></a>
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
<a name="API_connect-contact-lens_ExtractedInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-contact-lens-2020-08-21/ExtractedInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-contact-lens-2020-08-21/ExtractedInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-contact-lens-2020-08-21/ExtractedInformation)
