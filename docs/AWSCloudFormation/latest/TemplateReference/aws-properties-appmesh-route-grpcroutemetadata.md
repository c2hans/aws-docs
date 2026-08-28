---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-route-grpcroutemetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::Route GrpcRouteMetadata
<a name="aws-properties-appmesh-route-grpcroutemetadata"></a>

An object that represents the match metadata for the route.

## Syntax
<a name="aws-properties-appmesh-route-grpcroutemetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-route-grpcroutemetadata-syntax.json"></a>

```
{
  "[Invert](#cfn-appmesh-route-grpcroutemetadata-invert)" : {{Boolean}},
  "[Match](#cfn-appmesh-route-grpcroutemetadata-match)" : {{GrpcRouteMetadataMatchMethod}},
  "[Name](#cfn-appmesh-route-grpcroutemetadata-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-route-grpcroutemetadata-syntax.yaml"></a>

```
  [Invert](#cfn-appmesh-route-grpcroutemetadata-invert): {{Boolean}}
  [Match](#cfn-appmesh-route-grpcroutemetadata-match): {{
    GrpcRouteMetadataMatchMethod}}
  [Name](#cfn-appmesh-route-grpcroutemetadata-name): {{String}}
```

## Properties
<a name="aws-properties-appmesh-route-grpcroutemetadata-properties"></a>

`Invert`  <a name="cfn-appmesh-route-grpcroutemetadata-invert"></a>
Specify `True` to match anything except the match criteria. The default value is `False`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Match`  <a name="cfn-appmesh-route-grpcroutemetadata-match"></a>
An object that represents the data to match from the request.
*Required*: No
*Type*: [GrpcRouteMetadataMatchMethod](aws-properties-appmesh-route-grpcroutemetadatamatchmethod.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-appmesh-route-grpcroutemetadata-name"></a>
The name of the route.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
