---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-segmentdefinition-addressdimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition AddressDimension
<a name="aws-properties-customerprofiles-segmentdefinition-addressdimension"></a>

Object that segments on Customer Profile's address object.

## Syntax
<a name="aws-properties-customerprofiles-segmentdefinition-addressdimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-segmentdefinition-addressdimension-syntax.json"></a>

```
{
  "[City](#cfn-customerprofiles-segmentdefinition-addressdimension-city)" : {{ProfileDimension}},
  "[Country](#cfn-customerprofiles-segmentdefinition-addressdimension-country)" : {{ProfileDimension}},
  "[County](#cfn-customerprofiles-segmentdefinition-addressdimension-county)" : {{ProfileDimension}},
  "[PostalCode](#cfn-customerprofiles-segmentdefinition-addressdimension-postalcode)" : {{ProfileDimension}},
  "[Province](#cfn-customerprofiles-segmentdefinition-addressdimension-province)" : {{ProfileDimension}},
  "[State](#cfn-customerprofiles-segmentdefinition-addressdimension-state)" : {{ProfileDimension}}
}
```

### YAML
<a name="aws-properties-customerprofiles-segmentdefinition-addressdimension-syntax.yaml"></a>

```
  [City](#cfn-customerprofiles-segmentdefinition-addressdimension-city): {{
    ProfileDimension}}
  [Country](#cfn-customerprofiles-segmentdefinition-addressdimension-country): {{
    ProfileDimension}}
  [County](#cfn-customerprofiles-segmentdefinition-addressdimension-county): {{
    ProfileDimension}}
  [PostalCode](#cfn-customerprofiles-segmentdefinition-addressdimension-postalcode): {{
    ProfileDimension}}
  [Province](#cfn-customerprofiles-segmentdefinition-addressdimension-province): {{
    ProfileDimension}}
  [State](#cfn-customerprofiles-segmentdefinition-addressdimension-state): {{
    ProfileDimension}}
```

## Properties
<a name="aws-properties-customerprofiles-segmentdefinition-addressdimension-properties"></a>

`City`  <a name="cfn-customerprofiles-segmentdefinition-addressdimension-city"></a>
The city belonging to the address.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Country`  <a name="cfn-customerprofiles-segmentdefinition-addressdimension-country"></a>
The country belonging to the address.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`County`  <a name="cfn-customerprofiles-segmentdefinition-addressdimension-county"></a>
The county belonging to the address.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PostalCode`  <a name="cfn-customerprofiles-segmentdefinition-addressdimension-postalcode"></a>
The postal code belonging to the address.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Province`  <a name="cfn-customerprofiles-segmentdefinition-addressdimension-province"></a>
The province belonging to the address.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`State`  <a name="cfn-customerprofiles-segmentdefinition-addressdimension-state"></a>
The state belonging to the address.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
