---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3files-accesspoint-creationpermissions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Files::AccessPoint CreationPermissions
<a name="aws-properties-s3files-accesspoint-creationpermissions"></a>

Specifies the POSIX IDs and permissions to apply when creating the root directory for an access point.

## Syntax
<a name="aws-properties-s3files-accesspoint-creationpermissions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3files-accesspoint-creationpermissions-syntax.json"></a>

```
{
  "[OwnerGid](#cfn-s3files-accesspoint-creationpermissions-ownergid)" : {{String}},
  "[OwnerUid](#cfn-s3files-accesspoint-creationpermissions-owneruid)" : {{String}},
  "[Permissions](#cfn-s3files-accesspoint-creationpermissions-permissions)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3files-accesspoint-creationpermissions-syntax.yaml"></a>

```
  [OwnerGid](#cfn-s3files-accesspoint-creationpermissions-ownergid): {{String}}
  [OwnerUid](#cfn-s3files-accesspoint-creationpermissions-owneruid): {{String}}
  [Permissions](#cfn-s3files-accesspoint-creationpermissions-permissions): {{String}}
```

## Properties
<a name="aws-properties-s3files-accesspoint-creationpermissions-properties"></a>

`OwnerGid`  <a name="cfn-s3files-accesspoint-creationpermissions-ownergid"></a>
The POSIX group ID to apply to the root directory. Accepts values from 0 to 4294967295.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OwnerUid`  <a name="cfn-s3files-accesspoint-creationpermissions-owneruid"></a>
The POSIX user ID to apply to the root directory. Accepts values from 0 to 4294967295.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Permissions`  <a name="cfn-s3files-accesspoint-creationpermissions-permissions"></a>
The POSIX permissions to apply to the root directory, in the format of an octal number representing the file's mode bits.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-7]{3,4}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
