---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityagent-agentspace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::AgentSpace
<a name="aws-resource-securityagent-agentspace"></a>

The `AWS::SecurityAgent::AgentSpace` resource specifies an agent space for security testing. An agent space defines the scope of resources, integrations, and settings available to security testing operations.

## Syntax
<a name="aws-resource-securityagent-agentspace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityagent-agentspace-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityAgent::AgentSpace",
  "Properties" : {
      "[AwsResources](#cfn-securityagent-agentspace-awsresources)" : {{AWSResources}},
      "[CodeReviewSettings](#cfn-securityagent-agentspace-codereviewsettings)" : {{CodeReviewSettings}},
      "[Description](#cfn-securityagent-agentspace-description)" : {{String}},
      "[IntegratedResources](#cfn-securityagent-agentspace-integratedresources)" : {{[ IntegratedResource, ... ]}},
      "[KmsKeyId](#cfn-securityagent-agentspace-kmskeyid)" : {{String}},
      "[Name](#cfn-securityagent-agentspace-name)" : {{String}},
      "[Tags](#cfn-securityagent-agentspace-tags)" : {{[ Tag, ... ]}},
      "[TargetDomainIds](#cfn-securityagent-agentspace-targetdomainids)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-securityagent-agentspace-syntax.yaml"></a>

```
Type: AWS::SecurityAgent::AgentSpace
Properties:
  [AwsResources](#cfn-securityagent-agentspace-awsresources): {{
    AWSResources}}
  [CodeReviewSettings](#cfn-securityagent-agentspace-codereviewsettings): {{
    CodeReviewSettings}}
  [Description](#cfn-securityagent-agentspace-description): {{String}}
  [IntegratedResources](#cfn-securityagent-agentspace-integratedresources): {{
    - IntegratedResource}}
  [KmsKeyId](#cfn-securityagent-agentspace-kmskeyid): {{String}}
  [Name](#cfn-securityagent-agentspace-name): {{String}}
  [Tags](#cfn-securityagent-agentspace-tags): {{
    - Tag}}
  [TargetDomainIds](#cfn-securityagent-agentspace-targetdomainids): {{
    - String}}
```

## Properties
<a name="aws-resource-securityagent-agentspace-properties"></a>

`AwsResources`  <a name="cfn-securityagent-agentspace-awsresources"></a>
The Amazon Web Services resources to associate with the agent space.
*Required*: No
*Type*: [AWSResources](aws-properties-securityagent-agentspace-awsresources.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodeReviewSettings`  <a name="cfn-securityagent-agentspace-codereviewsettings"></a>
The code review settings for the agent space.
*Required*: No
*Type*: [CodeReviewSettings](aws-properties-securityagent-agentspace-codereviewsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-securityagent-agentspace-description"></a>
A description of the agent space.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegratedResources`  <a name="cfn-securityagent-agentspace-integratedresources"></a>
The list of integrated resource items to update.
*Required*: No
*Type*: Array of [IntegratedResource](aws-properties-securityagent-agentspace-integratedresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-securityagent-agentspace-kmskeyid"></a>
The identifier of the Amazon Web Services KMS key to use for encrypting data in the agent space.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-securityagent-agentspace-name"></a>
The name of the agent space.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-securityagent-agentspace-tags"></a>
The tags to associate with the agent space.
*Required*: No
*Type*: Array of [Tag](aws-properties-securityagent-agentspace-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetDomainIds`  <a name="cfn-securityagent-agentspace-targetdomainids"></a>
The list of target domain identifiers to associate with the agent space.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityagent-agentspace-return-values"></a>

### Ref
<a name="aws-resource-securityagent-agentspace-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the agent space ID. For example:

 `{ "Ref": "MyAgentSpace" }`

For the agent space `MyAgentSpace`, `Ref` returns the unique identifier of the agent space.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securityagent-agentspace-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityagent-agentspace-return-values-fn--getatt-fn--getatt"></a>

`AgentSpaceId`  <a name="AgentSpaceId-fn::getatt"></a>
The unique identifier of the agent space. For example: `as-0123456789abcdef0`.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the agent space was created, in ISO 8601 format. For example: `2024-01-01T00:00:00Z`.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the agent space was last updated, in ISO 8601 format. For example: `2024-01-01T00:00:00Z`.
