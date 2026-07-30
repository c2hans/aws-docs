---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-remediationconfiguration-remediationparametervalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::RemediationConfiguration RemediationParameterValue
<a name="aws-properties-config-remediationconfiguration-remediationparametervalue"></a>

The value is either a dynamic (resource) value or a static value. You must select either a dynamic value or a static value.

## Syntax
<a name="aws-properties-config-remediationconfiguration-remediationparametervalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-remediationconfiguration-remediationparametervalue-syntax.json"></a>

```
{
  "[ResourceValue](#cfn-config-remediationconfiguration-remediationparametervalue-resourcevalue)" : {{String}},
  "[StaticValue](#cfn-config-remediationconfiguration-remediationparametervalue-staticvalue)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-config-remediationconfiguration-remediationparametervalue-syntax.yaml"></a>

```
  [ResourceValue](#cfn-config-remediationconfiguration-remediationparametervalue-resourcevalue): {{String}}
  [StaticValue](#cfn-config-remediationconfiguration-remediationparametervalue-staticvalue): {{
    - String}}
```

## Properties
<a name="aws-properties-config-remediationconfiguration-remediationparametervalue-properties"></a>

`ResourceValue`  <a name="cfn-config-remediationconfiguration-remediationparametervalue-resourcevalue"></a>
The value is dynamic and changes at run-time.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticValue`  <a name="cfn-config-remediationconfiguration-remediationparametervalue-staticvalue"></a>
The value is static and does not change at run-time.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
