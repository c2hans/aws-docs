---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-agentregistry-registryrecord.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord
<a name="aws-resource-agentregistry-registryrecord"></a>

The `AWS::AgentRegistry::RegistryRecord` resource specifies a registry record within a registry. A registry record describes a discoverable resource, such as a Model Context Protocol (MCP) server, an agent, an agent skill, or a custom resource.

## Syntax
<a name="aws-resource-agentregistry-registryrecord-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-agentregistry-registryrecord-syntax.json"></a>

```
{
  "Type" : "AWS::AgentRegistry::RegistryRecord",
  "Properties" : {
      "[Description](#cfn-agentregistry-registryrecord-description)" : {{String}},
      "[Descriptors](#cfn-agentregistry-registryrecord-descriptors)" : {{Descriptors}},
      "[DisplayName](#cfn-agentregistry-registryrecord-displayname)" : {{String}},
      "[Name](#cfn-agentregistry-registryrecord-name)" : {{String}},
      "[RecordType](#cfn-agentregistry-registryrecord-recordtype)" : {{String}},
      "[RecordVersion](#cfn-agentregistry-registryrecord-recordversion)" : {{String}},
      "[RegistryId](#cfn-agentregistry-registryrecord-registryid)" : {{String}},
      "[Tags](#cfn-agentregistry-registryrecord-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-agentregistry-registryrecord-syntax.yaml"></a>

```
Type: AWS::AgentRegistry::RegistryRecord
Properties:
  [Description](#cfn-agentregistry-registryrecord-description): {{String}}
  [Descriptors](#cfn-agentregistry-registryrecord-descriptors): {{
    Descriptors}}
  [DisplayName](#cfn-agentregistry-registryrecord-displayname): {{String}}
  [Name](#cfn-agentregistry-registryrecord-name): {{String}}
  [RecordType](#cfn-agentregistry-registryrecord-recordtype): {{String}}
  [RecordVersion](#cfn-agentregistry-registryrecord-recordversion): {{String}}
  [RegistryId](#cfn-agentregistry-registryrecord-registryid): {{String}}
  [Tags](#cfn-agentregistry-registryrecord-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-agentregistry-registryrecord-properties"></a>

`Description`  <a name="cfn-agentregistry-registryrecord-description"></a>
The description of the registry record.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Descriptors`  <a name="cfn-agentregistry-registryrecord-descriptors"></a>
The typed descriptor content for the registry record. Exactly one descriptor field is populated based on the record type.
*Required*: Yes
*Type*: [Descriptors](aws-properties-agentregistry-registryrecord-descriptors.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-agentregistry-registryrecord-displayname"></a>
The human-readable display name of the registry record.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-agentregistry-registryrecord-name"></a>
The name of the registry record. Names are unique within a registry.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordType`  <a name="cfn-agentregistry-registryrecord-recordtype"></a>
The type of the registry record, which determines the descriptor format.
*Required*: Yes
*Type*: String
*Allowed values*: `MCP | AGENT | SKILL | CUSTOM`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecordVersion`  <a name="cfn-agentregistry-registryrecord-recordversion"></a>
The version of the registry record.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9.-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegistryId`  <a name="cfn-agentregistry-registryrecord-registryid"></a>
The identifier of the registry in which to create the record. You can specify either the registry ID or the registry Amazon Resource Name (ARN).
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-agentregistry-registryrecord-tags"></a>
A list of key-value pairs that contain metadata for the registry record. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-agentregistry-registryrecord-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-agentregistry-registryrecord-return-values"></a>

### Ref
<a name="aws-resource-agentregistry-registryrecord-return-values-ref"></a>

 When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns

The Amazon Resource Name (ARN) of the registry record.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-agentregistry-registryrecord-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-agentregistry-registryrecord-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the registry record was created.

`RecordArn`  <a name="RecordArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the registry record.

`RecordId`  <a name="RecordId-fn::getatt"></a>
The unique identifier of the registry record.

`RegistryArn`  <a name="RegistryArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the registry that contains this record.

`Status`  <a name="Status-fn::getatt"></a>
The current lifecycle status of the registry record.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the registry record was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
