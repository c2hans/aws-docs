---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LambdaFunctionMemoryProjectedMetric.html
---

# LambdaFunctionMemoryProjectedMetric
<a name="API_LambdaFunctionMemoryProjectedMetric"></a>

Describes a projected utilization metric of an AWS Lambda function recommendation option.

## Contents
<a name="API_LambdaFunctionMemoryProjectedMetric_Contents"></a>

 ** name **   <a name="computeoptimizer-Type-LambdaFunctionMemoryProjectedMetric-name"></a>
The name of the projected utilization metric.
Type: String
Valid Values: `Duration`
Required: No

 ** statistic **   <a name="computeoptimizer-Type-LambdaFunctionMemoryProjectedMetric-statistic"></a>
The statistic of the projected utilization metric.
Type: String
Valid Values: `LowerBound | UpperBound | Expected`
Required: No

 ** value **   <a name="computeoptimizer-Type-LambdaFunctionMemoryProjectedMetric-value"></a>
The values of the projected utilization metrics.
Type: Double
Required: No

## See Also
<a name="API_LambdaFunctionMemoryProjectedMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/LambdaFunctionMemoryProjectedMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/LambdaFunctionMemoryProjectedMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/LambdaFunctionMemoryProjectedMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
