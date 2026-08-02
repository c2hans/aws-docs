---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_OutboundRequest.html
---

# OutboundRequest
<a name="API_connect-outbound-campaigns-v2_OutboundRequest"></a>

Contains information about a outbound request.

## Contents
<a name="API_connect-outbound-campaigns-v2_OutboundRequest_Contents"></a>

 ** channelSubtypeParameters **   <a name="connect-Type-connect-outbound-campaigns-v2_OutboundRequest-channelSubtypeParameters"></a>
The overridden channel subtype parameters for an outbound request of a campaign.
Type: [ChannelSubtypeParameters](API_connect-outbound-campaigns-v2_ChannelSubtypeParameters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** clientToken **   <a name="connect-Type-connect-outbound-campaigns-v2_OutboundRequest-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/). The token is valid for 7 days after creation. If a dial request is already created, the dial request ID is returned.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `[a-zA-Z0-9_\-.]*`
Required: Yes

 ** expirationTime **   <a name="connect-Type-connect-outbound-campaigns-v2_OutboundRequest-expirationTime"></a>
A UNIX timestamp that specifies when a dial request expires.
Type: Timestamp
Required: Yes

## See Also
<a name="API_connect-outbound-campaigns-v2_OutboundRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/OutboundRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/OutboundRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/OutboundRequest)
