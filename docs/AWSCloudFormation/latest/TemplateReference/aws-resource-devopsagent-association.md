---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-devopsagent-association.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association
<a name="aws-resource-devopsagent-association"></a>

The `AWS::DevOpsAgent::Association` resource specifies an association between an Agent Space and a service, defining how the Agent Space interacts with external services like GitHub, Slack, AWS accounts, and others.

## Syntax
<a name="aws-resource-devopsagent-association-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-devopsagent-association-syntax.json"></a>

```
{
  "Type" : "AWS::DevOpsAgent::Association",
  "Properties" : {
      "[AgentSpaceId](#cfn-devopsagent-association-agentspaceid)" : {{String}},
      "[Configuration](#cfn-devopsagent-association-configuration)" : {{ServiceConfiguration}},
      "[LinkedAssociationIds](#cfn-devopsagent-association-linkedassociationids)" : {{[ String, ... ]}},
      "[ServiceId](#cfn-devopsagent-association-serviceid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-devopsagent-association-syntax.yaml"></a>

```
Type: AWS::DevOpsAgent::Association
Properties:
  [AgentSpaceId](#cfn-devopsagent-association-agentspaceid): {{String}}
  [Configuration](#cfn-devopsagent-association-configuration): {{
    ServiceConfiguration}}
  [LinkedAssociationIds](#cfn-devopsagent-association-linkedassociationids): {{
    - String}}
  [ServiceId](#cfn-devopsagent-association-serviceid): {{String}}
```

## Properties
<a name="aws-resource-devopsagent-association-properties"></a>

`AgentSpaceId`  <a name="cfn-devopsagent-association-agentspaceid"></a>
The unique identifier of the Agent Space.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: Updates are not supported.

`Configuration`  <a name="cfn-devopsagent-association-configuration"></a>
The configuration that directs how the Agent Space interacts with the given service. You can specify only one configuration type per association.
*Allowed Values*: `SourceAws` \| `Aws` \| `GitHub` \| `GitLab` \| `Slack` \| `Dynatrace` \| `ServiceNow` \| `MCPServer` \| `MCPServerNewRelic` \| `MCPServerDatadog` \| `MCPServerSplunk` \| `EventChannel`
*Required*: Yes
*Type*: [ServiceConfiguration](aws-properties-devopsagent-association-serviceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinkedAssociationIds`  <a name="cfn-devopsagent-association-linkedassociationids"></a>
Set of linked association IDs for parent-child relationships.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceId`  <a name="cfn-devopsagent-association-serviceid"></a>
The identifier for the associated service. For `SourceAws` and `Aws` configurations, this must be `aws`. For all other service types, this is a UUID generated from the RegisterService command.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-devopsagent-association-return-values"></a>

### Ref
<a name="aws-resource-devopsagent-association-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the association ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-devopsagent-association-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-devopsagent-association-return-values-fn--getatt-fn--getatt"></a>

`AssociationId`  <a name="AssociationId-fn::getatt"></a>
The unique identifier of the association.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the association was created.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the association was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
