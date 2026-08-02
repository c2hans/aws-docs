---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-additionaldestinations.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AdditionalDestinations
<a name="aws-properties-medialive-channel-additionaldestinations"></a>

Additional output destinations for a CMAF Ingest output group.

## Syntax
<a name="aws-properties-medialive-channel-additionaldestinations-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-additionaldestinations-syntax.json"></a>

```
{
  "[Destination](#cfn-medialive-channel-additionaldestinations-destination)" : {{OutputLocationRef}}
}
```

### YAML
<a name="aws-properties-medialive-channel-additionaldestinations-syntax.yaml"></a>

```
  [Destination](#cfn-medialive-channel-additionaldestinations-destination): {{
    OutputLocationRef}}
```

## Properties
<a name="aws-properties-medialive-channel-additionaldestinations-properties"></a>

`Destination`  <a name="cfn-medialive-channel-additionaldestinations-destination"></a>
The destination location.
*Required*: No
*Type*: [OutputLocationRef](aws-properties-medialive-channel-outputlocationref.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
