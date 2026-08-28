---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-modelpackage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage
<a name="aws-resource-sagemaker-modelpackage"></a>

A container for your trained model that can be deployed for SageMaker inference. This can include inference code, artifacts, and metadata. The model package type can be one of the following.
+ Versioned model: A part of a model package group in Model Registry.
+ Unversioned model: Not part of a model package group and used in AWS Marketplace.

For more information, see [`CreateModelPackage`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelPackage.html).

## Syntax
<a name="aws-resource-sagemaker-modelpackage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-modelpackage-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::ModelPackage",
  "Properties" : {
      "[AdditionalInferenceSpecifications](#cfn-sagemaker-modelpackage-additionalinferencespecifications)" : {{[ AdditionalInferenceSpecificationDefinition, ... ]}},
      "[AdditionalInferenceSpecificationsToAdd](#cfn-sagemaker-modelpackage-additionalinferencespecificationstoadd)" : {{[ AdditionalInferenceSpecificationDefinition, ... ]}},
      "[ApprovalDescription](#cfn-sagemaker-modelpackage-approvaldescription)" : {{String}},
      "[CertifyForMarketplace](#cfn-sagemaker-modelpackage-certifyformarketplace)" : {{Boolean}},
      "[ClientToken](#cfn-sagemaker-modelpackage-clienttoken)" : {{String}},
      "[CustomerMetadataProperties](#cfn-sagemaker-modelpackage-customermetadataproperties)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Domain](#cfn-sagemaker-modelpackage-domain)" : {{String}},
      "[DriftCheckBaselines](#cfn-sagemaker-modelpackage-driftcheckbaselines)" : {{DriftCheckBaselines}},
      "[InferenceSpecification](#cfn-sagemaker-modelpackage-inferencespecification)" : {{InferenceSpecification}},
      "[MetadataProperties](#cfn-sagemaker-modelpackage-metadataproperties)" : {{MetadataProperties}},
      "[ModelApprovalStatus](#cfn-sagemaker-modelpackage-modelapprovalstatus)" : {{String}},
      "[ModelCard](#cfn-sagemaker-modelpackage-modelcard)" : {{ModelCard}},
      "[ModelMetrics](#cfn-sagemaker-modelpackage-modelmetrics)" : {{ModelMetrics}},
      "[ModelPackageDescription](#cfn-sagemaker-modelpackage-modelpackagedescription)" : {{String}},
      "[ModelPackageGroupName](#cfn-sagemaker-modelpackage-modelpackagegroupname)" : {{String}},
      "[ModelPackageName](#cfn-sagemaker-modelpackage-modelpackagename)" : {{String}},
      "[ModelPackageStatusDetails](#cfn-sagemaker-modelpackage-modelpackagestatusdetails)" : {{ModelPackageStatusDetails}},
      "[ModelPackageVersion](#cfn-sagemaker-modelpackage-modelpackageversion)" : {{Integer}},
      "[SamplePayloadUrl](#cfn-sagemaker-modelpackage-samplepayloadurl)" : {{String}},
      "[SecurityConfig](#cfn-sagemaker-modelpackage-securityconfig)" : {{SecurityConfig}},
      "[SkipModelValidation](#cfn-sagemaker-modelpackage-skipmodelvalidation)" : {{String}},
      "[SourceAlgorithmSpecification](#cfn-sagemaker-modelpackage-sourcealgorithmspecification)" : {{SourceAlgorithmSpecification}},
      "[SourceUri](#cfn-sagemaker-modelpackage-sourceuri)" : {{String}},
      "[Tags](#cfn-sagemaker-modelpackage-tags)" : {{[ Tag, ... ]}},
      "[Task](#cfn-sagemaker-modelpackage-task)" : {{String}},
      "[ValidationSpecification](#cfn-sagemaker-modelpackage-validationspecification)" : {{ValidationSpecification}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-modelpackage-syntax.yaml"></a>

```
Type: AWS::SageMaker::ModelPackage
Properties:
  [AdditionalInferenceSpecifications](#cfn-sagemaker-modelpackage-additionalinferencespecifications): {{
    - AdditionalInferenceSpecificationDefinition}}
  [AdditionalInferenceSpecificationsToAdd](#cfn-sagemaker-modelpackage-additionalinferencespecificationstoadd): {{
    - AdditionalInferenceSpecificationDefinition}}
  [ApprovalDescription](#cfn-sagemaker-modelpackage-approvaldescription): {{String}}
  [CertifyForMarketplace](#cfn-sagemaker-modelpackage-certifyformarketplace): {{Boolean}}
  [ClientToken](#cfn-sagemaker-modelpackage-clienttoken): {{String}}
  [CustomerMetadataProperties](#cfn-sagemaker-modelpackage-customermetadataproperties): {{
    {{Key}}: {{Value}}}}
  [Domain](#cfn-sagemaker-modelpackage-domain): {{String}}
  [DriftCheckBaselines](#cfn-sagemaker-modelpackage-driftcheckbaselines): {{
    DriftCheckBaselines}}
  [InferenceSpecification](#cfn-sagemaker-modelpackage-inferencespecification): {{
    InferenceSpecification}}
  [MetadataProperties](#cfn-sagemaker-modelpackage-metadataproperties): {{
    MetadataProperties}}
  [ModelApprovalStatus](#cfn-sagemaker-modelpackage-modelapprovalstatus): {{String}}
  [ModelCard](#cfn-sagemaker-modelpackage-modelcard): {{
    ModelCard}}
  [ModelMetrics](#cfn-sagemaker-modelpackage-modelmetrics): {{
    ModelMetrics}}
  [ModelPackageDescription](#cfn-sagemaker-modelpackage-modelpackagedescription): {{String}}
  [ModelPackageGroupName](#cfn-sagemaker-modelpackage-modelpackagegroupname): {{String}}
  [ModelPackageName](#cfn-sagemaker-modelpackage-modelpackagename): {{String}}
  [ModelPackageStatusDetails](#cfn-sagemaker-modelpackage-modelpackagestatusdetails): {{
    ModelPackageStatusDetails}}
  [ModelPackageVersion](#cfn-sagemaker-modelpackage-modelpackageversion): {{Integer}}
  [SamplePayloadUrl](#cfn-sagemaker-modelpackage-samplepayloadurl): {{String}}
  [SecurityConfig](#cfn-sagemaker-modelpackage-securityconfig): {{
    SecurityConfig}}
  [SkipModelValidation](#cfn-sagemaker-modelpackage-skipmodelvalidation): {{String}}
  [SourceAlgorithmSpecification](#cfn-sagemaker-modelpackage-sourcealgorithmspecification): {{
    SourceAlgorithmSpecification}}
  [SourceUri](#cfn-sagemaker-modelpackage-sourceuri): {{String}}
  [Tags](#cfn-sagemaker-modelpackage-tags): {{
    - Tag}}
  [Task](#cfn-sagemaker-modelpackage-task): {{String}}
  [ValidationSpecification](#cfn-sagemaker-modelpackage-validationspecification): {{
    ValidationSpecification}}
```

## Properties
<a name="aws-resource-sagemaker-modelpackage-properties"></a>

`AdditionalInferenceSpecifications`  <a name="cfn-sagemaker-modelpackage-additionalinferencespecifications"></a>
An array of additional Inference Specification objects.
*Required*: No
*Type*: Array of [AdditionalInferenceSpecificationDefinition](aws-properties-sagemaker-modelpackage-additionalinferencespecificationdefinition.md)
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdditionalInferenceSpecificationsToAdd`  <a name="cfn-sagemaker-modelpackage-additionalinferencespecificationstoadd"></a>
An array of additional Inference Specification objects to be added to the existing array. The total number of additional Inference Specification objects cannot exceed 15. Each additional Inference Specification object specifies artifacts based on this model package that can be used on inference endpoints. Generally used with SageMaker Neo to store the compiled artifacts.
*Required*: No
*Type*: Array of [AdditionalInferenceSpecificationDefinition](aws-properties-sagemaker-modelpackage-additionalinferencespecificationdefinition.md)
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApprovalDescription`  <a name="cfn-sagemaker-modelpackage-approvaldescription"></a>
A description provided when the model approval is set.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CertifyForMarketplace`  <a name="cfn-sagemaker-modelpackage-certifyformarketplace"></a>
Whether the model package is to be certified to be listed on AWS Marketplace. For information about listing model packages on AWS Marketplace, see [List Your Algorithm or Model Package on AWS Marketplace](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-mkt-list.html).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientToken`  <a name="cfn-sagemaker-modelpackage-clienttoken"></a>
A unique token that guarantees that the call to this API is idempotent.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomerMetadataProperties`  <a name="cfn-sagemaker-modelpackage-customermetadataproperties"></a>
The metadata properties for the model package.
*Required*: No
*Type*: Object of String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)${1,128}`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Domain`  <a name="cfn-sagemaker-modelpackage-domain"></a>
The machine learning domain of your model package and its components. Common machine learning domains include computer vision and natural language processing.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DriftCheckBaselines`  <a name="cfn-sagemaker-modelpackage-driftcheckbaselines"></a>
Represents the drift check baselines that can be used when the model monitor is set using the model package.
*Required*: No
*Type*: [DriftCheckBaselines](aws-properties-sagemaker-modelpackage-driftcheckbaselines.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InferenceSpecification`  <a name="cfn-sagemaker-modelpackage-inferencespecification"></a>
Defines how to perform inference generation after a training job is run.
*Required*: No
*Type*: [InferenceSpecification](aws-properties-sagemaker-modelpackage-inferencespecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetadataProperties`  <a name="cfn-sagemaker-modelpackage-metadataproperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
*Required*: No
*Type*: [MetadataProperties](aws-properties-sagemaker-modelpackage-metadataproperties.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelApprovalStatus`  <a name="cfn-sagemaker-modelpackage-modelapprovalstatus"></a>
The approval status of the model. This can be one of the following values.
+ `APPROVED` - The model is approved
+ `REJECTED` - The model is rejected.
+ `PENDING_MANUAL_APPROVAL` - The model is waiting for manual approval.
*Required*: No
*Type*: String
*Allowed values*: `Approved | Rejected | PendingManualApproval`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelCard`  <a name="cfn-sagemaker-modelpackage-modelcard"></a>
An Amazon SageMaker Model Card.
*Required*: No
*Type*: [ModelCard](aws-properties-sagemaker-modelpackage-modelcard.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ModelMetrics`  <a name="cfn-sagemaker-modelpackage-modelmetrics"></a>
Metrics for the model.
*Required*: No
*Type*: [ModelMetrics](aws-properties-sagemaker-modelpackage-modelmetrics.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelPackageDescription`  <a name="cfn-sagemaker-modelpackage-modelpackagedescription"></a>
The description of the model package.
*Required*: No
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelPackageGroupName`  <a name="cfn-sagemaker-modelpackage-modelpackagegroupname"></a>
The model group to which the model belongs.
*Required*: No
*Type*: String
*Pattern*: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*\/)?([a-zA-Z0-9]([a-zA-Z0-9-]){0,62})(?<!-)$`
*Minimum*: `1`
*Maximum*: `170`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelPackageName`  <a name="cfn-sagemaker-modelpackage-modelpackagename"></a>
The name of the model package. The name can be as follows:
+ For a versioned model, the name is automatically generated by SageMaker Model Registry and follows the format '`ModelPackageGroupName/ModelPackageVersion`'.
+ For an unversioned model, you must provide the name.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelPackageStatusDetails`  <a name="cfn-sagemaker-modelpackage-modelpackagestatusdetails"></a>
Specifies the validation and image scan statuses of the model package.
*Required*: No
*Type*: [ModelPackageStatusDetails](aws-properties-sagemaker-modelpackage-modelpackagestatusdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelPackageVersion`  <a name="cfn-sagemaker-modelpackage-modelpackageversion"></a>
The version number of a versioned model.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SamplePayloadUrl`  <a name="cfn-sagemaker-modelpackage-samplepayloadurl"></a>
The Amazon Simple Storage Service path where the sample payload are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityConfig`  <a name="cfn-sagemaker-modelpackage-securityconfig"></a>
Security configuration for the model package, including encryption settings.
*Required*: No
*Type*: [SecurityConfig](aws-properties-sagemaker-modelpackage-securityconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SkipModelValidation`  <a name="cfn-sagemaker-modelpackage-skipmodelvalidation"></a>
Indicates if you want to skip model validation.
*Required*: No
*Type*: String
*Allowed values*: `None | All`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceAlgorithmSpecification`  <a name="cfn-sagemaker-modelpackage-sourcealgorithmspecification"></a>
A list of algorithms that were used to create a model package.
*Required*: No
*Type*: [SourceAlgorithmSpecification](aws-properties-sagemaker-modelpackage-sourcealgorithmspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceUri`  <a name="cfn-sagemaker-modelpackage-sourceuri"></a>
The URI of the source for the model package.
*Required*: No
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{Z}\p{N}\p{P}]{0,1024}`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Tags`  <a name="cfn-sagemaker-modelpackage-tags"></a>
A list of the tags associated with the model package. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-modelpackage-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Task`  <a name="cfn-sagemaker-modelpackage-task"></a>
The machine learning task your model package accomplishes. Common machine learning tasks include object detection and image classification.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ValidationSpecification`  <a name="cfn-sagemaker-modelpackage-validationspecification"></a>
Specifies batch transform jobs that SageMaker runs to validate your model package.
*Required*: No
*Type*: [ValidationSpecification](aws-properties-sagemaker-modelpackage-validationspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-modelpackage-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-modelpackage-return-values-ref"></a>

 When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the model package group.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sagemaker-modelpackage-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-modelpackage-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time that the model package was created.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The last time the model package was modified.

`ModelPackageArn`  <a name="ModelPackageArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the model package.

`ModelPackageStatus`  <a name="ModelPackageStatus-fn::getatt"></a>
The status of the model package. This can be one of the following values.
+ `PENDING` - The model package creation is pending.
+ `IN_PROGRESS` - The model package is in the process of being created.
+ `COMPLETED` - The model package was successfully created.
+ `FAILED` - The model package creation failed.
+ `DELETING` - The model package is in the process of being deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
