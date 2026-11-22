---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-parsingprompt.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase ParsingPrompt

Instructions for interpreting the contents of a document.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-parsingprompt-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-parsingprompt-syntax.json"></a>

```json
{
  "[ParsingPromptText](#cfn-wisdom-knowledgebase-parsingprompt-parsingprompttext)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-parsingprompt-syntax.yaml"></a>

```yaml
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
