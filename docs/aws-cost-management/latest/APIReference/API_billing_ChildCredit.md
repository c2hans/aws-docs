---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ChildCredit.html
---

# ChildCredit

A new credit that a split created.

## Contents
<a name="API_billing_ChildCredit_Contents"></a>

 ** amount **   <a name="awscostmanagement-Type-billing_ChildCredit-amount"></a>
The amount of the new credit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[0-9]{1,25}(\.[0-9]{1,6})?`
Required: Yes

 ** creditId **   <a name="awscostmanagement-Type-billing_ChildCredit-creditId"></a>
The ID of the new credit. A dry run omits this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[0-9]+`
Required: No

## See Also
<a name="API_billing_ChildCredit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/ChildCredit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/ChildCredit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/ChildCredit)
