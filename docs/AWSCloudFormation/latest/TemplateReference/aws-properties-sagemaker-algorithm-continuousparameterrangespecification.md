---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-algorithm-continuousparameterrangespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Algorithm ContinuousParameterRangeSpecification
<a name="aws-properties-sagemaker-algorithm-continuousparameterrangespecification"></a>

Defines the possible values for a continuous hyperparameter.

## Syntax
<a name="aws-properties-sagemaker-algorithm-continuousparameterrangespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-algorithm-continuousparameterrangespecification-syntax.json"></a>

```
{
  "[MaxValue](#cfn-sagemaker-algorithm-continuousparameterrangespecification-maxvalue)" : {{String}},
  "[MinValue](#cfn-sagemaker-algorithm-continuousparameterrangespecification-minvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-algorithm-continuousparameterrangespecification-syntax.yaml"></a>

```
  [MaxValue](#cfn-sagemaker-algorithm-continuousparameterrangespecification-maxvalue): {{String}}
  [MinValue](#cfn-sagemaker-algorithm-continuousparameterrangespecification-minvalue): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-algorithm-continuousparameterrangespecification-properties"></a>

`MaxValue`  <a name="cfn-sagemaker-algorithm-continuousparameterrangespecification-maxvalue"></a>
The maximum floating-point value allowed.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinValue`  <a name="cfn-sagemaker-algorithm-continuousparameterrangespecification-minvalue"></a>
The minimum floating-point value allowed.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
