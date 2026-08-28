---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdateBillingGroupAccountGrouping.html
---

# UpdateBillingGroupAccountGrouping
<a name="API_UpdateBillingGroupAccountGrouping"></a>

Specifies if the billing group has the following features enabled.

## Contents
<a name="API_UpdateBillingGroupAccountGrouping_Contents"></a>

 ** AutoAssociate **   <a name="billingconductor-Type-UpdateBillingGroupAccountGrouping-AutoAssociate"></a>
Specifies if this billing group will automatically associate newly added AWS accounts that join your consolidated billing family.
Type: Boolean
Required: No

 ** ResponsibilityTransferArn **   <a name="billingconductor-Type-UpdateBillingGroupAccountGrouping-ResponsibilityTransferArn"></a>
 The Amazon Resource Name (ARN) that identifies the transfer relationship. Note: Modifications to the ResponsibilityTransferArn are not permitted for existing billing groups.
Type: String
Pattern: `arn:[a-z0-9][a-z0-9-.]{0,62}:organizations::\d{12}:transfer/o-[a-z0-9]{10,32}/(billing)/(inbound|outbound)/rt-[0-9a-z]{8,32}`
Required: No

## See Also
<a name="API_UpdateBillingGroupAccountGrouping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/UpdateBillingGroupAccountGrouping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/UpdateBillingGroupAccountGrouping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/UpdateBillingGroupAccountGrouping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
