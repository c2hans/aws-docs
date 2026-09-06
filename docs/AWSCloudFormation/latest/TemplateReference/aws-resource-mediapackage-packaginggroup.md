---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediapackage-packaginggroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackage::PackagingGroup
<a name="aws-resource-mediapackage-packaginggroup"></a>

Creates a packaging group.

The packaging group holds one or more packaging configurations. When you create an asset, you specify the packaging group associated with the asset. The asset has playback endpoints for each packaging configuration within the group.

## Syntax
<a name="aws-resource-mediapackage-packaginggroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediapackage-packaginggroup-syntax.json"></a>

```
{
  "Type" : "AWS::MediaPackage::PackagingGroup",
  "Properties" : {
      "[Authorization](#cfn-mediapackage-packaginggroup-authorization)" : {{Authorization}},
      "[EgressAccessLogs](#cfn-mediapackage-packaginggroup-egressaccesslogs)" : {{LogConfiguration}},
      "[Id](#cfn-mediapackage-packaginggroup-id)" : {{String}},
      "[Tags](#cfn-mediapackage-packaginggroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-mediapackage-packaginggroup-syntax.yaml"></a>

```
Type: AWS::MediaPackage::PackagingGroup
Properties:
  [Authorization](#cfn-mediapackage-packaginggroup-authorization): {{
    Authorization}}
  [EgressAccessLogs](#cfn-mediapackage-packaginggroup-egressaccesslogs): {{
    LogConfiguration}}
  [Id](#cfn-mediapackage-packaginggroup-id): {{String}}
  [Tags](#cfn-mediapackage-packaginggroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-mediapackage-packaginggroup-properties"></a>

`Authorization`  <a name="cfn-mediapackage-packaginggroup-authorization"></a>
Parameters for CDN authorization.
*Required*: No
*Type*: [Authorization](aws-properties-mediapackage-packaginggroup-authorization.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EgressAccessLogs`  <a name="cfn-mediapackage-packaginggroup-egressaccesslogs"></a>
The configuration parameters for egress access logging.
*Required*: No
*Type*: [LogConfiguration](aws-properties-mediapackage-packaginggroup-logconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-mediapackage-packaginggroup-id"></a>
Unique identifier that you assign to the packaging group.
*Required*: Yes
*Type*: String
*Pattern*: `\A[0-9a-zA-Z-_]+\Z`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-mediapackage-packaginggroup-tags"></a>
The tags to assign to the packaging group.
*Required*: No
*Type*: Array of [Tag](aws-properties-mediapackage-packaginggroup-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-mediapackage-packaginggroup-return-values"></a>

### Ref
<a name="aws-resource-mediapackage-packaginggroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the packaging group.

For example: `{ "Ref": "myPackagingGroup" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-mediapackage-packaginggroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-mediapackage-packaginggroup-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the packaging group. You can get this from the response to any request to the packaging group.

`DomainName`  <a name="DomainName-fn::getatt"></a>
The URL for the assets in the PackagingGroup.
