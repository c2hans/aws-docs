---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-servicemanagedec2fleetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet ServiceManagedEc2FleetConfiguration
<a name="aws-properties-deadline-fleet-servicemanagedec2fleetconfiguration"></a>

The configuration details for a service managed EC2 fleet.

## Syntax
<a name="aws-properties-deadline-fleet-servicemanagedec2fleetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-servicemanagedec2fleetconfiguration-syntax.json"></a>

```
{
  "[AutoScalingConfiguration](#cfn-deadline-fleet-servicemanagedec2fleetconfiguration-autoscalingconfiguration)" : {{ServiceManagedEc2AutoScalingConfiguration}},
  "[InstanceCapabilities](#cfn-deadline-fleet-servicemanagedec2fleetconfiguration-instancecapabilities)" : {{ServiceManagedEc2InstanceCapabilities}},
  "[InstanceMarketOptions](#cfn-deadline-fleet-servicemanagedec2fleetconfiguration-instancemarketoptions)" : {{ServiceManagedEc2InstanceMarketOptions}},
  "[PersistentVolumeConfiguration](#cfn-deadline-fleet-servicemanagedec2fleetconfiguration-persistentvolumeconfiguration)" : {{PersistentVolumeConfiguration}},
  "[StorageProfileId](#cfn-deadline-fleet-servicemanagedec2fleetconfiguration-storageprofileid)" : {{String}},
  "[VpcConfiguration](#cfn-deadline-fleet-servicemanagedec2fleetconfiguration-vpcconfiguration)" : {{VpcConfiguration}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-servicemanagedec2fleetconfiguration-syntax.yaml"></a>

```
  [AutoScalingConfiguration](#cfn-deadline-fleet-servicemanagedec2fleetconfiguration-autoscalingconfiguration): {{
    ServiceManagedEc2AutoScalingConfiguration}}
  [InstanceCapabilities](#cfn-deadline-fleet-servicemanagedec2fleetconfiguration-instancecapabilities): {{
    ServiceManagedEc2InstanceCapabilities}}
  [InstanceMarketOptions](#cfn-deadline-fleet-servicemanagedec2fleetconfiguration-instancemarketoptions): {{
    ServiceManagedEc2InstanceMarketOptions}}
  [PersistentVolumeConfiguration](#cfn-deadline-fleet-servicemanagedec2fleetconfiguration-persistentvolumeconfiguration): {{
    PersistentVolumeConfiguration}}
  [StorageProfileId](#cfn-deadline-fleet-servicemanagedec2fleetconfiguration-storageprofileid): {{String}}
  [VpcConfiguration](#cfn-deadline-fleet-servicemanagedec2fleetconfiguration-vpcconfiguration): {{
    VpcConfiguration}}
```

## Properties
<a name="aws-properties-deadline-fleet-servicemanagedec2fleetconfiguration-properties"></a>

`AutoScalingConfiguration`  <a name="cfn-deadline-fleet-servicemanagedec2fleetconfiguration-autoscalingconfiguration"></a>
The auto scaling configuration settings for the service managed EC2 fleet.
*Required*: No
*Type*: [ServiceManagedEc2AutoScalingConfiguration](aws-properties-deadline-fleet-servicemanagedec2autoscalingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceCapabilities`  <a name="cfn-deadline-fleet-servicemanagedec2fleetconfiguration-instancecapabilities"></a>
The instance capabilities for the service managed EC2 fleet.
*Required*: Yes
*Type*: [ServiceManagedEc2InstanceCapabilities](aws-properties-deadline-fleet-servicemanagedec2instancecapabilities.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceMarketOptions`  <a name="cfn-deadline-fleet-servicemanagedec2fleetconfiguration-instancemarketoptions"></a>
The instance market options for the service managed EC2 fleet.
*Required*: Yes
*Type*: [ServiceManagedEc2InstanceMarketOptions](aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PersistentVolumeConfiguration`  <a name="cfn-deadline-fleet-servicemanagedec2fleetconfiguration-persistentvolumeconfiguration"></a>
The persistent volume configuration for the service managed EC2 fleet.
*Required*: No
*Type*: [PersistentVolumeConfiguration](aws-properties-deadline-fleet-persistentvolumeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageProfileId`  <a name="cfn-deadline-fleet-servicemanagedec2fleetconfiguration-storageprofileid"></a>
The storage profile ID for the service managed EC2 fleet.
*Required*: No
*Type*: String
*Pattern*: `^sp-[0-9a-f]{32}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcConfiguration`  <a name="cfn-deadline-fleet-servicemanagedec2fleetconfiguration-vpcconfiguration"></a>
The VPC configuration for the service managed EC2 fleet.
*Required*: No
*Type*: [VpcConfiguration](aws-properties-deadline-fleet-vpcconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
