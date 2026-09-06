---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_TargetDomain.html
---

# TargetDomain
<a name="API_TargetDomain"></a>

Represents a target domain registered for penetration testing. A target domain must be verified through DNS TXT or HTTP route verification before it can be used in pentests.

## Contents
<a name="API_TargetDomain_Contents"></a>

 ** domainName **   <a name="securityagent-Type-TargetDomain-domainName"></a>
The domain name of the target domain.
Type: String
Required: Yes

 ** targetDomainId **   <a name="securityagent-Type-TargetDomain-targetDomainId"></a>
The unique identifier of the target domain.
Type: String
Required: Yes

 ** createdAt **   <a name="securityagent-Type-TargetDomain-createdAt"></a>
The date and time the target domain was created, in UTC format.
Type: Timestamp
Required: No

 ** verificationDetails **   <a name="securityagent-Type-TargetDomain-verificationDetails"></a>
The verification details for the target domain.
Type: [VerificationDetails](API_VerificationDetails.md) object
Required: No

 ** verificationStatus **   <a name="securityagent-Type-TargetDomain-verificationStatus"></a>
The current verification status of the target domain.
Type: String
Valid Values: `PENDING | VERIFIED | FAILED | UNREACHABLE`
Required: No

 ** verificationStatusReason **   <a name="securityagent-Type-TargetDomain-verificationStatusReason"></a>
The reason for the current target domain verification status.
Type: String
Required: No

 ** verifiedAt **   <a name="securityagent-Type-TargetDomain-verifiedAt"></a>
The date and time the target domain was verified, in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_TargetDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/TargetDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/TargetDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/TargetDomain)
