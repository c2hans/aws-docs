---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-environmentblueprintconfiguration-regionalparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::EnvironmentBlueprintConfiguration RegionalParameter
<a name="aws-properties-datazone-environmentblueprintconfiguration-regionalparameter"></a>

The regional parameters in the environment blueprint.

## Syntax
<a name="aws-properties-datazone-environmentblueprintconfiguration-regionalparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-environmentblueprintconfiguration-regionalparameter-syntax.json"></a>

```
{
  "[Parameters](#cfn-datazone-environmentblueprintconfiguration-regionalparameter-parameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Region](#cfn-datazone-environmentblueprintconfiguration-regionalparameter-region)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-environmentblueprintconfiguration-regionalparameter-syntax.yaml"></a>

```
  [Parameters](#cfn-datazone-environmentblueprintconfiguration-regionalparameter-parameters): {{
    {{Key}}: {{Value}}}}
  [Region](#cfn-datazone-environmentblueprintconfiguration-regionalparameter-region): {{String}}
```

## Properties
<a name="aws-properties-datazone-environmentblueprintconfiguration-regionalparameter-properties"></a>

`Parameters`  <a name="cfn-datazone-environmentblueprintconfiguration-regionalparameter-parameters"></a>
A string to string map containing parameters for the region.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-datazone-environmentblueprintconfiguration-regionalparameter-region"></a>
The region specified in the environment parameter.
*Required*: No
*Type*: String
*Pattern*: `^[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
