---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-responseheaderspolicy-removeheadersconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ResponseHeadersPolicy RemoveHeadersConfig
<a name="aws-properties-cloudfront-responseheaderspolicy-removeheadersconfig"></a>

A list of HTTP header names that CloudFront removes from HTTP responses to requests that match the cache behavior that this response headers policy is attached to.

## Syntax
<a name="aws-properties-cloudfront-responseheaderspolicy-removeheadersconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-responseheaderspolicy-removeheadersconfig-syntax.json"></a>

```
{
  "[Items](#cfn-cloudfront-responseheaderspolicy-removeheadersconfig-items)" : {{[ RemoveHeader, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudfront-responseheaderspolicy-removeheadersconfig-syntax.yaml"></a>

```
  [Items](#cfn-cloudfront-responseheaderspolicy-removeheadersconfig-items): {{
    - RemoveHeader}}
```

## Properties
<a name="aws-properties-cloudfront-responseheaderspolicy-removeheadersconfig-properties"></a>

`Items`  <a name="cfn-cloudfront-responseheaderspolicy-removeheadersconfig-items"></a>
The list of HTTP header names.
*Required*: Yes
*Type*: Array of [RemoveHeader](aws-properties-cloudfront-responseheaderspolicy-removeheader.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
