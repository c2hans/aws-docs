---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-statuscodes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution StatusCodes
<a name="aws-properties-cloudfront-distribution-statuscodes"></a>

A complex data type for the status codes that you specify that, when returned by a primary origin, trigger CloudFront to failover to a second origin.

## Syntax
<a name="aws-properties-cloudfront-distribution-statuscodes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-statuscodes-syntax.json"></a>

```
{
  "[Items](#cfn-cloudfront-distribution-statuscodes-items)" : {{[ Integer, ... ]}},
  "[Quantity](#cfn-cloudfront-distribution-statuscodes-quantity)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-statuscodes-syntax.yaml"></a>

```
  [Items](#cfn-cloudfront-distribution-statuscodes-items): {{
    - Integer}}
  [Quantity](#cfn-cloudfront-distribution-statuscodes-quantity): {{Integer}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-statuscodes-properties"></a>

`Items`  <a name="cfn-cloudfront-distribution-statuscodes-items"></a>
The items (status codes) for an origin group.
*Required*: Yes
*Type*: Array of Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Quantity`  <a name="cfn-cloudfront-distribution-statuscodes-quantity"></a>
The number of status codes.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
