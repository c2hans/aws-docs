---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ScalingConfigurationOutput.html
---

# ScalingConfigurationOutput
<a name="API_ScalingConfigurationOutput"></a>

The scaling configuration output of a compute fleet.

## Contents
<a name="API_ScalingConfigurationOutput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** desiredCapacity **   <a name="CodeBuild-Type-ScalingConfigurationOutput-desiredCapacity"></a>
The desired number of instances in the ﬂeet when auto-scaling.
Type: Integer
Required: No

 ** maxCapacity **   <a name="CodeBuild-Type-ScalingConfigurationOutput-maxCapacity"></a>
The maximum number of instances in the ﬂeet when auto-scaling.
Type: Integer
Required: No

 ** scalingType **   <a name="CodeBuild-Type-ScalingConfigurationOutput-scalingType"></a>
The scaling type for a compute fleet.
Type: String
Valid Values: `TARGET_TRACKING_SCALING`
Required: No

 ** targetTrackingScalingConfigs **   <a name="CodeBuild-Type-ScalingConfigurationOutput-targetTrackingScalingConfigs"></a>
A list of `TargetTrackingScalingConfiguration` objects.
Type: Array of [TargetTrackingScalingConfiguration](API_TargetTrackingScalingConfiguration.md) objects
Required: No

## See Also
<a name="API_ScalingConfigurationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ScalingConfigurationOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ScalingConfigurationOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ScalingConfigurationOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
