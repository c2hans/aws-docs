---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionendpoint-throttleconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunctionEndpoint ThrottleConfig
<a name="aws-properties-lambda-webfunctionendpoint-throttleconfig"></a>

The throttling configuration for a web function endpoint.

## Syntax
<a name="aws-properties-lambda-webfunctionendpoint-throttleconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-webfunctionendpoint-throttleconfig-syntax.json"></a>

```
{
  "[RateLimit](#cfn-lambda-webfunctionendpoint-throttleconfig-ratelimit)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-webfunctionendpoint-throttleconfig-syntax.yaml"></a>

```
  [RateLimit](#cfn-lambda-webfunctionendpoint-throttleconfig-ratelimit): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-webfunctionendpoint-throttleconfig-properties"></a>

`RateLimit`  <a name="cfn-lambda-webfunctionendpoint-throttleconfig-ratelimit"></a>
The maximum request rate per second for the endpoint. This optional setting further constrains the endpoint's request rate; when omitted, the endpoint's request rate is limited only by your account's rate limit quota. Specify `0` to reject all new requests. Other supported values are `100` through `1000` in increments of 100, and `2000` through `10000` in increments of 1000. Supported values can vary by Region; if you specify an unsupported value, the error lists the values available in that Region. On an update, omit `ThrottleConfig` to keep the current value, or specify an empty object to clear a previously set value.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
