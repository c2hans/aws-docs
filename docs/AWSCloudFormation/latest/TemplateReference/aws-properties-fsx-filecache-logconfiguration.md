---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-filecache-logconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::FileCache LogConfiguration
<a name="aws-properties-fsx-filecache-logconfiguration"></a>

<a name="aws-properties-fsx-filecache-logconfiguration-description"></a>The `LogConfiguration` property type specifies Property description not available. for an [AWS::FSx::FileCache](aws-resource-fsx-filecache.md).

## Syntax
<a name="aws-properties-fsx-filecache-logconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-filecache-logconfiguration-syntax.json"></a>

```
{
  "[Destination](#cfn-fsx-filecache-logconfiguration-destination)" : {{String}},
  "[Level](#cfn-fsx-filecache-logconfiguration-level)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-filecache-logconfiguration-syntax.yaml"></a>

```
  [Destination](#cfn-fsx-filecache-logconfiguration-destination): {{String}}
  [Level](#cfn-fsx-filecache-logconfiguration-level): {{String}}
```

## Properties
<a name="aws-properties-fsx-filecache-logconfiguration-properties"></a>

`Destination`  <a name="cfn-fsx-filecache-logconfiguration-destination"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `8`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Level`  <a name="cfn-fsx-filecache-logconfiguration-level"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `DISABLED | WARN_ONLY | ERROR_ONLY | WARN_ERROR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
