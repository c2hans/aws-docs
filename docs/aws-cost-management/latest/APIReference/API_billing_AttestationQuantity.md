---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_AttestationQuantity.html
---

# AttestationQuantity
<a name="API_billing_AttestationQuantity"></a>

A quantity-based attestation value, such as a count of workloads migrated.

## Contents
<a name="API_billing_AttestationQuantity_Contents"></a>

 ** attestationUnit **   <a name="awscostmanagement-Type-billing_AttestationQuantity-attestationUnit"></a>
The unit of the attestation, such as `workloads migrated`. This value is 1–1000 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** attestationVolume **   <a name="awscostmanagement-Type-billing_AttestationQuantity-attestationVolume"></a>
The number of units being attested, expressed as a decimal string to preserve precision. The value is digits with an optional decimal point and is 1–1000 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[0-9]+(\.[0-9]+)?`
Required: Yes

## See Also
<a name="API_billing_AttestationQuantity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/AttestationQuantity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/AttestationQuantity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/AttestationQuantity)
