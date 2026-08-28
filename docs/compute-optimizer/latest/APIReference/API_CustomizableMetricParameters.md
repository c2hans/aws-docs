---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_CustomizableMetricParameters.html
---

# CustomizableMetricParameters
<a name="API_CustomizableMetricParameters"></a>

 Defines the various metric parameters that can be customized, such as threshold and headroom.

## Contents
<a name="API_CustomizableMetricParameters_Contents"></a>

 ** headroom **   <a name="computeoptimizer-Type-CustomizableMetricParameters-headroom"></a>
 The headroom value in percentage used for the specified metric parameter.
The following lists the valid values for CPU and memory utilization.
+ CPU utilization: `PERCENT_30 | PERCENT_20 | PERCENT_0`
+ Memory utilization: `PERCENT_30 | PERCENT_20 | PERCENT_10`
Type: String
Valid Values: `PERCENT_30 | PERCENT_20 | PERCENT_10 | PERCENT_0`
Required: No

 ** threshold **   <a name="computeoptimizer-Type-CustomizableMetricParameters-threshold"></a>
 The threshold value used for the specified metric parameter.
You can only specify the threshold value for CPU utilization.
Type: String
Valid Values: `P90 | P95 | P99_5`
Required: No

## See Also
<a name="API_CustomizableMetricParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/CustomizableMetricParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/CustomizableMetricParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/CustomizableMetricParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
