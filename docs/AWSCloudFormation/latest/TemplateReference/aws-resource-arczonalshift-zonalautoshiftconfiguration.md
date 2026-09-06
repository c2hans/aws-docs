---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-arczonalshift-zonalautoshiftconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCZonalShift::ZonalAutoshiftConfiguration
<a name="aws-resource-arczonalshift-zonalautoshiftconfiguration"></a>

The zonal autoshift configuration for a resource includes the practice run configuration and the status for running autoshifts, zonal autoshift status. When a resource has a practice run configuation, ARC starts weekly zonal shifts for the resource, to shift traffic away from an Availability Zone. Weekly practice runs help you to make sure that your application can continue to operate normally with the loss of one Availability Zone.

You can update the zonal autoshift autoshift status to enable or disable zonal autoshift. When zonal autoshift is `ENABLED`, you authorize AWS to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery. Traffic is also shifted away for the required weekly practice runs.

## Syntax
<a name="aws-resource-arczonalshift-zonalautoshiftconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-arczonalshift-zonalautoshiftconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::ARCZonalShift::ZonalAutoshiftConfiguration",
  "Properties" : {
      "[PracticeRunConfiguration](#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration)" : {{PracticeRunConfiguration}},
      "[ResourceIdentifier](#cfn-arczonalshift-zonalautoshiftconfiguration-resourceidentifier)" : {{String}},
      "[ZonalAutoshiftStatus](#cfn-arczonalshift-zonalautoshiftconfiguration-zonalautoshiftstatus)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-arczonalshift-zonalautoshiftconfiguration-syntax.yaml"></a>

```
Type: AWS::ARCZonalShift::ZonalAutoshiftConfiguration
Properties:
  [PracticeRunConfiguration](#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration): {{
    PracticeRunConfiguration}}
  [ResourceIdentifier](#cfn-arczonalshift-zonalautoshiftconfiguration-resourceidentifier): {{String}}
  [ZonalAutoshiftStatus](#cfn-arczonalshift-zonalautoshiftconfiguration-zonalautoshiftstatus): {{String}}
```

## Properties
<a name="aws-resource-arczonalshift-zonalautoshiftconfiguration-properties"></a>

`PracticeRunConfiguration`  <a name="cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration"></a>
A practice run configuration for a resource includes the Amazon CloudWatch alarms that you've specified for a practice run, as well as any blocked dates or blocked windows for the practice run. When a resource has a practice run configuration, ARC shifts traffic for the resource weekly for practice runs.
Practice runs are required for zonal autoshift. The zonal shifts that ARC starts for practice runs help you to ensure that shifting away traffic from an Availability Zone during an autoshift is safe for your application.
You can update or delete a practice run configuration. Before you delete a practice run configuration, you must disable zonal autoshift for the resource. A practice run configuration is required when zonal autoshift is enabled.
*Required*: No
*Type*: [PracticeRunConfiguration](aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceIdentifier`  <a name="cfn-arczonalshift-zonalautoshiftconfiguration-resourceidentifier"></a>
The identifier for the resource that AWS shifts traffic for. The identifier is the Amazon Resource Name (ARN) for the resource.
At this time, supported resources are Network Load Balancers and Application Load Balancers.
*Required*: No
*Type*: String
*Minimum*: `8`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ZonalAutoshiftStatus`  <a name="cfn-arczonalshift-zonalautoshiftconfiguration-zonalautoshiftstatus"></a>
When zonal autoshift is `ENABLED`, you authorize AWS to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery. Traffic is also shifted away for the required weekly practice runs.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-arczonalshift-zonalautoshiftconfiguration-return-values"></a>

### Ref
<a name="aws-resource-arczonalshift-zonalautoshiftconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the resource.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).
