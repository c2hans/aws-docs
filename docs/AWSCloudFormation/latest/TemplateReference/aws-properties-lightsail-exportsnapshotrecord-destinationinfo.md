---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-exportsnapshotrecord-destinationinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::ExportSnapshotRecord DestinationInfo
<a name="aws-properties-lightsail-exportsnapshotrecord-destinationinfo"></a>

Describes the destination of a record.

## Syntax
<a name="aws-properties-lightsail-exportsnapshotrecord-destinationinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-exportsnapshotrecord-destinationinfo-syntax.json"></a>

```
{
  "[Id](#cfn-lightsail-exportsnapshotrecord-destinationinfo-id)" : {{String}},
  "[Service](#cfn-lightsail-exportsnapshotrecord-destinationinfo-service)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-exportsnapshotrecord-destinationinfo-syntax.yaml"></a>

```
  [Id](#cfn-lightsail-exportsnapshotrecord-destinationinfo-id): {{String}}
  [Service](#cfn-lightsail-exportsnapshotrecord-destinationinfo-service): {{String}}
```

## Properties
<a name="aws-properties-lightsail-exportsnapshotrecord-destinationinfo-properties"></a>

`Id`  <a name="cfn-lightsail-exportsnapshotrecord-destinationinfo-id"></a>
The ID of the resource created at the destination.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Service`  <a name="cfn-lightsail-exportsnapshotrecord-destinationinfo-service"></a>
The destination service of the record.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
