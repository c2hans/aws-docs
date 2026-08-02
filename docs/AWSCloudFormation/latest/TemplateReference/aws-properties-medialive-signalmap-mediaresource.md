---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-signalmap-mediaresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::SignalMap MediaResource
<a name="aws-properties-medialive-signalmap-mediaresource"></a>

An Amazon Web Services resource used in media workflows.

## Syntax
<a name="aws-properties-medialive-signalmap-mediaresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-signalmap-mediaresource-syntax.json"></a>

```
{
  "[Destinations](#cfn-medialive-signalmap-mediaresource-destinations)" : {{[ MediaResourceNeighbor, ... ]}},
  "[Name](#cfn-medialive-signalmap-mediaresource-name)" : {{String}},
  "[Sources](#cfn-medialive-signalmap-mediaresource-sources)" : {{[ MediaResourceNeighbor, ... ]}}
}
```

### YAML
<a name="aws-properties-medialive-signalmap-mediaresource-syntax.yaml"></a>

```
  [Destinations](#cfn-medialive-signalmap-mediaresource-destinations): {{
    - MediaResourceNeighbor}}
  [Name](#cfn-medialive-signalmap-mediaresource-name): {{String}}
  [Sources](#cfn-medialive-signalmap-mediaresource-sources): {{
    - MediaResourceNeighbor}}
```

## Properties
<a name="aws-properties-medialive-signalmap-mediaresource-properties"></a>

`Destinations`  <a name="cfn-medialive-signalmap-mediaresource-destinations"></a>
A direct destination neighbor to an Amazon Web Services media resource.
*Required*: No
*Type*: Array of [MediaResourceNeighbor](aws-properties-medialive-signalmap-mediaresourceneighbor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-medialive-signalmap-mediaresource-name"></a>
The logical name of an Amazon Web Services media resource.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sources`  <a name="cfn-medialive-signalmap-mediaresource-sources"></a>
A direct source neighbor to an Amazon Web Services media resource.
*Required*: No
*Type*: Array of [MediaResourceNeighbor](aws-properties-medialive-signalmap-mediaresourceneighbor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
