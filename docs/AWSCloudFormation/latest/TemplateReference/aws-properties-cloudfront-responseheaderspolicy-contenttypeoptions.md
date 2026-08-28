---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-responseheaderspolicy-contenttypeoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ResponseHeadersPolicy ContentTypeOptions
<a name="aws-properties-cloudfront-responseheaderspolicy-contenttypeoptions"></a>

Determines whether CloudFront includes the `X-Content-Type-Options` HTTP response header with its value set to `nosniff`.

For more information about the `X-Content-Type-Options` HTTP response header, see [X-Content-Type-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options) in the MDN Web Docs.

## Syntax
<a name="aws-properties-cloudfront-responseheaderspolicy-contenttypeoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-responseheaderspolicy-contenttypeoptions-syntax.json"></a>

```
{
  "[Override](#cfn-cloudfront-responseheaderspolicy-contenttypeoptions-override)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cloudfront-responseheaderspolicy-contenttypeoptions-syntax.yaml"></a>

```
  [Override](#cfn-cloudfront-responseheaderspolicy-contenttypeoptions-override): {{Boolean}}
```

## Properties
<a name="aws-properties-cloudfront-responseheaderspolicy-contenttypeoptions-properties"></a>

`Override`  <a name="cfn-cloudfront-responseheaderspolicy-contenttypeoptions-override"></a>
A Boolean that determines whether CloudFront overrides the `X-Content-Type-Options` HTTP response header received from the origin with the one specified in this response headers policy.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
