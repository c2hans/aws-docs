---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3files-accesspoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Files::AccessPoint
<a name="aws-resource-s3files-accesspoint"></a>

The `AWS::S3Files::AccessPoint` resource specifies an access point for an Amazon S3 Files file system. Access points provide application-specific access with POSIX user identity and root directory enforcement.

## Syntax
<a name="aws-resource-s3files-accesspoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3files-accesspoint-syntax.json"></a>

```
{
  "Type" : "AWS::S3Files::AccessPoint",
  "Properties" : {
      "[ClientToken](#cfn-s3files-accesspoint-clienttoken)" : {{String}},
      "[FileSystemId](#cfn-s3files-accesspoint-filesystemid)" : {{String}},
      "[PosixUser](#cfn-s3files-accesspoint-posixuser)" : {{PosixUser}},
      "[RootDirectory](#cfn-s3files-accesspoint-rootdirectory)" : {{RootDirectory}},
      "[Tags](#cfn-s3files-accesspoint-tags)" : {{[ AccessPointTag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-s3files-accesspoint-syntax.yaml"></a>

```
Type: AWS::S3Files::AccessPoint
Properties:
  [ClientToken](#cfn-s3files-accesspoint-clienttoken): {{String}}
  [FileSystemId](#cfn-s3files-accesspoint-filesystemid): {{String}}
  [PosixUser](#cfn-s3files-accesspoint-posixuser): {{
    PosixUser}}
  [RootDirectory](#cfn-s3files-accesspoint-rootdirectory): {{
    RootDirectory}}
  [Tags](#cfn-s3files-accesspoint-tags): {{
    - AccessPointTag}}
```

## Properties
<a name="aws-resource-s3files-accesspoint-properties"></a>

`ClientToken`  <a name="cfn-s3files-accesspoint-clienttoken"></a>
A string of up to 64 ASCII characters that Amazon S3 Files uses to ensure idempotent creation.
*Required*: No
*Type*: String
*Pattern*: `^(.+)$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileSystemId`  <a name="cfn-s3files-accesspoint-filesystemid"></a>
The ID of the S3 Files file system that the access point provides access to.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PosixUser`  <a name="cfn-s3files-accesspoint-posixuser"></a>
The POSIX identity configured for this access point.
*Required*: No
*Type*: [PosixUser](aws-properties-s3files-accesspoint-posixuser.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RootDirectory`  <a name="cfn-s3files-accesspoint-rootdirectory"></a>
The root directory configuration for this access point.
*Required*: No
*Type*: [RootDirectory](aws-properties-s3files-accesspoint-rootdirectory.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-s3files-accesspoint-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [AccessPointTag](aws-properties-s3files-accesspoint-accesspointtag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-s3files-accesspoint-return-values"></a>

### Ref
<a name="aws-resource-s3files-accesspoint-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the access point ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-s3files-accesspoint-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-s3files-accesspoint-return-values-fn--getatt-fn--getatt"></a>

`AccessPointArn`  <a name="AccessPointArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the access point.

`AccessPointId`  <a name="AccessPointId-fn::getatt"></a>
The ID of the access point.

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
The AWS account ID of the access point owner.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the access point.
