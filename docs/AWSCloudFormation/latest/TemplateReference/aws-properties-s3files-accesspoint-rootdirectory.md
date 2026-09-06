---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3files-accesspoint-rootdirectory.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Files::AccessPoint RootDirectory
<a name="aws-properties-s3files-accesspoint-rootdirectory"></a>

Specifies the root directory path and optional creation permissions for newly created directories.

## Syntax
<a name="aws-properties-s3files-accesspoint-rootdirectory-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3files-accesspoint-rootdirectory-syntax.json"></a>

```
{
  "[CreationPermissions](#cfn-s3files-accesspoint-rootdirectory-creationpermissions)" : {{CreationPermissions}},
  "[Path](#cfn-s3files-accesspoint-rootdirectory-path)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3files-accesspoint-rootdirectory-syntax.yaml"></a>

```
  [CreationPermissions](#cfn-s3files-accesspoint-rootdirectory-creationpermissions): {{
    CreationPermissions}}
  [Path](#cfn-s3files-accesspoint-rootdirectory-path): {{String}}
```

## Properties
<a name="aws-properties-s3files-accesspoint-rootdirectory-properties"></a>

`CreationPermissions`  <a name="cfn-s3files-accesspoint-rootdirectory-creationpermissions"></a>
The POSIX IDs and permissions to apply to the access point's root directory. If the root directory path specified does not exist, Amazon S3 Files creates the root directory using these settings when a client connects to the access point. When specifying `CreationPermissions`, you must provide values for all properties.
*Required*: No
*Type*: [CreationPermissions](aws-properties-s3files-accesspoint-creationpermissions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Path`  <a name="cfn-s3files-accesspoint-rootdirectory-path"></a>
The path on the S3 Files file system to expose as the root directory to clients using the access point. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the `CreationPermissions`.
*Required*: No
*Type*: String
*Pattern*: `^(\/|(\/(?!\.)+[^$#<>;;`|&?{}^*/\n]+){1,4})$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
