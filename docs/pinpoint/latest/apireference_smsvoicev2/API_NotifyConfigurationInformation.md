---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_NotifyConfigurationInformation.html
---

# NotifyConfigurationInformation
<a name="API_NotifyConfigurationInformation"></a>

The information for a notify configuration in an AWS account.

## Contents
<a name="API_NotifyConfigurationInformation_Contents"></a>

 ** CreatedTimestamp **   <a name="pinpoint-Type-NotifyConfigurationInformation-CreatedTimestamp"></a>
The time when the notify configuration was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: Yes

 ** DeletionProtectionEnabled **   <a name="pinpoint-Type-NotifyConfigurationInformation-DeletionProtectionEnabled"></a>
When set to true deletion protection is enabled. By default this is set to false.
Type: Boolean
Required: Yes

 ** DisplayName **   <a name="pinpoint-Type-NotifyConfigurationInformation-DisplayName"></a>
The display name associated with the notify configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `[A-Za-z0-9_ -]+`
Required: Yes

 ** EnabledChannels **   <a name="pinpoint-Type-NotifyConfigurationInformation-EnabledChannels"></a>
An array of channels enabled for the notify configuration. Supported values include `SMS` and `VOICE`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SMS | VOICE | MMS | RCS`
Required: Yes

 ** NotifyConfigurationArn **   <a name="pinpoint-Type-NotifyConfigurationInformation-NotifyConfigurationArn"></a>
The Amazon Resource Name (ARN) for the notify configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:\S+`
Required: Yes

 ** NotifyConfigurationId **   <a name="pinpoint-Type-NotifyConfigurationInformation-NotifyConfigurationId"></a>
The unique identifier for the notify configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** Status **   <a name="pinpoint-Type-NotifyConfigurationInformation-Status"></a>
The current status of the notify configuration.
Type: String
Valid Values: `PENDING | ACTIVE | REJECTED | REQUIRES_VERIFICATION`
Required: Yes

 ** Tier **   <a name="pinpoint-Type-NotifyConfigurationInformation-Tier"></a>
The tier of the notify configuration.
Type: String
Valid Values: `BASIC | ADVANCED`
Required: Yes

 ** TierUpgradeStatus **   <a name="pinpoint-Type-NotifyConfigurationInformation-TierUpgradeStatus"></a>
The tier upgrade status of the notify configuration.
Type: String
Valid Values: `BASIC | PENDING_UPGRADE | ADVANCED | REJECTED`
Required: Yes

 ** UseCase **   <a name="pinpoint-Type-NotifyConfigurationInformation-UseCase"></a>
The use case for the notify configuration.
Type: String
Valid Values: `CODE_VERIFICATION`
Required: Yes

 ** DefaultTemplateId **   <a name="pinpoint-Type-NotifyConfigurationInformation-DefaultTemplateId"></a>
The default template identifier associated with the notify configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([A-Za-z0-9_-]*|UNSET_DEFAULT_TEMPLATE)`
Required: No

 ** EnabledCountries **   <a name="pinpoint-Type-NotifyConfigurationInformation-EnabledCountries"></a>
An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, that are enabled for the notify configuration.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: No

 ** PoolId **   <a name="pinpoint-Type-NotifyConfigurationInformation-PoolId"></a>
The identifier of the pool associated with the notify configuration.
Type: String
Required: No

 ** RejectionReason **   <a name="pinpoint-Type-NotifyConfigurationInformation-RejectionReason"></a>
The reason the notify configuration was rejected, if applicable.
Type: String
Required: No

## See Also
<a name="API_NotifyConfigurationInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/NotifyConfigurationInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/NotifyConfigurationInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/NotifyConfigurationInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
