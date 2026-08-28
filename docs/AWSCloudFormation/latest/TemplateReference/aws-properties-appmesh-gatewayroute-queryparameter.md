---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-gatewayroute-queryparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::GatewayRoute QueryParameter
<a name="aws-properties-appmesh-gatewayroute-queryparameter"></a>

An object that represents the query parameter in the request.

## Syntax
<a name="aws-properties-appmesh-gatewayroute-queryparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-gatewayroute-queryparameter-syntax.json"></a>

```
{
  "[Match](#cfn-appmesh-gatewayroute-queryparameter-match)" : {{HttpQueryParameterMatch}},
  "[Name](#cfn-appmesh-gatewayroute-queryparameter-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-gatewayroute-queryparameter-syntax.yaml"></a>

```
  [Match](#cfn-appmesh-gatewayroute-queryparameter-match): {{
    HttpQueryParameterMatch}}
  [Name](#cfn-appmesh-gatewayroute-queryparameter-name): {{String}}
```

## Properties
<a name="aws-properties-appmesh-gatewayroute-queryparameter-properties"></a>

`Match`  <a name="cfn-appmesh-gatewayroute-queryparameter-match"></a>
The query parameter to match on.
*Required*: No
*Type*: [HttpQueryParameterMatch](aws-properties-appmesh-gatewayroute-httpqueryparametermatch.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-appmesh-gatewayroute-queryparameter-name"></a>
A name for the query parameter that will be matched on.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
