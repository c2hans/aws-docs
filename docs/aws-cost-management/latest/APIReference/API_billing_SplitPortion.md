---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_SplitPortion.html
---

# SplitPortion
<a name="API_billing_SplitPortion"></a>

One new credit to create from a split.

## Contents
<a name="API_billing_SplitPortion_Contents"></a>

 ** amount **   <a name="awscostmanagement-Type-billing_SplitPortion-amount"></a>
The amount of the new credit, in the currency of the credit that you split. The amount must be at least 100.00 in that currency. For example, if the credit is in USD, the amount must be at least USD $100.00.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[0-9]{1,25}(\.[0-9]{1,6})?`
Required: Yes

 ** description **   <a name="awscostmanagement-Type-billing_SplitPortion-description"></a>
The description of the new credit. If you omit it, the new credit gets the original credit's description followed by its position in the request, for example `MAP credit - 1/3`. If you split that credit again, the name extends, for example `MAP credit - 1/3 - 2/2`. A generated name is at most 93 characters. If it would be longer, the name keeps only the beginning of the original description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\x21-\x7E\xA1-\xFF][\x20-\x7E\xA1-\xFF]*`
Required: No

## See Also
<a name="API_billing_SplitPortion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/SplitPortion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/SplitPortion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/SplitPortion)
