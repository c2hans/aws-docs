---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessskill.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessSkill
<a name="aws-properties-bedrockagentcore-harness-harnessskill"></a>

A skill available to the agent.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessskill-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessskill-syntax.json"></a>

```
{
  "[AwsSkills](#cfn-bedrockagentcore-harness-harnessskill-awsskills)" : {{HarnessSkillAwsSkillsSource}},
  "[Git](#cfn-bedrockagentcore-harness-harnessskill-git)" : {{HarnessSkillGitSource}},
  "[Path](#cfn-bedrockagentcore-harness-harnessskill-path)" : {{String}},
  "[S3](#cfn-bedrockagentcore-harness-harnessskill-s3)" : {{HarnessSkillS3Source}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessskill-syntax.yaml"></a>

```
  [AwsSkills](#cfn-bedrockagentcore-harness-harnessskill-awsskills): {{
    HarnessSkillAwsSkillsSource}}
  [Git](#cfn-bedrockagentcore-harness-harnessskill-git): {{
    HarnessSkillGitSource}}
  [Path](#cfn-bedrockagentcore-harness-harnessskill-path): {{String}}
  [S3](#cfn-bedrockagentcore-harness-harnessskill-s3): {{
    HarnessSkillS3Source}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessskill-properties"></a>

`AwsSkills`  <a name="cfn-bedrockagentcore-harness-harnessskill-awsskills"></a>
AWS Skills baked into the harness's underlying Runtime.
*Required*: No
*Type*: [HarnessSkillAwsSkillsSource](aws-properties-bedrockagentcore-harness-harnessskillawsskillssource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Git`  <a name="cfn-bedrockagentcore-harness-harnessskill-git"></a>
A git repository containing the skill.
*Required*: No
*Type*: [HarnessSkillGitSource](aws-properties-bedrockagentcore-harness-harnessskillgitsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-bedrockagentcore-harness-harnessskill-path"></a>
The filesystem path to the skill definition.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3`  <a name="cfn-bedrockagentcore-harness-harnessskill-s3"></a>
An S3 source containing the skill.
*Required*: No
*Type*: [HarnessSkillS3Source](aws-properties-bedrockagentcore-harness-harnessskills3source.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
