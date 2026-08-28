---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentconfig-zonalconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentConfig ZonalConfig
<a name="aws-properties-codedeploy-deploymentconfig-zonalconfig"></a>

Configure the `ZonalConfig` object if you want AWS CodeDeploy to deploy your application to one [Availability Zone](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones) at a time, within an AWS Region. By deploying to one Availability Zone at a time, you can expose your deployment to a progressively larger audience as confidence in the deployment's performance and viability grows. If you don't configure the `ZonalConfig` object, CodeDeploy deploys your application to a random selection of hosts across a Region.

For more information about the zonal configuration feature, see [zonal configuration](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config) in the *CodeDeploy User Guide*.

## Syntax
<a name="aws-properties-codedeploy-deploymentconfig-zonalconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentconfig-zonalconfig-syntax.json"></a>

```
{
  "[FirstZoneMonitorDurationInSeconds](#cfn-codedeploy-deploymentconfig-zonalconfig-firstzonemonitordurationinseconds)" : {{Integer}},
  "[MinimumHealthyHostsPerZone](#cfn-codedeploy-deploymentconfig-zonalconfig-minimumhealthyhostsperzone)" : {{MinimumHealthyHostsPerZone}},
  "[MonitorDurationInSeconds](#cfn-codedeploy-deploymentconfig-zonalconfig-monitordurationinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentconfig-zonalconfig-syntax.yaml"></a>

```
  [FirstZoneMonitorDurationInSeconds](#cfn-codedeploy-deploymentconfig-zonalconfig-firstzonemonitordurationinseconds): {{Integer}}
  [MinimumHealthyHostsPerZone](#cfn-codedeploy-deploymentconfig-zonalconfig-minimumhealthyhostsperzone): {{
    MinimumHealthyHostsPerZone}}
  [MonitorDurationInSeconds](#cfn-codedeploy-deploymentconfig-zonalconfig-monitordurationinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentconfig-zonalconfig-properties"></a>

`FirstZoneMonitorDurationInSeconds`  <a name="cfn-codedeploy-deploymentconfig-zonalconfig-firstzonemonitordurationinseconds"></a>
The period of time, in seconds, that CodeDeploy must wait after completing a deployment to the *first* Availability Zone. CodeDeploy will wait this amount of time before starting a deployment to the second Availability Zone. You might set this option if you want to allow extra bake time for the first Availability Zone. If you don't specify a value for `firstZoneMonitorDurationInSeconds`, then CodeDeploy uses the `monitorDurationInSeconds` value for the first Availability Zone.
For more information about the zonal configuration feature, see [zonal configuration](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config) in the *CodeDeploy User Guide*.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinimumHealthyHostsPerZone`  <a name="cfn-codedeploy-deploymentconfig-zonalconfig-minimumhealthyhostsperzone"></a>
The number or percentage of instances that must remain available per Availability Zone during a deployment. This option works in conjunction with the `MinimumHealthyHosts` option. For more information, see [About the minimum number of healthy hosts per Availability Zone](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html#minimum-healthy-hosts-az) in the *CodeDeploy User Guide*.
If you don't specify the `minimumHealthyHostsPerZone` option, then CodeDeploy uses a default value of `0` percent.
For more information about the zonal configuration feature, see [zonal configuration](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config) in the *CodeDeploy User Guide*.
*Required*: No
*Type*: [MinimumHealthyHostsPerZone](aws-properties-codedeploy-deploymentconfig-minimumhealthyhostsperzone.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MonitorDurationInSeconds`  <a name="cfn-codedeploy-deploymentconfig-zonalconfig-monitordurationinseconds"></a>
The period of time, in seconds, that CodeDeploy must wait after completing a deployment to an Availability Zone. CodeDeploy will wait this amount of time before starting a deployment to the next Availability Zone. Consider adding a monitor duration to give the deployment some time to prove itself (or 'bake') in one Availability Zone before it is released in the next zone. If you don't specify a `monitorDurationInSeconds`, CodeDeploy starts deploying to the next Availability Zone immediately.
For more information about the zonal configuration feature, see [zonal configuration](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config) in the *CodeDeploy User Guide*.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
