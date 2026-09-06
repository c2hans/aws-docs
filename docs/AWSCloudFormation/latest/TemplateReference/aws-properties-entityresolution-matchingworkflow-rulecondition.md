---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-matchingworkflow-rulecondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::MatchingWorkflow RuleCondition
<a name="aws-properties-entityresolution-matchingworkflow-rulecondition"></a>

An object that defines the `ruleCondition` and the `ruleName` to use in a matching workflow.

## Syntax
<a name="aws-properties-entityresolution-matchingworkflow-rulecondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-matchingworkflow-rulecondition-syntax.json"></a>

```
{
  "[Condition](#cfn-entityresolution-matchingworkflow-rulecondition-condition)" : {{String}},
  "[RuleName](#cfn-entityresolution-matchingworkflow-rulecondition-rulename)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-matchingworkflow-rulecondition-syntax.yaml"></a>

```
  [Condition](#cfn-entityresolution-matchingworkflow-rulecondition-condition): {{String}}
  [RuleName](#cfn-entityresolution-matchingworkflow-rulecondition-rulename): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-matchingworkflow-rulecondition-properties"></a>

`Condition`  <a name="cfn-entityresolution-matchingworkflow-rulecondition-condition"></a>
A statement that specifies the conditions for a matching rule.
If your data is accurate, use an Exact matching function: `Exact` or `ExactManyToMany`.
If your data has variations in spelling or pronunciation, use a Fuzzy matching function: `Cosine`, `Levenshtein`, or `Soundex`.
Use operators if you want to combine (`AND`), separate (`OR`), or group matching functions `(...)`.
For example: `(Cosine(a, 10) AND Exact(b, true)) OR ExactManyToMany(c, d)`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleName`  <a name="cfn-entityresolution-matchingworkflow-rulecondition-rulename"></a>
A name for the matching rule.
For example: `Rule1`
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z_0-9- \t]*$`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
