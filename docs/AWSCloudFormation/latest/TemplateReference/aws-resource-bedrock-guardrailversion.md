---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-guardrailversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::GuardrailVersion
<a name="aws-resource-bedrock-guardrailversion"></a>

Creates a version of the guardrail. Use this API to create a snapshot of the guardrail when you are satisfied with a configuration, or to compare the configuration with another version.

## Syntax
<a name="aws-resource-bedrock-guardrailversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-guardrailversion-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::GuardrailVersion",
  "Properties" : {
      "[Description](#cfn-bedrock-guardrailversion-description)" : {{String}},
      "[GuardrailIdentifier](#cfn-bedrock-guardrailversion-guardrailidentifier)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-guardrailversion-syntax.yaml"></a>

```
Type: AWS::Bedrock::GuardrailVersion
Properties:
  [Description](#cfn-bedrock-guardrailversion-description): {{String}}
  [GuardrailIdentifier](#cfn-bedrock-guardrailversion-guardrailidentifier): {{String}}
```

## Properties
<a name="aws-resource-bedrock-guardrailversion-properties"></a>

`Description`  <a name="cfn-bedrock-guardrailversion-description"></a>
A description of the guardrail version.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GuardrailIdentifier`  <a name="cfn-bedrock-guardrailversion-guardrailidentifier"></a>
The unique identifier of the guardrail. This can be an ID or the ARN.
*Required*: Yes
*Type*: String
*Pattern*: `^(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-bedrock-guardrailversion-return-values"></a>

### Ref
<a name="aws-resource-bedrock-guardrailversion-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the guardrail ID and version, separated by a pipe (`|`) in the format (`guardrail-id|guardrail-version`).

For example, `{ "Ref": "myGuardrailVersion" }` would return the value `"3mzzryddufkp|2"`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrock-guardrailversion-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrock-guardrailversion-return-values-fn--getatt-fn--getatt"></a>

`GuardrailArn`  <a name="GuardrailArn-fn::getatt"></a>
The ARN of the guardrail.

`GuardrailId`  <a name="GuardrailId-fn::getatt"></a>
The unique identifier of the guardrail.

`Version`  <a name="Version-fn::getatt"></a>
The version of the guardrail.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
