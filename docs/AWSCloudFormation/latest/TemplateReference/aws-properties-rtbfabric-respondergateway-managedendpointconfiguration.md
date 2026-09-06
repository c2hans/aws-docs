---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-respondergateway-managedendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::ResponderGateway ManagedEndpointConfiguration
<a name="aws-properties-rtbfabric-respondergateway-managedendpointconfiguration"></a>

Describes the configuration of a managed endpoint.

## Syntax
<a name="aws-properties-rtbfabric-respondergateway-managedendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-respondergateway-managedendpointconfiguration-syntax.json"></a>

```
{
  "[AutoScalingGroupsConfiguration](#cfn-rtbfabric-respondergateway-managedendpointconfiguration-autoscalinggroupsconfiguration)" : {{AutoScalingGroupsConfiguration}},
  "[EksEndpointsConfiguration](#cfn-rtbfabric-respondergateway-managedendpointconfiguration-eksendpointsconfiguration)" : {{EksEndpointsConfiguration}}
}
```

### YAML
<a name="aws-properties-rtbfabric-respondergateway-managedendpointconfiguration-syntax.yaml"></a>

```
  [AutoScalingGroupsConfiguration](#cfn-rtbfabric-respondergateway-managedendpointconfiguration-autoscalinggroupsconfiguration): {{
    AutoScalingGroupsConfiguration}}
  [EksEndpointsConfiguration](#cfn-rtbfabric-respondergateway-managedendpointconfiguration-eksendpointsconfiguration): {{
    EksEndpointsConfiguration}}
```

## Properties
<a name="aws-properties-rtbfabric-respondergateway-managedendpointconfiguration-properties"></a>

`AutoScalingGroupsConfiguration`  <a name="cfn-rtbfabric-respondergateway-managedendpointconfiguration-autoscalinggroupsconfiguration"></a>
Describes the configuration of an auto scaling group.
*Required*: No
*Type*: [AutoScalingGroupsConfiguration](aws-properties-rtbfabric-respondergateway-autoscalinggroupsconfiguration.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`EksEndpointsConfiguration`  <a name="cfn-rtbfabric-respondergateway-managedendpointconfiguration-eksendpointsconfiguration"></a>
Describes the configuration of an Amazon Elastic Kubernetes Service endpoint.
*Required*: No
*Type*: [EksEndpointsConfiguration](aws-properties-rtbfabric-respondergateway-eksendpointsconfiguration.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
