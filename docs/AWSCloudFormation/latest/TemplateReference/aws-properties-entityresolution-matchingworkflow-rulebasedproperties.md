---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-matchingworkflow-rulebasedproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::MatchingWorkflow RuleBasedProperties
<a name="aws-properties-entityresolution-matchingworkflow-rulebasedproperties"></a>

An object which defines the list of matching rules to run in a matching workflow.

## Syntax
<a name="aws-properties-entityresolution-matchingworkflow-rulebasedproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-matchingworkflow-rulebasedproperties-syntax.json"></a>

```
{
  "[AttributeMatchingModel](#cfn-entityresolution-matchingworkflow-rulebasedproperties-attributematchingmodel)" : {{String}},
  "[MatchPurpose](#cfn-entityresolution-matchingworkflow-rulebasedproperties-matchpurpose)" : {{String}},
  "[Rules](#cfn-entityresolution-matchingworkflow-rulebasedproperties-rules)" : {{[ Rule, ... ]}}
}
```

### YAML
<a name="aws-properties-entityresolution-matchingworkflow-rulebasedproperties-syntax.yaml"></a>

```
  [AttributeMatchingModel](#cfn-entityresolution-matchingworkflow-rulebasedproperties-attributematchingmodel): {{String}}
  [MatchPurpose](#cfn-entityresolution-matchingworkflow-rulebasedproperties-matchpurpose): {{String}}
  [Rules](#cfn-entityresolution-matchingworkflow-rulebasedproperties-rules): {{
    - Rule}}
```

## Properties
<a name="aws-properties-entityresolution-matchingworkflow-rulebasedproperties-properties"></a>

`AttributeMatchingModel`  <a name="cfn-entityresolution-matchingworkflow-rulebasedproperties-attributematchingmodel"></a>
The comparison type. You can choose `ONE_TO_ONE` or `MANY_TO_MANY` as the `attributeMatchingModel`.
If you choose `ONE_TO_ONE`, the system can only match attributes if the sub-types are an exact match. For example, for the `Email` attribute type, the system will only consider it a match if the value of the `Email` field of Profile A matches the value of the `Email` field of Profile B.
If you choose `MANY_TO_MANY`, the system can match attributes across the sub-types of an attribute type. For example, if the value of the `Email` field of Profile A and the value of `BusinessEmail` field of Profile B matches, the two profiles are matched on the `Email` attribute type.
*Required*: Yes
*Type*: String
*Allowed values*: `ONE_TO_ONE | MANY_TO_MANY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchPurpose`  <a name="cfn-entityresolution-matchingworkflow-rulebasedproperties-matchpurpose"></a>
 An indicator of whether to generate IDs and index the data or not.
If you choose `IDENTIFIER_GENERATION`, the process generates IDs and indexes the data.
If you choose `INDEXING`, the process indexes the data without generating IDs.
*Required*: No
*Type*: String
*Allowed values*: `IDENTIFIER_GENERATION | INDEXING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rules`  <a name="cfn-entityresolution-matchingworkflow-rulebasedproperties-rules"></a>
A list of `Rule` objects, each of which have fields `RuleName` and `MatchingKeys`.
*Required*: Yes
*Type*: Array of [Rule](aws-properties-entityresolution-matchingworkflow-rule.md)
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
