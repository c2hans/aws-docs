---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-messagetemplate-agentattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplate AgentAttributes
<a name="aws-properties-wisdom-messagetemplate-agentattributes"></a>

Information about an agent.

## Syntax
<a name="aws-properties-wisdom-messagetemplate-agentattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-messagetemplate-agentattributes-syntax.json"></a>

```
{
  "[FirstName](#cfn-wisdom-messagetemplate-agentattributes-firstname)" : {{String}},
  "[LastName](#cfn-wisdom-messagetemplate-agentattributes-lastname)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-messagetemplate-agentattributes-syntax.yaml"></a>

```
  [FirstName](#cfn-wisdom-messagetemplate-agentattributes-firstname): {{String}}
  [LastName](#cfn-wisdom-messagetemplate-agentattributes-lastname): {{String}}
```

## Properties
<a name="aws-properties-wisdom-messagetemplate-agentattributes-properties"></a>

`FirstName`  <a name="cfn-wisdom-messagetemplate-agentattributes-firstname"></a>
The agent’s first name as entered in their Amazon Connect user account.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastName`  <a name="cfn-wisdom-messagetemplate-agentattributes-lastname"></a>
The agent’s last name as entered in their Amazon Connect user account.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
