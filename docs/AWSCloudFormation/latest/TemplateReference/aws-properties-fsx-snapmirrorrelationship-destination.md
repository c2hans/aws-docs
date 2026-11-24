---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-snapmirrorrelationship-destination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::SnapmirrorRelationship Destination

<a name="aws-properties-fsx-snapmirrorrelationship-destination-description"></a>The `Destination` property type specifies Property description not available. for an [AWS::FSx::SnapmirrorRelationship](aws-resource-fsx-snapmirrorrelationship.md).

## Syntax
<a name="aws-properties-fsx-snapmirrorrelationship-destination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-snapmirrorrelationship-destination-syntax.json"></a>

```json
{
  "[Path](#cfn-fsx-snapmirrorrelationship-destination-path)" : {{String}},
  "[VolumeId](#cfn-fsx-snapmirrorrelationship-destination-volumeid)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-snapmirrorrelationship-destination-syntax.yaml"></a>

```yaml
  [Path](#cfn-fsx-snapmirrorrelationship-destination-path): {{String}}
  [VolumeId](#cfn-fsx-snapmirrorrelationship-destination-volumeid): {{String}}
```

## Properties
<a name="aws-properties-fsx-snapmirrorrelationship-destination-properties"></a>

`Path`  <a name="cfn-fsx-snapmirrorrelationship-destination-path"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{1,512}$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeId`  <a name="cfn-fsx-snapmirrorrelationship-destination-volumeid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(fsvol-[0-9a-f]{17,})$`
*Minimum*: `23`
*Maximum*: `23`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
