---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListBillingGroupAccountGrouping.html
---

# ListBillingGroupAccountGrouping
<a name="API_ListBillingGroupAccountGrouping"></a>

Specifies if the billing group has the following features enabled.

## Contents
<a name="API_ListBillingGroupAccountGrouping_Contents"></a>

 ** AutoAssociate **   <a name="billingconductor-Type-ListBillingGroupAccountGrouping-AutoAssociate"></a>
Specifies if this billing group will automatically associate newly added AWS accounts that join your consolidated billing family.
Type: Boolean
Required: No

 ** ResponsibilityTransferArn **   <a name="billingconductor-Type-ListBillingGroupAccountGrouping-ResponsibilityTransferArn"></a>
 The Amazon Resource Name (ARN) that identifies the transfer relationship for the billing group.
Type: String
Pattern: `arn:[a-z0-9][a-z0-9-.]{0,62}:organizations::\d{12}:transfer/o-[a-z0-9]{10,32}/(billing)/(inbound|outbound)/rt-[0-9a-z]{8,32}`
Required: No

## See Also
<a name="API_ListBillingGroupAccountGrouping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListBillingGroupAccountGrouping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListBillingGroupAccountGrouping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListBillingGroupAccountGrouping)
