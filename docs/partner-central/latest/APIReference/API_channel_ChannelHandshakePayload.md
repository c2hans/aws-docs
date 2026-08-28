---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ChannelHandshakePayload.html
---

# ChannelHandshakePayload
<a name="API_channel_ChannelHandshakePayload"></a>

Contains the payload data for different types of channel handshakes.

## Contents
<a name="API_channel_ChannelHandshakePayload_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** revokeServicePeriodPayload **   <a name="AWSPartnerCentral-Type-channel_ChannelHandshakePayload-revokeServicePeriodPayload"></a>
Payload for revoking a service period handshake.
Type: [RevokeServicePeriodPayload](API_channel_RevokeServicePeriodPayload.md) object
Required: No

 ** startServicePeriodPayload **   <a name="AWSPartnerCentral-Type-channel_ChannelHandshakePayload-startServicePeriodPayload"></a>
Payload for starting a service period handshake.
Type: [StartServicePeriodPayload](API_channel_StartServicePeriodPayload.md) object
Required: No

## See Also
<a name="API_channel_ChannelHandshakePayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/ChannelHandshakePayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/ChannelHandshakePayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/ChannelHandshakePayload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
