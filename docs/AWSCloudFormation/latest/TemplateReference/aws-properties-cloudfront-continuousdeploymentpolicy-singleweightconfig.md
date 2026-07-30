---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-continuousdeploymentpolicy-singleweightconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ContinuousDeploymentPolicy SingleWeightConfig
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleweightconfig"></a>

This configuration determines the percentage of HTTP requests that are sent to the staging distribution.

## Syntax
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleweightconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleweightconfig-syntax.json"></a>

```
{
  "[SessionStickinessConfig](#cfn-cloudfront-continuousdeploymentpolicy-singleweightconfig-sessionstickinessconfig)" : {{SessionStickinessConfig}},
  "[Weight](#cfn-cloudfront-continuousdeploymentpolicy-singleweightconfig-weight)" : {{Number}}
}
```

### YAML
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleweightconfig-syntax.yaml"></a>

```
  [SessionStickinessConfig](#cfn-cloudfront-continuousdeploymentpolicy-singleweightconfig-sessionstickinessconfig): {{
    SessionStickinessConfig}}
  [Weight](#cfn-cloudfront-continuousdeploymentpolicy-singleweightconfig-weight): {{Number}}
```

## Properties
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleweightconfig-properties"></a>

`SessionStickinessConfig`  <a name="cfn-cloudfront-continuousdeploymentpolicy-singleweightconfig-sessionstickinessconfig"></a>
Session stickiness provides the ability to define multiple requests from a single viewer as a single session. This prevents the potentially inconsistent experience of sending some of a given user's requests to your staging distribution, while others are sent to your primary distribution. Define the session duration using TTL values.
*Required*: No
*Type*: [SessionStickinessConfig](aws-properties-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-cloudfront-continuousdeploymentpolicy-singleweightconfig-weight"></a>
The percentage of traffic to send to a staging distribution, expressed as a decimal number between 0 and 0.15. For example, a value of 0.10 means 10% of traffic is sent to the staging distribution.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
