---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-associationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL AssociationConfig
<a name="aws-properties-wafv2-webacl-associationconfig"></a>

Specifies custom configurations for the associations between the web ACL and protected resources.

Use this to customize the maximum size of the request body that your protected resources forward to AWS WAF for inspection. You can customize this setting for CloudFront, API Gateway, Amazon Cognito, App Runner, or Verified Access resources. The default setting is 16 KB (16,384 bytes).

**Note**
You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).

For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).

## Syntax
<a name="aws-properties-wafv2-webacl-associationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-associationconfig-syntax.json"></a>

```
{
  "[RequestBody](#cfn-wafv2-webacl-associationconfig-requestbody)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-associationconfig-syntax.yaml"></a>

```
  [RequestBody](#cfn-wafv2-webacl-associationconfig-requestbody): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-wafv2-webacl-associationconfig-properties"></a>

`RequestBody`  <a name="cfn-wafv2-webacl-associationconfig-requestbody"></a>
Customizes the maximum size of the request body that your protected CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access resources forward to AWS WAF for inspection. The default size is 16 KB (16,384 bytes). You can change the setting for any of the available resource types.
You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).
Example JSON: ` { "API_GATEWAY": "KB_48", "APP_RUNNER_SERVICE": "KB_32" }`
For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).
*Required*: No
*Type*: Object of [RequestBodyAssociatedResourceTypeConfig](aws-properties-wafv2-webacl-requestbodyassociatedresourcetypeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
