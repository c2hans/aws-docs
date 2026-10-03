---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_NotifyCodeConfiguration.html
---

# NotifyCodeConfiguration
<a name="API_NotifyCodeConfiguration"></a>

Contains the settings of a notify code configuration, which is a reusable one-time passcode policy.

## Contents
<a name="API_NotifyCodeConfiguration_Contents"></a>

 ** createdAt **   <a name="endusermessaging-Type-NotifyCodeConfiguration-createdAt"></a>
The time when the resource was created, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** deletionProtectionEnabled **   <a name="endusermessaging-Type-NotifyCodeConfiguration-deletionProtectionEnabled"></a>
Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.
Type: Boolean
Required: Yes

 ** notifyCodeConfigurationArn **   <a name="endusermessaging-Type-NotifyCodeConfiguration-notifyCodeConfigurationArn"></a>
The Amazon Resource Name (ARN) of the notify code configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 256.
Pattern: `arn:[A-Za-z0-9_:/-]+`
Required: Yes

 ** notifyCodeConfigurationId **   <a name="endusermessaging-Type-NotifyCodeConfiguration-notifyCodeConfigurationId"></a>
The unique identifier of the notify code configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** notifyCodeConfigurationName **   <a name="endusermessaging-Type-NotifyCodeConfiguration-notifyCodeConfigurationName"></a>
The name of the notify code configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`
Required: Yes

 ** updatedAt **   <a name="endusermessaging-Type-NotifyCodeConfiguration-updatedAt"></a>
The time when the resource was last updated, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** channelParameters **   <a name="endusermessaging-Type-NotifyCodeConfiguration-channelParameters"></a>
The channel-specific parameters used to render and deliver the one-time passcode. A configuration can carry parameters for every channel at once, and the send route selects the matching channel at send time.
Type: [ChannelParameters](API_ChannelParameters.md) object
Required: No

 ** codeConfigurationParameters **   <a name="endusermessaging-Type-NotifyCodeConfiguration-codeConfigurationParameters"></a>
The passcode policy parameters, including the code type, length, validity period, and maximum number of attempts.
Type: [CodeConfigurationParameters](API_CodeConfigurationParameters.md) object
Required: No

## See Also
<a name="API_NotifyCodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/NotifyCodeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/NotifyCodeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/NotifyCodeConfiguration)
