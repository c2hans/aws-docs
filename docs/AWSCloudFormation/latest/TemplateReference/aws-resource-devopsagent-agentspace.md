---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-devopsagent-agentspace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::AgentSpace
<a name="aws-resource-devopsagent-agentspace"></a>

The `AWS::DevOpsAgent::AgentSpace` resource specifies an Agent Space for the AWS DevOps Agent Service.

## Syntax
<a name="aws-resource-devopsagent-agentspace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-devopsagent-agentspace-syntax.json"></a>

```
{
  "Type" : "AWS::DevOpsAgent::AgentSpace",
  "Properties" : {
      "[Description](#cfn-devopsagent-agentspace-description)" : {{String}},
      "[KmsKeyArn](#cfn-devopsagent-agentspace-kmskeyarn)" : {{String}},
      "[Locale](#cfn-devopsagent-agentspace-locale)" : {{String}},
      "[Name](#cfn-devopsagent-agentspace-name)" : {{String}},
      "[OperatorApp](#cfn-devopsagent-agentspace-operatorapp)" : {{OperatorApp}},
      "[Tags](#cfn-devopsagent-agentspace-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-devopsagent-agentspace-syntax.yaml"></a>

```
Type: AWS::DevOpsAgent::AgentSpace
Properties:
  [Description](#cfn-devopsagent-agentspace-description): {{String}}
  [KmsKeyArn](#cfn-devopsagent-agentspace-kmskeyarn): {{String}}
  [Locale](#cfn-devopsagent-agentspace-locale): {{String}}
  [Name](#cfn-devopsagent-agentspace-name): {{String}}
  [OperatorApp](#cfn-devopsagent-agentspace-operatorapp): {{
    OperatorApp}}
  [Tags](#cfn-devopsagent-agentspace-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-devopsagent-agentspace-properties"></a>

`Description`  <a name="cfn-devopsagent-agentspace-description"></a>
The description of the Agent Space.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-devopsagent-agentspace-kmskeyarn"></a>
The ARN of the customer managed key used to encrypt the data of the Agent Space at rest.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: Updates are not supported.

`Locale`  <a name="cfn-devopsagent-agentspace-locale"></a>
The locale of the Agent Space, which determines the language used in agent responses.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z]{2,3}(-[a-zA-Z0-9]{2,8})*$`
*Minimum*: `2`
*Maximum*: `35`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-devopsagent-agentspace-name"></a>
The name of the Agent Space.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OperatorApp`  <a name="cfn-devopsagent-agentspace-operatorapp"></a>
Configuration for the connection to the DevOps Agent web app.
*Required*: No
*Type*: [OperatorApp](aws-properties-devopsagent-agentspace-operatorapp.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-devopsagent-agentspace-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-devopsagent-agentspace-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-devopsagent-agentspace-return-values"></a>

### Ref
<a name="aws-resource-devopsagent-agentspace-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the AgentSpaceId.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-devopsagent-agentspace-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-devopsagent-agentspace-return-values-fn--getatt-fn--getatt"></a>

`AgentSpaceId`  <a name="AgentSpaceId-fn::getatt"></a>
The unique identifier of the Agent Space.

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Agent Space.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the resource was created.

`OperatorApp.Iam.CreatedAt`  <a name="OperatorApp.Iam.CreatedAt-fn::getatt"></a>
The timestamp when the IAM authentication configuration was created.

`OperatorApp.Iam.UpdatedAt`  <a name="OperatorApp.Iam.UpdatedAt-fn::getatt"></a>
The timestamp when the IAM authentication configuration was last updated.

`OperatorApp.Idc.CreatedAt`  <a name="OperatorApp.Idc.CreatedAt-fn::getatt"></a>
The timestamp when the IAM Identity Center authentication configuration was created.

`OperatorApp.Idc.IdcApplicationArn`  <a name="OperatorApp.Idc.IdcApplicationArn-fn::getatt"></a>
The ARN of the IAM Identity Center application created for the DevOps Agent web app.

`OperatorApp.Idc.UpdatedAt`  <a name="OperatorApp.Idc.UpdatedAt-fn::getatt"></a>
The timestamp when the IAM Identity Center authentication configuration was last updated.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the resource was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
