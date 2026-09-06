---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-connectionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection ConnectionConfiguration
<a name="aws-properties-datazone-connection-connectionconfiguration"></a>

<a name="aws-properties-datazone-connection-connectionconfiguration-description"></a>The `ConnectionConfiguration` property type specifies Property description not available. for an [AWS::DataZone::Connection](aws-resource-datazone-connection.md).

## Syntax
<a name="aws-properties-datazone-connection-connectionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-connectionconfiguration-syntax.json"></a>

```
{
  "[Classification](#cfn-datazone-connection-connectionconfiguration-classification)" : {{String}},
  "[Properties](#cfn-datazone-connection-connectionconfiguration-properties)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-datazone-connection-connectionconfiguration-syntax.yaml"></a>

```
  [Classification](#cfn-datazone-connection-connectionconfiguration-classification): {{String}}
  [Properties](#cfn-datazone-connection-connectionconfiguration-properties): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-datazone-connection-connectionconfiguration-properties"></a>

`Classification`  <a name="cfn-datazone-connection-connectionconfiguration-classification"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\w][\w\.\-\_]*$`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Properties`  <a name="cfn-datazone-connection-connectionconfiguration-properties"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFF\t]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
