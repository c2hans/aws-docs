---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InstanceGroupScalingMetadata.html
---

# InstanceGroupScalingMetadata
<a name="API_InstanceGroupScalingMetadata"></a>

Metadata information about scaling operations for an instance group.

## Contents
<a name="API_InstanceGroupScalingMetadata_Contents"></a>

 ** FailureMessage **   <a name="sagemaker-Type-InstanceGroupScalingMetadata-FailureMessage"></a>
An error message describing why the scaling operation failed, if applicable.
Type: String
Required: No

 ** InstanceCount **   <a name="sagemaker-Type-InstanceGroupScalingMetadata-InstanceCount"></a>
The current number of instances in the group.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000000.
Required: No

 ** MinCount **   <a name="sagemaker-Type-InstanceGroupScalingMetadata-MinCount"></a>
Minimum instance count of the instance group.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000000.
Required: No

 ** TargetCount **   <a name="sagemaker-Type-InstanceGroupScalingMetadata-TargetCount"></a>
The desired number of instances for the group after scaling.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_InstanceGroupScalingMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InstanceGroupScalingMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InstanceGroupScalingMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InstanceGroupScalingMetadata)
