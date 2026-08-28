---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-parsingprompt.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase ParsingPrompt
<a name="aws-properties-wisdom-knowledgebase-parsingprompt"></a>

Instructions for interpreting the contents of a document.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-parsingprompt-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-parsingprompt-syntax.json"></a>

```
{
  "[ParsingPromptText](#cfn-wisdom-knowledgebase-parsingprompt-parsingprompttext)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-parsingprompt-syntax.yaml"></a>

```
  [ParsingPromptText](#cfn-wisdom-knowledgebase-parsingprompt-parsingprompttext): {{String}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-parsingprompt-properties"></a>

`ParsingPromptText`  <a name="cfn-wisdom-knowledgebase-parsingprompt-parsingprompttext"></a>
Instructions for interpreting the contents of a document.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
