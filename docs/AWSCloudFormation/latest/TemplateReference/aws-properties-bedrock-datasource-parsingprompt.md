---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-parsingprompt.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource ParsingPrompt
<a name="aws-properties-bedrock-datasource-parsingprompt"></a>

Instructions for interpreting the contents of a document.

## Syntax
<a name="aws-properties-bedrock-datasource-parsingprompt-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-parsingprompt-syntax.json"></a>

```
{
  "[ParsingPromptText](#cfn-bedrock-datasource-parsingprompt-parsingprompttext)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-parsingprompt-syntax.yaml"></a>

```
  [ParsingPromptText](#cfn-bedrock-datasource-parsingprompt-parsingprompttext): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-parsingprompt-properties"></a>

`ParsingPromptText`  <a name="cfn-bedrock-datasource-parsingprompt-parsingprompttext"></a>
Instructions for interpreting the contents of a document.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
