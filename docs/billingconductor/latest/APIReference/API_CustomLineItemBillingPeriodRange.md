---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CustomLineItemBillingPeriodRange.html
---

# CustomLineItemBillingPeriodRange
<a name="API_CustomLineItemBillingPeriodRange"></a>

The billing period range in which the custom line item request will be applied.

## Contents
<a name="API_CustomLineItemBillingPeriodRange_Contents"></a>

 ** InclusiveStartBillingPeriod **   <a name="billingconductor-Type-CustomLineItemBillingPeriodRange-InclusiveStartBillingPeriod"></a>
The inclusive start billing period that defines a billing period range where a custom line is applied.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`
Required: Yes

 ** ExclusiveEndBillingPeriod **   <a name="billingconductor-Type-CustomLineItemBillingPeriodRange-ExclusiveEndBillingPeriod"></a>
The inclusive end billing period that defines a billing period range where a custom line is applied.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`
Required: No

## See Also
<a name="API_CustomLineItemBillingPeriodRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/CustomLineItemBillingPeriodRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/CustomLineItemBillingPeriodRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/CustomLineItemBillingPeriodRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
