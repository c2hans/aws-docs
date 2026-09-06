---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ChannelTargetInfo.html
---

# ChannelTargetInfo
<a name="API_SSMContacts_ChannelTargetInfo"></a>

Information about the contact channel that Incident Manager uses to engage the contact.

## Contents
<a name="API_SSMContacts_ChannelTargetInfo_Contents"></a>

 ** ContactChannelId **   <a name="IncidentManager-Type-SSMContacts_ChannelTargetInfo-ContactChannelId"></a>
The Amazon Resource Name (ARN) of the contact channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** RetryIntervalInMinutes **   <a name="IncidentManager-Type-SSMContacts_ChannelTargetInfo-RetryIntervalInMinutes"></a>
The number of minutes to wait before retrying to send engagement if the engagement initially failed.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 60.
Required: No

## See Also
<a name="API_SSMContacts_ChannelTargetInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/ChannelTargetInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/ChannelTargetInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/ChannelTargetInfo)
