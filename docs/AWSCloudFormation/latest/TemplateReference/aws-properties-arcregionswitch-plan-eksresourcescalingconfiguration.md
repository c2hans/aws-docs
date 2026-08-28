---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-eksresourcescalingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan EksResourceScalingConfiguration
<a name="aws-properties-arcregionswitch-plan-eksresourcescalingconfiguration"></a>

The AWS EKS resource scaling configuration.

## Syntax
<a name="aws-properties-arcregionswitch-plan-eksresourcescalingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-eksresourcescalingconfiguration-syntax.json"></a>

```
{
  "[CapacityMonitoringApproach](#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-capacitymonitoringapproach)" : {{}},
  "[EksClusters](#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-eksclusters)" : {{[ EksCluster, ... ]}},
  "[KubernetesResourceType](#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-kubernetesresourcetype)" : {{KubernetesResourceType}},
  "[ScalingResources](#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-scalingresources)" : {{[ {{{Key}}: {{Value}}, ...}, ... ]}},
  "[TargetPercent](#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-targetpercent)" : {{Number}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-timeoutminutes)" : {{Number}},
  "[Ungraceful](#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-ungraceful)" : {{EksResourceScalingUngraceful}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-eksresourcescalingconfiguration-syntax.yaml"></a>

```
  [CapacityMonitoringApproach](#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-capacitymonitoringapproach): {{
    }}
  [EksClusters](#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-eksclusters): {{
    - EksCluster}}
  [KubernetesResourceType](#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-kubernetesresourcetype): {{
    KubernetesResourceType}}
  [ScalingResources](#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-scalingresources): {{
    -
    {{Key}}: {{Value}}}}
  [TargetPercent](#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-targetpercent): {{Number}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-timeoutminutes): {{Number}}
  [Ungraceful](#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-ungraceful): {{
    EksResourceScalingUngraceful}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-eksresourcescalingconfiguration-properties"></a>

`CapacityMonitoringApproach`  <a name="cfn-arcregionswitch-plan-eksresourcescalingconfiguration-capacitymonitoringapproach"></a>
The monitoring approach for the configuration, that is, whether it was sampled in the last 24 hours or autoscaled in the last 24 hours.
*Required*: No
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EksClusters`  <a name="cfn-arcregionswitch-plan-eksresourcescalingconfiguration-eksclusters"></a>
The clusters for the configuration.
*Required*: No
*Type*: Array of [EksCluster](aws-properties-arcregionswitch-plan-ekscluster.md)
*Minimum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KubernetesResourceType`  <a name="cfn-arcregionswitch-plan-eksresourcescalingconfiguration-kubernetesresourcetype"></a>
The Kubernetes resource type for the configuration.
*Required*: Yes
*Type*: [KubernetesResourceType](aws-properties-arcregionswitch-plan-kubernetesresourcetype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingResources`  <a name="cfn-arcregionswitch-plan-eksresourcescalingconfiguration-scalingresources"></a>
The scaling resources for the configuration.
*Required*: No
*Type*: Array of Object
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetPercent`  <a name="cfn-arcregionswitch-plan-eksresourcescalingconfiguration-targetpercent"></a>
The target percentage for the configuration. The default is 100.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-eksresourcescalingconfiguration-timeoutminutes"></a>
The timeout value specified for the configuration.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ungraceful`  <a name="cfn-arcregionswitch-plan-eksresourcescalingconfiguration-ungraceful"></a>
The settings for ungraceful execution.
*Required*: No
*Type*: [EksResourceScalingUngraceful](aws-properties-arcregionswitch-plan-eksresourcescalingungraceful.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
