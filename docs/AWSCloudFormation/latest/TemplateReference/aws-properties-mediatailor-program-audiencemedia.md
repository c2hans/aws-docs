---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-program-audiencemedia.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Program AudienceMedia
<a name="aws-properties-mediatailor-program-audiencemedia"></a>

An AudienceMedia object contains an Audience and a list of AlternateMedia.

## Syntax
<a name="aws-properties-mediatailor-program-audiencemedia-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-program-audiencemedia-syntax.json"></a>

```
{
  "[AlternateMedia](#cfn-mediatailor-program-audiencemedia-alternatemedia)" : {{[ AlternateMedia, ... ]}},
  "[Audience](#cfn-mediatailor-program-audiencemedia-audience)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-program-audiencemedia-syntax.yaml"></a>

```
  [AlternateMedia](#cfn-mediatailor-program-audiencemedia-alternatemedia): {{
    - AlternateMedia}}
  [Audience](#cfn-mediatailor-program-audiencemedia-audience): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-program-audiencemedia-properties"></a>

`AlternateMedia`  <a name="cfn-mediatailor-program-audiencemedia-alternatemedia"></a>
The list of AlternateMedia defined in AudienceMedia.
*Required*: No
*Type*: [Array](aws-properties-mediatailor-program-alternatemedia.md) of [AlternateMedia](aws-properties-mediatailor-program-alternatemedia.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Audience`  <a name="cfn-mediatailor-program-audiencemedia-audience"></a>
The Audience defined in AudienceMedia.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
