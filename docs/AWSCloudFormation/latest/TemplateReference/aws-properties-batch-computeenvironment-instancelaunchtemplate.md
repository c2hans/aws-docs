---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-instancelaunchtemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment InstanceLaunchTemplate
<a name="aws-properties-batch-computeenvironment-instancelaunchtemplate"></a>

<a name="aws-properties-batch-computeenvironment-instancelaunchtemplate-description"></a>The `InstanceLaunchTemplate` property type specifies Property description not available. for an [AWS::Batch::ComputeEnvironment](aws-resource-batch-computeenvironment.md).

## Syntax
<a name="aws-properties-batch-computeenvironment-instancelaunchtemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-instancelaunchtemplate-syntax.json"></a>

```
{
  "[CapacityOptionType](#cfn-batch-computeenvironment-instancelaunchtemplate-capacityoptiontype)" : {{String}},
  "[CapacityReservations](#cfn-batch-computeenvironment-instancelaunchtemplate-capacityreservations)" : {{CapacityReservations}},
  "[Ec2InstanceProfileArn](#cfn-batch-computeenvironment-instancelaunchtemplate-ec2instanceprofilearn)" : {{String}},
  "[FipsEnabled](#cfn-batch-computeenvironment-instancelaunchtemplate-fipsenabled)" : {{Boolean}},
  "[InstanceMetadataTagsPropagation](#cfn-batch-computeenvironment-instancelaunchtemplate-instancemetadatatagspropagation)" : {{Boolean}},
  "[InstanceRequirements](#cfn-batch-computeenvironment-instancelaunchtemplate-instancerequirements)" : {{InstanceRequirements}},
  "[LocalStorageConfiguration](#cfn-batch-computeenvironment-instancelaunchtemplate-localstorageconfiguration)" : {{ManagedInstancesLocalStorageConfiguration}},
  "[Monitoring](#cfn-batch-computeenvironment-instancelaunchtemplate-monitoring)" : {{String}},
  "[NetworkConfiguration](#cfn-batch-computeenvironment-instancelaunchtemplate-networkconfiguration)" : {{ManagedInstancesNetworkConfiguration}},
  "[StorageConfiguration](#cfn-batch-computeenvironment-instancelaunchtemplate-storageconfiguration)" : {{ManagedInstancesStorageConfiguration}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-instancelaunchtemplate-syntax.yaml"></a>

```
  [CapacityOptionType](#cfn-batch-computeenvironment-instancelaunchtemplate-capacityoptiontype): {{String}}
  [CapacityReservations](#cfn-batch-computeenvironment-instancelaunchtemplate-capacityreservations): {{
    CapacityReservations}}
  [Ec2InstanceProfileArn](#cfn-batch-computeenvironment-instancelaunchtemplate-ec2instanceprofilearn): {{String}}
  [FipsEnabled](#cfn-batch-computeenvironment-instancelaunchtemplate-fipsenabled): {{Boolean}}
  [InstanceMetadataTagsPropagation](#cfn-batch-computeenvironment-instancelaunchtemplate-instancemetadatatagspropagation): {{Boolean}}
  [InstanceRequirements](#cfn-batch-computeenvironment-instancelaunchtemplate-instancerequirements): {{
    InstanceRequirements}}
  [LocalStorageConfiguration](#cfn-batch-computeenvironment-instancelaunchtemplate-localstorageconfiguration): {{
    ManagedInstancesLocalStorageConfiguration}}
  [Monitoring](#cfn-batch-computeenvironment-instancelaunchtemplate-monitoring): {{String}}
  [NetworkConfiguration](#cfn-batch-computeenvironment-instancelaunchtemplate-networkconfiguration): {{
    ManagedInstancesNetworkConfiguration}}
  [StorageConfiguration](#cfn-batch-computeenvironment-instancelaunchtemplate-storageconfiguration): {{
    ManagedInstancesStorageConfiguration}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-instancelaunchtemplate-properties"></a>

`CapacityOptionType`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-capacityoptiontype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `ON_DEMAND | SPOT | RESERVED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CapacityReservations`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-capacityreservations"></a>
Property description not available.
*Required*: No
*Type*: [CapacityReservations](aws-properties-batch-computeenvironment-capacityreservations.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ec2InstanceProfileArn`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-ec2instanceprofilearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FipsEnabled`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-fipsenabled"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceMetadataTagsPropagation`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-instancemetadatatagspropagation"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceRequirements`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-instancerequirements"></a>
Property description not available.
*Required*: No
*Type*: [InstanceRequirements](aws-properties-batch-computeenvironment-instancerequirements.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalStorageConfiguration`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-localstorageconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [ManagedInstancesLocalStorageConfiguration](aws-properties-batch-computeenvironment-managedinstanceslocalstorageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Monitoring`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-monitoring"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkConfiguration`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-networkconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [ManagedInstancesNetworkConfiguration](aws-properties-batch-computeenvironment-managedinstancesnetworkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageConfiguration`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-storageconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [ManagedInstancesStorageConfiguration](aws-properties-batch-computeenvironment-managedinstancesstorageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
