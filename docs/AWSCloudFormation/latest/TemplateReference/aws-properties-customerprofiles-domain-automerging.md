---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-domain-automerging.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Domain AutoMerging
<a name="aws-properties-customerprofiles-domain-automerging"></a>

Configuration information about the auto-merging process.

## Syntax
<a name="aws-properties-customerprofiles-domain-automerging-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-domain-automerging-syntax.json"></a>

```
{
  "[ConflictResolution](#cfn-customerprofiles-domain-automerging-conflictresolution)" : {{ConflictResolution}},
  "[Consolidation](#cfn-customerprofiles-domain-automerging-consolidation)" : {{Consolidation}},
  "[Enabled](#cfn-customerprofiles-domain-automerging-enabled)" : {{Boolean}},
  "[MinAllowedConfidenceScoreForMerging](#cfn-customerprofiles-domain-automerging-minallowedconfidencescoreformerging)" : {{Number}}
}
```

### YAML
<a name="aws-properties-customerprofiles-domain-automerging-syntax.yaml"></a>

```
  [ConflictResolution](#cfn-customerprofiles-domain-automerging-conflictresolution): {{
    ConflictResolution}}
  [Consolidation](#cfn-customerprofiles-domain-automerging-consolidation): {{
    Consolidation}}
  [Enabled](#cfn-customerprofiles-domain-automerging-enabled): {{Boolean}}
  [MinAllowedConfidenceScoreForMerging](#cfn-customerprofiles-domain-automerging-minallowedconfidencescoreformerging): {{Number}}
```

## Properties
<a name="aws-properties-customerprofiles-domain-automerging-properties"></a>

`ConflictResolution`  <a name="cfn-customerprofiles-domain-automerging-conflictresolution"></a>
Determines how the auto-merging process should resolve conflicts between different profiles. For example, if Profile A and Profile B have the same `FirstName` and `LastName`, `ConflictResolution` specifies which `EmailAddress` should be used.
*Required*: No
*Type*: [ConflictResolution](aws-properties-customerprofiles-domain-conflictresolution.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Consolidation`  <a name="cfn-customerprofiles-domain-automerging-consolidation"></a>
A list of matching attributes that represent matching criteria. If two profiles meet at least one of the requirements in the matching attributes list, they will be merged.
*Required*: No
*Type*: [Consolidation](aws-properties-customerprofiles-domain-consolidation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-customerprofiles-domain-automerging-enabled"></a>
The flag that enables the auto-merging of duplicate profiles.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinAllowedConfidenceScoreForMerging`  <a name="cfn-customerprofiles-domain-automerging-minallowedconfidencescoreformerging"></a>
A number between 0 and 1 that represents the minimum confidence score required for profiles within a matching group to be merged during the auto-merge process. A higher score means that a higher similarity is required to merge profiles.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
