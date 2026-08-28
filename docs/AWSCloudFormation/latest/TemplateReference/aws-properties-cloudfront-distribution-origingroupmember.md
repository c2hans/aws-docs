---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-origingroupmember.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution OriginGroupMember
<a name="aws-properties-cloudfront-distribution-origingroupmember"></a>

An origin in an origin group.

## Syntax
<a name="aws-properties-cloudfront-distribution-origingroupmember-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-origingroupmember-syntax.json"></a>

```
{
  "[OriginId](#cfn-cloudfront-distribution-origingroupmember-originid)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-origingroupmember-syntax.yaml"></a>

```
  [OriginId](#cfn-cloudfront-distribution-origingroupmember-originid): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-origingroupmember-properties"></a>

`OriginId`  <a name="cfn-cloudfront-distribution-origingroupmember-originid"></a>
The ID for an origin in an origin group.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
