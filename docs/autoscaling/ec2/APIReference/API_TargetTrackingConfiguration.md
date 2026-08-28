---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TargetTrackingConfiguration.html
---

# TargetTrackingConfiguration
<a name="API_TargetTrackingConfiguration"></a>

Represents a target tracking scaling policy configuration to use with Amazon EC2 Auto Scaling.

## Contents
<a name="API_TargetTrackingConfiguration_Contents"></a>

 ** TargetValue **
The target value for the metric.
Some metrics are based on a count instead of a percentage, such as the request count for an Application Load Balancer or the number of messages in an SQS queue. If the scaling policy specifies one of these metrics, specify the target utilization as the optimal average request or message count per instance during any one-minute interval.
Type: Double
Required: Yes

 ** CustomizedMetricSpecification **
A customized metric. You must specify either a predefined metric or a customized metric.
Type: [CustomizedMetricSpecification](API_CustomizedMetricSpecification.md) object
Required: No

 ** DisableScaleIn **
Indicates whether scaling in by the target tracking scaling policy is disabled. If scaling in is disabled, the target tracking scaling policy doesn't remove instances from the Auto Scaling group. Otherwise, the target tracking scaling policy can remove instances from the Auto Scaling group. The default is `false`.
Type: Boolean
Required: No

 ** PredefinedMetricSpecification **
A predefined metric. You must specify either a predefined metric or a customized metric.
Type: [PredefinedMetricSpecification](API_PredefinedMetricSpecification.md) object
Required: No

## See Also
<a name="API_TargetTrackingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/TargetTrackingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/TargetTrackingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/TargetTrackingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
