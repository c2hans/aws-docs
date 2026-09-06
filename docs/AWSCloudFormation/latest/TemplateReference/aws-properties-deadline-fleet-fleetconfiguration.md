---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-fleetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet FleetConfiguration
<a name="aws-properties-deadline-fleet-fleetconfiguration"></a>

Fleet configuration details.

## Syntax
<a name="aws-properties-deadline-fleet-fleetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-fleetconfiguration-syntax.json"></a>

```
{
  "[CustomerManaged](#cfn-deadline-fleet-fleetconfiguration-customermanaged)" : {{CustomerManagedFleetConfiguration}},
  "[ServiceManagedEc2](#cfn-deadline-fleet-fleetconfiguration-servicemanagedec2)" : {{ServiceManagedEc2FleetConfiguration}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-fleetconfiguration-syntax.yaml"></a>

```
  [CustomerManaged](#cfn-deadline-fleet-fleetconfiguration-customermanaged): {{
    CustomerManagedFleetConfiguration}}
  [ServiceManagedEc2](#cfn-deadline-fleet-fleetconfiguration-servicemanagedec2): {{
    ServiceManagedEc2FleetConfiguration}}
```

## Properties
<a name="aws-properties-deadline-fleet-fleetconfiguration-properties"></a>

`CustomerManaged`  <a name="cfn-deadline-fleet-fleetconfiguration-customermanaged"></a>
The customer managed fleets within a fleet configuration.
*Required*: No
*Type*: [CustomerManagedFleetConfiguration](aws-properties-deadline-fleet-customermanagedfleetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceManagedEc2`  <a name="cfn-deadline-fleet-fleetconfiguration-servicemanagedec2"></a>
The service managed Amazon EC2 instances for a fleet configuration.
*Required*: No
*Type*: [ServiceManagedEc2FleetConfiguration](aws-properties-deadline-fleet-servicemanagedec2fleetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
