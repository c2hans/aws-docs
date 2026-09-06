---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmincidents-responseplan-ssmparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMIncidents::ResponsePlan SsmParameter
<a name="aws-properties-ssmincidents-responseplan-ssmparameter"></a>

The key-value pair parameters to use when running the Automation runbook.

## Syntax
<a name="aws-properties-ssmincidents-responseplan-ssmparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmincidents-responseplan-ssmparameter-syntax.json"></a>

```
{
  "[Key](#cfn-ssmincidents-responseplan-ssmparameter-key)" : {{String}},
  "[Values](#cfn-ssmincidents-responseplan-ssmparameter-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ssmincidents-responseplan-ssmparameter-syntax.yaml"></a>

```
  [Key](#cfn-ssmincidents-responseplan-ssmparameter-key): {{String}}
  [Values](#cfn-ssmincidents-responseplan-ssmparameter-values): {{
    - String}}
```

## Properties
<a name="aws-properties-ssmincidents-responseplan-ssmparameter-properties"></a>

`Key`  <a name="cfn-ssmincidents-responseplan-ssmparameter-key"></a>
The key parameter to use when running the Automation runbook.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-ssmincidents-responseplan-ssmparameter-values"></a>
The value parameter to use when running the Automation runbook.
*Required*: Yes
*Type*: Array of String
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
