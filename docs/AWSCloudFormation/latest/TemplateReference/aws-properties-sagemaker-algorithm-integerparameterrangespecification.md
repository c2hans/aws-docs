---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-algorithm-integerparameterrangespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Algorithm IntegerParameterRangeSpecification
<a name="aws-properties-sagemaker-algorithm-integerparameterrangespecification"></a>

Defines the possible values for an integer hyperparameter.

## Syntax
<a name="aws-properties-sagemaker-algorithm-integerparameterrangespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-algorithm-integerparameterrangespecification-syntax.json"></a>

```
{
  "[MaxValue](#cfn-sagemaker-algorithm-integerparameterrangespecification-maxvalue)" : {{String}},
  "[MinValue](#cfn-sagemaker-algorithm-integerparameterrangespecification-minvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-algorithm-integerparameterrangespecification-syntax.yaml"></a>

```
  [MaxValue](#cfn-sagemaker-algorithm-integerparameterrangespecification-maxvalue): {{String}}
  [MinValue](#cfn-sagemaker-algorithm-integerparameterrangespecification-minvalue): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-algorithm-integerparameterrangespecification-properties"></a>

`MaxValue`  <a name="cfn-sagemaker-algorithm-integerparameterrangespecification-maxvalue"></a>
The maximum integer value allowed.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinValue`  <a name="cfn-sagemaker-algorithm-integerparameterrangespecification-minvalue"></a>
The minimum integer value allowed.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
