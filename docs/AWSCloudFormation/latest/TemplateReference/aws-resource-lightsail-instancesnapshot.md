---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lightsail-instancesnapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::InstanceSnapshot
<a name="aws-resource-lightsail-instancesnapshot"></a>

Describes an instance snapshot.

## Syntax
<a name="aws-resource-lightsail-instancesnapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lightsail-instancesnapshot-syntax.json"></a>

```
{
  "Type" : "AWS::Lightsail::InstanceSnapshot",
  "Properties" : {
      "[InstanceName](#cfn-lightsail-instancesnapshot-instancename)" : {{String}},
      "[InstanceSnapshotName](#cfn-lightsail-instancesnapshot-instancesnapshotname)" : {{String}},
      "[Tags](#cfn-lightsail-instancesnapshot-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-lightsail-instancesnapshot-syntax.yaml"></a>

```
Type: AWS::Lightsail::InstanceSnapshot
Properties:
  [InstanceName](#cfn-lightsail-instancesnapshot-instancename): {{String}}
  [InstanceSnapshotName](#cfn-lightsail-instancesnapshot-instancesnapshotname): {{String}}
  [Tags](#cfn-lightsail-instancesnapshot-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-lightsail-instancesnapshot-properties"></a>

`InstanceName`  <a name="cfn-lightsail-instancesnapshot-instancename"></a>
The name the user gave the instance (`Amazon_Linux_2023-1`).
*Required*: Yes
*Type*: String
*Pattern*: `\w[\w\-]*\w`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceSnapshotName`  <a name="cfn-lightsail-instancesnapshot-instancesnapshotname"></a>
The name of the snapshot.
*Required*: Yes
*Type*: String
*Pattern*: `\w[\w\-]*\w`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-lightsail-instancesnapshot-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
*Required*: No
*Type*: Array of [Tag](aws-properties-lightsail-instancesnapshot-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lightsail-instancesnapshot-return-values"></a>

### Ref
<a name="aws-resource-lightsail-instancesnapshot-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-lightsail-instancesnapshot-return-values-fn--getatt"></a>

####
<a name="aws-resource-lightsail-instancesnapshot-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the snapshot (`arn:aws:lightsail:us-east-2:123456789101:InstanceSnapshot/d23b5706-3322-4d83-81e5-12345EXAMPLE`).

`FromInstanceArn`  <a name="FromInstanceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the instance from which the snapshot was created (`arn:aws:lightsail:us-east-2:123456789101:Instance/64b8404c-ccb1-430b-8daf-12345EXAMPLE`).

`FromInstanceName`  <a name="FromInstanceName-fn::getatt"></a>
The instance from which the snapshot was created.

`IsFromAutoSnapshot`  <a name="IsFromAutoSnapshot-fn::getatt"></a>
A Boolean value indicating whether the snapshot was created from an automatic snapshot.

`ResourceType`  <a name="ResourceType-fn::getatt"></a>
The type of resource (usually `InstanceSnapshot`).

`SizeInGb`  <a name="SizeInGb-fn::getatt"></a>
The size in GB of the SSD.

`State`  <a name="State-fn::getatt"></a>
The state the snapshot is in.

`SupportCode`  <a name="SupportCode-fn::getatt"></a>
The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
