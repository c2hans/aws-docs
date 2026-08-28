---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-anycastiplist-tags.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::AnycastIpList Tags
<a name="aws-properties-cloudfront-anycastiplist-tags"></a>

A complex type that contains zero or more `Tag` elements.

## Syntax
<a name="aws-properties-cloudfront-anycastiplist-tags-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-anycastiplist-tags-syntax.json"></a>

```
{
  "[Items](#cfn-cloudfront-anycastiplist-tags-items)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudfront-anycastiplist-tags-syntax.yaml"></a>

```
  [Items](#cfn-cloudfront-anycastiplist-tags-items): {{
    - Tag}}
```

## Properties
<a name="aws-properties-cloudfront-anycastiplist-tags-properties"></a>

`Items`  <a name="cfn-cloudfront-anycastiplist-tags-items"></a>
A complex type that contains `Tag` elements.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudfront-anycastiplist-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
