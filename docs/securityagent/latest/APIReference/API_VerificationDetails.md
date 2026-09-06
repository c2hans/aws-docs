---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_VerificationDetails.html
---

# VerificationDetails
<a name="API_VerificationDetails"></a>

Contains the verification details for a target domain, including the verification method and provider-specific details.

## Contents
<a name="API_VerificationDetails_Contents"></a>

 ** dnsTxt **   <a name="securityagent-Type-VerificationDetails-dnsTxt"></a>
The DNS TXT verification details.
Type: [DnsVerification](API_DnsVerification.md) object
Required: No

 ** httpRoute **   <a name="securityagent-Type-VerificationDetails-httpRoute"></a>
The HTTP route verification details.
Type: [HttpVerification](API_HttpVerification.md) object
Required: No

 ** method **   <a name="securityagent-Type-VerificationDetails-method"></a>
The verification method used for the target domain.
Type: String
Valid Values: `DNS_TXT | HTTP_ROUTE | PRIVATE_VPC`
Required: No

## See Also
<a name="API_VerificationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/VerificationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/VerificationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/VerificationDetails)
