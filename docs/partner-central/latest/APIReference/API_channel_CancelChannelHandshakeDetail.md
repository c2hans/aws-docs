---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_CancelChannelHandshakeDetail.html
---

# CancelChannelHandshakeDetail
<a name="API_channel_CancelChannelHandshakeDetail"></a>

Contains details about a canceled channel handshake.

## Contents
<a name="API_channel_CancelChannelHandshakeDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="AWSPartnerCentral-Type-channel_CancelChannelHandshakeDetail-arn"></a>
The Amazon Resource Name (ARN) of the canceled handshake.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: No

 ** id **   <a name="AWSPartnerCentral-Type-channel_CancelChannelHandshakeDetail-id"></a>
The unique identifier of the canceled handshake.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `ch-[a-z0-9]{13}`
Required: No

 ** status **   <a name="AWSPartnerCentral-Type-channel_CancelChannelHandshakeDetail-status"></a>
The current status of the canceled handshake.
Type: String
Valid Values: `PENDING | ACCEPTED | REJECTED | CANCELED | EXPIRED`
Required: No

## See Also
<a name="API_channel_CancelChannelHandshakeDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/CancelChannelHandshakeDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/CancelChannelHandshakeDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/CancelChannelHandshakeDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
