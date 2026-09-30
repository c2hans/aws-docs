---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-program-cliprange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Program ClipRange
<a name="aws-properties-mediatailor-program-cliprange"></a>

Clip range configuration for the VOD source associated with the program.

## Syntax
<a name="aws-properties-mediatailor-program-cliprange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-program-cliprange-syntax.json"></a>

```
{
  "[EndOffsetMillis](#cfn-mediatailor-program-cliprange-endoffsetmillis)" : {{Integer}},
  "[StartOffsetMillis](#cfn-mediatailor-program-cliprange-startoffsetmillis)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediatailor-program-cliprange-syntax.yaml"></a>

```
  [EndOffsetMillis](#cfn-mediatailor-program-cliprange-endoffsetmillis): {{Integer}}
  [StartOffsetMillis](#cfn-mediatailor-program-cliprange-startoffsetmillis): {{Integer}}
```

## Properties
<a name="aws-properties-mediatailor-program-cliprange-properties"></a>

`EndOffsetMillis`  <a name="cfn-mediatailor-program-cliprange-endoffsetmillis"></a>
The end offset of the clip range, in milliseconds, starting from the beginning of the VOD source associated with the program.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartOffsetMillis`  <a name="cfn-mediatailor-program-cliprange-startoffsetmillis"></a>
The start offset of the clip range, in milliseconds. This offset truncates the start at the number of milliseconds into the duration of the VOD source.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
