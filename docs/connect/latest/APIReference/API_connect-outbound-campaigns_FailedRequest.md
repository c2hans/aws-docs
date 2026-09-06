---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_FailedRequest.html
---

# FailedRequest
<a name="API_connect-outbound-campaigns_FailedRequest"></a>

Failure details for a [DialRequest](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DialRequest.html).

## Contents
<a name="API_connect-outbound-campaigns_FailedRequest_Contents"></a>

 ** clientToken **   <a name="connect-Type-connect-outbound-campaigns_FailedRequest-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `[a-zA-Z0-9_\-.]*`
Required: No

 ** failureCode **   <a name="connect-Type-connect-outbound-campaigns_FailedRequest-failureCode"></a>
The failure code of the campaign.
Type: String
Valid Values: `InvalidInput | RequestThrottled | UnknownError`
Required: No

 ** id **   <a name="connect-Type-connect-outbound-campaigns_FailedRequest-id"></a>
The identifier of the campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: No

## See Also
<a name="API_connect-outbound-campaigns_FailedRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/FailedRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/FailedRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/FailedRequest)
