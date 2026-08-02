---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datasync-locationefs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationEFS
<a name="aws-resource-datasync-locationefs"></a>

The `AWS::DataSync::LocationEFS` resource creates an endpoint for an Amazon EFS file system. AWS DataSync can access this endpoint as a source or destination location.

## Syntax
<a name="aws-resource-datasync-locationefs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datasync-locationefs-syntax.json"></a>

```
{
  "Type" : "AWS::DataSync::LocationEFS",
  "Properties" : {
      "[AccessPointArn](#cfn-datasync-locationefs-accesspointarn)" : {{String}},
      "[Ec2Config](#cfn-datasync-locationefs-ec2config)" : {{Ec2Config}},
      "[EfsFilesystemArn](#cfn-datasync-locationefs-efsfilesystemarn)" : {{String}},
      "[FileSystemAccessRoleArn](#cfn-datasync-locationefs-filesystemaccessrolearn)" : {{String}},
      "[InTransitEncryption](#cfn-datasync-locationefs-intransitencryption)" : {{String}},
      "[Subdirectory](#cfn-datasync-locationefs-subdirectory)" : {{String}},
      "[Tags](#cfn-datasync-locationefs-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-datasync-locationefs-syntax.yaml"></a>

```
Type: AWS::DataSync::LocationEFS
Properties:
  [AccessPointArn](#cfn-datasync-locationefs-accesspointarn): {{String}}
  [Ec2Config](#cfn-datasync-locationefs-ec2config): {{
    Ec2Config}}
  [EfsFilesystemArn](#cfn-datasync-locationefs-efsfilesystemarn): {{String}}
  [FileSystemAccessRoleArn](#cfn-datasync-locationefs-filesystemaccessrolearn): {{String}}
  [InTransitEncryption](#cfn-datasync-locationefs-intransitencryption): {{String}}
  [Subdirectory](#cfn-datasync-locationefs-subdirectory): {{String}}
  [Tags](#cfn-datasync-locationefs-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-datasync-locationefs-properties"></a>

`AccessPointArn`  <a name="cfn-datasync-locationefs-accesspointarn"></a>
Specifies the Amazon Resource Name (ARN) of the access point that DataSync uses to mount your Amazon EFS file system.
For more information, see [Accessing restricted file systems](https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam).
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):elasticfilesystem:[a-z\-0-9]+:[0-9]{12}:access-point/fsap-[0-9a-f]{8,40}$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ec2Config`  <a name="cfn-datasync-locationefs-ec2config"></a>
Specifies the subnet and security groups DataSync uses to connect to one of your Amazon EFS file system's [mount targets](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html).
*Required*: Yes
*Type*: [Ec2Config](aws-properties-datasync-locationefs-ec2config.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EfsFilesystemArn`  <a name="cfn-datasync-locationefs-efsfilesystemarn"></a>
Specifies the ARN for your Amazon EFS file system.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):elasticfilesystem:[a-z\-0-9]*:[0-9]{12}:file-system/fs-.*$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileSystemAccessRoleArn`  <a name="cfn-datasync-locationefs-filesystemaccessrolearn"></a>
Specifies an AWS Identity and Access Management (IAM) role that allows DataSync to access your Amazon EFS file system.
For information on creating this role, see [Creating a DataSync IAM role for file system access](https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam-role).
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InTransitEncryption`  <a name="cfn-datasync-locationefs-intransitencryption"></a>
Specifies whether you want DataSync to use Transport Layer Security (TLS) 1.2 encryption when it transfers data to or from your Amazon EFS file system.
If you specify an access point using `AccessPointArn` or an IAM role using `FileSystemAccessRoleArn`, you must set this parameter to `TLS1_2`.
*Required*: No
*Type*: String
*Allowed values*: `NONE | TLS1_2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subdirectory`  <a name="cfn-datasync-locationefs-subdirectory"></a>
Specifies a mount path for your Amazon EFS file system. This is where DataSync reads or writes data on your file system (depending on if this is a source or destination location).
By default, DataSync uses the root directory (or [access point](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html) if you provide one by using `AccessPointArn`). You can also include subdirectories using forward slashes (for example, `/path/to/folder`).
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-datasync-locationefs-tags"></a>
Specifies the key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.
*Required*: No
*Type*: Array of [Tag](aws-properties-datasync-locationefs-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datasync-locationefs-return-values"></a>

### Ref
<a name="aws-resource-datasync-locationefs-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the location resource ARN. For example:

 `arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50s3`

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datasync-locationefs-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datasync-locationefs-return-values-fn--getatt-fn--getatt"></a>

`LocationArn`  <a name="LocationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Amazon EFS file system.

`LocationUri`  <a name="LocationUri-fn::getatt"></a>
The URI of the Amazon EFS file system.

## Examples
<a name="aws-resource-datasync-locationefs--examples"></a>

**Topics**
+ [Creating an Amazon EFS location](#aws-resource-datasync-locationefs--examples--Creating_an_Amazon_EFS_location)
+ [Creating an Amazon EFS location with a higher level of security](#aws-resource-datasync-locationefs--examples--Creating_an_Amazon_EFS_location_with_a_higher_level_of_security)

### Creating an Amazon EFS location
<a name="aws-resource-datasync-locationefs--examples--Creating_an_Amazon_EFS_location"></a>

The following example creates a DataSync location for an Amazon EFS file system.

#### JSON
<a name="aws-resource-datasync-locationefs--examples--Creating_an_Amazon_EFS_location--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Specifies a DataSync location for an Amazon EFS file system.",
    "Resources": {
        "LocationEFS": {
            "Type": "AWS::DataSync::LocationEFS",
            "Properties": {
                "Ec2Config": {
                    "SecurityGroupArns": [
                        "arn:aws:ec2:us-east-2:11122233344:security-group/sg-1234567890abcdef2"
                    ],
                    "SubnetArn": "arn:aws:ec2:us-east-2:11122233344:subnet/subnet-1234567890abcdef1"
                },
                "EfsFilesystemArn": "arn:aws:elasticfilesystem:us-east-2:111222333444:file-system/fs-021345abcdef6789",
                "Subdirectory": "/mount/path"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-datasync-locationefs--examples--Creating_an_Amazon_EFS_location--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: Specifies a DataSync location for an Amazon EFS file system.
Resources:
  LocationEFS:
    Type: AWS::DataSync::LocationEFS
      Properties:
        Ec2Config:
          SecurityGroupArns:
            - arn:aws:ec2:us-east-2:11122233344:security-group/sg-1234567890abcdef2
          SubnetArn: arn:aws:ec2:us-east-2:11122233344:subnet/subnet-1234567890abcdef1
        EfsFilesystemArn: arn:aws:elasticfilesystem:us-east-2:111222333444:file-system/fs-021345abcdef6789
        Subdirectory: /mount/path
```

### Creating an Amazon EFS location with a higher level of security
<a name="aws-resource-datasync-locationefs--examples--Creating_an_Amazon_EFS_location_with_a_higher_level_of_security"></a>

The following example creates a DataSync location for an Amazon EFS file system that's configured for restricted access.

#### JSON
<a name="aws-resource-datasync-locationefs--examples--Creating_an_Amazon_EFS_location_with_a_higher_level_of_security--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Specifies a DataSync location for an Amazon EFS file system configured for restricted access.",
    "Resources": {
        "LocationEFS": {
            "Type": "AWS::DataSync::LocationEFS",
            "Properties": {
                "AccessPointArn": "arn:aws:elasticfilesystem:us-east-2:111222333444:access-point/fsap-1234567890abcdef0",
                "Ec2Config": {
                    "SecurityGroupArns": [
                        "arn:aws:ec2:us-east-2:11122233344:security-group/sg-1234567890abcdef2"
                    ],
                    "SubnetArn": "arn:aws:ec2:us-east-2:11122233344:subnet/subnet-1234567890abcdef1"
                },
                "EfsFilesystemArn": "arn:aws:elasticfilesystem:us-east-2:111222333444:file-system/fs-021345abcdef6789",
                "FileSystemAccessRoleArn": "arn:aws:iam::111222333444:role/AllowDataSyncAccess",
                "InTransitEncryption": "TLS1_2"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-datasync-locationefs--examples--Creating_an_Amazon_EFS_location_with_a_higher_level_of_security--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: Specifies a DataSync location for an Amazon EFS file system configured for restricted access.
Resources:
  LocationEFS:
    Type: AWS::DataSync::LocationEFS
      Properties:
        AccessPointArn: arn:aws:elasticfilesystem:us-east-2:111222333444:access-point/fsap-1234567890abcdef0
        Ec2Config:
          SecurityGroupArns:
            - arn:aws:ec2:us-east-2:11122233344:security-group/sg-1234567890abcdef2
          SubnetArn: arn:aws:ec2:us-east-2:11122233344:subnet/subnet-1234567890abcdef1
        EfsFilesystemArn: arn:aws:elasticfilesystem:us-east-2:111222333444:file-system/fs-021345abcdef6789
        FileSystemAccessRoleArn: arn:aws:iam::111222333444:role/AllowDataSyncAccess
        InTransitEncryption: TLS1_2
```
