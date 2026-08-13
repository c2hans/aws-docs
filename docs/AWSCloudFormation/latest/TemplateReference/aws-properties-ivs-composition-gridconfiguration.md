---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-composition-gridconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::Composition GridConfiguration
<a name="aws-properties-ivs-composition-gridconfiguration"></a>

<a name="aws-properties-ivs-composition-gridconfiguration-description"></a>The `GridConfiguration` property type specifies Property description not available. for an [AWS::IVS::Composition](aws-resource-ivs-composition.md).

## Syntax
<a name="aws-properties-ivs-composition-gridconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-composition-gridconfiguration-syntax.json"></a>

```
{
  "[FeaturedParticipantAttribute](#cfn-ivs-composition-gridconfiguration-featuredparticipantattribute)" : {{String}},
  "[GridGap](#cfn-ivs-composition-gridconfiguration-gridgap)" : {{Integer}},
  "[OmitStoppedVideo](#cfn-ivs-composition-gridconfiguration-omitstoppedvideo)" : {{Boolean}},
  "[ParticipantOrderAttribute](#cfn-ivs-composition-gridconfiguration-participantorderattribute)" : {{String}},
  "[VideoAspectRatio](#cfn-ivs-composition-gridconfiguration-videoaspectratio)" : {{String}},
  "[VideoFillMode](#cfn-ivs-composition-gridconfiguration-videofillmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-ivs-composition-gridconfiguration-syntax.yaml"></a>

```
  [FeaturedParticipantAttribute](#cfn-ivs-composition-gridconfiguration-featuredparticipantattribute): {{String}}
  [GridGap](#cfn-ivs-composition-gridconfiguration-gridgap): {{Integer}}
  [OmitStoppedVideo](#cfn-ivs-composition-gridconfiguration-omitstoppedvideo): {{Boolean}}
  [ParticipantOrderAttribute](#cfn-ivs-composition-gridconfiguration-participantorderattribute): {{String}}
  [VideoAspectRatio](#cfn-ivs-composition-gridconfiguration-videoaspectratio): {{String}}
  [VideoFillMode](#cfn-ivs-composition-gridconfiguration-videofillmode): {{String}}
```

## Properties
<a name="aws-properties-ivs-composition-gridconfiguration-properties"></a>

`FeaturedParticipantAttribute`  <a name="cfn-ivs-composition-gridconfiguration-featuredparticipantattribute"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]*$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GridGap`  <a name="cfn-ivs-composition-gridconfiguration-gridgap"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OmitStoppedVideo`  <a name="cfn-ivs-composition-gridconfiguration-omitstoppedvideo"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ParticipantOrderAttribute`  <a name="cfn-ivs-composition-gridconfiguration-participantorderattribute"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]*$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VideoAspectRatio`  <a name="cfn-ivs-composition-gridconfiguration-videoaspectratio"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | VIDEO | SQUARE | PORTRAIT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VideoFillMode`  <a name="cfn-ivs-composition-gridconfiguration-videofillmode"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `FILL | COVER | CONTAIN`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
