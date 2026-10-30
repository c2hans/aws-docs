---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ApproverDetails.html
---

# ApproverDetails
<a name="API_billing_ApproverDetails"></a>

Information about the executive approver who signs off on an investment attestation.

## Contents
<a name="API_billing_ApproverDetails_Contents"></a>

 ** email **   <a name="awscostmanagement-Type-billing_ApproverDetails-email"></a>
The email address of the approver. This value is 3–256 characters and must be a valid email address.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Pattern: `[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}`
Required: Yes

 ** name **   <a name="awscostmanagement-Type-billing_ApproverDetails-name"></a>
The name of the approver as it appears on the contract. This value can be up to 256 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** title **   <a name="awscostmanagement-Type-billing_ApproverDetails-title"></a>
The title of the approver, such as `Chief Financial Officer`. This value can be up to 256 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_billing_ApproverDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/ApproverDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/ApproverDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/ApproverDetails)
