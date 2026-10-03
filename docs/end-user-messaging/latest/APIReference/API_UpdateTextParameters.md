---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_UpdateTextParameters.html
---

# UpdateTextParameters
<a name="API_UpdateTextParameters"></a>

The updated delivery parameters for the text channel. Absent members preserve the current value, and the empty sentinel on a member clears it.

## Contents
<a name="API_UpdateTextParameters_Contents"></a>

 ** destinationCountryParameters **   <a name="endusermessaging-Type-UpdateTextParameters-destinationCountryParameters"></a>
The updated map of country-specific parameters that control one-time passcode delivery. An empty map clears the previously stored value.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `\S+`
Value Length Constraints: Minimum length of 1. Maximum length of 64.
Value Pattern: `\S+`
Required: No

 ** inlineTemplateBody **   <a name="endusermessaging-Type-UpdateTextParameters-inlineTemplateBody"></a>
The updated freeform SMS or RCS template body. An empty string clears the previously stored value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 6000.
Pattern: `([\s\S]*\S[\s\S]*)?`
Required: No

## See Also
<a name="API_UpdateTextParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/UpdateTextParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/UpdateTextParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/UpdateTextParameters)
