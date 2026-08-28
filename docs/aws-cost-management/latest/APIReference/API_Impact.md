---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Impact.html
---

# Impact
<a name="API_Impact"></a>

The dollar value of the anomaly.

## Contents
<a name="API_Impact_Contents"></a>

 ** MaxImpact **   <a name="awscostmanagement-Type-Impact-MaxImpact"></a>
The maximum dollar value that's observed for an anomaly.
Type: Double
Required: Yes

 ** TotalActualSpend **   <a name="awscostmanagement-Type-Impact-TotalActualSpend"></a>
The cumulative dollar amount that was actually spent during the anomaly.
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

 ** TotalExpectedSpend **   <a name="awscostmanagement-Type-Impact-TotalExpectedSpend"></a>
The cumulative dollar amount that was expected to be spent during the anomaly. It is calculated using advanced machine learning models to determine the typical spending pattern based on historical data for a customer.
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

 ** TotalImpact **   <a name="awscostmanagement-Type-Impact-TotalImpact"></a>
The cumulative dollar difference between the total actual spend and total expected spend. It is calculated as `TotalActualSpend - TotalExpectedSpend`.
Type: Double
Required: No

 ** TotalImpactPercentage **   <a name="awscostmanagement-Type-Impact-TotalImpactPercentage"></a>
The cumulative percentage difference between the total actual spend and total expected spend. It is calculated as `(TotalImpact / TotalExpectedSpend) * 100`. When `TotalExpectedSpend` is zero, this field is omitted. Expected spend can be zero in situations such as when you start to use a service for the first time.
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

## See Also
<a name="API_Impact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/Impact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/Impact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/Impact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
