---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ChannelHandshakeSummary.html
---

# ChannelHandshakeSummary
<a name="API_channel_ChannelHandshakeSummary"></a>

Summary information about a channel handshake.

## Contents
<a name="API_channel_ChannelHandshakeSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="AWSPartnerCentral-Type-channel_ChannelHandshakeSummary-arn"></a>
The Amazon Resource Name (ARN) of the handshake.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: No

 ** associatedResourceId **   <a name="AWSPartnerCentral-Type-channel_ChannelHandshakeSummary-associatedResourceId"></a>
The identifier of the resource associated with the handshake.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 17.
Pattern: `(pma|rs)-[a-z0-9]{13}`
Required: No

 ** catalog **   <a name="AWSPartnerCentral-Type-channel_ChannelHandshakeSummary-catalog"></a>
The catalog identifier associated with the handshake.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]*`
Required: No

 ** createdAt **   <a name="AWSPartnerCentral-Type-channel_ChannelHandshakeSummary-createdAt"></a>
The timestamp when the handshake was created.
Type: Timestamp
Required: No

 ** detail **   <a name="AWSPartnerCentral-Type-channel_ChannelHandshakeSummary-detail"></a>
Detailed information about the handshake.
Type: [HandshakeDetail](API_channel_HandshakeDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** handshakeType **   <a name="AWSPartnerCentral-Type-channel_ChannelHandshakeSummary-handshakeType"></a>
The type of the handshake.
Type: String
Valid Values: `START_SERVICE_PERIOD | REVOKE_SERVICE_PERIOD | PROGRAM_MANAGEMENT_ACCOUNT`
Required: No

 ** id **   <a name="AWSPartnerCentral-Type-channel_ChannelHandshakeSummary-id"></a>
The unique identifier of the handshake.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `ch-[a-z0-9]{13}`
Required: No

 ** ownerAccountId **   <a name="AWSPartnerCentral-Type-channel_ChannelHandshakeSummary-ownerAccountId"></a>
The AWS account ID of the handshake owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: No

 ** receiverAccountId **   <a name="AWSPartnerCentral-Type-channel_ChannelHandshakeSummary-receiverAccountId"></a>
The AWS account ID of the handshake receiver.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: No

 ** senderAccountId **   <a name="AWSPartnerCentral-Type-channel_ChannelHandshakeSummary-senderAccountId"></a>
The AWS account ID of the handshake sender.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: No

 ** senderDisplayName **   <a name="AWSPartnerCentral-Type-channel_ChannelHandshakeSummary-senderDisplayName"></a>
The display name of the handshake sender.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[\x00-\x7E\xA9\xAE\xA2-\xA5\u202F]+`
Required: No

 ** status **   <a name="AWSPartnerCentral-Type-channel_ChannelHandshakeSummary-status"></a>
The current status of the handshake.
Type: String
Valid Values: `PENDING | ACCEPTED | REJECTED | CANCELED | EXPIRED`
Required: No

 ** updatedAt **   <a name="AWSPartnerCentral-Type-channel_ChannelHandshakeSummary-updatedAt"></a>
The timestamp when the handshake was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_channel_ChannelHandshakeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/ChannelHandshakeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/ChannelHandshakeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/ChannelHandshakeSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
