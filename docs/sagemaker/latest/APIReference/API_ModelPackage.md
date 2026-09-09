---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelPackage.html
---

# ModelPackage
<a name="API_ModelPackage"></a>

A container for your trained model that can be deployed for SageMaker inference. This can include inference code, artifacts, and metadata. The model package type can be one of the following.
+ Versioned model: A part of a model package group in Model Registry.
+ Unversioned model: Not part of a model package group and used in AWS Marketplace.

For more information, see [`CreateModelPackage`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelPackage.html).

## Contents
<a name="API_ModelPackage_Contents"></a>

 ** AdditionalInferenceSpecifications **   <a name="sagemaker-Type-ModelPackage-AdditionalInferenceSpecifications"></a>
An array of additional Inference Specification objects.
Type: Array of [AdditionalInferenceSpecificationDefinition](API_AdditionalInferenceSpecificationDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Required: No

 ** ApprovalDescription **   <a name="sagemaker-Type-ModelPackage-ApprovalDescription"></a>
A description provided when the model approval is set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** CertifyForMarketplace **   <a name="sagemaker-Type-ModelPackage-CertifyForMarketplace"></a>
Whether the model package is to be certified to be listed on AWS Marketplace. For information about listing model packages on AWS Marketplace, see [List Your Algorithm or Model Package on AWS Marketplace](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-mkt-list.html).
Type: Boolean
Required: No

 ** CreatedBy **   <a name="sagemaker-Type-ModelPackage-CreatedBy"></a>
Information about the user who created or modified an experiment, trial, trial component, lineage group, or project.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** CreationTime **   <a name="sagemaker-Type-ModelPackage-CreationTime"></a>
The time that the model package was created.
Type: Timestamp
Required: No

 ** CustomerMetadataProperties **   <a name="sagemaker-Type-ModelPackage-CustomerMetadataProperties"></a>
The metadata properties for the model package.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)${1,128}`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)${1,256}`
Required: No

 ** Domain **   <a name="sagemaker-Type-ModelPackage-Domain"></a>
The machine learning domain of your model package and its components. Common machine learning domains include computer vision and natural language processing.
Type: String
Required: No

 ** DriftCheckBaselines **   <a name="sagemaker-Type-ModelPackage-DriftCheckBaselines"></a>
Represents the drift check baselines that can be used when the model monitor is set using the model package.
Type: [DriftCheckBaselines](API_DriftCheckBaselines.md) object
Required: No

 ** InferenceSpecification **   <a name="sagemaker-Type-ModelPackage-InferenceSpecification"></a>
Defines how to perform inference generation after a training job is run.
Type: [InferenceSpecification](API_InferenceSpecification.md) object
Required: No

 ** LastModifiedBy **   <a name="sagemaker-Type-ModelPackage-LastModifiedBy"></a>
Information about the user who created or modified an experiment, trial, trial component, lineage group, or project.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** MetadataProperties **   <a name="sagemaker-Type-ModelPackage-MetadataProperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
Type: [MetadataProperties](API_MetadataProperties.md) object
Required: No

 ** ModelApprovalStatus **   <a name="sagemaker-Type-ModelPackage-ModelApprovalStatus"></a>
The approval status of the model. This can be one of the following values.
+  `APPROVED` - The model is approved
+  `REJECTED` - The model is rejected.
+  `PENDING_MANUAL_APPROVAL` - The model is waiting for manual approval.
Type: String
Valid Values: `Approved | Rejected | PendingManualApproval`
Required: No

 ** ModelCard **   <a name="sagemaker-Type-ModelPackage-ModelCard"></a>
The model card associated with the model package. Since `ModelPackageModelCard` is tied to a model package, it is a specific usage of a model card and its schema is simplified compared to the schema of `ModelCard`. The `ModelPackageModelCard` schema does not include `model_package_details`, and `model_overview` is composed of the `model_creator` and `model_artifact` properties. For more information about the model package model card schema, see [Model package model card schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html#model-card-schema). For more information about the model card associated with the model package, see [View the Details of a Model Version](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html).
Type: [ModelPackageModelCard](API_ModelPackageModelCard.md) object
Required: No

 ** ModelLifeCycle **   <a name="sagemaker-Type-ModelPackage-ModelLifeCycle"></a>
 A structure describing the current state of the model in its life cycle.
Type: [ModelLifeCycle](API_ModelLifeCycle.md) object
Required: No

 ** ModelMetrics **   <a name="sagemaker-Type-ModelPackage-ModelMetrics"></a>
Metrics for the model.
Type: [ModelMetrics](API_ModelMetrics.md) object
Required: No

 ** ModelPackageArn **   <a name="sagemaker-Type-ModelPackage-ModelPackageArn"></a>
The Amazon Resource Name (ARN) of the model package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`
Required: No

 ** ModelPackageDescription **   <a name="sagemaker-Type-ModelPackage-ModelPackageDescription"></a>
The description of the model package.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

 ** ModelPackageGroupName **   <a name="sagemaker-Type-ModelPackage-ModelPackageGroupName"></a>
The model group to which the model belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ModelPackageName **   <a name="sagemaker-Type-ModelPackage-ModelPackageName"></a>
The name of the model package. The name can be as follows:
+ For a versioned model, the name is automatically generated by SageMaker Model Registry and follows the format '`ModelPackageGroupName/ModelPackageVersion`'.
+ For an unversioned model, you must provide the name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ModelPackageRegistrationType **   <a name="sagemaker-Type-ModelPackage-ModelPackageRegistrationType"></a>
 The package registration type of the model package.
Type: String
Valid Values: `Logged | Registered`
Required: No

 ** ModelPackageStatus **   <a name="sagemaker-Type-ModelPackage-ModelPackageStatus"></a>
The status of the model package. This can be one of the following values.
+  `PENDING` - The model package is pending being created.
+  `IN_PROGRESS` - The model package is in the process of being created.
+  `COMPLETED` - The model package was successfully created.
+  `FAILED` - The model package failed.
+  `DELETING` - The model package is in the process of being deleted.
Type: String
Valid Values: `Pending | InProgress | Completed | Failed | Deleting`
Required: No

 ** ModelPackageStatusDetails **   <a name="sagemaker-Type-ModelPackage-ModelPackageStatusDetails"></a>
Specifies the validation and image scan statuses of the model package.
Type: [ModelPackageStatusDetails](API_ModelPackageStatusDetails.md) object
Required: No

 ** ModelPackageVersion **   <a name="sagemaker-Type-ModelPackage-ModelPackageVersion"></a>
The version number of a versioned model.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** SamplePayloadUrl **   <a name="sagemaker-Type-ModelPackage-SamplePayloadUrl"></a>
The Amazon Simple Storage Service path where the sample payload are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
Type: String
Required: No

 ** SecurityConfig **   <a name="sagemaker-Type-ModelPackage-SecurityConfig"></a>
An optional AWS Key Management Service key to encrypt, decrypt, and re-encrypt model package information for regulated workloads with highly sensitive data.
Type: [ModelPackageSecurityConfig](API_ModelPackageSecurityConfig.md) object
Required: No

 ** SkipModelValidation **   <a name="sagemaker-Type-ModelPackage-SkipModelValidation"></a>
Indicates if you want to skip model validation.
Type: String
Valid Values: `All | None`
Required: No

 ** SourceAlgorithmSpecification **   <a name="sagemaker-Type-ModelPackage-SourceAlgorithmSpecification"></a>
A list of algorithms that were used to create a model package.
Type: [SourceAlgorithmSpecification](API_SourceAlgorithmSpecification.md) object
Required: No

 ** SourceUri **   <a name="sagemaker-Type-ModelPackage-SourceUri"></a>
The URI of the source for the model package.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{N}\p{P}]{0,1024}`
Required: No

 ** Tags **   <a name="sagemaker-Type-ModelPackage-Tags"></a>
A list of the tags associated with the model package. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** Task **   <a name="sagemaker-Type-ModelPackage-Task"></a>
The machine learning task your model package accomplishes. Common machine learning tasks include object detection and image classification.
Type: String
Required: No

 ** ValidationSpecification **   <a name="sagemaker-Type-ModelPackage-ValidationSpecification"></a>
Specifies batch transform jobs that SageMaker runs to validate your model package.
Type: [ModelPackageValidationSpecification](API_ModelPackageValidationSpecification.md) object
Required: No

## See Also
<a name="API_ModelPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelPackage)
