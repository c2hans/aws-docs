---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-domain-conflictresolution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Domain ConflictResolution
<a name="aws-properties-customerprofiles-domain-conflictresolution"></a>

Determines how the auto-merging process should resolve conflicts between different profiles. For example, if Profile A and Profile B have the same `FirstName` and `LastName`, `ConflictResolution` specifies which `EmailAddress` should be used.

## Syntax
<a name="aws-properties-customerprofiles-domain-conflictresolution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-domain-conflictresolution-syntax.json"></a>

```
{
  "[ConflictResolvingModel](#cfn-customerprofiles-domain-conflictresolution-conflictresolvingmodel)" : {{String}},
  "[SourceName](#cfn-customerprofiles-domain-conflictresolution-sourcename)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-domain-conflictresolution-syntax.yaml"></a>

```
  [ConflictResolvingModel](#cfn-customerprofiles-domain-conflictresolution-conflictresolvingmodel): {{String}}
  [SourceName](#cfn-customerprofiles-domain-conflictresolution-sourcename): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-domain-conflictresolution-properties"></a>

`ConflictResolvingModel`  <a name="cfn-customerprofiles-domain-conflictresolution-conflictresolvingmodel"></a>
How the auto-merging process should resolve conflicts between different profiles.
*Required*: Yes
*Type*: String
*Allowed values*: `RECENCY | SOURCE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceName`  <a name="cfn-customerprofiles-domain-conflictresolution-sourcename"></a>
The `ObjectType` name that is used to resolve profile merging conflicts when choosing `SOURCE` as the `ConflictResolvingModel`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
