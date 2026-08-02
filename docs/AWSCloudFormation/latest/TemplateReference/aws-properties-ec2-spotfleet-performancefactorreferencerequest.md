---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-performancefactorreferencerequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet PerformanceFactorReferenceRequest
<a name="aws-properties-ec2-spotfleet-performancefactorreferencerequest"></a>

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture.

**Note**
Currently, only one instance family can be specified in the list.

## Syntax
<a name="aws-properties-ec2-spotfleet-performancefactorreferencerequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-performancefactorreferencerequest-syntax.json"></a>

```
{
  "[InstanceFamily](#cfn-ec2-spotfleet-performancefactorreferencerequest-instancefamily)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-performancefactorreferencerequest-syntax.yaml"></a>

```
  [InstanceFamily](#cfn-ec2-spotfleet-performancefactorreferencerequest-instancefamily): {{String}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-performancefactorreferencerequest-properties"></a>

`InstanceFamily`  <a name="cfn-ec2-spotfleet-performancefactorreferencerequest-instancefamily"></a>
The instance family to use as a baseline reference.
Ensure that you specify the correct value for the instance family. The instance family is everything before the period (`.`) in the instance type name. For example, in the instance type `c6i.large`, the instance family is `c6i`, not `c6`. For more information, see [Amazon EC2 instance type naming conventions](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html) in *Amazon EC2 Instance Types*.
The following instance families are *not supported* for performance protection:
+  `c1`
+ `g3` \| `g3s`
+  `hpc7g`
+ `m1` \| `m2`
+ `mac1` \| `mac2` \| `mac2-m1ultra` \| `mac2-m2` \| `mac2-m2pro`
+ `p3dn` \| `p4d` \| `p5`
+  `t1`
+ `u-12tb1` \| `u-18tb1` \| `u-24tb1` \| `u-3tb1` \| `u-6tb1` \| `u-9tb1` \| `u7i-12tb` \| `u7in-16tb` \| `u7in-24tb` \| `u7in-32tb`
If you enable performance protection by specifying a supported instance family, the returned instance types will exclude the above unsupported instance families.
If you specify an unsupported instance family as a value for baseline performance, the API returns an empty response for [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) and an exception for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet.html), [RequestSpotFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet.html), [ModifyFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFleet.html), and [ModifySpotFleetRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySpotFleetRequest.html).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
