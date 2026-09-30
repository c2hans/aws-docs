---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-program-slatesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Program SlateSource
<a name="aws-properties-mediatailor-program-slatesource"></a>

Slate VOD source configuration.

## Syntax
<a name="aws-properties-mediatailor-program-slatesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-program-slatesource-syntax.json"></a>

```
{
  "[SourceLocationName](#cfn-mediatailor-program-slatesource-sourcelocationname)" : {{String}},
  "[VodSourceName](#cfn-mediatailor-program-slatesource-vodsourcename)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-program-slatesource-syntax.yaml"></a>

```
  [SourceLocationName](#cfn-mediatailor-program-slatesource-sourcelocationname): {{String}}
  [VodSourceName](#cfn-mediatailor-program-slatesource-vodsourcename): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-program-slatesource-properties"></a>

`SourceLocationName`  <a name="cfn-mediatailor-program-slatesource-sourcelocationname"></a>
The name of the source location where the slate VOD source is stored.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VodSourceName`  <a name="cfn-mediatailor-program-slatesource-vodsourcename"></a>
The slate VOD source name. The VOD source must already exist in a source location before it can be used for slate.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
