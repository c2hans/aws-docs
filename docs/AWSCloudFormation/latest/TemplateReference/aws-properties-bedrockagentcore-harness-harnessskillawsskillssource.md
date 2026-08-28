---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessskillawsskillssource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessSkillAwsSkillsSource
<a name="aws-properties-bedrockagentcore-harness-harnessskillawsskillssource"></a>

Passed to show that AWS Skills should be included.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessskillawsskillssource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessskillawsskillssource-syntax.json"></a>

```
{
  "[Paths](#cfn-bedrockagentcore-harness-harnessskillawsskillssource-paths)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessskillawsskillssource-syntax.yaml"></a>

```
  [Paths](#cfn-bedrockagentcore-harness-harnessskillawsskillssource-paths): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessskillawsskillssource-properties"></a>

`Paths`  <a name="cfn-bedrockagentcore-harness-harnessskillawsskillssource-paths"></a>
Optionally filter allowed skills with glob syntax, e.g., ['core-skills/\*'].
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
