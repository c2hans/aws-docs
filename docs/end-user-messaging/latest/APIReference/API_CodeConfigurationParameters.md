---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_CodeConfigurationParameters.html
---

# CodeConfigurationParameters
<a name="API_CodeConfigurationParameters"></a>

The passcode policy parameters that are grouped for reuse across a notify code configuration and its create request. Each member is optional. When you omit a member on a create request, no value is applied at create time and the default is applied when a passcode is sent.

## Contents
<a name="API_CodeConfigurationParameters_Contents"></a>

 ** codeLength **   <a name="endusermessaging-Type-CodeConfigurationParameters-codeLength"></a>
The number of characters in the one-time passcode. Valid values range from 4 through 8. When you do not specify a value, the default is applied when a passcode is sent.
Type: Integer
Valid Range: Minimum value of 4. Maximum value of 8.
Required: No

 ** codeType **   <a name="endusermessaging-Type-CodeConfigurationParameters-codeType"></a>
The character set used to generate the one-time passcode. Valid values are NUMERIC (digits only), ALPHA (uppercase letters only), and ALPHANUMERIC (uppercase letters and digits). When you do not specify a value, the default is applied when a passcode is sent.
Type: String
Valid Values: `NUMERIC | ALPHA | ALPHANUMERIC`
Required: No

 ** maxAttempts **   <a name="endusermessaging-Type-CodeConfigurationParameters-maxAttempts"></a>
The maximum number of validation attempts that are allowed before the verification is locked. Valid values range from 1 through 5. When you do not specify a value, the default is applied when a passcode is sent.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** validityPeriodMinutes **   <a name="endusermessaging-Type-CodeConfigurationParameters-validityPeriodMinutes"></a>
The length of time, in minutes, that the one-time passcode remains valid. Valid values range from 1 through 60. When you do not specify a value, the default is applied when a passcode is sent.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60.
Required: No

## See Also
<a name="API_CodeConfigurationParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/CodeConfigurationParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/CodeConfigurationParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/CodeConfigurationParameters)
