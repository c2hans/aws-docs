---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-link-respondererrormaskingforhttpcode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link ResponderErrorMaskingForHttpCode
<a name="aws-properties-rtbfabric-link-respondererrormaskingforhttpcode"></a>

Describes the masking for HTTP error codes.

## Syntax
<a name="aws-properties-rtbfabric-link-respondererrormaskingforhttpcode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-link-respondererrormaskingforhttpcode-syntax.json"></a>

```
{
  "[Action](#cfn-rtbfabric-link-respondererrormaskingforhttpcode-action)" : {{String}},
  "[HttpCode](#cfn-rtbfabric-link-respondererrormaskingforhttpcode-httpcode)" : {{String}},
  "[LoggingTypes](#cfn-rtbfabric-link-respondererrormaskingforhttpcode-loggingtypes)" : {{[ String, ... ]}},
  "[ResponseLoggingPercentage](#cfn-rtbfabric-link-respondererrormaskingforhttpcode-responseloggingpercentage)" : {{Number}}
}
```

### YAML
<a name="aws-properties-rtbfabric-link-respondererrormaskingforhttpcode-syntax.yaml"></a>

```
  [Action](#cfn-rtbfabric-link-respondererrormaskingforhttpcode-action): {{String}}
  [HttpCode](#cfn-rtbfabric-link-respondererrormaskingforhttpcode-httpcode): {{String}}
  [LoggingTypes](#cfn-rtbfabric-link-respondererrormaskingforhttpcode-loggingtypes): {{
    - String}}
  [ResponseLoggingPercentage](#cfn-rtbfabric-link-respondererrormaskingforhttpcode-responseloggingpercentage): {{Number}}
```

## Properties
<a name="aws-properties-rtbfabric-link-respondererrormaskingforhttpcode-properties"></a>

`Action`  <a name="cfn-rtbfabric-link-respondererrormaskingforhttpcode-action"></a>
The action for the error..
*Required*: Yes
*Type*: [String](aws-properties-rtbfabric-link-action.md)
*Allowed values*: `NO_BID | PASSTHROUGH`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`HttpCode`  <a name="cfn-rtbfabric-link-respondererrormaskingforhttpcode-httpcode"></a>
The HTTP error code.
*Required*: Yes
*Type*: String
*Pattern*: `^DEFAULT|4XX|5XX|\d{3}$`
*Minimum*: `3`
*Maximum*: `7`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LoggingTypes`  <a name="cfn-rtbfabric-link-respondererrormaskingforhttpcode-loggingtypes"></a>
The error log type.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ResponseLoggingPercentage`  <a name="cfn-rtbfabric-link-respondererrormaskingforhttpcode-responseloggingpercentage"></a>
The percentage of response logging.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
