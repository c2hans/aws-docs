---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distributiontenant-webaclcustomization.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::DistributionTenant WebAclCustomization
<a name="aws-properties-cloudfront-distributiontenant-webaclcustomization"></a>

The AWS WAF web ACL customization specified for the distribution tenant.

## Syntax
<a name="aws-properties-cloudfront-distributiontenant-webaclcustomization-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distributiontenant-webaclcustomization-syntax.json"></a>

```
{
  "[Action](#cfn-cloudfront-distributiontenant-webaclcustomization-action)" : {{String}},
  "[Arn](#cfn-cloudfront-distributiontenant-webaclcustomization-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distributiontenant-webaclcustomization-syntax.yaml"></a>

```
  [Action](#cfn-cloudfront-distributiontenant-webaclcustomization-action): {{String}}
  [Arn](#cfn-cloudfront-distributiontenant-webaclcustomization-arn): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distributiontenant-webaclcustomization-properties"></a>

`Action`  <a name="cfn-cloudfront-distributiontenant-webaclcustomization-action"></a>
The action for the AWS WAF web ACL customization. You can specify `override` to specify a separate AWS WAF web ACL for the distribution tenant. If you specify `disable`, the distribution tenant won't have AWS WAF web ACL protections and won't inherit from the multi-tenant distribution.
*Required*: No
*Type*: String
*Allowed values*: `override | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Arn`  <a name="cfn-cloudfront-distributiontenant-webaclcustomization-arn"></a>
The Amazon Resource Name (ARN) of the AWS WAF web ACL.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
