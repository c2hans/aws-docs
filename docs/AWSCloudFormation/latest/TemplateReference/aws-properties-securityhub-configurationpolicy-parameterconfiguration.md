---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-configurationpolicy-parameterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConfigurationPolicy ParameterConfiguration
<a name="aws-properties-securityhub-configurationpolicy-parameterconfiguration"></a>

 An object that provides the current value of a security control parameter and identifies whether it has been customized.

## Syntax
<a name="aws-properties-securityhub-configurationpolicy-parameterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-configurationpolicy-parameterconfiguration-syntax.json"></a>

```
{
  "[Value](#cfn-securityhub-configurationpolicy-parameterconfiguration-value)" : {{ParameterValue}},
  "[ValueType](#cfn-securityhub-configurationpolicy-parameterconfiguration-valuetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-configurationpolicy-parameterconfiguration-syntax.yaml"></a>

```
  [Value](#cfn-securityhub-configurationpolicy-parameterconfiguration-value): {{
    ParameterValue}}
  [ValueType](#cfn-securityhub-configurationpolicy-parameterconfiguration-valuetype): {{String}}
```

## Properties
<a name="aws-properties-securityhub-configurationpolicy-parameterconfiguration-properties"></a>

`Value`  <a name="cfn-securityhub-configurationpolicy-parameterconfiguration-value"></a>
 The current value of a control parameter.
*Required*: No
*Type*: [ParameterValue](aws-properties-securityhub-configurationpolicy-parametervalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueType`  <a name="cfn-securityhub-configurationpolicy-parameterconfiguration-valuetype"></a>
 Identifies whether a control parameter uses a custom user-defined value or subscribes to the default AWS Security Hub CSPM behavior.
When `ValueType` is set equal to `DEFAULT`, the default behavior can be a specific Security Hub CSPM default value, or the default behavior can be to ignore a specific parameter. When `ValueType` is set equal to `DEFAULT`, Security Hub CSPM ignores user-provided input for the `Value` field.
When `ValueType` is set equal to `CUSTOM`, the `Value` field can't be empty.
*Required*: Yes
*Type*: String
*Allowed values*: `DEFAULT | CUSTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
