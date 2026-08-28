---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-objectivefunction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard ObjectiveFunction
<a name="aws-properties-sagemaker-modelcard-objectivefunction"></a>

The function that is optimized during model training.

## Syntax
<a name="aws-properties-sagemaker-modelcard-objectivefunction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-objectivefunction-syntax.json"></a>

```
{
  "[Function](#cfn-sagemaker-modelcard-objectivefunction-function)" : {{Function}},
  "[Notes](#cfn-sagemaker-modelcard-objectivefunction-notes)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-objectivefunction-syntax.yaml"></a>

```
  [Function](#cfn-sagemaker-modelcard-objectivefunction-function): {{
    Function}}
  [Notes](#cfn-sagemaker-modelcard-objectivefunction-notes): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-objectivefunction-properties"></a>

`Function`  <a name="cfn-sagemaker-modelcard-objectivefunction-function"></a>
A function object that details optimization direction, metric, and additional descriptions.
*Required*: No
*Type*: [Function](aws-properties-sagemaker-modelcard-function.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Notes`  <a name="cfn-sagemaker-modelcard-objectivefunction-notes"></a>
Notes about the object function, including other considerations for possible objective functions.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
