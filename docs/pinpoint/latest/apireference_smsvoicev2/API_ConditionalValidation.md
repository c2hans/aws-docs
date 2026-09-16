---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ConditionalValidation.html
---

# ConditionalValidation
<a name="API_ConditionalValidation"></a>

Per-rule validation constraints that override the field's default validation when the containing rule matches. All fields are optional; only the constraints that need to differ from the field's default validation are provided.

## Contents
<a name="API_ConditionalValidation_Contents"></a>

 ** AllowedValues **   <a name="pinpoint-Type-ConditionalValidation-AllowedValues"></a>
The allowed values for a select field when this rule applies. A subset of the field's full option list.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** MaxLength **   <a name="pinpoint-Type-ConditionalValidation-MaxLength"></a>
The maximum length for the field value when this rule applies.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MinLength **   <a name="pinpoint-Type-ConditionalValidation-MinLength"></a>
The minimum length for the field value when this rule applies.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Pattern **   <a name="pinpoint-Type-ConditionalValidation-Pattern"></a>
A regular expression that the field value must match when this rule applies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_ConditionalValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/ConditionalValidation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/ConditionalValidation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/ConditionalValidation)
