---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-mediapackageadditionaldestinations.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MediaPackageAdditionalDestinations
<a name="aws-properties-medialive-channel-mediapackageadditionaldestinations"></a>

Optional, an array of additional destination HTTP destinations for the output group outputs.

## Syntax
<a name="aws-properties-medialive-channel-mediapackageadditionaldestinations-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-mediapackageadditionaldestinations-syntax.json"></a>

```
{
  "[Destination](#cfn-medialive-channel-mediapackageadditionaldestinations-destination)" : {{OutputLocationRef}}
}
```

### YAML
<a name="aws-properties-medialive-channel-mediapackageadditionaldestinations-syntax.yaml"></a>

```
  [Destination](#cfn-medialive-channel-mediapackageadditionaldestinations-destination): {{
    OutputLocationRef}}
```

## Properties
<a name="aws-properties-medialive-channel-mediapackageadditionaldestinations-properties"></a>

`Destination`  <a name="cfn-medialive-channel-mediapackageadditionaldestinations-destination"></a>
The destination location for an additional CMAF Ingest output destination.
*Required*: No
*Type*: [OutputLocationRef](aws-properties-medialive-channel-outputlocationref.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
