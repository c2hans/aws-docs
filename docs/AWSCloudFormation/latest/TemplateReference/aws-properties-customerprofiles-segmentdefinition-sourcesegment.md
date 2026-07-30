---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-segmentdefinition-sourcesegment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition SourceSegment
<a name="aws-properties-customerprofiles-segmentdefinition-sourcesegment"></a>

The source segments to build off of.

## Syntax
<a name="aws-properties-customerprofiles-segmentdefinition-sourcesegment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-segmentdefinition-sourcesegment-syntax.json"></a>

```
{
  "[SegmentDefinitionName](#cfn-customerprofiles-segmentdefinition-sourcesegment-segmentdefinitionname)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-segmentdefinition-sourcesegment-syntax.yaml"></a>

```
  [SegmentDefinitionName](#cfn-customerprofiles-segmentdefinition-sourcesegment-segmentdefinitionname): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-segmentdefinition-sourcesegment-properties"></a>

`SegmentDefinitionName`  <a name="cfn-customerprofiles-segmentdefinition-sourcesegment-segmentdefinitionname"></a>
The name of the source segment.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
