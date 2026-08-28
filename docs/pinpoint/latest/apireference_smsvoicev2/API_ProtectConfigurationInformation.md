---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ProtectConfigurationInformation.html
---

# ProtectConfigurationInformation
<a name="API_ProtectConfigurationInformation"></a>

Provides information on the specified protect configuration.

## Contents
<a name="API_ProtectConfigurationInformation_Contents"></a>

 ** AccountDefault **   <a name="pinpoint-Type-ProtectConfigurationInformation-AccountDefault"></a>
This is true if the protect configuration is set as your account default protect configuration.
Type: Boolean
Required: Yes

 ** CreatedTimestamp **   <a name="pinpoint-Type-ProtectConfigurationInformation-CreatedTimestamp"></a>
The time when the protect configuration was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: Yes

 ** DeletionProtectionEnabled **   <a name="pinpoint-Type-ProtectConfigurationInformation-DeletionProtectionEnabled"></a>
The status of deletion protection for the protect configuration. When set to true deletion protection is enabled. By default this is set to false.
Type: Boolean
Required: Yes

 ** ProtectConfigurationArn **   <a name="pinpoint-Type-ProtectConfigurationInformation-ProtectConfigurationArn"></a>
The Amazon Resource Name (ARN) of the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:\S+`
Required: Yes

 ** ProtectConfigurationId **   <a name="pinpoint-Type-ProtectConfigurationInformation-ProtectConfigurationId"></a>
The unique identifier for the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

## See Also
<a name="API_ProtectConfigurationInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/ProtectConfigurationInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/ProtectConfigurationInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/ProtectConfigurationInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
