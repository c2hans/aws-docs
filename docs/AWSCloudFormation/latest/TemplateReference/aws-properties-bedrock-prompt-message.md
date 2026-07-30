---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-prompt-message.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Prompt Message
<a name="aws-properties-bedrock-prompt-message"></a>

A message input, or returned from, a call to [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html).

## Syntax
<a name="aws-properties-bedrock-prompt-message-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-prompt-message-syntax.json"></a>

```
{
  "[Content](#cfn-bedrock-prompt-message-content)" : {{[ ContentBlock, ... ]}},
  "[Role](#cfn-bedrock-prompt-message-role)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-prompt-message-syntax.yaml"></a>

```
  [Content](#cfn-bedrock-prompt-message-content): {{
    - ContentBlock}}
  [Role](#cfn-bedrock-prompt-message-role): {{String}}
```

## Properties
<a name="aws-properties-bedrock-prompt-message-properties"></a>

`Content`  <a name="cfn-bedrock-prompt-message-content"></a>
The message content. Note the following restrictions:
+ You can include up to 20 images. Each image's size, height, and width must be no more than 3.75 MB, 8000 px, and 8000 px, respectively.
+ You can include up to five documents. Each document's size must be no more than 4.5 MB.
+ If you include a `ContentBlock` with a `document` field in the array, you must also include a `ContentBlock` with a `text` field.
+ You can only include images and documents if the `role` is `user`.
*Required*: Yes
*Type*: Array of [ContentBlock](aws-properties-bedrock-prompt-contentblock.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Role`  <a name="cfn-bedrock-prompt-message-role"></a>
The role that the message plays in the message.
*Required*: Yes
*Type*: String
*Allowed values*: `user | assistant`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
