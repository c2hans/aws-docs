---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-agentregistry-registry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Registry
<a name="aws-resource-agentregistry-registry"></a>

The `AWS::AgentRegistry::Registry` resource specifies a registry. A registry is a managed catalog for publishing and discovering resources such as Model Context Protocol (MCP) servers, agents, and agent skills. It organizes registry records and defines how consumers discover them, how they are authorized, and how submitted records are approved.

## Syntax
<a name="aws-resource-agentregistry-registry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-agentregistry-registry-syntax.json"></a>

```
{
  "Type" : "AWS::AgentRegistry::Registry",
  "Properties" : {
      "[ApprovalConfiguration](#cfn-agentregistry-registry-approvalconfiguration)" : {{ApprovalConfiguration}},
      "[AuthorizerType](#cfn-agentregistry-registry-authorizertype)" : {{String}},
      "[AutoDetectionEnabled](#cfn-agentregistry-registry-autodetectionenabled)" : {{Boolean}},
      "[AutoDetectionScope](#cfn-agentregistry-registry-autodetectionscope)" : {{String}},
      "[CustomMetadataSchemaConfiguration](#cfn-agentregistry-registry-custommetadataschemaconfiguration)" : {{CustomMetadataSchemaConfiguration}},
      "[Description](#cfn-agentregistry-registry-description)" : {{String}},
      "[DiscoveryConfiguration](#cfn-agentregistry-registry-discoveryconfiguration)" : {{DiscoveryConfiguration}},
      "[EncryptionConfiguration](#cfn-agentregistry-registry-encryptionconfiguration)" : {{EncryptionConfiguration}},
      "[Name](#cfn-agentregistry-registry-name)" : {{String}},
      "[Tags](#cfn-agentregistry-registry-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-agentregistry-registry-syntax.yaml"></a>

```
Type: AWS::AgentRegistry::Registry
Properties:
  [ApprovalConfiguration](#cfn-agentregistry-registry-approvalconfiguration): {{
    ApprovalConfiguration}}
  [AuthorizerType](#cfn-agentregistry-registry-authorizertype): {{String}}
  [AutoDetectionEnabled](#cfn-agentregistry-registry-autodetectionenabled): {{Boolean}}
  [AutoDetectionScope](#cfn-agentregistry-registry-autodetectionscope): {{String}}
  [CustomMetadataSchemaConfiguration](#cfn-agentregistry-registry-custommetadataschemaconfiguration): {{
    CustomMetadataSchemaConfiguration}}
  [Description](#cfn-agentregistry-registry-description): {{String}}
  [DiscoveryConfiguration](#cfn-agentregistry-registry-discoveryconfiguration): {{
    DiscoveryConfiguration}}
  [EncryptionConfiguration](#cfn-agentregistry-registry-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [Name](#cfn-agentregistry-registry-name): {{String}}
  [Tags](#cfn-agentregistry-registry-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-agentregistry-registry-properties"></a>

`ApprovalConfiguration`  <a name="cfn-agentregistry-registry-approvalconfiguration"></a>
The configuration for the registry's record approval workflow. It controls whether submitted records require manual review before becoming discoverable, or are automatically approved.
*Required*: No
*Type*: [ApprovalConfiguration](aws-properties-agentregistry-registry-approvalconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizerType`  <a name="cfn-agentregistry-registry-authorizertype"></a>
The type of authorizer that controls how consumers access the registry's search and MCP invoke operations.
*Required*: No
*Type*: String
*Allowed values*: `CUSTOM_JWT | AWS_IAM`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AutoDetectionEnabled`  <a name="cfn-agentregistry-registry-autodetectionenabled"></a>
Specifies whether auto-detection is requested for the registry. You must specify this property together with `AutoDetectionScope`.
Setting this property to `true` is necessary but not sufficient for auto-detection to become active. The preconditions of the configured scope must also be met. To check whether auto-detection is active, use the `AutoDetectionStatus` return value.
To turn off auto-detection, explicitly set this property to `false`. If you remove `AutoDetectionEnabled` and `AutoDetectionScope` from the template, the existing auto-detection settings don't change.
You can't delete a registry while auto-detection is enabled. Before you delete the registry, set this property to `false` and update the stack.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoDetectionScope`  <a name="cfn-agentregistry-registry-autodetectionscope"></a>
The source from which the registry detects resources. The only supported value is `ORGANIZATION`, which detects resources from all member accounts of an AWS organization. You must specify this property together with `AutoDetectionEnabled`.
*Required*: No
*Type*: String
*Allowed values*: `ORGANIZATION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomMetadataSchemaConfiguration`  <a name="cfn-agentregistry-registry-custommetadataschemaconfiguration"></a>
The configuration that defines a typed custom metadata schema for the registry. Registry records use this schema for their custom metadata. You can specify a default schema, schema overrides for specific record types, or both. Both are optional.
Schema evolution is additive only. You can add fields and enum values. You can't remove fields, change field types, or remove enum values.
If you remove this property from the template during a stack update, the existing schema isn't cleared. The service keeps the current schema.
*Required*: No
*Type*: [CustomMetadataSchemaConfiguration](aws-properties-agentregistry-registry-custommetadataschemaconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-agentregistry-registry-description"></a>
The description of the registry.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DiscoveryConfiguration`  <a name="cfn-agentregistry-registry-discoveryconfiguration"></a>
The discovery configuration for the registry. It controls how consumers are authorized to search the registry and invoke its MCP endpoint.
*Required*: No
*Type*: [DiscoveryConfiguration](aws-properties-agentregistry-registry-discoveryconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionConfiguration`  <a name="cfn-agentregistry-registry-encryptionconfiguration"></a>
The server-side encryption configuration for the registry. It specifies a customer managed AWS Key Management Service (AWS KMS) key that encrypts the registry's content. If you omit this property, the registry's content is encrypted with an AWS owned key.
You can't change the encryption configuration after you create the registry. If you specify a different KMS key, add this property to an existing registry, or remove it, CloudFormation replaces the registry. CloudFormation creates a new registry with a new Amazon Resource Name (ARN). Then it deletes the original registry, including the registry records that it contains.
CloudFormation doesn't re-create registry records that the stack doesn't manage. If any of these records remain in the original registry, CloudFormation can't delete the original registry, and it remains in your account.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-agentregistry-registry-encryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-agentregistry-registry-name"></a>
The name of the registry.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-agentregistry-registry-tags"></a>
A list of key-value pairs that contain metadata for the registry. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-agentregistry-registry-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-agentregistry-registry-return-values"></a>

### Ref
<a name="aws-resource-agentregistry-registry-return-values-ref"></a>

 When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns

The Amazon Resource Name (ARN) of the registry.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-agentregistry-registry-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-agentregistry-registry-return-values-fn--getatt-fn--getatt"></a>

`AutoDetectionStatus`  <a name="AutoDetectionStatus-fn::getatt"></a>
The current auto-detection status of the registry. `ACTIVE` indicates that the registry is actively being populated with detected resources. `INACTIVE` indicates that the preconditions required at the configured scope aren't currently met.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the registry was created.

`RegistryArn`  <a name="RegistryArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the registry.

`RegistryId`  <a name="RegistryId-fn::getatt"></a>
The unique identifier of the registry.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the registry.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the registry was last updated.
