---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionendpoint-scalingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunctionEndpoint ScalingConfig
<a name="aws-properties-lambda-webfunctionendpoint-scalingconfig"></a>

The scaling configuration for a web function endpoint.

## Syntax
<a name="aws-properties-lambda-webfunctionendpoint-scalingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-webfunctionendpoint-scalingconfig-syntax.json"></a>

```
{
  "[MaxEnvironments](#cfn-lambda-webfunctionendpoint-scalingconfig-maxenvironments)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-webfunctionendpoint-scalingconfig-syntax.yaml"></a>

```
  [MaxEnvironments](#cfn-lambda-webfunctionendpoint-scalingconfig-maxenvironments): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-webfunctionendpoint-scalingconfig-properties"></a>

`MaxEnvironments`  <a name="cfn-lambda-webfunctionendpoint-scalingconfig-maxenvironments"></a>
The maximum number of concurrent execution environments for the endpoint. The minimum value is 2 and the maximum value is 10000. This optional setting further constrains the endpoint's scaling; when omitted, the endpoint's scaling is limited only by your account's vCPU quota. On an update, omit `ScalingConfig` to keep the current value, or specify an empty object to clear a previously set value.
*Required*: No
*Type*: Integer
*Minimum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
