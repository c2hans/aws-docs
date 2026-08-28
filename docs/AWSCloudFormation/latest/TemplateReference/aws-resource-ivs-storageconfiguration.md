---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ivs-storageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::StorageConfiguration
<a name="aws-resource-ivs-storageconfiguration"></a>

The `AWS::IVS::StorageConfiguration` resource specifies an Amazon IVS storage configuration. A storage configuration describes an S3 location where recorded videos will be stored. For more information, see [Auto-Record to Amazon S3 (Low-Latency Streaming)](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/record-to-s3.html) in the *Amazon IVS Low-Latency Streaming User Guide*.

## Syntax
<a name="aws-resource-ivs-storageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ivs-storageconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::IVS::StorageConfiguration",
  "Properties" : {
      "[Name](#cfn-ivs-storageconfiguration-name)" : {{String}},
      "[S3](#cfn-ivs-storageconfiguration-s3)" : {{S3StorageConfiguration}},
      "[Tags](#cfn-ivs-storageconfiguration-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ivs-storageconfiguration-syntax.yaml"></a>

```
Type: AWS::IVS::StorageConfiguration
Properties:
  [Name](#cfn-ivs-storageconfiguration-name): {{String}}
  [S3](#cfn-ivs-storageconfiguration-s3): {{
    S3StorageConfiguration}}
  [Tags](#cfn-ivs-storageconfiguration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ivs-storageconfiguration-properties"></a>

`Name`  <a name="cfn-ivs-storageconfiguration-name"></a>
Storage cnfiguration name.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]*$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3`  <a name="cfn-ivs-storageconfiguration-s3"></a>
An S3 storage configuration contains information about where recorded video will be stored. See the [S3StorageConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-storageconfiguration-s3storageconfiguration.html) property type for more information.
*Required*: Yes
*Type*: [S3StorageConfiguration](aws-properties-ivs-storageconfiguration-s3storageconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ivs-storageconfiguration-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-storageconfiguration-tag.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-ivs-storageconfiguration-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ivs-storageconfiguration-return-values"></a>

### Ref
<a name="aws-resource-ivs-storageconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the storage-configuration ARN. For example:

 `{ "Ref": "myStorageConfiguration" }`

For the Amazon IVS storage configuration `"myStorageConfiguration"`, `Ref` returns the storage-configuration ARN.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ivs-storageconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ivs-storageconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The storage-configuration ARN. For example: `arn:aws:ivs:us-west-2:123456789012:storage-configuration/abcdABCDefgh`

## Examples
<a name="aws-resource-ivs-storageconfiguration--examples"></a>

### StorageConfiguration Template Examples
<a name="aws-resource-ivs-storageconfiguration--examples--StorageConfiguration_Template_Examples"></a>

The following examples specify an Amazon IVS storage configuration.

#### JSON
<a name="aws-resource-ivs-storageconfiguration--examples--StorageConfiguration_Template_Examples--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "StorageConfiguration": {
            "Type": "AWS::IVS::StorageConfiguration",
            "Properties": {
                "Name": "myStorageConfiguration",
                "S3": { "BucketName": "my-bucket" },
                "Tags": [
                    {
                        "Key": "MyKey",
                        "Value": "MyValue"
                    }
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-ivs-storageconfiguration--examples--StorageConfiguration_Template_Examples--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  StorageConfiguration:
    Type: AWS::IVS::StorageConfiguration
    Properties:
      Name: myStorageConfiguration
      S3:
        BucketName: my-bucket
      Tags:
        - Key: myKey
          Value: myValue
```

## See also
<a name="aws-resource-ivs-storageconfiguration--seealso"></a>
+  [Getting Started with IVS Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started.html)
+  [ Server-Side Composition (Real-Time Streaming)](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/server-side-composition.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
