---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-devopsagent-asset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Asset
<a name="aws-resource-devopsagent-asset"></a>

The `AWS::DevOpsAgent::Asset` resource attaches an asset to an Agent Space for the AWS DevOps Agent Service. An asset is a versioned bundle of files, with optional metadata, that the Agent Space uses, such as a skill, an `agents_md` document, or an attachment.

## Syntax
<a name="aws-resource-devopsagent-asset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-devopsagent-asset-syntax.json"></a>

```
{
  "Type" : "AWS::DevOpsAgent::Asset",
  "Properties" : {
      "[AgentSpaceId](#cfn-devopsagent-asset-agentspaceid)" : {{String}},
      "[AssetType](#cfn-devopsagent-asset-assettype)" : {{String}},
      "[Files](#cfn-devopsagent-asset-files)" : {{[ AssetFile, ... ]}},
      "[Metadata](#cfn-devopsagent-asset-metadata)" : {{Json}},
      "[Zip](#cfn-devopsagent-asset-zip)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-devopsagent-asset-syntax.yaml"></a>

```
Type: AWS::DevOpsAgent::Asset
Properties:
  [AgentSpaceId](#cfn-devopsagent-asset-agentspaceid): {{String}}
  [AssetType](#cfn-devopsagent-asset-assettype): {{String}}
  [Files](#cfn-devopsagent-asset-files): {{
    - AssetFile}}
  [Metadata](#cfn-devopsagent-asset-metadata): {{Json}}
  [Zip](#cfn-devopsagent-asset-zip): {{String}}
```

## Properties
<a name="aws-resource-devopsagent-asset-properties"></a>

`AgentSpaceId`  <a name="cfn-devopsagent-asset-agentspaceid"></a>
The unique identifier of the parent Agent Space. The asset is created as a child of this Agent Space.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: Updates are not supported.

`AssetType`  <a name="cfn-devopsagent-asset-assettype"></a>
The type of asset. As of launch, the customer-creatable types are `skill`, `agents_md`, and `attachment`. The service treats this as an open string; call `ListAssetTypes` for the current authoritative set of supported types.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9_]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: Updates are not supported.

`Files`  <a name="cfn-devopsagent-asset-files"></a>
The list of files that make up the asset bundle. Mutually exclusive with `Zip`. On update, the `Path` of each file is the key used to determine which files are added, changed, or removed.
This is a write-only property. Its value is not returned by read operations.
*Required*: No
*Type*: Array of [AssetFile](aws-properties-devopsagent-asset-assetfile.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metadata`  <a name="cfn-devopsagent-asset-metadata"></a>
The asset metadata document. The required and optional keys depend on the value of `AssetType`. Values may be strings, numbers, booleans, or lists of any of those, and are validated server-side. See the AWS DevOps Agent Asset API documentation for the per-type metadata schema.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Zip`  <a name="cfn-devopsagent-asset-zip"></a>
A base64-encoded zip bundle containing all files for the asset. Mutually exclusive with `Files`. The service treats a zip as a complete replacement of the asset's files.
This is a write-only property. Its value is not returned by read operations.
*Required*: No
*Type*: String
*Maximum*: `8388608`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-devopsagent-asset-return-values"></a>

### Ref
<a name="aws-resource-devopsagent-asset-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the asset identifier, which is a combination of the Agent Space ID and the asset ID, separated by a vertical bar (for example, `as-1234567890abcdef0|asset-0987654321fedcba0`).

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-devopsagent-asset-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-devopsagent-asset-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the asset.

`AssetId`  <a name="AssetId-fn::getatt"></a>
The unique identifier of the asset, assigned by the service when the asset is created.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the asset was created.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the asset was last updated.

`Version`  <a name="Version-fn::getatt"></a>
The current version of the asset. The service manages this value and increments it on every successful update.
