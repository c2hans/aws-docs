---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_UpdateCodeConfigurationParameters.html
---

# UpdateCodeConfigurationParameters
<a name="API_UpdateCodeConfigurationParameters"></a>

The loose variant of the passcode policy parameters that is used only when you update a notify code configuration. When you omit a member, its current value is preserved.

## Contents
<a name="API_UpdateCodeConfigurationParameters_Contents"></a>

 ** codeLength **   <a name="endusermessaging-Type-UpdateCodeConfigurationParameters-codeLength"></a>
The updated number of characters in the one-time passcode. Valid values range from 4 through 8. Omit this member to preserve the current value.
Type: Integer
Valid Range: Minimum value of 4. Maximum value of 8.
Required: No

 ** codeType **   <a name="endusermessaging-Type-UpdateCodeConfigurationParameters-codeType"></a>
The updated character set used to generate the one-time passcode. Omit this member to preserve the current value.
Type: String
Valid Values: `NUMERIC | ALPHA | ALPHANUMERIC`
Required: No

 ** maxAttempts **   <a name="endusermessaging-Type-UpdateCodeConfigurationParameters-maxAttempts"></a>
The updated maximum number of validation attempts that are allowed before the verification is locked. Valid values range from 1 through 5. Omit this member to preserve the current value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** validityPeriodMinutes **   <a name="endusermessaging-Type-UpdateCodeConfigurationParameters-validityPeriodMinutes"></a>
The updated length of time, in minutes, that the one-time passcode remains valid. Valid values range from 1 through 60. Omit this member to preserve the current value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60.
Required: No

## See Also
<a name="API_UpdateCodeConfigurationParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/UpdateCodeConfigurationParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/UpdateCodeConfigurationParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/UpdateCodeConfigurationParameters)
