---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-customrequesthandling.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL CustomRequestHandling
<a name="aws-properties-wafv2-webacl-customrequesthandling"></a>

Custom request handling behavior that inserts custom headers into a web request. You can add custom request handling for AWS WAF to use when the rule action doesn't block the request. For example, `CaptchaAction` for requests with valid t okens, and `AllowAction`.

For information about customizing web requests and responses, see [Customizing web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the *AWS WAF Developer Guide*.

## Syntax
<a name="aws-properties-wafv2-webacl-customrequesthandling-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-customrequesthandling-syntax.json"></a>

```
{
  "[InsertHeaders](#cfn-wafv2-webacl-customrequesthandling-insertheaders)" : {{[ CustomHTTPHeader, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-customrequesthandling-syntax.yaml"></a>

```
  [InsertHeaders](#cfn-wafv2-webacl-customrequesthandling-insertheaders): {{
    - CustomHTTPHeader}}
```

## Properties
<a name="aws-properties-wafv2-webacl-customrequesthandling-properties"></a>

`InsertHeaders`  <a name="cfn-wafv2-webacl-customrequesthandling-insertheaders"></a>
The HTTP headers to insert into the request. Duplicate header names are not allowed.
For information about the limits on count and size for custom request and response settings, see [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the *AWS WAF Developer Guide*.
*Required*: Yes
*Type*: Array of [CustomHTTPHeader](aws-properties-wafv2-webacl-customhttpheader.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
