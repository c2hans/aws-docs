---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Model.html
---

# Model
<a name="API_Model"></a>

The properties of a model as returned by the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API.

## Contents
<a name="API_Model_Contents"></a>

 ** Containers **   <a name="sagemaker-Type-Model-Containers"></a>
The containers in the inference pipeline.
Type: Array of [ContainerDefinition](API_ContainerDefinition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Required: No

 ** DeploymentRecommendation **   <a name="sagemaker-Type-Model-DeploymentRecommendation"></a>
A set of recommended deployment configurations for the model.
Type: [DeploymentRecommendation](API_DeploymentRecommendation.md) object
Required: No

 ** EnableNetworkIsolation **   <a name="sagemaker-Type-Model-EnableNetworkIsolation"></a>
Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
Type: Boolean
Required: No

 ** ExecutionRoleArn **   <a name="sagemaker-Type-Model-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that you specified for the model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** InferenceExecutionConfig **   <a name="sagemaker-Type-Model-InferenceExecutionConfig"></a>
Specifies details about how containers in a multi-container endpoint are run.
Type: [InferenceExecutionConfig](API_InferenceExecutionConfig.md) object
Required: No

 ** ModelArn **   <a name="sagemaker-Type-Model-ModelArn"></a>
The Amazon Resource Name (ARN) of the model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:model/.*`
Required: No

 ** ModelName **   <a name="sagemaker-Type-Model-ModelName"></a>
The name of the model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: No

 ** PrimaryContainer **   <a name="sagemaker-Type-Model-PrimaryContainer"></a>
Describes the container, as part of model definition.
Type: [ContainerDefinition](API_ContainerDefinition.md) object
Required: No

 ** Tags **   <a name="sagemaker-Type-Model-Tags"></a>
A list of key-value pairs associated with the model. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** VpcConfig **   <a name="sagemaker-Type-Model-VpcConfig"></a>
Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_Model_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Model)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Model)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Model)
