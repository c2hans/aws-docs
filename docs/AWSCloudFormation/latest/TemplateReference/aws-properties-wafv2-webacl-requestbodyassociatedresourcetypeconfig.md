---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-requestbodyassociatedresourcetypeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL RequestBodyAssociatedResourceTypeConfig
<a name="aws-properties-wafv2-webacl-requestbodyassociatedresourcetypeconfig"></a>

Customizes the maximum size of the request body that your protected CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access resources forward to AWS WAF for inspection. The default size is 16 KB (16,384 bytes). You can change the setting for any of the available resource types.

**Note**
You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).

Example JSON: ` { "API_GATEWAY": "KB_48", "APP_RUNNER_SERVICE": "KB_32" }`

For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).

This is used in the `AssociationConfig` of the web ACL.

## Syntax
<a name="aws-properties-wafv2-webacl-requestbodyassociatedresourcetypeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-requestbodyassociatedresourcetypeconfig-syntax.json"></a>

```
{
  "[DefaultSizeInspectionLimit](#cfn-wafv2-webacl-requestbodyassociatedresourcetypeconfig-defaultsizeinspectionlimit)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-requestbodyassociatedresourcetypeconfig-syntax.yaml"></a>

```
  [DefaultSizeInspectionLimit](#cfn-wafv2-webacl-requestbodyassociatedresourcetypeconfig-defaultsizeinspectionlimit): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-requestbodyassociatedresourcetypeconfig-properties"></a>

`DefaultSizeInspectionLimit`  <a name="cfn-wafv2-webacl-requestbodyassociatedresourcetypeconfig-defaultsizeinspectionlimit"></a>
Specifies the maximum size of the web request body component that an associated CloudFront, API Gateway, Amazon Cognito, App Runner, or Verified Access resource should send to AWS WAF for inspection. This applies to statements in the web ACL that inspect the body or JSON body.
Default: `16 KB (16,384 bytes)`
*Required*: Yes
*Type*: String
*Allowed values*: `KB_16 | KB_32 | KB_48 | KB_64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
