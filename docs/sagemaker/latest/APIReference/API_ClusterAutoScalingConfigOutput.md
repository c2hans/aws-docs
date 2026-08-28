---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterAutoScalingConfigOutput.html
---

# ClusterAutoScalingConfigOutput
<a name="API_ClusterAutoScalingConfigOutput"></a>

The autoscaling configuration and status information for a HyperPod cluster.

## Contents
<a name="API_ClusterAutoScalingConfigOutput_Contents"></a>

 ** Mode **   <a name="sagemaker-Type-ClusterAutoScalingConfigOutput-Mode"></a>
Describes whether autoscaling is enabled or disabled for the cluster.
Type: String
Valid Values: `Enable | Disable`
Required: Yes

 ** Status **   <a name="sagemaker-Type-ClusterAutoScalingConfigOutput-Status"></a>
The current status of the autoscaling configuration. Valid values are `InService`, `Failed`, `Creating`, and `Deleting`.
Type: String
Valid Values: `InService | Failed | Creating | Deleting`
Required: Yes

 ** AutoScalerType **   <a name="sagemaker-Type-ClusterAutoScalingConfigOutput-AutoScalerType"></a>
The type of autoscaler configured for the cluster.
Type: String
Valid Values: `Karpenter`
Required: No

 ** FailureMessage **   <a name="sagemaker-Type-ClusterAutoScalingConfigOutput-FailureMessage"></a>
If the autoscaling status is `Failed`, this field contains a message describing the failure.
Type: String
Required: No

## See Also
<a name="API_ClusterAutoScalingConfigOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterAutoScalingConfigOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterAutoScalingConfigOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterAutoScalingConfigOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
