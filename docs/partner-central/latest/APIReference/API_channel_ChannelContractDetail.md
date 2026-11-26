---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ChannelContractDetail.html
---

# ChannelContractDetail

Detailed information about a channel contract.

## Contents
<a name="API_channel_ChannelContractDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="AWSPartnerCentral-Type-channel_ChannelContractDetail-arn"></a>
The Amazon Resource Name (ARN) of the channel contract.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

 ** catalog **   <a name="AWSPartnerCentral-Type-channel_ChannelContractDetail-catalog"></a>
The catalog identifier associated with the channel contract.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]*`
Required: Yes

 ** contractType **   <a name="AWSPartnerCentral-Type-channel_ChannelContractDetail-contractType"></a>
The type of the channel contract.
Type: String
Valid Values: `MANAGED_SERVICES_ATTESTATION`
Required: Yes

 ** createdAt **   <a name="AWSPartnerCentral-Type-channel_ChannelContractDetail-createdAt"></a>
The timestamp when the channel contract was created.
Type: Timestamp
Required: Yes

 ** details **   <a name="AWSPartnerCentral-Type-channel_ChannelContractDetail-details"></a>
Type-specific details of the channel contract.
Type: [ChannelContractDetails](API_channel_ChannelContractDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** id **   <a name="AWSPartnerCentral-Type-channel_ChannelContractDetail-id"></a>
The unique identifier of the channel contract.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `cc-[a-z0-9]{13}`
Required: Yes

 ** status **   <a name="AWSPartnerCentral-Type-channel_ChannelContractDetail-status"></a>
The current status of the channel contract.
Type: String
Valid Values: `PENDING | ACCEPTED | EXPIRED | CANCELED | INACTIVE`
Required: Yes

 ** updatedAt **   <a name="AWSPartnerCentral-Type-channel_ChannelContractDetail-updatedAt"></a>
The timestamp when the channel contract was last updated.
Type: Timestamp
Required: Yes

 ** cancellationReason **   <a name="AWSPartnerCentral-Type-channel_ChannelContractDetail-cancellationReason"></a>
The reason the channel contract was canceled, if one was provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[^\x00-\x1F\x7F]*`
Required: No

 ** respondedAt **   <a name="AWSPartnerCentral-Type-channel_ChannelContractDetail-respondedAt"></a>
The timestamp when the channel contract was accepted, if applicable.
Type: Timestamp
Required: No

## See Also
<a name="API_channel_ChannelContractDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/ChannelContractDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/ChannelContractDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/ChannelContractDetail)
