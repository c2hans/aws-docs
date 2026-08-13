---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-prompt.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Prompt
<a name="aws-resource-bedrock-prompt"></a>

Creates a prompt in your prompt library that you can add to a flow. For more information, see [Prompt management in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html), [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html) and [Prompt flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-resource-bedrock-prompt-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-prompt-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::Prompt",
  "Properties" : {
      "[CustomerEncryptionKeyArn](#cfn-bedrock-prompt-customerencryptionkeyarn)" : {{String}},
      "[DefaultVariant](#cfn-bedrock-prompt-defaultvariant)" : {{String}},
      "[Description](#cfn-bedrock-prompt-description)" : {{String}},
      "[Name](#cfn-bedrock-prompt-name)" : {{String}},
      "[Tags](#cfn-bedrock-prompt-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Variants](#cfn-bedrock-prompt-variants)" : {{[ PromptVariant, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-prompt-syntax.yaml"></a>

```
Type: AWS::Bedrock::Prompt
Properties:
  [CustomerEncryptionKeyArn](#cfn-bedrock-prompt-customerencryptionkeyarn): {{String}}
  [DefaultVariant](#cfn-bedrock-prompt-defaultvariant): {{String}}
  [Description](#cfn-bedrock-prompt-description): {{String}}
  [Name](#cfn-bedrock-prompt-name): {{String}}
  [Tags](#cfn-bedrock-prompt-tags): {{
    {{Key}}: {{Value}}}}
  [Variants](#cfn-bedrock-prompt-variants): {{
    - PromptVariant}}
```

## Properties
<a name="aws-resource-bedrock-prompt-properties"></a>

`CustomerEncryptionKeyArn`  <a name="cfn-bedrock-prompt-customerencryptionkeyarn"></a>
The Amazon Resource Name (ARN) of the KMS key that the prompt is encrypted with.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultVariant`  <a name="cfn-bedrock-prompt-defaultvariant"></a>
The name of the default variant for the prompt. This value must match the `name` field in the relevant [PromptVariant](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html) object.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrock-prompt-description"></a>
The description of the prompt.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-prompt-name"></a>
The name of the prompt.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrock-prompt-tags"></a>
Metadata that you can assign to a resource as key-value pairs. For more information, see the following resources:
+  [Tag naming limits and requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions)
+  [Tagging best practices](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices)
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Variants`  <a name="cfn-bedrock-prompt-variants"></a>
A list of objects, each containing details about a variant of the prompt.
*Required*: No
*Type*: Array of [PromptVariant](aws-properties-bedrock-prompt-promptvariant.md)
*Minimum*: `0`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrock-prompt-return-values"></a>

### Ref
<a name="aws-resource-bedrock-prompt-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Number (ARN) of the prompt.

For example, `{ "Ref": "myPrompt" }` could return the value `"arn:aws:bedrock:us-east-1:123456789012:prompt/PROMPT12345"`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrock-prompt-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrock-prompt-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the prompt or the prompt version (if you specified a version in the request).

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time at which the prompt was created.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the prompt.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time at which the prompt was last updated.

`Version`  <a name="Version-fn::getatt"></a>
The version of the prompt that this summary applies to.
