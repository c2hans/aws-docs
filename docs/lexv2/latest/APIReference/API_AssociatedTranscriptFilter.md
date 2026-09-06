---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AssociatedTranscriptFilter.html
---

# AssociatedTranscriptFilter
<a name="API_AssociatedTranscriptFilter"></a>

Filters to search for the associated transcript.

## Contents
<a name="API_AssociatedTranscriptFilter_Contents"></a>

 ** name **   <a name="lexv2-Type-AssociatedTranscriptFilter-name"></a>
The name of the field to use for filtering. The allowed names are IntentId and SlotTypeId.
Type: String
Valid Values: `IntentId | SlotTypeId`
Required: Yes

 ** values **   <a name="lexv2-Type-AssociatedTranscriptFilter-values"></a>
The values to use to filter the transcript.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[0-9a-zA-Z_()\s-]+$`
Required: Yes

## See Also
<a name="API_AssociatedTranscriptFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AssociatedTranscriptFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AssociatedTranscriptFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AssociatedTranscriptFilter)
