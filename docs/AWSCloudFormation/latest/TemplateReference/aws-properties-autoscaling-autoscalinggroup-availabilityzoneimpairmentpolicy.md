---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-availabilityzoneimpairmentpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup AvailabilityZoneImpairmentPolicy
<a name="aws-properties-autoscaling-autoscalinggroup-availabilityzoneimpairmentpolicy"></a>

 Describes an Availability Zone impairment policy.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-availabilityzoneimpairmentpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-availabilityzoneimpairmentpolicy-syntax.json"></a>

```
{
  "[ImpairedZoneHealthCheckBehavior](#cfn-autoscaling-autoscalinggroup-availabilityzoneimpairmentpolicy-impairedzonehealthcheckbehavior)" : {{String}},
  "[ZonalShiftEnabled](#cfn-autoscaling-autoscalinggroup-availabilityzoneimpairmentpolicy-zonalshiftenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-availabilityzoneimpairmentpolicy-syntax.yaml"></a>

```
  [ImpairedZoneHealthCheckBehavior](#cfn-autoscaling-autoscalinggroup-availabilityzoneimpairmentpolicy-impairedzonehealthcheckbehavior): {{String}}
  [ZonalShiftEnabled](#cfn-autoscaling-autoscalinggroup-availabilityzoneimpairmentpolicy-zonalshiftenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-availabilityzoneimpairmentpolicy-properties"></a>

`ImpairedZoneHealthCheckBehavior`  <a name="cfn-autoscaling-autoscalinggroup-availabilityzoneimpairmentpolicy-impairedzonehealthcheckbehavior"></a>
 Specifies the health check behavior for the impaired Availability Zone in an active zonal shift. If you select `Replace unhealthy`, instances that appear unhealthy will be replaced in all Availability Zones. If you select `Ignore unhealthy`, instances will not be replaced in the Availability Zone with the active zonal shift. For more information, see [Auto Scaling group zonal shift](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html) in the *Amazon EC2 Auto Scaling User Guide*.
*Required*: Yes
*Type*: String
*Allowed values*: `IgnoreUnhealthy | ReplaceUnhealthy`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ZonalShiftEnabled`  <a name="cfn-autoscaling-autoscalinggroup-availabilityzoneimpairmentpolicy-zonalshiftenabled"></a>
 If `true`, enable zonal shift for your Auto Scaling group.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
