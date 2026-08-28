---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listenerrule-httprequestmethodconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerRule HttpRequestMethodConfig
<a name="aws-properties-elasticloadbalancingv2-listenerrule-httprequestmethodconfig"></a>

Information about an HTTP method condition.

HTTP defines a set of request methods, also referred to as HTTP verbs. For more information, see the [HTTP Method Registry](https://www.iana.org/assignments/http-methods/http-methods.xhtml). You can also define custom HTTP methods.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listenerrule-httprequestmethodconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-httprequestmethodconfig-syntax.json"></a>

```
{
  "[Values](#cfn-elasticloadbalancingv2-listenerrule-httprequestmethodconfig-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-httprequestmethodconfig-syntax.yaml"></a>

```
  [Values](#cfn-elasticloadbalancingv2-listenerrule-httprequestmethodconfig-values): {{
    - String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listenerrule-httprequestmethodconfig-properties"></a>

`Values`  <a name="cfn-elasticloadbalancingv2-listenerrule-httprequestmethodconfig-values"></a>
The name of the request method. The maximum length is 40 characters. The allowed characters are A-Z, hyphen (-), and underscore (\_). The comparison is case sensitive. Wildcards are not supported; therefore, the method name must be an exact match.
If you specify multiple strings, the condition is satisfied if one of the strings matches the HTTP request method. We recommend that you route GET and HEAD requests in the same way, because the response to a HEAD request may be cached.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
