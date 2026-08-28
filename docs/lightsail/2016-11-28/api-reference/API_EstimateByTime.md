---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_EstimateByTime.html
---

# EstimateByTime
<a name="API_EstimateByTime"></a>

An estimate that's associated with a time period.

## Contents
<a name="API_EstimateByTime_Contents"></a>

 ** currency **   <a name="Lightsail-Type-EstimateByTime-currency"></a>
The currency of the estimate in USD.
Type: String
Valid Values: `USD`
Required: No

 ** pricingUnit **   <a name="Lightsail-Type-EstimateByTime-pricingUnit"></a>
The unit of measurement that's used for the cost estimate.
Type: String
Valid Values: `GB | Hrs | GB-Mo | Bundles | Queries`
Required: No

 ** timePeriod **   <a name="Lightsail-Type-EstimateByTime-timePeriod"></a>
The period of time, in days, that an estimate covers. The period has a start date and an end date. The start date must come before the end date.
Type: [TimePeriod](API_TimePeriod.md) object
Required: No

 ** unit **   <a name="Lightsail-Type-EstimateByTime-unit"></a>
The number of pricing units used to calculate the total number of hours. For example, 1 unit equals 1 hour.
Type: Double
Required: No

 ** usageCost **   <a name="Lightsail-Type-EstimateByTime-usageCost"></a>
The amount of cost or usage that's measured for the cost estimate.
Type: Double
Required: No

## See Also
<a name="API_EstimateByTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/EstimateByTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/EstimateByTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/EstimateByTime)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
