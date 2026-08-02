---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostDriver.html
---

# CostDriver
<a name="API_CostDriver"></a>

Represents factors that contribute to cost variations between the baseline and comparison time periods, including the type of driver, an identifier of the driver, and associated metrics.

## Contents
<a name="API_CostDriver_Contents"></a>

 ** Metrics **   <a name="awscostmanagement-Type-CostDriver-Metrics"></a>
A mapping of metric names to their comparison values, measuring the impact of this cost driver.
Type: String to [ComparisonMetricValue](API_ComparisonMetricValue.md) object map
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[\S\s]*`
Required: No

 ** Name **   <a name="awscostmanagement-Type-CostDriver-Name"></a>
The specific identifier of the cost driver.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Type **   <a name="awscostmanagement-Type-CostDriver-Type"></a>
The category or classification of the cost driver.
Values include: BUNDLED\_DISCOUNT, CREDIT, OUT\_OF\_CYCLE\_CHARGE, REFUND, RECURRING\_RESERVATION\_FEE, RESERVATION\_USAGE, RI\_VOLUME\_DISCOUNT, SAVINGS\_PLAN\_USAGE, SAVINGS\_PLAN\_RECURRING\_FEE, SUPPORT\_FEE, TAX, UPFRONT\_RESERVATION\_FEE, USAGE\_CHANGE, COMMITMENT
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_CostDriver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CostDriver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CostDriver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CostDriver)
