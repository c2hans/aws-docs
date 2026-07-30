---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-domain-rulebasedmatching.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Domain RuleBasedMatching
<a name="aws-properties-customerprofiles-domain-rulebasedmatching"></a>

The process of matching duplicate profiles using Rule-Based matching. If `RuleBasedMatching = true`, Connect Customer Customer Profiles will start to match and merge your profiles according to your configuration in the `RuleBasedMatchingRequest`. You can use the `ListRuleBasedMatches` and `GetSimilarProfiles` API to return and review the results. Also, if you have configured `ExportingConfig` in the `RuleBasedMatchingRequest`, you can download the results from S3.

## Syntax
<a name="aws-properties-customerprofiles-domain-rulebasedmatching-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-domain-rulebasedmatching-syntax.json"></a>

```
{
  "[AttributeTypesSelector](#cfn-customerprofiles-domain-rulebasedmatching-attributetypesselector)" : {{AttributeTypesSelector}},
  "[ConflictResolution](#cfn-customerprofiles-domain-rulebasedmatching-conflictresolution)" : {{ConflictResolution}},
  "[Enabled](#cfn-customerprofiles-domain-rulebasedmatching-enabled)" : {{Boolean}},
  "[ExportingConfig](#cfn-customerprofiles-domain-rulebasedmatching-exportingconfig)" : {{ExportingConfig}},
  "[MatchingRules](#cfn-customerprofiles-domain-rulebasedmatching-matchingrules)" : {{[ MatchingRule, ... ]}},
  "[MaxAllowedRuleLevelForMatching](#cfn-customerprofiles-domain-rulebasedmatching-maxallowedrulelevelformatching)" : {{Integer}},
  "[MaxAllowedRuleLevelForMerging](#cfn-customerprofiles-domain-rulebasedmatching-maxallowedrulelevelformerging)" : {{Integer}},
  "[Status](#cfn-customerprofiles-domain-rulebasedmatching-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-domain-rulebasedmatching-syntax.yaml"></a>

```
  [AttributeTypesSelector](#cfn-customerprofiles-domain-rulebasedmatching-attributetypesselector): {{
    AttributeTypesSelector}}
  [ConflictResolution](#cfn-customerprofiles-domain-rulebasedmatching-conflictresolution): {{
    ConflictResolution}}
  [Enabled](#cfn-customerprofiles-domain-rulebasedmatching-enabled): {{Boolean}}
  [ExportingConfig](#cfn-customerprofiles-domain-rulebasedmatching-exportingconfig): {{
    ExportingConfig}}
  [MatchingRules](#cfn-customerprofiles-domain-rulebasedmatching-matchingrules): {{
    - MatchingRule}}
  [MaxAllowedRuleLevelForMatching](#cfn-customerprofiles-domain-rulebasedmatching-maxallowedrulelevelformatching): {{Integer}}
  [MaxAllowedRuleLevelForMerging](#cfn-customerprofiles-domain-rulebasedmatching-maxallowedrulelevelformerging): {{Integer}}
  [Status](#cfn-customerprofiles-domain-rulebasedmatching-status): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-domain-rulebasedmatching-properties"></a>

`AttributeTypesSelector`  <a name="cfn-customerprofiles-domain-rulebasedmatching-attributetypesselector"></a>
Configures information about the `AttributeTypesSelector` where the rule-based identity resolution uses to match profiles.
*Required*: No
*Type*: [AttributeTypesSelector](aws-properties-customerprofiles-domain-attributetypesselector.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConflictResolution`  <a name="cfn-customerprofiles-domain-rulebasedmatching-conflictresolution"></a>
Determines how the auto-merging process should resolve conflicts between different profiles. For example, if Profile A and Profile B have the same `FirstName` and `LastName`, `ConflictResolution` specifies which `EmailAddress` should be used.
*Required*: No
*Type*: [ConflictResolution](aws-properties-customerprofiles-domain-conflictresolution.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-customerprofiles-domain-rulebasedmatching-enabled"></a>
The flag that enables the matching process of duplicate profiles.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportingConfig`  <a name="cfn-customerprofiles-domain-rulebasedmatching-exportingconfig"></a>
The S3 location where Identity Resolution Jobs write result files.
*Required*: No
*Type*: [ExportingConfig](aws-properties-customerprofiles-domain-exportingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchingRules`  <a name="cfn-customerprofiles-domain-rulebasedmatching-matchingrules"></a>
Configures how the rule-based matching process should match profiles. You can have up to 15 `MatchingRule` in the `MatchingRules`.
*Required*: No
*Type*: Array of [MatchingRule](aws-properties-customerprofiles-domain-matchingrule.md)
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxAllowedRuleLevelForMatching`  <a name="cfn-customerprofiles-domain-rulebasedmatching-maxallowedrulelevelformatching"></a>
Indicates the maximum allowed rule level for matching.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxAllowedRuleLevelForMerging`  <a name="cfn-customerprofiles-domain-rulebasedmatching-maxallowedrulelevelformerging"></a>
Indicates the maximum allowed rule level for merging.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-customerprofiles-domain-rulebasedmatching-status"></a>
The status of rule-based matching rule.
*Required*: No
*Type*: String
*Allowed values*: `PENDING | IN_PROGRESS | ACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
