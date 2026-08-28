---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_BillingPeriodRange.html
---

# BillingPeriodRange
<a name="API_BillingPeriodRange"></a>

A time range for which the margin summary is effective. The time range can be up to 12 months.

## Contents
<a name="API_BillingPeriodRange_Contents"></a>

 ** ExclusiveEndBillingPeriod **   <a name="billingconductor-Type-BillingPeriodRange-ExclusiveEndBillingPeriod"></a>
The exclusive end billing period that defines a billing period range for the margin summary. For example, if you choose a billing period that starts in October 2023 and ends in December 2023, the margin summary will only include data from October 2023 and November 2023.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`
Required: Yes

 ** InclusiveStartBillingPeriod **   <a name="billingconductor-Type-BillingPeriodRange-InclusiveStartBillingPeriod"></a>
The inclusive start billing period that defines a billing period range for the margin summary.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`
Required: Yes

## See Also
<a name="API_BillingPeriodRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/BillingPeriodRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/BillingPeriodRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/BillingPeriodRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
