---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-modelpackagedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard ModelPackageDetails
<a name="aws-properties-sagemaker-modelcard-modelpackagedetails"></a>

Details about the model package associated with the model card.

## Syntax
<a name="aws-properties-sagemaker-modelcard-modelpackagedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-modelpackagedetails-syntax.json"></a>

```
{
  "[ApprovalDescription](#cfn-sagemaker-modelcard-modelpackagedetails-approvaldescription)" : {{String}},
  "[CreatedBy](#cfn-sagemaker-modelcard-modelpackagedetails-createdby)" : {{ModelPackageCreator}},
  "[Domain](#cfn-sagemaker-modelcard-modelpackagedetails-domain)" : {{String}},
  "[InferenceSpecification](#cfn-sagemaker-modelcard-modelpackagedetails-inferencespecification)" : {{InferenceSpecification}},
  "[ModelApprovalStatus](#cfn-sagemaker-modelcard-modelpackagedetails-modelapprovalstatus)" : {{String}},
  "[ModelPackageArn](#cfn-sagemaker-modelcard-modelpackagedetails-modelpackagearn)" : {{String}},
  "[ModelPackageDescription](#cfn-sagemaker-modelcard-modelpackagedetails-modelpackagedescription)" : {{String}},
  "[ModelPackageGroupName](#cfn-sagemaker-modelcard-modelpackagedetails-modelpackagegroupname)" : {{String}},
  "[ModelPackageName](#cfn-sagemaker-modelcard-modelpackagedetails-modelpackagename)" : {{String}},
  "[ModelPackageStatus](#cfn-sagemaker-modelcard-modelpackagedetails-modelpackagestatus)" : {{String}},
  "[ModelPackageVersion](#cfn-sagemaker-modelcard-modelpackagedetails-modelpackageversion)" : {{Number}},
  "[SourceAlgorithms](#cfn-sagemaker-modelcard-modelpackagedetails-sourcealgorithms)" : {{[ SourceAlgorithm, ... ]}},
  "[Task](#cfn-sagemaker-modelcard-modelpackagedetails-task)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-modelpackagedetails-syntax.yaml"></a>

```
  [ApprovalDescription](#cfn-sagemaker-modelcard-modelpackagedetails-approvaldescription): {{String}}
  [CreatedBy](#cfn-sagemaker-modelcard-modelpackagedetails-createdby): {{
    ModelPackageCreator}}
  [Domain](#cfn-sagemaker-modelcard-modelpackagedetails-domain): {{String}}
  [InferenceSpecification](#cfn-sagemaker-modelcard-modelpackagedetails-inferencespecification): {{
    InferenceSpecification}}
  [ModelApprovalStatus](#cfn-sagemaker-modelcard-modelpackagedetails-modelapprovalstatus): {{String}}
  [ModelPackageArn](#cfn-sagemaker-modelcard-modelpackagedetails-modelpackagearn): {{String}}
  [ModelPackageDescription](#cfn-sagemaker-modelcard-modelpackagedetails-modelpackagedescription): {{String}}
  [ModelPackageGroupName](#cfn-sagemaker-modelcard-modelpackagedetails-modelpackagegroupname): {{String}}
  [ModelPackageName](#cfn-sagemaker-modelcard-modelpackagedetails-modelpackagename): {{String}}
  [ModelPackageStatus](#cfn-sagemaker-modelcard-modelpackagedetails-modelpackagestatus): {{String}}
  [ModelPackageVersion](#cfn-sagemaker-modelcard-modelpackagedetails-modelpackageversion): {{Number}}
  [SourceAlgorithms](#cfn-sagemaker-modelcard-modelpackagedetails-sourcealgorithms): {{
    - SourceAlgorithm}}
  [Task](#cfn-sagemaker-modelcard-modelpackagedetails-task): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-modelpackagedetails-properties"></a>

`ApprovalDescription`  <a name="cfn-sagemaker-modelcard-modelpackagedetails-approvaldescription"></a>
A description of the approval status of the model package.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreatedBy`  <a name="cfn-sagemaker-modelcard-modelpackagedetails-createdby"></a>
Information about the user who created the model package.
*Required*: No
*Type*: [ModelPackageCreator](aws-properties-sagemaker-modelcard-modelpackagecreator.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Domain`  <a name="cfn-sagemaker-modelcard-modelpackagedetails-domain"></a>
The machine learning domain of the model package.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InferenceSpecification`  <a name="cfn-sagemaker-modelcard-modelpackagedetails-inferencespecification"></a>
Details about the inference specification for the model package.
*Required*: No
*Type*: [InferenceSpecification](aws-properties-sagemaker-modelcard-inferencespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelApprovalStatus`  <a name="cfn-sagemaker-modelcard-modelpackagedetails-modelapprovalstatus"></a>
The approval status of the model package.
*Required*: No
*Type*: String
*Allowed values*: `Approved | Rejected | PendingManualApproval`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelPackageArn`  <a name="cfn-sagemaker-modelcard-modelpackagedetails-modelpackagearn"></a>
The Amazon Resource Name (ARN) of the model package.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelPackageDescription`  <a name="cfn-sagemaker-modelcard-modelpackagedetails-modelpackagedescription"></a>
A description of the model package.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelPackageGroupName`  <a name="cfn-sagemaker-modelcard-modelpackagedetails-modelpackagegroupname"></a>
The name of the model package group.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelPackageName`  <a name="cfn-sagemaker-modelcard-modelpackagedetails-modelpackagename"></a>
The name of the model package.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelPackageStatus`  <a name="cfn-sagemaker-modelcard-modelpackagedetails-modelpackagestatus"></a>
The status of the model package.
*Required*: No
*Type*: String
*Allowed values*: `Pending | InProgress | Completed | Failed | Deleting`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelPackageVersion`  <a name="cfn-sagemaker-modelcard-modelpackagedetails-modelpackageversion"></a>
The version of the model package.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceAlgorithms`  <a name="cfn-sagemaker-modelcard-modelpackagedetails-sourcealgorithms"></a>
A list of algorithms that were used to create the model package.
*Required*: No
*Type*: Array of [SourceAlgorithm](aws-properties-sagemaker-modelcard-sourcealgorithm.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Task`  <a name="cfn-sagemaker-modelcard-modelpackagedetails-task"></a>
The machine learning task performed by the model package.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
