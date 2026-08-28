---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-responseheaderspolicy-removeheader.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ResponseHeadersPolicy RemoveHeader
<a name="aws-properties-cloudfront-responseheaderspolicy-removeheader"></a>

The name of an HTTP header that CloudFront removes from HTTP responses to requests that match the cache behavior that this response headers policy is attached to.

## Syntax
<a name="aws-properties-cloudfront-responseheaderspolicy-removeheader-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-responseheaderspolicy-removeheader-syntax.json"></a>

```
{
  "[Header](#cfn-cloudfront-responseheaderspolicy-removeheader-header)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-responseheaderspolicy-removeheader-syntax.yaml"></a>

```
  [Header](#cfn-cloudfront-responseheaderspolicy-removeheader-header): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-responseheaderspolicy-removeheader-properties"></a>

`Header`  <a name="cfn-cloudfront-responseheaderspolicy-removeheader-header"></a>
The HTTP header name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
