---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_TextParameters.html
---

# TextParameters
<a name="API_TextParameters"></a>

The delivery parameters for the text channel, which delivers over SMS or RCS.

## Contents
<a name="API_TextParameters_Contents"></a>

 ** destinationCountryParameters **   <a name="endusermessaging-Type-TextParameters-destinationCountryParameters"></a>
A map of country-specific parameters that control one-time passcode delivery.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `\S+`
Value Length Constraints: Minimum length of 1. Maximum length of 64.
Value Pattern: `\S+`
Required: No

 ** inlineTemplateBody **   <a name="endusermessaging-Type-TextParameters-inlineTemplateBody"></a>
The freeform message template used to render the one-time passcode for the SMS or RCS channels. The template must contain the code placeholder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6000.
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

## See Also
<a name="API_TextParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/TextParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/TextParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/TextParameters)
