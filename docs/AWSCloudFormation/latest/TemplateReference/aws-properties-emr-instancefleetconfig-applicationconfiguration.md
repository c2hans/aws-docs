---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancefleetconfig-applicationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceFleetConfig ApplicationConfiguration
<a name="aws-properties-emr-instancefleetconfig-applicationconfiguration"></a>

<a name="aws-properties-emr-instancefleetconfig-applicationconfiguration-description"></a>The `ApplicationConfiguration` property type specifies Property description not available. for an [AWS::EMR::InstanceFleetConfig](aws-resource-emr-instancefleetconfig.md).

## Syntax
<a name="aws-properties-emr-instancefleetconfig-applicationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancefleetconfig-applicationconfiguration-syntax.json"></a>

```
{
  "[Classification](#cfn-emr-instancefleetconfig-applicationconfiguration-classification)" : {{String}},
  "[ConfigurationProperties](#cfn-emr-instancefleetconfig-applicationconfiguration-configurationproperties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Configurations](#cfn-emr-instancefleetconfig-applicationconfiguration-configurations)" : {{[ ApplicationConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-emr-instancefleetconfig-applicationconfiguration-syntax.yaml"></a>

```
  [Classification](#cfn-emr-instancefleetconfig-applicationconfiguration-classification): {{String}}
  [ConfigurationProperties](#cfn-emr-instancefleetconfig-applicationconfiguration-configurationproperties): {{
    {{Key}}: {{Value}}}}
  [Configurations](#cfn-emr-instancefleetconfig-applicationconfiguration-configurations): {{
    - ApplicationConfiguration}}
```

## Properties
<a name="aws-properties-emr-instancefleetconfig-applicationconfiguration-properties"></a>

`Classification`  <a name="cfn-emr-instancefleetconfig-applicationconfiguration-classification"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigurationProperties`  <a name="cfn-emr-instancefleetconfig-applicationconfiguration-configurationproperties"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z0-9]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Configurations`  <a name="cfn-emr-instancefleetconfig-applicationconfiguration-configurations"></a>
Property description not available.
*Required*: No
*Type*: Array of [ApplicationConfiguration](#aws-properties-emr-instancefleetconfig-applicationconfiguration)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
