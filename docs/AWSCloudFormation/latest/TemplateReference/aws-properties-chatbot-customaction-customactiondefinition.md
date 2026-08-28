---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-chatbot-customaction-customactiondefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Chatbot::CustomAction CustomActionDefinition
<a name="aws-properties-chatbot-customaction-customactiondefinition"></a>

**Note**
AWS Chatbot is now Amazon Q Developer. [Learn more](https://docs.aws.amazon.com/chatbot/latest/adminguide/service-rename.html)
`Type` attribute values remain unchanged.

The definition of the command to run when invoked as an alias or as an action button.

## Syntax
<a name="aws-properties-chatbot-customaction-customactiondefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-chatbot-customaction-customactiondefinition-syntax.json"></a>

```
{
  "[CommandText](#cfn-chatbot-customaction-customactiondefinition-commandtext)" : {{String}}
}
```

### YAML
<a name="aws-properties-chatbot-customaction-customactiondefinition-syntax.yaml"></a>

```
  [CommandText](#cfn-chatbot-customaction-customactiondefinition-commandtext): {{String}}
```

## Properties
<a name="aws-properties-chatbot-customaction-customactiondefinition-properties"></a>

`CommandText`  <a name="cfn-chatbot-customaction-customactiondefinition-commandtext"></a>
The command string to run which may include variables by prefixing with a dollar sign ($).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
