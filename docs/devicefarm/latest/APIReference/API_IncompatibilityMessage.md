---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_IncompatibilityMessage.html
---

# IncompatibilityMessage
<a name="API_IncompatibilityMessage"></a>

Represents information about incompatibility.

## Contents
<a name="API_IncompatibilityMessage_Contents"></a>

 ** message **   <a name="devicefarm-Type-IncompatibilityMessage-message"></a>
A message about the incompatibility.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** type **   <a name="devicefarm-Type-IncompatibilityMessage-type"></a>
The type of incompatibility.
Allowed values include:
+ ARN
+ FORM\_FACTOR (for example, phone or tablet)
+ MANUFACTURER
+ PLATFORM (for example, Android or iOS)
+ REMOTE\_ACCESS\_ENABLED
+ APPIUM\_VERSION
Type: String
Valid Values: `ARN | PLATFORM | FORM_FACTOR | MANUFACTURER | REMOTE_ACCESS_ENABLED | REMOTE_DEBUG_ENABLED | APPIUM_VERSION | INSTANCE_ARN | INSTANCE_LABELS | FLEET_TYPE | OS_VERSION | MODEL | AVAILABILITY`
Required: No

## See Also
<a name="API_IncompatibilityMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/IncompatibilityMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/IncompatibilityMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/IncompatibilityMessage)
