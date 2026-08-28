---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-promptversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::PromptVersion
<a name="aws-resource-bedrock-promptversion"></a>

Creates a static snapshot of your prompt that can be deployed to production. For more information, see [Deploy prompts using Prompt management by creating versions](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-resource-bedrock-promptversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-promptversion-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::PromptVersion",
  "Properties" : {
      "[Description](#cfn-bedrock-promptversion-description)" : {{String}},
      "[PromptArn](#cfn-bedrock-promptversion-promptarn)" : {{String}},
      "[Tags](#cfn-bedrock-promptversion-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-promptversion-syntax.yaml"></a>

```
Type: AWS::Bedrock::PromptVersion
Properties:
  [Description](#cfn-bedrock-promptversion-description): {{String}}
  [PromptArn](#cfn-bedrock-promptversion-promptarn): {{String}}
  [Tags](#cfn-bedrock-promptversion-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-bedrock-promptversion-properties"></a>

`Description`  <a name="cfn-bedrock-promptversion-description"></a>
The description of the prompt version.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PromptArn`  <a name="cfn-bedrock-promptversion-promptarn"></a>
The Amazon Resource Name (ARN) of the version of the prompt.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10})$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrock-promptversion-tags"></a>
A map of tags attached to the prompt version and their values.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-bedrock-promptversion-return-values"></a>

### Ref
<a name="aws-resource-bedrock-promptversion-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Number (ARN) of the prompt version.

For example, `{ "Ref": "myPromptVersion" }` could return the value `""arn:aws:bedrock:us-east-1:123456789012:prompt/PROMPT12345:1"`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrock-promptversion-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrock-promptversion-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the prompt or the prompt version (if you specified a version in the request).

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time at which the prompt was created.

`CustomerEncryptionKeyArn`  <a name="CustomerEncryptionKeyArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the KMS key that the prompt version is encrypted with.

`DefaultVariant`  <a name="DefaultVariant-fn::getatt"></a>
The name of the default variant for the prompt. This value must match the `name` field in the relevant [PromptVariant](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html) object.

`Name`  <a name="Name-fn::getatt"></a>
The name of the prompt.

`PromptId`  <a name="PromptId-fn::getatt"></a>
The unique identifier of the prompt.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time at which the prompt was last updated.

`Variants`  <a name="Variants-fn::getatt"></a>
A list of objects, each containing details about a variant of the prompt.

`Version`  <a name="Version-fn::getatt"></a>
The version of the prompt that this summary applies to.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
