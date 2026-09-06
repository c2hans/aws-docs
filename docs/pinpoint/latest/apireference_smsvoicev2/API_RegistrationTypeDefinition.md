---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RegistrationTypeDefinition.html
---

# RegistrationTypeDefinition
<a name="API_RegistrationTypeDefinition"></a>

Provides information on the supported registration type.

## Contents
<a name="API_RegistrationTypeDefinition_Contents"></a>

 ** DisplayHints **   <a name="pinpoint-Type-RegistrationTypeDefinition-DisplayHints"></a>
Provides help information on the registration.
Type: [RegistrationTypeDisplayHints](API_RegistrationTypeDisplayHints.md) object
Required: Yes

 ** RegistrationType **   <a name="pinpoint-Type-RegistrationTypeDefinition-RegistrationType"></a>
The type of registration form. The list of **RegistrationTypes** can be found using the [DescribeRegistrationTypeDefinitions](API_DescribeRegistrationTypeDefinitions.md) action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_]+`
Required: Yes

 ** SupportedAssociations **   <a name="pinpoint-Type-RegistrationTypeDefinition-SupportedAssociations"></a>
The supported association behavior for the registration type.
Type: Array of [SupportedAssociation](API_SupportedAssociation.md) objects
Required: No

## See Also
<a name="API_RegistrationTypeDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RegistrationTypeDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RegistrationTypeDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RegistrationTypeDefinition)
