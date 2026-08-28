---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-prompt.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Prompt
<a name="aws-resource-connect-prompt"></a>

Creates a prompt for the specified Connect Customer instance.

## Syntax
<a name="aws-resource-connect-prompt-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-prompt-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::Prompt",
  "Properties" : {
      "[Description](#cfn-connect-prompt-description)" : {{String}},
      "[InstanceArn](#cfn-connect-prompt-instancearn)" : {{String}},
      "[Name](#cfn-connect-prompt-name)" : {{String}},
      "[S3Uri](#cfn-connect-prompt-s3uri)" : {{String}},
      "[Tags](#cfn-connect-prompt-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-connect-prompt-syntax.yaml"></a>

```
Type: AWS::Connect::Prompt
Properties:
  [Description](#cfn-connect-prompt-description): {{String}}
  [InstanceArn](#cfn-connect-prompt-instancearn): {{String}}
  [Name](#cfn-connect-prompt-name): {{String}}
  [S3Uri](#cfn-connect-prompt-s3uri): {{String}}
  [Tags](#cfn-connect-prompt-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-connect-prompt-properties"></a>

`Description`  <a name="cfn-connect-prompt-description"></a>
The description of the prompt.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-prompt-instancearn"></a>
The identifier of the Connect Customer instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connect-prompt-name"></a>
The name of the prompt.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Uri`  <a name="cfn-connect-prompt-s3uri"></a>
The URI for the S3 bucket where the prompt is stored. This property is required when you create a prompt.
*Required*: Conditional
*Type*: String
*Pattern*: `s3://\S+/.+|https://\S+\.s3(\.\S+)?\.amazonaws\.com/\S+`
*Minimum*: `1`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-connect-prompt-tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-prompt-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-prompt-return-values"></a>

### Ref
<a name="aws-resource-connect-prompt-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the quick rule name. For example:

 `{ "Ref": "myPromptName" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-prompt-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-prompt-return-values-fn--getatt-fn--getatt"></a>

`PromptArn`  <a name="PromptArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the prompt.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
