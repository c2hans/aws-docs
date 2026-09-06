---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datasync-locationfsxwindows.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationFSxWindows
<a name="aws-resource-datasync-locationfsxwindows"></a>

The `AWS::DataSync::LocationFSxWindows` resource specifies an endpoint for an Amazon FSx for Windows Server file system.

## Syntax
<a name="aws-resource-datasync-locationfsxwindows-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datasync-locationfsxwindows-syntax.json"></a>

```
{
  "Type" : "AWS::DataSync::LocationFSxWindows",
  "Properties" : {
      "[CmkSecretConfig](#cfn-datasync-locationfsxwindows-cmksecretconfig)" : {{CmkSecretConfig}},
      "[CustomSecretConfig](#cfn-datasync-locationfsxwindows-customsecretconfig)" : {{CustomSecretConfig}},
      "[Domain](#cfn-datasync-locationfsxwindows-domain)" : {{String}},
      "[FsxFilesystemArn](#cfn-datasync-locationfsxwindows-fsxfilesystemarn)" : {{String}},
      "[Password](#cfn-datasync-locationfsxwindows-password)" : {{String}},
      "[SecurityGroupArns](#cfn-datasync-locationfsxwindows-securitygrouparns)" : {{[ String, ... ]}},
      "[Subdirectory](#cfn-datasync-locationfsxwindows-subdirectory)" : {{String}},
      "[Tags](#cfn-datasync-locationfsxwindows-tags)" : {{[ Tag, ... ]}},
      "[User](#cfn-datasync-locationfsxwindows-user)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-datasync-locationfsxwindows-syntax.yaml"></a>

```
Type: AWS::DataSync::LocationFSxWindows
Properties:
  [CmkSecretConfig](#cfn-datasync-locationfsxwindows-cmksecretconfig): {{
    CmkSecretConfig}}
  [CustomSecretConfig](#cfn-datasync-locationfsxwindows-customsecretconfig): {{
    CustomSecretConfig}}
  [Domain](#cfn-datasync-locationfsxwindows-domain): {{String}}
  [FsxFilesystemArn](#cfn-datasync-locationfsxwindows-fsxfilesystemarn): {{String}}
  [Password](#cfn-datasync-locationfsxwindows-password): {{String}}
  [SecurityGroupArns](#cfn-datasync-locationfsxwindows-securitygrouparns): {{
    - String}}
  [Subdirectory](#cfn-datasync-locationfsxwindows-subdirectory): {{String}}
  [Tags](#cfn-datasync-locationfsxwindows-tags): {{
    - Tag}}
  [User](#cfn-datasync-locationfsxwindows-user): {{String}}
```

## Properties
<a name="aws-resource-datasync-locationfsxwindows-properties"></a>

`CmkSecretConfig`  <a name="cfn-datasync-locationfsxwindows-cmksecretconfig"></a>
Specifies configuration information for a DataSync-managed secret, such as an authentication token, secret key, password, or Kerberos keytab that DataSync uses to access a specific storage location, with a customer-managed AWS KMS key.
You can use either `CmkSecretConfig` or `CustomSecretConfig` to provide credentials for a `CreateLocation` request. Do not provide both parameters for the same request.
*Required*: No
*Type*: [CmkSecretConfig](aws-properties-datasync-locationfsxwindows-cmksecretconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomSecretConfig`  <a name="cfn-datasync-locationfsxwindows-customsecretconfig"></a>
Specifies configuration information for a customer-managed Secrets Manager secret where a storage location credentials is stored in Secrets Manager as plain text (for authentication token, secret key, or password) or as binary (for Kerberos keytab). This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret.
You can use either `CmkSecretConfig` or `CustomSecretConfig` to provide credentials for a `CreateLocation` request. Do not provide both parameters for the same request.
*Required*: No
*Type*: [CustomSecretConfig](aws-properties-datasync-locationfsxwindows-customsecretconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Domain`  <a name="cfn-datasync-locationfsxwindows-domain"></a>
Specifies the name of the Windows domain that the FSx for Windows File Server file system belongs to.
If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right file system.
*Required*: No
*Type*: String
*Pattern*: `^([A-Za-z0-9]+[A-Za-z0-9-.]*)*[A-Za-z0-9-]*[A-Za-z0-9]$`
*Maximum*: `253`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FsxFilesystemArn`  <a name="cfn-datasync-locationfsxwindows-fsxfilesystemarn"></a>
Specifies the Amazon Resource Name (ARN) for the FSx for Windows File Server file system.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):fsx:[a-z\-0-9]*:[0-9]{12}:file-system/fs-.*$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Password`  <a name="cfn-datasync-locationfsxwindows-password"></a>
Specifies the password of the user with the permissions to mount and access the files, folders, and file metadata in your FSx for Windows File Server file system.
*Required*: No
*Type*: String
*Pattern*: `^.{0,104}$`
*Maximum*: `104`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupArns`  <a name="cfn-datasync-locationfsxwindows-securitygrouparns"></a>
The Amazon Resource Names (ARNs) of the security groups that are used to configure the FSx for Windows File Server file system.
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/.*$`
*Length constraints*: Maximum length of 128.
*Required*: Yes
*Type*: Array of String
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Subdirectory`  <a name="cfn-datasync-locationfsxwindows-subdirectory"></a>
Specifies a mount path for your file system using forward slashes. This is where DataSync reads or writes data (depending on if this is a source or destination location).
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-datasync-locationfsxwindows-tags"></a>
Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.
*Required*: No
*Type*: Array of [Tag](aws-properties-datasync-locationfsxwindows-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`User`  <a name="cfn-datasync-locationfsxwindows-user"></a>
The user who has the permissions to access files and folders in the FSx for Windows File Server file system.
For information about choosing a user name that ensures sufficient permissions to files, folders, and metadata, see [user](https://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html#FSxWuser).
*Required*: Yes
*Type*: String
*Pattern*: `^[^\x5B\x5D\\/:;|=,+*?]{1,104}$`
*Maximum*: `104`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datasync-locationfsxwindows-return-values"></a>

### Ref
<a name="aws-resource-datasync-locationfsxwindows-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the location resource ARN. For example:

 `arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50s3`

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datasync-locationfsxwindows-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datasync-locationfsxwindows-return-values-fn--getatt-fn--getatt"></a>

`CmkSecretConfig.SecretArn`  <a name="CmkSecretConfig.SecretArn-fn::getatt"></a>
Property description not available.

`LocationArn`  <a name="LocationArn-fn::getatt"></a>
The ARN of the specified FSx for Windows Server file system location.

`LocationUri`  <a name="LocationUri-fn::getatt"></a>
The URI of the specified FSx for Windows Server file system location.

## Examples
<a name="aws-resource-datasync-locationfsxwindows--examples"></a>

### Specify an Amazon FSx for Windows File Server location for DataSync
<a name="aws-resource-datasync-locationfsxwindows--examples--Specify_an_Amazon_FSx_for_Windows_File_Server_location_for_DataSync"></a>

The following examples specify an FSx for Windows File Server location for DataSync, including the subdirectory `/MySubdirectory`, user `Admin`, and password.

#### JSON
<a name="aws-resource-datasync-locationfsxwindows--examples--Specify_an_Amazon_FSx_for_Windows_File_Server_location_for_DataSync--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Specifies an FSx for Windows File Server location for DataSync",
    "Resources": {
        "LocationFSxWindows": {
            "Type": "AWS::DataSync::LocationFSxWindows",
            "Properties": {
                "FsxFilesystemArn": "arn:aws:fsx:us-east-2:111222333444:file-system/fs-12345fsx",
                "SecurityGroupArns": [
                    "arn:aws:ec2:us-east-2:11122233344:security-group/sg-12345678901212345"
                ],
                "Subdirectory": "/MySubdirectory",
                "User": "Admin",
                "Password": {
                    "Ref": "Password"
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-datasync-locationfsxwindows--examples--Specify_an_Amazon_FSx_for_Windows_File_Server_location_for_DataSync--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: Specifies an FSx for Windows File Server location for DataSync
Resources:
  LocationFSxWindows:
    Type: AWS::DataSync::LocationFSxWindows
    Properties:
      FsxFilesystemArn: arn:aws:fsx:us-east-2:111222333444:file-system/fs-12345fsx
      SecurityGroupArns:
        - arn:aws:ec2:us-east-2:11122233344:security-group/sg-12345678901212345
      Subdirectory: /MySubdirectory
      User: Admin
      Password: !Ref Password
```
