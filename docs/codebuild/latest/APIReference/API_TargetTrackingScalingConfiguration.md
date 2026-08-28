---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_TargetTrackingScalingConfiguration.html
---

# TargetTrackingScalingConfiguration
<a name="API_TargetTrackingScalingConfiguration"></a>

Defines when a new instance is auto-scaled into the compute fleet.

## Contents
<a name="API_TargetTrackingScalingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** metricType **   <a name="CodeBuild-Type-TargetTrackingScalingConfiguration-metricType"></a>
The metric type to determine auto-scaling.
Type: String
Valid Values: `FLEET_UTILIZATION_RATE`
Required: No

 ** targetValue **   <a name="CodeBuild-Type-TargetTrackingScalingConfiguration-targetValue"></a>
The value of `metricType` when to start scaling.
Type: Double
Required: No

## See Also
<a name="API_TargetTrackingScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/TargetTrackingScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/TargetTrackingScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/TargetTrackingScalingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
