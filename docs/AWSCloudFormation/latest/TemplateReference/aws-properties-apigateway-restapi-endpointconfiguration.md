---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigateway-restapi-endpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::RestApi EndpointConfiguration
<a name="aws-properties-apigateway-restapi-endpointconfiguration"></a>

The `EndpointConfiguration` property type specifies the endpoint types and IP address types of a REST API.

`EndpointConfiguration` is a property of the [AWS::ApiGateway::RestApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html) resource.

## Syntax
<a name="aws-properties-apigateway-restapi-endpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigateway-restapi-endpointconfiguration-syntax.json"></a>

```
{
  "[IpAddressType](#cfn-apigateway-restapi-endpointconfiguration-ipaddresstype)" : {{String}},
  "[Types](#cfn-apigateway-restapi-endpointconfiguration-types)" : {{[ String, ... ]}},
  "[VpcEndpointIds](#cfn-apigateway-restapi-endpointconfiguration-vpcendpointids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-apigateway-restapi-endpointconfiguration-syntax.yaml"></a>

```
  [IpAddressType](#cfn-apigateway-restapi-endpointconfiguration-ipaddresstype): {{String}}
  [Types](#cfn-apigateway-restapi-endpointconfiguration-types): {{
    - String}}
  [VpcEndpointIds](#cfn-apigateway-restapi-endpointconfiguration-vpcendpointids): {{
    - String}}
```

## Properties
<a name="aws-properties-apigateway-restapi-endpointconfiguration-properties"></a>

`IpAddressType`  <a name="cfn-apigateway-restapi-endpointconfiguration-ipaddresstype"></a>
The IP address types that can invoke an API (RestApi). Use `ipv4` to allow only IPv4 addresses to invoke an API, or use `dualstack` to allow both IPv4 and IPv6 addresses to invoke an API. For the `PRIVATE` endpoint type, only `dualstack` is supported.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | dualstack`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Types`  <a name="cfn-apigateway-restapi-endpointconfiguration-types"></a>
A list of endpoint types of an API (RestApi) or its custom domain name (DomainName). For an edge-optimized API and its custom domain name, the endpoint type is `"EDGE"`. For a regional API and its custom domain name, the endpoint type is `REGIONAL`. For a private API, the endpoint type is `PRIVATE`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcEndpointIds`  <a name="cfn-apigateway-restapi-endpointconfiguration-vpcendpointids"></a>
A list of VpcEndpointIds of an API (RestApi) against which to create Route53 ALIASes. It is only supported for `PRIVATE` endpoint type.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-apigateway-restapi-endpointconfiguration--seealso"></a>
+ [RestApi](https://docs.aws.amazon.com/apigateway/latest/api/API_RestApi.html) in the *Amazon API Gateway REST API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
