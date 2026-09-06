---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessskillgitsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessSkillGitSource
<a name="aws-properties-bedrockagentcore-harness-harnessskillgitsource"></a>

A git repository source for a skill.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessskillgitsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessskillgitsource-syntax.json"></a>

```
{
  "[Auth](#cfn-bedrockagentcore-harness-harnessskillgitsource-auth)" : {{HarnessSkillGitAuth}},
  "[Path](#cfn-bedrockagentcore-harness-harnessskillgitsource-path)" : {{String}},
  "[Url](#cfn-bedrockagentcore-harness-harnessskillgitsource-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessskillgitsource-syntax.yaml"></a>

```
  [Auth](#cfn-bedrockagentcore-harness-harnessskillgitsource-auth): {{
    HarnessSkillGitAuth}}
  [Path](#cfn-bedrockagentcore-harness-harnessskillgitsource-path): {{String}}
  [Url](#cfn-bedrockagentcore-harness-harnessskillgitsource-url): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessskillgitsource-properties"></a>

`Auth`  <a name="cfn-bedrockagentcore-harness-harnessskillgitsource-auth"></a>
Authentication configuration for private repositories.
*Required*: No
*Type*: [HarnessSkillGitAuth](aws-properties-bedrockagentcore-harness-harnessskillgitauth.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-bedrockagentcore-harness-harnessskillgitsource-path"></a>
Subdirectory within the repository containing the skill.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-bedrockagentcore-harness-harnessskillgitsource-url"></a>
The HTTPS URL of the git repository.
*Required*: Yes
*Type*: String
*Pattern*: `^https://`
*Minimum*: `8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
