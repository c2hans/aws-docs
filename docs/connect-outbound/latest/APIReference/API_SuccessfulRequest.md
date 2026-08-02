---
source_url: https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_SuccessfulRequest.html
---

# SuccessfulRequest
<a name="API_connect-outbound-campaigns_SuccessfulRequest"></a>

Success details for a [DialRequest](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DialRequest.html).

## Contents
<a name="API_connect-outbound-campaigns_SuccessfulRequest_Contents"></a>

 ** clientToken **   <a name="connect-Type-connect-outbound-campaigns_SuccessfulRequest-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `[a-zA-Z0-9_\-.]*`
Required: No

 ** id **   <a name="connect-Type-connect-outbound-campaigns_SuccessfulRequest-id"></a>
The identifier of the dial request, which is the identifier of the contact in the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: No

## See Also
<a name="API_connect-outbound-campaigns_SuccessfulRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/SuccessfulRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/SuccessfulRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/SuccessfulRequest)
