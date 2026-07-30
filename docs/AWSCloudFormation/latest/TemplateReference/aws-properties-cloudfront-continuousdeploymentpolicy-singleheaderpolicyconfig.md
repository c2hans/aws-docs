---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ContinuousDeploymentPolicy SingleHeaderPolicyConfig
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig"></a>

Defines a single header policy for a CloudFront distribution.

**Note**
This property is legacy. We recommend that you use [TrafficConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-trafficconfig.html) and specify the [SingleHeaderConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-trafficconfig.html#cfn-cloudfront-continuousdeploymentpolicy-trafficconfig-singleheaderconfig) property instead.

## Syntax
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig-syntax.json"></a>

```
{
  "[Header](#cfn-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig-header)" : {{String}},
  "[Value](#cfn-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig-syntax.yaml"></a>

```
  [Header](#cfn-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig-header): {{String}}
  [Value](#cfn-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig-value): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig-properties"></a>

`Header`  <a name="cfn-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig-header"></a>
The name of the HTTP header that CloudFront uses to configure for the single header policy.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig-value"></a>
Specifies the value to assign to the header for a single header policy.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1783`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
