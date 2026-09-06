---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceSpec.html
---

# ResourceSpec
<a name="API_ResourceSpec"></a>

Specifies the ARN's of a SageMaker AI image and SageMaker AI image version, and the instance type that the version runs on.

**Note**
When both `SageMakerImageVersionArn` and `SageMakerImageArn` are passed, `SageMakerImageVersionArn` is used. Any updates to `SageMakerImageArn` will not take effect if `SageMakerImageVersionArn` already exists in the `ResourceSpec` because `SageMakerImageVersionArn` always takes precedence. To clear the value set for `SageMakerImageVersionArn`, pass `None` as the value.

## Contents
<a name="API_ResourceSpec_Contents"></a>

 ** InstanceType **   <a name="sagemaker-Type-ResourceSpec-InstanceType"></a>
The instance type that the image version runs on.
 **JupyterServer apps** only support the `system` value.
For **KernelGateway apps**, the `system` value is translated to `ml.t3.medium`. KernelGateway apps also support all other values for available instance types.
Type: String
Valid Values: `system | ml.t3.micro | ml.t3.small | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.8xlarge | ml.m5.12xlarge | ml.m5.16xlarge | ml.m5.24xlarge | ml.m5d.large | ml.m5d.xlarge | ml.m5d.2xlarge | ml.m5d.4xlarge | ml.m5d.8xlarge | ml.m5d.12xlarge | ml.m5d.16xlarge | ml.m5d.24xlarge | ml.c5.large | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.12xlarge | ml.c5.18xlarge | ml.c5.24xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.p3dn.24xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.8xlarge | ml.r5.12xlarge | ml.r5.16xlarge | ml.r5.24xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.16xlarge | ml.g5.12xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.geospatial.interactive | ml.p4d.24xlarge | ml.p4de.24xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.p5.48xlarge | ml.p5en.48xlarge | ml.p6-b200.48xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.m6id.large | ml.m6id.xlarge | ml.m6id.2xlarge | ml.m6id.4xlarge | ml.m6id.8xlarge | ml.m6id.12xlarge | ml.m6id.16xlarge | ml.m6id.24xlarge | ml.m6id.32xlarge | ml.c6id.large | ml.c6id.xlarge | ml.c6id.2xlarge | ml.c6id.4xlarge | ml.c6id.8xlarge | ml.c6id.12xlarge | ml.c6id.16xlarge | ml.c6id.24xlarge | ml.c6id.32xlarge | ml.r6id.large | ml.r6id.xlarge | ml.r6id.2xlarge | ml.r6id.4xlarge | ml.r6id.8xlarge | ml.r6id.12xlarge | ml.r6id.16xlarge | ml.r6id.24xlarge | ml.r6id.32xlarge | ml.p5.4xlarge | ml.g7.2xlarge | ml.g7.4xlarge | ml.g7.8xlarge | ml.g7.12xlarge | ml.g7.24xlarge | ml.g7.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge`
Required: No

 ** LifecycleConfigArn **   <a name="sagemaker-Type-ResourceSpec-LifecycleConfigArn"></a>
 The Amazon Resource Name (ARN) of the Lifecycle Configuration attached to the Resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*|None)`
Required: No

 ** SageMakerImageArn **   <a name="sagemaker-Type-ResourceSpec-SageMakerImageArn"></a>
The ARN of the SageMaker AI image that the image version belongs to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:sagemaker:.+:[0-9]{12}:image/[a-zA-Z0-9]([-.]?[a-zA-Z0-9])*`
Required: No

 ** SageMakerImageVersionAlias **   <a name="sagemaker-Type-ResourceSpec-SageMakerImageVersionAlias"></a>
The SageMakerImageVersionAlias of the image to launch with. This value is in SemVer 2.0.0 versioning format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^\d+$)|(^\d+.\d+$)|(^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$)`
Required: No

 ** SageMakerImageVersionArn **   <a name="sagemaker-Type-ResourceSpec-SageMakerImageVersionArn"></a>
The ARN of the image version created on the instance. To clear the value set for `SageMakerImageVersionArn`, pass `None` as the value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws(-[\w]+)*:sagemaker:.+:[0-9]{12}:image-version/[a-z0-9]([-.]?[a-z0-9])*/[0-9]+|None)`
Required: No

 ** TrainingPlanArn **   <a name="sagemaker-Type-ResourceSpec-TrainingPlanArn"></a>
The ARN of the SageMaker AI Training Plan to use for this app. When you specify a training plan, the app launches on reserved GPU capacity. This field is supported for JupyterLab and CodeEditor app types.
For more information about how to reserve GPU capacity with SageMaker AI Training Plans, see [Using training plans in Studio applications](https://docs.aws.amazon.com/sagemaker/latest/dg/training-plan-utilization-for-studio-apps.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*|None)`
Required: No

## See Also
<a name="API_ResourceSpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ResourceSpec)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ResourceSpec)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ResourceSpec)
