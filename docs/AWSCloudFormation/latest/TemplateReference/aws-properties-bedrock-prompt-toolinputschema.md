---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-prompt-toolinputschema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Prompt ToolInputSchema
<a name="aws-properties-bedrock-prompt-toolinputschema"></a>

The schema for the tool. The top level schema type must be `object`. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-prompt-toolinputschema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-prompt-toolinputschema-syntax.json"></a>

```
{
  "[Json](#cfn-bedrock-prompt-toolinputschema-json)" : {{Json}}
}
```

### YAML
<a name="aws-properties-bedrock-prompt-toolinputschema-syntax.yaml"></a>

```
  [Json](#cfn-bedrock-prompt-toolinputschema-json): {{
    Json}}
```

## Properties
<a name="aws-properties-bedrock-prompt-toolinputschema-properties"></a>

`Json`  <a name="cfn-bedrock-prompt-toolinputschema-json"></a>
The JSON schema for the tool. For more information, see [JSON Schema Reference](https://json-schema.org/understanding-json-schema/reference).
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
