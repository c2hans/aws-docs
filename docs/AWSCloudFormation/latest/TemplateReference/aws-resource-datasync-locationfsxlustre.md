---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datasync-locationfsxlustre.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationFSxLustre
<a name="aws-resource-datasync-locationfsxlustre"></a>

The `AWS::DataSync::LocationFSxLustre` resource specifies an endpoint for an Amazon FSx for Lustre file system.

## Syntax
<a name="aws-resource-datasync-locationfsxlustre-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datasync-locationfsxlustre-syntax.json"></a>

```
{
  "Type" : "AWS::DataSync::LocationFSxLustre",
  "Properties" : {
      "[FsxFilesystemArn](#cfn-datasync-locationfsxlustre-fsxfilesystemarn)" : {{String}},
      "[SecurityGroupArns](#cfn-datasync-locationfsxlustre-securitygrouparns)" : {{[ String, ... ]}},
      "[Subdirectory](#cfn-datasync-locationfsxlustre-subdirectory)" : {{String}},
      "[Tags](#cfn-datasync-locationfsxlustre-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-datasync-locationfsxlustre-syntax.yaml"></a>

```
Type: AWS::DataSync::LocationFSxLustre
Properties:
  [FsxFilesystemArn](#cfn-datasync-locationfsxlustre-fsxfilesystemarn): {{String}}
  [SecurityGroupArns](#cfn-datasync-locationfsxlustre-securitygrouparns): {{
    - String}}
  [Subdirectory](#cfn-datasync-locationfsxlustre-subdirectory): {{String}}
  [Tags](#cfn-datasync-locationfsxlustre-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-datasync-locationfsxlustre-properties"></a>

`FsxFilesystemArn`  <a name="cfn-datasync-locationfsxlustre-fsxfilesystemarn"></a>
Specifies the Amazon Resource Name (ARN) of the FSx for Lustre file system.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):fsx:[a-z\-0-9]+:[0-9]{12}:file-system/fs-[0-9a-f]+$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupArns`  <a name="cfn-datasync-locationfsxlustre-securitygrouparns"></a>
The ARNs of the security groups that are used to configure the FSx for Lustre file system.
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/.*$`
*Length constraints*: Maximum length of 128.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `128 | 5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Subdirectory`  <a name="cfn-datasync-locationfsxlustre-subdirectory"></a>
Specifies a mount path for your FSx for Lustre file system. The path can include subdirectories.
When the location is used as a source, DataSync reads data from the mount path. When the location is used as a destination, DataSync writes data to the mount path. If you don't include this parameter, DataSync uses the file system's root directory (`/`).
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-datasync-locationfsxlustre-tags"></a>
Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.
*Required*: No
*Type*: Array of [Tag](aws-properties-datasync-locationfsxlustre-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datasync-locationfsxlustre-return-values"></a>

### Ref
<a name="aws-resource-datasync-locationfsxlustre-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the location resource ARN. For example:

 `arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50s3`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datasync-locationfsxlustre-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datasync-locationfsxlustre-return-values-fn--getatt-fn--getatt"></a>

`LocationArn`  <a name="LocationArn-fn::getatt"></a>
The ARN of the specified FSx for Lustre file system location.

`LocationUri`  <a name="LocationUri-fn::getatt"></a>
The URI of the specified FSx for Lustre file system location.

## Examples
<a name="aws-resource-datasync-locationfsxlustre--examples"></a>

### Specify an Amazon FSx for Lustre location for DataSync
<a name="aws-resource-datasync-locationfsxlustre--examples--Specify_an_Amazon_FSx_for_Lustre_location_for_DataSync"></a>

The following examples specify an FSx for Lustre location for DataSync, including the subdirectory `/MySubdirectory`.

#### JSON
<a name="aws-resource-datasync-locationfsxlustre--examples--Specify_an_Amazon_FSx_for_Lustre_location_for_DataSync--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Specifies an FSx for Lustre location for DataSync",
    "Resources": {
        "LocationFSxLustre": {
            "Type": "AWS::DataSync::LocationFSxLustre",
            "Properties": {
                "FsxFilesystemArn": "arn:aws:fsx:us-east-2:111222333444:file-system/fs-12345fsx",
                "SecurityGroupArns": [
                    "arn:aws:ec2:us-east-2:11122233344:security-group/sg-12345678901212345"
                ],
                "Subdirectory": "/MySubdirectory"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-datasync-locationfsxlustre--examples--Specify_an_Amazon_FSx_for_Lustre_location_for_DataSync--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: Specifies an FSx for Lustre location for DataSync
Resources:
  LocationFSxLustre:
    Type: AWS::DataSync::LocationFSxLustre
    Properties:
      FsxFilesystemArn: arn:aws:fsx:us-east-2:111222333444:file-system/fs-12345fsx
      SecurityGroupArns:
        - arn:aws:ec2:us-east-2:11122233344:security-group/sg-12345678901212345
      Subdirectory: /MySubdirectory
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
