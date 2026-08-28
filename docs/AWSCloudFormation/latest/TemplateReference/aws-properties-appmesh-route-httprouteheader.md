---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-route-httprouteheader.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::Route HttpRouteHeader
<a name="aws-properties-appmesh-route-httprouteheader"></a>

An object that represents the HTTP header in the request.

## Syntax
<a name="aws-properties-appmesh-route-httprouteheader-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-route-httprouteheader-syntax.json"></a>

```
{
  "[Invert](#cfn-appmesh-route-httprouteheader-invert)" : {{Boolean}},
  "[Match](#cfn-appmesh-route-httprouteheader-match)" : {{HeaderMatchMethod}},
  "[Name](#cfn-appmesh-route-httprouteheader-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-route-httprouteheader-syntax.yaml"></a>

```
  [Invert](#cfn-appmesh-route-httprouteheader-invert): {{Boolean}}
  [Match](#cfn-appmesh-route-httprouteheader-match): {{
    HeaderMatchMethod}}
  [Name](#cfn-appmesh-route-httprouteheader-name): {{String}}
```

## Properties
<a name="aws-properties-appmesh-route-httprouteheader-properties"></a>

`Invert`  <a name="cfn-appmesh-route-httprouteheader-invert"></a>
Specify `True` to match anything except the match criteria. The default value is `False`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Match`  <a name="cfn-appmesh-route-httprouteheader-match"></a>
The `HeaderMatchMethod` object.
*Required*: No
*Type*: [HeaderMatchMethod](aws-properties-appmesh-route-headermatchmethod.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-appmesh-route-httprouteheader-name"></a>
A name for the HTTP header in the client request that will be matched on.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
