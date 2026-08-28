---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediapackage-asset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackage::Asset
<a name="aws-resource-mediapackage-asset"></a>

Creates an asset to ingest VOD content.

After it's created, the asset starts ingesting content and generates playback URLs for the packaging configurations associated with it. When ingest is complete, downstream devices use the appropriate URL to request VOD content from AWS Elemental MediaPackage.

## Syntax
<a name="aws-resource-mediapackage-asset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediapackage-asset-syntax.json"></a>

```
{
  "Type" : "AWS::MediaPackage::Asset",
  "Properties" : {
      "[EgressEndpoints](#cfn-mediapackage-asset-egressendpoints)" : {{[ EgressEndpoint, ... ]}},
      "[Id](#cfn-mediapackage-asset-id)" : {{String}},
      "[PackagingGroupId](#cfn-mediapackage-asset-packaginggroupid)" : {{String}},
      "[ResourceId](#cfn-mediapackage-asset-resourceid)" : {{String}},
      "[SourceArn](#cfn-mediapackage-asset-sourcearn)" : {{String}},
      "[SourceRoleArn](#cfn-mediapackage-asset-sourcerolearn)" : {{String}},
      "[Tags](#cfn-mediapackage-asset-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-mediapackage-asset-syntax.yaml"></a>

```
Type: AWS::MediaPackage::Asset
Properties:
  [EgressEndpoints](#cfn-mediapackage-asset-egressendpoints): {{
    - EgressEndpoint}}
  [Id](#cfn-mediapackage-asset-id): {{String}}
  [PackagingGroupId](#cfn-mediapackage-asset-packaginggroupid): {{String}}
  [ResourceId](#cfn-mediapackage-asset-resourceid): {{String}}
  [SourceArn](#cfn-mediapackage-asset-sourcearn): {{String}}
  [SourceRoleArn](#cfn-mediapackage-asset-sourcerolearn): {{String}}
  [Tags](#cfn-mediapackage-asset-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-mediapackage-asset-properties"></a>

`EgressEndpoints`  <a name="cfn-mediapackage-asset-egressendpoints"></a>
List of playback endpoints that are available for this asset.
*Required*: No
*Type*: Array of [EgressEndpoint](aws-properties-mediapackage-asset-egressendpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-mediapackage-asset-id"></a>
Unique identifier that you assign to the asset.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PackagingGroupId`  <a name="cfn-mediapackage-asset-packaginggroupid"></a>
The ID of the packaging group associated with this asset.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceId`  <a name="cfn-mediapackage-asset-resourceid"></a>
Unique identifier for this asset, as it's configured in the key provider service.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceArn`  <a name="cfn-mediapackage-asset-sourcearn"></a>
The ARN for the source content in Amazon S3.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceRoleArn`  <a name="cfn-mediapackage-asset-sourcerolearn"></a>
The ARN for the IAM role that provides AWS Elemental MediaPackage access to the Amazon S3 bucket where the source content is stored. Valid format: arn:aws:iam::{accountID}:role/{name}
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-mediapackage-asset-tags"></a>
The tags to assign to the asset.
*Required*: No
*Type*: Array of [Tag](aws-properties-mediapackage-asset-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-mediapackage-asset-return-values"></a>

### Ref
<a name="aws-resource-mediapackage-asset-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the asset.

For example: `{ "Ref": "myAsset" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-mediapackage-asset-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-mediapackage-asset-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the asset. You can get this from the response to any request to the asset.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that the asset was initially submitted for ingest.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
