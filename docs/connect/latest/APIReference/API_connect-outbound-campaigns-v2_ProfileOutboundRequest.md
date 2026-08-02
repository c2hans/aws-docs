---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_ProfileOutboundRequest.html
---

# ProfileOutboundRequest
<a name="API_connect-outbound-campaigns-v2_ProfileOutboundRequest"></a>

Contains information about a profile outbound request.

## Contents
<a name="API_connect-outbound-campaigns-v2_ProfileOutboundRequest_Contents"></a>

 ** clientToken **   <a name="connect-Type-connect-outbound-campaigns-v2_ProfileOutboundRequest-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/). The token is valid for 7 days after creation. If a profile outbound request is already created, the profile outbound request ID is returned.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `[a-zA-Z0-9_\-.]*`
Required: Yes

 ** profileId **   <a name="connect-Type-connect-outbound-campaigns-v2_ProfileOutboundRequest-profileId"></a>
The identifier of the customer profile.
Type: String
Pattern: `[a-f0-9]{32}`
Required: Yes

 ** eventTriggerContext **   <a name="connect-Type-connect-outbound-campaigns-v2_ProfileOutboundRequest-eventTriggerContext"></a>
The event trigger context, including the source event and channel context, for the profile outbound request.
Type: [EventTriggerContext](API_connect-outbound-campaigns-v2_EventTriggerContext.md) object
Required: No

 ** expirationTime **   <a name="connect-Type-connect-outbound-campaigns-v2_ProfileOutboundRequest-expirationTime"></a>
A UNIX timestamp that specifies when a profile outbound request expires.
Type: Timestamp
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_ProfileOutboundRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/ProfileOutboundRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/ProfileOutboundRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/ProfileOutboundRequest)
