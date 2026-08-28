---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lightsail-disksnapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::DiskSnapshot
<a name="aws-resource-lightsail-disksnapshot"></a>

Describes a block storage disk snapshot.

## Syntax
<a name="aws-resource-lightsail-disksnapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lightsail-disksnapshot-syntax.json"></a>

```
{
  "Type" : "AWS::Lightsail::DiskSnapshot",
  "Properties" : {
      "[DiskName](#cfn-lightsail-disksnapshot-diskname)" : {{String}},
      "[DiskSnapshotName](#cfn-lightsail-disksnapshot-disksnapshotname)" : {{String}},
      "[Tags](#cfn-lightsail-disksnapshot-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-lightsail-disksnapshot-syntax.yaml"></a>

```
Type: AWS::Lightsail::DiskSnapshot
Properties:
  [DiskName](#cfn-lightsail-disksnapshot-diskname): {{String}}
  [DiskSnapshotName](#cfn-lightsail-disksnapshot-disksnapshotname): {{String}}
  [Tags](#cfn-lightsail-disksnapshot-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-lightsail-disksnapshot-properties"></a>

`DiskName`  <a name="cfn-lightsail-disksnapshot-diskname"></a>
The unique name of the disk.
*Required*: Yes
*Type*: String
*Pattern*: `^\w[\w\-]*\w$`
*Minimum*: `2`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DiskSnapshotName`  <a name="cfn-lightsail-disksnapshot-disksnapshotname"></a>
The name of the disk snapshot (`my-disk-snapshot`).
*Required*: Yes
*Type*: String
*Pattern*: `^\w[\w\-]*\w$`
*Minimum*: `2`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-lightsail-disksnapshot-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
*Required*: No
*Type*: Array of [Tag](aws-properties-lightsail-disksnapshot-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lightsail-disksnapshot-return-values"></a>

### Ref
<a name="aws-resource-lightsail-disksnapshot-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-lightsail-disksnapshot-return-values-fn--getatt"></a>

####
<a name="aws-resource-lightsail-disksnapshot-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date when the disk snapshot was created.

`DiskSnapshotArn`  <a name="DiskSnapshotArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the disk snapshot.

`FromDiskName`  <a name="FromDiskName-fn::getatt"></a>
The unique name of the source disk from which the disk snapshot was created.

`IsFromAutoSnapshot`  <a name="IsFromAutoSnapshot-fn::getatt"></a>
A Boolean value indicating whether the snapshot was created from an automatic snapshot.

`Progress`  <a name="Progress-fn::getatt"></a>
The progress of the snapshot.

`ResourceType`  <a name="ResourceType-fn::getatt"></a>
The Lightsail resource type (`DiskSnapshot`).

`SizeInGb`  <a name="SizeInGb-fn::getatt"></a>
The size of the disk in GB.

`State`  <a name="State-fn::getatt"></a>
The status of the disk snapshot operation.

`SupportCode`  <a name="SupportCode-fn::getatt"></a>
The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
