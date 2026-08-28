---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-onlineevaluationconfig-sessionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OnlineEvaluationConfig SessionConfig
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-sessionconfig"></a>

 The session configuration that defines timeout settings for detecting when agent sessions are complete and ready for evaluation.

## Syntax
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-sessionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-sessionconfig-syntax.json"></a>

```
{
  "[SessionTimeoutMinutes](#cfn-bedrockagentcore-onlineevaluationconfig-sessionconfig-sessiontimeoutminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-sessionconfig-syntax.yaml"></a>

```
  [SessionTimeoutMinutes](#cfn-bedrockagentcore-onlineevaluationconfig-sessionconfig-sessiontimeoutminutes): {{Integer}}
```

## Properties
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-sessionconfig-properties"></a>

`SessionTimeoutMinutes`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-sessionconfig-sessiontimeoutminutes"></a>
 The number of minutes of inactivity after which an agent session is considered complete and ready for evaluation.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1440`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
