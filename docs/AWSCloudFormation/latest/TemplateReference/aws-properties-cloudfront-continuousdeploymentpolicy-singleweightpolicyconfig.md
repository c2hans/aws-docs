---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ContinuousDeploymentPolicy SingleWeightPolicyConfig
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig"></a>

Configure a policy that CloudFront uses to route requests to different origins or use different cache settings, based on the weight assigned to each option.

**Note**
This property is legacy. We recommend that you use [TrafficConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-trafficconfig.html) and specify the [SingleWeightConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-trafficconfig.html#cfn-cloudfront-continuousdeploymentpolicy-trafficconfig-singleweightconfig) property instead.

## Syntax
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig-syntax.json"></a>

```
{
  "[SessionStickinessConfig](#cfn-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig-sessionstickinessconfig)" : {{SessionStickinessConfig}},
  "[Weight](#cfn-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig-weight)" : {{Number}}
}
```

### YAML
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig-syntax.yaml"></a>

```
  [SessionStickinessConfig](#cfn-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig-sessionstickinessconfig): {{
    SessionStickinessConfig}}
  [Weight](#cfn-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig-weight): {{Number}}
```

## Properties
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig-properties"></a>

`SessionStickinessConfig`  <a name="cfn-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig-sessionstickinessconfig"></a>
Enable session stickiness for the associated origin or cache settings.
*Required*: No
*Type*: [SessionStickinessConfig](aws-properties-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig-weight"></a>
The percentage of requests that CloudFront will use to send to an associated origin or cache settings.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
