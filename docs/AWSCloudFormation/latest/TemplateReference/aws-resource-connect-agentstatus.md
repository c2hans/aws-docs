---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-agentstatus.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::AgentStatus
<a name="aws-resource-connect-agentstatus"></a>

Contains information about an agent status.

## Syntax
<a name="aws-resource-connect-agentstatus-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-agentstatus-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::AgentStatus",
  "Properties" : {
      "[Description](#cfn-connect-agentstatus-description)" : {{String}},
      "[DisplayOrder](#cfn-connect-agentstatus-displayorder)" : {{Integer}},
      "[InstanceArn](#cfn-connect-agentstatus-instancearn)" : {{String}},
      "[Name](#cfn-connect-agentstatus-name)" : {{String}},
      "[ResetOrderNumber](#cfn-connect-agentstatus-resetordernumber)" : {{Boolean}},
      "[State](#cfn-connect-agentstatus-state)" : {{String}},
      "[Tags](#cfn-connect-agentstatus-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-connect-agentstatus-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-agentstatus-syntax.yaml"></a>

```
Type: AWS::Connect::AgentStatus
Properties:
  [Description](#cfn-connect-agentstatus-description): {{String}}
  [DisplayOrder](#cfn-connect-agentstatus-displayorder): {{Integer}}
  [InstanceArn](#cfn-connect-agentstatus-instancearn): {{String}}
  [Name](#cfn-connect-agentstatus-name): {{String}}
  [ResetOrderNumber](#cfn-connect-agentstatus-resetordernumber): {{Boolean}}
  [State](#cfn-connect-agentstatus-state): {{String}}
  [Tags](#cfn-connect-agentstatus-tags): {{
    - Tag}}
  [Type](#cfn-connect-agentstatus-type): {{String}}
```

## Properties
<a name="aws-resource-connect-agentstatus-properties"></a>

`Description`  <a name="cfn-connect-agentstatus-description"></a>
The description of the agent status.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayOrder`  <a name="cfn-connect-agentstatus-displayorder"></a>
The display order of the agent status.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-agentstatus-instancearn"></a>
The Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connect-agentstatus-name"></a>
The name of the agent status.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResetOrderNumber`  <a name="cfn-connect-agentstatus-resetordernumber"></a>
A number indicating the reset order of the agent status.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-connect-agentstatus-state"></a>
The state of the agent status.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-connect-agentstatus-tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-agentstatus-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-connect-agentstatus-type"></a>
The type of agent status.
*Required*: No
*Type*: String
*Allowed values*: `ROUTABLE | CUSTOM | OFFLINE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-agentstatus-return-values"></a>

### Ref
<a name="aws-resource-connect-agentstatus-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the agent status. For example:

 `{ "Ref": "myAgentStatus" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-agentstatus-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-agentstatus-return-values-fn--getatt-fn--getatt"></a>

`AgentStatusArn`  <a name="AgentStatusArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the agent status.

`LastModifiedRegion`  <a name="LastModifiedRegion-fn::getatt"></a>
The AWS Region where this resource was last modified.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The timestamp when this resource was last modified.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
