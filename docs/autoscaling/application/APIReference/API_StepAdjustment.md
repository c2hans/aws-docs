---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepAdjustment.html
---

# StepAdjustment
<a name="API_StepAdjustment"></a>

Represents a step adjustment for a [StepScalingPolicyConfiguration](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepScalingPolicyConfiguration.html). Describes an adjustment based on the difference between the value of the aggregated CloudWatch metric and the breach threshold that you've defined for the alarm.

For the following examples, suppose that you have an alarm with a breach threshold of 50:
+ To initiate the adjustment when the metric is greater than or equal to 50 and less than 60, specify a lower bound of `0` and an upper bound of `10`.
+ To initiate the adjustment when the metric is greater than 40 and less than or equal to 50, specify a lower bound of `-10` and an upper bound of `0`.

There are a few rules for the step adjustments for your step policy:
+ The ranges of your step adjustments can't overlap or have a gap.
+ At most one step adjustment can have a null lower bound. If one step adjustment has a negative lower bound, then there must be a step adjustment with a null lower bound.
+ At most one step adjustment can have a null upper bound. If one step adjustment has a positive upper bound, then there must be a step adjustment with a null upper bound.
+ The upper and lower bound can't be null in the same step adjustment.

## Contents
<a name="API_StepAdjustment_Contents"></a>

 ** ScalingAdjustment **   <a name="autoscaling-Type-StepAdjustment-ScalingAdjustment"></a>
The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a non-negative value.
Type: Integer
Required: Yes

 ** MetricIntervalLowerBound **   <a name="autoscaling-Type-StepAdjustment-MetricIntervalLowerBound"></a>
The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it's exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.
Type: Double
Required: No

 ** MetricIntervalUpperBound **   <a name="autoscaling-Type-StepAdjustment-MetricIntervalUpperBound"></a>
The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it's inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.
The upper bound must be greater than the lower bound.
Type: Double
Required: No

## See Also
<a name="API_StepAdjustment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/StepAdjustment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/StepAdjustment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/StepAdjustment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
