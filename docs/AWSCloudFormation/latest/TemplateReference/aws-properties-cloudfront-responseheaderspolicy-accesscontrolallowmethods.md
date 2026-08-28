---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowmethods.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ResponseHeadersPolicy AccessControlAllowMethods
<a name="aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowmethods"></a>

A list of HTTP methods that CloudFront includes as values for the `Access-Control-Allow-Methods` HTTP response header.

For more information about the `Access-Control-Allow-Methods` HTTP response header, see [Access-Control-Allow-Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods) in the MDN Web Docs.

## Syntax
<a name="aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowmethods-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowmethods-syntax.json"></a>

```
{
  "[Items](#cfn-cloudfront-responseheaderspolicy-accesscontrolallowmethods-items)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowmethods-syntax.yaml"></a>

```
  [Items](#cfn-cloudfront-responseheaderspolicy-accesscontrolallowmethods-items): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowmethods-properties"></a>

`Items`  <a name="cfn-cloudfront-responseheaderspolicy-accesscontrolallowmethods-items"></a>
The list of HTTP methods. Valid values are:
+  `GET`
+  `DELETE`
+  `HEAD`
+  `OPTIONS`
+  `PATCH`
+  `POST`
+  `PUT`
+  `ALL`
`ALL` is a special value that includes all of the listed HTTP methods.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
