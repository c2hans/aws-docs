---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-function.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard Function
<a name="aws-properties-sagemaker-modelcard-function"></a>

Function details.

## Syntax
<a name="aws-properties-sagemaker-modelcard-function-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-function-syntax.json"></a>

```
{
  "[Condition](#cfn-sagemaker-modelcard-function-condition)" : {{String}},
  "[Facet](#cfn-sagemaker-modelcard-function-facet)" : {{String}},
  "[Function](#cfn-sagemaker-modelcard-function-function)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-function-syntax.yaml"></a>

```
  [Condition](#cfn-sagemaker-modelcard-function-condition): {{String}}
  [Facet](#cfn-sagemaker-modelcard-function-facet): {{String}}
  [Function](#cfn-sagemaker-modelcard-function-function): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-function-properties"></a>

`Condition`  <a name="cfn-sagemaker-modelcard-function-condition"></a>
An optional description of any conditions of your objective function metric.
*Required*: No
*Type*: String
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Facet`  <a name="cfn-sagemaker-modelcard-function-facet"></a>
The metric of the model's objective function. For example, *loss* or *rmse*. The following list shows examples of the values that you can specify for the metric:
+  `ACCURACY`
+  `AUC`
+  `LOSS`
+  `MAE`
+  `RMSE`
*Required*: No
*Type*: String
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Function`  <a name="cfn-sagemaker-modelcard-function-function"></a>
The optimization direction of the model's objective function. You must specify one of the following values:
+  `Maximize`
+  `Minimize`
*Required*: No
*Type*: [String](#aws-properties-sagemaker-modelcard-function)
*Allowed values*: `Maximize | Minimize`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
