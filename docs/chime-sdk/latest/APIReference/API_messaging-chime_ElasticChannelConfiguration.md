---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ElasticChannelConfiguration.html
---

# ElasticChannelConfiguration
<a name="API_messaging-chime_ElasticChannelConfiguration"></a>

The attributes required to configure and create an elastic channel. An elastic channel can support a maximum of 1-million members.

## Contents
<a name="API_messaging-chime_ElasticChannelConfiguration_Contents"></a>

 ** MaximumSubChannels **   <a name="chimesdk-Type-messaging-chime_ElasticChannelConfiguration-MaximumSubChannels"></a>
The maximum number of SubChannels that you want to allow in the elastic channel.
Type: Integer
Valid Range: Minimum value of 2.
Required: Yes

 ** MinimumMembershipPercentage **   <a name="chimesdk-Type-messaging-chime_ElasticChannelConfiguration-MinimumMembershipPercentage"></a>
The minimum allowed percentage of TargetMembershipsPerSubChannel users. Ceil of the calculated value is used in balancing members among SubChannels of the elastic channel.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 40.
Required: Yes

 ** TargetMembershipsPerSubChannel **   <a name="chimesdk-Type-messaging-chime_ElasticChannelConfiguration-TargetMembershipsPerSubChannel"></a>
The maximum number of members allowed in a SubChannel.
Type: Integer
Valid Range: Minimum value of 2.
Required: Yes

## See Also
<a name="API_messaging-chime_ElasticChannelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/ElasticChannelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/ElasticChannelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/ElasticChannelConfiguration)
