---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::OutboundExternalLink ResponderErrorMaskingForHttpCode
<a name="aws-properties-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode"></a>

<a name="aws-properties-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-description"></a>The `ResponderErrorMaskingForHttpCode` property type specifies Property description not available. for an [AWS::RTBFabric::OutboundExternalLink](aws-resource-rtbfabric-outboundexternallink.md).

## Syntax
<a name="aws-properties-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-syntax.json"></a>

```
{
  "[Action](#cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-action)" : {{String}},
  "[HttpCode](#cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-httpcode)" : {{String}},
  "[LoggingTypes](#cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-loggingtypes)" : {{[ String, ... ]}},
  "[ResponseLoggingPercentage](#cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-responseloggingpercentage)" : {{Number}}
}
```

### YAML
<a name="aws-properties-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-syntax.yaml"></a>

```
  [Action](#cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-action): {{String}}
  [HttpCode](#cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-httpcode): {{String}}
  [LoggingTypes](#cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-loggingtypes): {{
    - String}}
  [ResponseLoggingPercentage](#cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-responseloggingpercentage): {{Number}}
```

## Properties
<a name="aws-properties-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-properties"></a>

`Action`  <a name="cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-action"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `NO_BID | PASSTHROUGH`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`HttpCode`  <a name="cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-httpcode"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^DEFAULT|4XX|5XX|\d{3}$`
*Minimum*: `3`
*Maximum*: `7`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LoggingTypes`  <a name="cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-loggingtypes"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ResponseLoggingPercentage`  <a name="cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-responseloggingpercentage"></a>
Property description not available.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
