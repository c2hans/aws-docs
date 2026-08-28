---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trialcomponent-trialcomponentparametervalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrialComponent TrialComponentParameterValue
<a name="aws-properties-sagemaker-trialcomponent-trialcomponentparametervalue"></a>

The value of a hyperparameter. Only one of `NumberValue` or `StringValue` can be specified.

This object is specified in the [CreateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html) request.

## Syntax
<a name="aws-properties-sagemaker-trialcomponent-trialcomponentparametervalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trialcomponent-trialcomponentparametervalue-syntax.json"></a>

```
{
  "[NumberValue](#cfn-sagemaker-trialcomponent-trialcomponentparametervalue-numbervalue)" : {{Number}},
  "[StringValue](#cfn-sagemaker-trialcomponent-trialcomponentparametervalue-stringvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-trialcomponent-trialcomponentparametervalue-syntax.yaml"></a>

```
  [NumberValue](#cfn-sagemaker-trialcomponent-trialcomponentparametervalue-numbervalue): {{
    Number}}
  [StringValue](#cfn-sagemaker-trialcomponent-trialcomponentparametervalue-stringvalue): {{
    String}}
```

## Properties
<a name="aws-properties-sagemaker-trialcomponent-trialcomponentparametervalue-properties"></a>

`NumberValue`  <a name="cfn-sagemaker-trialcomponent-trialcomponentparametervalue-numbervalue"></a>
The numeric value of a numeric hyperparameter. If you specify a value for this parameter, you can't specify the `StringValue` parameter.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringValue`  <a name="cfn-sagemaker-trialcomponent-trialcomponentparametervalue-stringvalue"></a>
The string value of a categorical hyperparameter. If you specify a value for this parameter, you can't specify the `NumberValue` parameter.
*Required*: No
*Type*: String
*Maximum*: `2500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
