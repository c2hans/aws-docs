---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registry-claimmatchvaluetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Registry ClaimMatchValueType
<a name="aws-properties-agentregistry-registry-claimmatchvaluetype"></a>

The expected value used to match a claim. Specify exactly one member.

## Syntax
<a name="aws-properties-agentregistry-registry-claimmatchvaluetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registry-claimmatchvaluetype-syntax.json"></a>

```
{
  "[MatchValueString](#cfn-agentregistry-registry-claimmatchvaluetype-matchvaluestring)" : {{String}},
  "[MatchValueStringList](#cfn-agentregistry-registry-claimmatchvaluetype-matchvaluestringlist)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-agentregistry-registry-claimmatchvaluetype-syntax.yaml"></a>

```
  [MatchValueString](#cfn-agentregistry-registry-claimmatchvaluetype-matchvaluestring): {{
    String}}
  [MatchValueStringList](#cfn-agentregistry-registry-claimmatchvaluetype-matchvaluestringlist): {{
    - String}}
```

## Properties
<a name="aws-properties-agentregistry-registry-claimmatchvaluetype-properties"></a>

`MatchValueString`  <a name="cfn-agentregistry-registry-claimmatchvaluetype-matchvaluestring"></a>
A single string value to match the claim against.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_.:/-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchValueStringList`  <a name="cfn-agentregistry-registry-claimmatchvaluetype-matchvaluestringlist"></a>
A list of string values to match the claim against.
*Required*: No
*Type*: Array of String
*Maximum*: `255`
*Minimum*: `1 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
