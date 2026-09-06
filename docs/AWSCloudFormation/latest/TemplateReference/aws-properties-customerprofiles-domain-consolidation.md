---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-domain-consolidation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Domain Consolidation
<a name="aws-properties-customerprofiles-domain-consolidation"></a>

A list of matching attributes that represent matching criteria. If two profiles meet at least one of the requirements in the matching attributes list, they will be merged.

## Syntax
<a name="aws-properties-customerprofiles-domain-consolidation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-domain-consolidation-syntax.json"></a>

```
{
  "[MatchingAttributesList](#cfn-customerprofiles-domain-consolidation-matchingattributeslist)" : {{[ [ , ... ], ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-domain-consolidation-syntax.yaml"></a>

```
  [MatchingAttributesList](#cfn-customerprofiles-domain-consolidation-matchingattributeslist): {{
    -
    - }}
```

## Properties
<a name="aws-properties-customerprofiles-domain-consolidation-properties"></a>

`MatchingAttributesList`  <a name="cfn-customerprofiles-domain-consolidation-matchingattributeslist"></a>
A list of matching criteria.
*Required*: Yes
*Type*: Array of Array
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
