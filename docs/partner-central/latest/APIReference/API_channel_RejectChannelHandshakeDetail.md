---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_RejectChannelHandshakeDetail.html
---

# RejectChannelHandshakeDetail
<a name="API_channel_RejectChannelHandshakeDetail"></a>

Contains details about a rejected channel handshake.

## Contents
<a name="API_channel_RejectChannelHandshakeDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="AWSPartnerCentral-Type-channel_RejectChannelHandshakeDetail-arn"></a>
The Amazon Resource Name (ARN) of the rejected handshake.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: No

 ** id **   <a name="AWSPartnerCentral-Type-channel_RejectChannelHandshakeDetail-id"></a>
The unique identifier of the rejected handshake.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `ch-[a-z0-9]{13}`
Required: No

 ** status **   <a name="AWSPartnerCentral-Type-channel_RejectChannelHandshakeDetail-status"></a>
The current status of the rejected handshake.
Type: String
Valid Values: `PENDING | ACCEPTED | REJECTED | CANCELED | EXPIRED`
Required: No

## See Also
<a name="API_channel_RejectChannelHandshakeDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/RejectChannelHandshakeDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/RejectChannelHandshakeDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/RejectChannelHandshakeDetail)
