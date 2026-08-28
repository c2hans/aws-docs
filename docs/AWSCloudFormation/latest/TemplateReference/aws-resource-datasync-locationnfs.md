---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datasync-locationnfs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationNFS
<a name="aws-resource-datasync-locationnfs"></a>

The `AWS::DataSync::LocationNFS` resource specifies a Network File System (NFS) file server that AWS DataSync can use as a transfer source or destination.

## Syntax
<a name="aws-resource-datasync-locationnfs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datasync-locationnfs-syntax.json"></a>

```
{
  "Type" : "AWS::DataSync::LocationNFS",
  "Properties" : {
      "[MountOptions](#cfn-datasync-locationnfs-mountoptions)" : {{MountOptions}},
      "[OnPremConfig](#cfn-datasync-locationnfs-onpremconfig)" : {{OnPremConfig}},
      "[ServerHostname](#cfn-datasync-locationnfs-serverhostname)" : {{String}},
      "[Subdirectory](#cfn-datasync-locationnfs-subdirectory)" : {{String}},
      "[Tags](#cfn-datasync-locationnfs-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-datasync-locationnfs-syntax.yaml"></a>

```
Type: AWS::DataSync::LocationNFS
Properties:
  [MountOptions](#cfn-datasync-locationnfs-mountoptions): {{
    MountOptions}}
  [OnPremConfig](#cfn-datasync-locationnfs-onpremconfig): {{
    OnPremConfig}}
  [ServerHostname](#cfn-datasync-locationnfs-serverhostname): {{String}}
  [Subdirectory](#cfn-datasync-locationnfs-subdirectory): {{String}}
  [Tags](#cfn-datasync-locationnfs-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-datasync-locationnfs-properties"></a>

`MountOptions`  <a name="cfn-datasync-locationnfs-mountoptions"></a>
Specifies the options that DataSync can use to mount your NFS file server.
*Required*: No
*Type*: [MountOptions](aws-properties-datasync-locationnfs-mountoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnPremConfig`  <a name="cfn-datasync-locationnfs-onpremconfig"></a>
Specifies the Amazon Resource Name (ARN) of the DataSync agent that can connect to your NFS file server.
You can specify more than one agent. For more information, see [Using multiple DataSync agents](https://docs.aws.amazon.com/datasync/latest/userguide/do-i-need-datasync-agent.html#multiple-agents).
*Required*: Yes
*Type*: [OnPremConfig](aws-properties-datasync-locationnfs-onpremconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerHostname`  <a name="cfn-datasync-locationnfs-serverhostname"></a>
Specifies the DNS name or IP address (IPv4 or IPv6) of the NFS file server that your DataSync agent connects to.
*Required*: No
*Type*: String
*Pattern*: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])$`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subdirectory`  <a name="cfn-datasync-locationnfs-subdirectory"></a>
Specifies the export path in your NFS file server that you want DataSync to mount.
This path (or a subdirectory of the path) is where DataSync transfers data to or from. For information on configuring an export for DataSync, see [Accessing NFS file servers](https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html#accessing-nfs).
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-datasync-locationnfs-tags"></a>
Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.
*Required*: No
*Type*: Array of [Tag](aws-properties-datasync-locationnfs-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datasync-locationnfs-return-values"></a>

### Ref
<a name="aws-resource-datasync-locationnfs-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the location resource ARN. For example:

 `arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50s3`

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datasync-locationnfs-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datasync-locationnfs-return-values-fn--getatt-fn--getatt"></a>

`LocationArn`  <a name="LocationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the NFS location that you created.

`LocationUri`  <a name="LocationUri-fn::getatt"></a>
The URI of the NFS location that you created.

## Examples
<a name="aws-resource-datasync-locationnfs--examples"></a>

### Create an NFS location for DataSync
<a name="aws-resource-datasync-locationnfs--examples--Create_an_NFS_location_for_DataSync"></a>

The following example specifies an NFS location for DataSync, using a source and destination location. In this example, the server hostname is `MyServer@example.com`, using NFS version 4.0, in the subdirectory `/MySubdirectory`.

#### JSON
<a name="aws-resource-datasync-locationnfs--examples--Create_an_NFS_location_for_DataSync--json"></a>

```
{
    "Resources": {
        "LocationNFS": {
            "Type": "AWS::DataSync::LocationNFS",
            "Properties": {
                "MountOptions": {
                    "Version": "NFS4_0"
                },
                "OnPremConfig": {
                    "AgentArns": [
                        "arn:aws:datasync:us-east-2:111222333444:agent/agent-000addbcdf44bbnfs"
                    ]
                },
                "ServerHostname": "MyServer@example.com",
                "Subdirectory": "/MySubdirectory"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-datasync-locationnfs--examples--Create_an_NFS_location_for_DataSync--yaml"></a>

```
Resources:
  LocationNFS:
    Type: 'AWS::DataSync::LocationNFS'
    Properties:
      MountOptions:
        Version: NFS4_0
      OnPremConfig:
        AgentArns:
          - >-
            arn:aws:datasync:us-east-2:111222333444:agent/agent-000addbcdf44bbnfs
      ServerHostname: MyServer@example.com
      Subdirectory: /MySubdirectory
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
