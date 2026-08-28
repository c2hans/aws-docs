---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessskills3source.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessSkillS3Source
<a name="aws-properties-bedrockagentcore-harness-harnessskills3source"></a>

An S3 source for a skill.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessskills3source-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessskills3source-syntax.json"></a>

```
{
  "[Uri](#cfn-bedrockagentcore-harness-harnessskills3source-uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessskills3source-syntax.yaml"></a>

```
  [Uri](#cfn-bedrockagentcore-harness-harnessskills3source-uri): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessskills3source-properties"></a>

`Uri`  <a name="cfn-bedrockagentcore-harness-harnessskills3source-uri"></a>
The S3 URI pointing to the skill directory (e.g., s3://bucket/skills/my-skill/).
*Required*: Yes
*Type*: String
*Pattern*: `^s3://`
*Minimum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
