---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ChannelContractSummary.html
---

# ChannelContractSummary

Summary information about a channel contract.

## Contents
<a name="API_channel_ChannelContractSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="AWSPartnerCentral-Type-channel_ChannelContractSummary-arn"></a>
The Amazon Resource Name (ARN) of the channel contract.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

 ** catalog **   <a name="AWSPartnerCentral-Type-channel_ChannelContractSummary-catalog"></a>
The catalog identifier associated with the channel contract.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]*`
Required: Yes

 ** contractType **   <a name="AWSPartnerCentral-Type-channel_ChannelContractSummary-contractType"></a>
The type of the channel contract.
Type: String
Valid Values: `MANAGED_SERVICES_ATTESTATION`
Required: Yes

 ** createdAt **   <a name="AWSPartnerCentral-Type-channel_ChannelContractSummary-createdAt"></a>
The timestamp when the channel contract was created.
Type: Timestamp
Required: Yes

 ** details **   <a name="AWSPartnerCentral-Type-channel_ChannelContractSummary-details"></a>
Type-specific summary details of the channel contract.
Type: [ChannelContractSummaryDetails](API_channel_ChannelContractSummaryDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** id **   <a name="AWSPartnerCentral-Type-channel_ChannelContractSummary-id"></a>
The unique identifier of the channel contract.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `cc-[a-z0-9]{13}`
Required: Yes

 ** status **   <a name="AWSPartnerCentral-Type-channel_ChannelContractSummary-status"></a>
The current status of the channel contract.
Type: String
Valid Values: `PENDING | ACCEPTED | EXPIRED | CANCELED | INACTIVE`
Required: Yes

 ** updatedAt **   <a name="AWSPartnerCentral-Type-channel_ChannelContractSummary-updatedAt"></a>
The timestamp when the channel contract was last updated.
Type: Timestamp
Required: Yes

 ** respondedAt **   <a name="AWSPartnerCentral-Type-channel_ChannelContractSummary-respondedAt"></a>
The timestamp when the channel contract was accepted, if applicable.
Type: Timestamp
Required: No

## See Also
<a name="API_channel_ChannelContractSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/ChannelContractSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/ChannelContractSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/ChannelContractSummary)
