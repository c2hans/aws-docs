---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_SuccessfulProfileOutboundRequest.html
---

# SuccessfulProfileOutboundRequest
<a name="API_connect-outbound-campaigns-v2_SuccessfulProfileOutboundRequest"></a>

Success details for a profile outbound request.

## Contents
<a name="API_connect-outbound-campaigns-v2_SuccessfulProfileOutboundRequest_Contents"></a>

 ** clientToken **   <a name="connect-Type-connect-outbound-campaigns-v2_SuccessfulProfileOutboundRequest-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `[a-zA-Z0-9_\-.]*`
Required: No

 ** id **   <a name="connect-Type-connect-outbound-campaigns-v2_SuccessfulProfileOutboundRequest-id"></a>
The identifier of the profile outbound request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\-.]*`
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_SuccessfulProfileOutboundRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/SuccessfulProfileOutboundRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/SuccessfulProfileOutboundRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/SuccessfulProfileOutboundRequest)
