---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-exportsnapshotrecord-resourcelocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::ExportSnapshotRecord ResourceLocation
<a name="aws-properties-lightsail-exportsnapshotrecord-resourcelocation"></a>

Describes the resource location.

## Syntax
<a name="aws-properties-lightsail-exportsnapshotrecord-resourcelocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-exportsnapshotrecord-resourcelocation-syntax.json"></a>

```
{
  "[AvailabilityZone](#cfn-lightsail-exportsnapshotrecord-resourcelocation-availabilityzone)" : {{String}},
  "[RegionName](#cfn-lightsail-exportsnapshotrecord-resourcelocation-regionname)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-exportsnapshotrecord-resourcelocation-syntax.yaml"></a>

```
  [AvailabilityZone](#cfn-lightsail-exportsnapshotrecord-resourcelocation-availabilityzone): {{String}}
  [RegionName](#cfn-lightsail-exportsnapshotrecord-resourcelocation-regionname): {{String}}
```

## Properties
<a name="aws-properties-lightsail-exportsnapshotrecord-resourcelocation-properties"></a>

`AvailabilityZone`  <a name="cfn-lightsail-exportsnapshotrecord-resourcelocation-availabilityzone"></a>
The Availability Zone. Follows the format `us-east-2a` (case-sensitive).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionName`  <a name="cfn-lightsail-exportsnapshotrecord-resourcelocation-regionname"></a>
The AWS Region name.
*Required*: No
*Type*: String
*Allowed values*: `us-east-1 | us-east-2 | us-west-1 | us-west-2 | eu-west-1 | eu-west-2 | eu-west-3 | eu-central-1 | eu-north-1 | ca-central-1 | ap-south-1 | ap-southeast-1 | ap-southeast-2 | ap-northeast-1 | ap-northeast-2 | ap-southeast-3 | ap-southeast-5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
