---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-customerprofiles-segmentdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition
<a name="aws-resource-customerprofiles-segmentdefinition"></a>

A segment definition resource of Amazon Connect Customer Profiles.

## Syntax
<a name="aws-resource-customerprofiles-segmentdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-customerprofiles-segmentdefinition-syntax.json"></a>

```
{
  "Type" : "AWS::CustomerProfiles::SegmentDefinition",
  "Properties" : {
      "[Description](#cfn-customerprofiles-segmentdefinition-description)" : {{String}},
      "[DisplayName](#cfn-customerprofiles-segmentdefinition-displayname)" : {{String}},
      "[DomainName](#cfn-customerprofiles-segmentdefinition-domainname)" : {{String}},
      "[SegmentDefinitionName](#cfn-customerprofiles-segmentdefinition-segmentdefinitionname)" : {{String}},
      "[SegmentGroups](#cfn-customerprofiles-segmentdefinition-segmentgroups)" : {{SegmentGroup}},
      "[SegmentSort](#cfn-customerprofiles-segmentdefinition-segmentsort)" : {{SegmentSort}},
      "[SegmentSqlQuery](#cfn-customerprofiles-segmentdefinition-segmentsqlquery)" : {{String}},
      "[Tags](#cfn-customerprofiles-segmentdefinition-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-customerprofiles-segmentdefinition-syntax.yaml"></a>

```
Type: AWS::CustomerProfiles::SegmentDefinition
Properties:
  [Description](#cfn-customerprofiles-segmentdefinition-description): {{String}}
  [DisplayName](#cfn-customerprofiles-segmentdefinition-displayname): {{String}}
  [DomainName](#cfn-customerprofiles-segmentdefinition-domainname): {{String}}
  [SegmentDefinitionName](#cfn-customerprofiles-segmentdefinition-segmentdefinitionname): {{String}}
  [SegmentGroups](#cfn-customerprofiles-segmentdefinition-segmentgroups): {{
    SegmentGroup}}
  [SegmentSort](#cfn-customerprofiles-segmentdefinition-segmentsort): {{
    SegmentSort}}
  [SegmentSqlQuery](#cfn-customerprofiles-segmentdefinition-segmentsqlquery): {{String}}
  [Tags](#cfn-customerprofiles-segmentdefinition-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-customerprofiles-segmentdefinition-properties"></a>

`Description`  <a name="cfn-customerprofiles-segmentdefinition-description"></a>
The description of the segment definition.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-customerprofiles-segmentdefinition-displayname"></a>
Display name of the segment definition.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainName`  <a name="cfn-customerprofiles-segmentdefinition-domainname"></a>
The name of the domain.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SegmentDefinitionName`  <a name="cfn-customerprofiles-segmentdefinition-segmentdefinitionname"></a>
Name of the segment definition.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SegmentGroups`  <a name="cfn-customerprofiles-segmentdefinition-segmentgroups"></a>
Contains all groups of the segment definition.
*Required*: No
*Type*: [SegmentGroup](aws-properties-customerprofiles-segmentdefinition-segmentgroup.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SegmentSort`  <a name="cfn-customerprofiles-segmentdefinition-segmentsort"></a>
Property description not available.
*Required*: No
*Type*: [SegmentSort](aws-properties-customerprofiles-segmentdefinition-segmentsort.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentSqlQuery`  <a name="cfn-customerprofiles-segmentdefinition-segmentsqlquery"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `50000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-customerprofiles-segmentdefinition-tags"></a>
The tags belonging to the segment definition.
*Required*: No
*Type*: Array of [Tag](aws-properties-customerprofiles-segmentdefinition-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-customerprofiles-segmentdefinition-return-values"></a>

### Ref
<a name="aws-resource-customerprofiles-segmentdefinition-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-customerprofiles-segmentdefinition-return-values-fn--getatt"></a>

####
<a name="aws-resource-customerprofiles-segmentdefinition-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
When the segment definition was created.

`SegmentDefinitionArn`  <a name="SegmentDefinitionArn-fn::getatt"></a>
The arn of the segment definition.

`SegmentType`  <a name="SegmentType-fn::getatt"></a>
The segment type.
 Classic : Segments created using traditional SegmentGroup structure
 Enhanced : Segments created using SQL queries

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
