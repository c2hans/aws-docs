---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-servicecatalog-serviceaction-definitionparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceCatalog::ServiceAction DefinitionParameter
<a name="aws-properties-servicecatalog-serviceaction-definitionparameter"></a>

The list of parameters in JSON format. For example: `[{\"Name\":\"InstanceId\",\"Type\":\"TARGET\"}] or [{\"Name\":\"InstanceId\",\"Type\":\"TEXT_VALUE\"}]`.

## Syntax
<a name="aws-properties-servicecatalog-serviceaction-definitionparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-servicecatalog-serviceaction-definitionparameter-syntax.json"></a>

```
{
  "[Key](#cfn-servicecatalog-serviceaction-definitionparameter-key)" : {{String}},
  "[Value](#cfn-servicecatalog-serviceaction-definitionparameter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-servicecatalog-serviceaction-definitionparameter-syntax.yaml"></a>

```
  [Key](#cfn-servicecatalog-serviceaction-definitionparameter-key): {{String}}
  [Value](#cfn-servicecatalog-serviceaction-definitionparameter-value): {{String}}
```

## Properties
<a name="aws-properties-servicecatalog-serviceaction-definitionparameter-properties"></a>

`Key`  <a name="cfn-servicecatalog-serviceaction-definitionparameter-key"></a>
The parameter key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-servicecatalog-serviceaction-definitionparameter-value"></a>
The value of the parameter.
*Required*: Yes
*Type*: String
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
