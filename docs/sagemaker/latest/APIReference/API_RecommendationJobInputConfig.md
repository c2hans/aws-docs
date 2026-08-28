---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RecommendationJobInputConfig.html
---

# RecommendationJobInputConfig
<a name="API_RecommendationJobInputConfig"></a>

The input configuration of the recommendation job.

## Contents
<a name="API_RecommendationJobInputConfig_Contents"></a>

 ** ContainerConfig **   <a name="sagemaker-Type-RecommendationJobInputConfig-ContainerConfig"></a>
Specifies mandatory fields for running an Inference Recommender job. The fields specified in `ContainerConfig` override the corresponding fields in the model package.
Type: [RecommendationJobContainerConfig](API_RecommendationJobContainerConfig.md) object
Required: No

 ** EndpointConfigurations **   <a name="sagemaker-Type-RecommendationJobInputConfig-EndpointConfigurations"></a>
Specifies the endpoint configuration to use for a job.
Type: Array of [EndpointInputConfiguration](API_EndpointInputConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** Endpoints **   <a name="sagemaker-Type-RecommendationJobInputConfig-Endpoints"></a>
Existing customer endpoints on which to run an Inference Recommender job.
Type: Array of [EndpointInfo](API_EndpointInfo.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** JobDurationInSeconds **   <a name="sagemaker-Type-RecommendationJobInputConfig-JobDurationInSeconds"></a>
Specifies the maximum duration of the job, in seconds. The maximum value is 18,000 seconds.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ModelName **   <a name="sagemaker-Type-RecommendationJobInputConfig-ModelName"></a>
The name of the created model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: No

 ** ModelPackageVersionArn **   <a name="sagemaker-Type-RecommendationJobInputConfig-ModelPackageVersionArn"></a>
The Amazon Resource Name (ARN) of a versioned model package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`
Required: No

 ** ResourceLimit **   <a name="sagemaker-Type-RecommendationJobInputConfig-ResourceLimit"></a>
Defines the resource limit of the job.
Type: [RecommendationJobResourceLimit](API_RecommendationJobResourceLimit.md) object
Required: No

 ** TrafficPattern **   <a name="sagemaker-Type-RecommendationJobInputConfig-TrafficPattern"></a>
Specifies the traffic pattern of the job.
Type: [TrafficPattern](API_TrafficPattern.md) object
Required: No

 ** VolumeKmsKeyId **   <a name="sagemaker-Type-RecommendationJobInputConfig-VolumeKmsKeyId"></a>
The Amazon Resource Name (ARN) of a AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint. This key will be passed to SageMaker Hosting for endpoint creation.
The SageMaker execution role must have `kms:CreateGrant` permission in order to encrypt data on the storage volume of the endpoints created for inference recommendation. The inference recommendation job will fail asynchronously during endpoint configuration creation if the role passed does not have `kms:CreateGrant` permission.
The `KmsKeyId` can be any of the following formats:
+ // KMS Key ID

   `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ // Amazon Resource Name (ARN) of a KMS Key

   `"arn:aws:kms:<region>:<account>:key/<key-id-12ab-34cd-56ef-1234567890ab>"`
+ // KMS Key Alias

   `"alias/ExampleAlias"`
+ // Amazon Resource Name (ARN) of a KMS Key Alias

   `"arn:aws:kms:<region>:<account>:alias/<ExampleAlias>"`
For more information about key identifiers, see [Key identifiers (KeyID)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id) in the AWS Key Management Service (AWS KMS) documentation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** VpcConfig **   <a name="sagemaker-Type-RecommendationJobInputConfig-VpcConfig"></a>
Inference Recommender provisions SageMaker endpoints with access to VPC in the inference recommendation job.
Type: [RecommendationJobVpcConfig](API_RecommendationJobVpcConfig.md) object
Required: No

## See Also
<a name="API_RecommendationJobInputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RecommendationJobInputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RecommendationJobInputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RecommendationJobInputConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
