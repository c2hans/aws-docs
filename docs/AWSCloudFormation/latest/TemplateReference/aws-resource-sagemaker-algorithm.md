---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-algorithm.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Algorithm
<a name="aws-resource-sagemaker-algorithm"></a>

Create a machine learning algorithm that you can use in SageMaker and list in the AWS Marketplace.

## Syntax
<a name="aws-resource-sagemaker-algorithm-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-algorithm-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::Algorithm",
  "Properties" : {
      "[AlgorithmDescription](#cfn-sagemaker-algorithm-algorithmdescription)" : {{String}},
      "[AlgorithmName](#cfn-sagemaker-algorithm-algorithmname)" : {{String}},
      "[CertifyForMarketplace](#cfn-sagemaker-algorithm-certifyformarketplace)" : {{Boolean}},
      "[InferenceSpecification](#cfn-sagemaker-algorithm-inferencespecification)" : {{InferenceSpecification}},
      "[Tags](#cfn-sagemaker-algorithm-tags)" : {{[ Tag, ... ]}},
      "[TrainingSpecification](#cfn-sagemaker-algorithm-trainingspecification)" : {{TrainingSpecification}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-algorithm-syntax.yaml"></a>

```
Type: AWS::SageMaker::Algorithm
Properties:
  [AlgorithmDescription](#cfn-sagemaker-algorithm-algorithmdescription): {{String}}
  [AlgorithmName](#cfn-sagemaker-algorithm-algorithmname): {{String}}
  [CertifyForMarketplace](#cfn-sagemaker-algorithm-certifyformarketplace): {{Boolean}}
  [InferenceSpecification](#cfn-sagemaker-algorithm-inferencespecification): {{
    InferenceSpecification}}
  [Tags](#cfn-sagemaker-algorithm-tags): {{
    - Tag}}
  [TrainingSpecification](#cfn-sagemaker-algorithm-trainingspecification): {{
    TrainingSpecification}}
```

## Properties
<a name="aws-resource-sagemaker-algorithm-properties"></a>

`AlgorithmDescription`  <a name="cfn-sagemaker-algorithm-algorithmdescription"></a>
A brief description of the algorithm.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AlgorithmName`  <a name="cfn-sagemaker-algorithm-algorithmname"></a>
The name of the algorithm that is described by the summary.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CertifyForMarketplace`  <a name="cfn-sagemaker-algorithm-certifyformarketplace"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InferenceSpecification`  <a name="cfn-sagemaker-algorithm-inferencespecification"></a>
Defines how to perform inference generation after a training job is run.
*Required*: No
*Type*: [InferenceSpecification](aws-properties-sagemaker-algorithm-inferencespecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-algorithm-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-algorithm-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrainingSpecification`  <a name="cfn-sagemaker-algorithm-trainingspecification"></a>
Defines how the algorithm is used for a training job.
*Required*: Yes
*Type*: [TrainingSpecification](aws-properties-sagemaker-algorithm-trainingspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-algorithm-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-algorithm-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-algorithm-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-algorithm-return-values-fn--getatt-fn--getatt"></a>

`AlgorithmArn`  <a name="AlgorithmArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the algorithm.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
A timestamp that shows when the algorithm was created.
