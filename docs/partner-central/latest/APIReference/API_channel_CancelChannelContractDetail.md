---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_CancelChannelContractDetail.html
---

# CancelChannelContractDetail

Contains details about a canceled channel contract.

## Contents
<a name="API_channel_CancelChannelContractDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="AWSPartnerCentral-Type-channel_CancelChannelContractDetail-arn"></a>
The Amazon Resource Name (ARN) of the canceled channel contract.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: No

 ** cancellationReason **   <a name="AWSPartnerCentral-Type-channel_CancelChannelContractDetail-cancellationReason"></a>
The reason the channel contract was canceled, if one was provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[^\x00-\x1F\x7F]*`
Required: No

 ** id **   <a name="AWSPartnerCentral-Type-channel_CancelChannelContractDetail-id"></a>
The unique identifier of the canceled channel contract.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `cc-[a-z0-9]{13}`
Required: No

 ** status **   <a name="AWSPartnerCentral-Type-channel_CancelChannelContractDetail-status"></a>
The current status of the canceled channel contract.
Type: String
Valid Values: `PENDING | ACCEPTED | EXPIRED | CANCELED | INACTIVE`
Required: No

## See Also
<a name="API_channel_CancelChannelContractDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/CancelChannelContractDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/CancelChannelContractDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/CancelChannelContractDetail)
