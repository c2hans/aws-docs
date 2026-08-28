---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-enforcedguardrailconfiguration-modelenforcement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::EnforcedGuardrailConfiguration ModelEnforcement
<a name="aws-properties-bedrock-enforcedguardrailconfiguration-modelenforcement"></a>

Model-specific information for the enforced guardrail configuration.

## Syntax
<a name="aws-properties-bedrock-enforcedguardrailconfiguration-modelenforcement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-enforcedguardrailconfiguration-modelenforcement-syntax.json"></a>

```
{
  "[ExcludedModels](#cfn-bedrock-enforcedguardrailconfiguration-modelenforcement-excludedmodels)" : {{[ String, ... ]}},
  "[IncludedModels](#cfn-bedrock-enforcedguardrailconfiguration-modelenforcement-includedmodels)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-enforcedguardrailconfiguration-modelenforcement-syntax.yaml"></a>

```
  [ExcludedModels](#cfn-bedrock-enforcedguardrailconfiguration-modelenforcement-excludedmodels): {{
    - String}}
  [IncludedModels](#cfn-bedrock-enforcedguardrailconfiguration-modelenforcement-includedmodels): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrock-enforcedguardrailconfiguration-modelenforcement-properties"></a>

`ExcludedModels`  <a name="cfn-bedrock-enforcedguardrailconfiguration-modelenforcement-excludedmodels"></a>
Models to exclude from enforcement of the guardrail.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludedModels`  <a name="cfn-bedrock-enforcedguardrailconfiguration-modelenforcement-includedmodels"></a>
Models to enforce the guardrail on.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
