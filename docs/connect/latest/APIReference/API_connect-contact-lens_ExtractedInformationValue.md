---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-contact-lens_ExtractedInformationValue.html
---

# ExtractedInformationValue
<a name="API_connect-contact-lens_ExtractedInformationValue"></a>

An individual value extracted from the conversation, including its content and the locations where it was found.

## Contents
<a name="API_connect-contact-lens_ExtractedInformationValue_Contents"></a>

 ** Content **   <a name="connect-Type-connect-contact-lens_ExtractedInformationValue-Content"></a>
The text content of the extracted value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** PointsOfInterest **   <a name="connect-Type-connect-contact-lens_ExtractedInformationValue-PointsOfInterest"></a>
The sections in the conversation that indicate where the extracted value was found.
Type: Array of [PointOfInterest](API_connect-contact-lens_PointOfInterest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: Yes

## See Also
<a name="API_connect-contact-lens_ExtractedInformationValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-contact-lens-2020-08-21/ExtractedInformationValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-contact-lens-2020-08-21/ExtractedInformationValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-contact-lens-2020-08-21/ExtractedInformationValue)
