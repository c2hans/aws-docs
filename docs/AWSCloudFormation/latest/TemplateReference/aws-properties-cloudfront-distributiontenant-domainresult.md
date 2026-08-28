---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distributiontenant-domainresult.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::DistributionTenant DomainResult
<a name="aws-properties-cloudfront-distributiontenant-domainresult"></a>

The details about the domain result.

## Syntax
<a name="aws-properties-cloudfront-distributiontenant-domainresult-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distributiontenant-domainresult-syntax.json"></a>

```
{
  "[Domain](#cfn-cloudfront-distributiontenant-domainresult-domain)" : {{String}},
  "[Status](#cfn-cloudfront-distributiontenant-domainresult-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distributiontenant-domainresult-syntax.yaml"></a>

```
  [Domain](#cfn-cloudfront-distributiontenant-domainresult-domain): {{String}}
  [Status](#cfn-cloudfront-distributiontenant-domainresult-status): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distributiontenant-domainresult-properties"></a>

`Domain`  <a name="cfn-cloudfront-distributiontenant-domainresult-domain"></a>
The specified domain.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-cloudfront-distributiontenant-domainresult-status"></a>
Whether the domain is active or inactive.
*Required*: No
*Type*: String
*Allowed values*: `active | inactive`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
