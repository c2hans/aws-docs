---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancegroupconfig-appconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceGroupConfig AppConfiguration
<a name="aws-properties-emr-instancegroupconfig-appconfiguration"></a>

<a name="aws-properties-emr-instancegroupconfig-appconfiguration-description"></a>The `AppConfiguration` property type specifies Property description not available. for an [AWS::EMR::InstanceGroupConfig](aws-resource-emr-instancegroupconfig.md).

## Syntax
<a name="aws-properties-emr-instancegroupconfig-appconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancegroupconfig-appconfiguration-syntax.json"></a>

```
{
  "[Classification](#cfn-emr-instancegroupconfig-appconfiguration-classification)" : {{String}},
  "[ConfigurationProperties](#cfn-emr-instancegroupconfig-appconfiguration-configurationproperties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Configurations](#cfn-emr-instancegroupconfig-appconfiguration-configurations)" : {{[ AppConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-emr-instancegroupconfig-appconfiguration-syntax.yaml"></a>

```
  [Classification](#cfn-emr-instancegroupconfig-appconfiguration-classification): {{String}}
  [ConfigurationProperties](#cfn-emr-instancegroupconfig-appconfiguration-configurationproperties): {{
    {{Key}}: {{Value}}}}
  [Configurations](#cfn-emr-instancegroupconfig-appconfiguration-configurations): {{
    - AppConfiguration}}
```

## Properties
<a name="aws-properties-emr-instancegroupconfig-appconfiguration-properties"></a>

`Classification`  <a name="cfn-emr-instancegroupconfig-appconfiguration-classification"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConfigurationProperties`  <a name="cfn-emr-instancegroupconfig-appconfiguration-configurationproperties"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^.*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configurations`  <a name="cfn-emr-instancegroupconfig-appconfiguration-configurations"></a>
Property description not available.
*Required*: No
*Type*: Array of [AppConfiguration](#aws-properties-emr-instancegroupconfig-appconfiguration)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
