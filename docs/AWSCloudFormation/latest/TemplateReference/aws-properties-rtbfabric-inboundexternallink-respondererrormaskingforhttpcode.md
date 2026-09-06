---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::InboundExternalLink ResponderErrorMaskingForHttpCode
<a name="aws-properties-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode"></a>

<a name="aws-properties-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-description"></a>The `ResponderErrorMaskingForHttpCode` property type specifies Property description not available. for an [AWS::RTBFabric::InboundExternalLink](aws-resource-rtbfabric-inboundexternallink.md).

## Syntax
<a name="aws-properties-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-syntax.json"></a>

```
{
  "[Action](#cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-action)" : {{String}},
  "[HttpCode](#cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-httpcode)" : {{String}},
  "[LoggingTypes](#cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-loggingtypes)" : {{[ String, ... ]}},
  "[ResponseLoggingPercentage](#cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-responseloggingpercentage)" : {{Number}}
}
```

### YAML
<a name="aws-properties-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-syntax.yaml"></a>

```
  [Action](#cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-action): {{String}}
  [HttpCode](#cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-httpcode): {{String}}
  [LoggingTypes](#cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-loggingtypes): {{
    - String}}
  [ResponseLoggingPercentage](#cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-responseloggingpercentage): {{Number}}
```

## Properties
<a name="aws-properties-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-properties"></a>

`Action`  <a name="cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-action"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `NO_BID | PASSTHROUGH`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`HttpCode`  <a name="cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-httpcode"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^DEFAULT|4XX|5XX|\d{3}$`
*Minimum*: `3`
*Maximum*: `7`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LoggingTypes`  <a name="cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-loggingtypes"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ResponseLoggingPercentage`  <a name="cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-responseloggingpercentage"></a>
Property description not available.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
