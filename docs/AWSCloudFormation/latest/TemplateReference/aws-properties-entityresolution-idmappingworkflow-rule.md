---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-idmappingworkflow-rule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::IdMappingWorkflow Rule
<a name="aws-properties-entityresolution-idmappingworkflow-rule"></a>

An object containing the `ruleName` and `matchingKeys`.

## Syntax
<a name="aws-properties-entityresolution-idmappingworkflow-rule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-idmappingworkflow-rule-syntax.json"></a>

```
{
  "[MatchingKeys](#cfn-entityresolution-idmappingworkflow-rule-matchingkeys)" : {{[ String, ... ]}},
  "[RuleName](#cfn-entityresolution-idmappingworkflow-rule-rulename)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-idmappingworkflow-rule-syntax.yaml"></a>

```
  [MatchingKeys](#cfn-entityresolution-idmappingworkflow-rule-matchingkeys): {{
    - String}}
  [RuleName](#cfn-entityresolution-idmappingworkflow-rule-rulename): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-idmappingworkflow-rule-properties"></a>

`MatchingKeys`  <a name="cfn-entityresolution-idmappingworkflow-rule-matchingkeys"></a>
A list of `MatchingKeys`. The `MatchingKeys` must have been defined in the `SchemaMapping`. Two records are considered to match according to this rule if all of the `MatchingKeys` match.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleName`  <a name="cfn-entityresolution-idmappingworkflow-rule-rulename"></a>
A name for the matching rule.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z_0-9- \t]*$`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
