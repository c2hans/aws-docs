---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-placementtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster PlacementType
<a name="aws-properties-emr-cluster-placementtype"></a>

`PlacementType` is a property of the `AWS::EMR::Cluster` resource. `PlacementType` determines the Amazon EC2 Availability Zone configuration of the cluster (job flow).

## Syntax
<a name="aws-properties-emr-cluster-placementtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-placementtype-syntax.json"></a>

```
{
  "[AvailabilityZone](#cfn-emr-cluster-placementtype-availabilityzone)" : {{String}}
}
```

### YAML
<a name="aws-properties-emr-cluster-placementtype-syntax.yaml"></a>

```
  [AvailabilityZone](#cfn-emr-cluster-placementtype-availabilityzone): {{String}}
```

## Properties
<a name="aws-properties-emr-cluster-placementtype-properties"></a>

`AvailabilityZone`  <a name="cfn-emr-cluster-placementtype-availabilityzone"></a>
The Amazon EC2 Availability Zone for the cluster. `AvailabilityZone` is used for uniform instance groups, while `AvailabilityZones` (plural) is used for instance fleets.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10280`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
