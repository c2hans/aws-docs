---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigateway-domainname-endpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::DomainName EndpointConfiguration
<a name="aws-properties-apigateway-domainname-endpointconfiguration"></a>

The `EndpointConfiguration` property type specifies the endpoint types and IP address types of an Amazon API Gateway domain name.

`EndpointConfiguration` is a property of the [AWS::ApiGateway::DomainName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html) resource.

## Syntax
<a name="aws-properties-apigateway-domainname-endpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigateway-domainname-endpointconfiguration-syntax.json"></a>

```
{
  "[IpAddressType](#cfn-apigateway-domainname-endpointconfiguration-ipaddresstype)" : {{String}},
  "[Types](#cfn-apigateway-domainname-endpointconfiguration-types)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-apigateway-domainname-endpointconfiguration-syntax.yaml"></a>

```
  [IpAddressType](#cfn-apigateway-domainname-endpointconfiguration-ipaddresstype): {{String}}
  [Types](#cfn-apigateway-domainname-endpointconfiguration-types): {{
    - String}}
```

## Properties
<a name="aws-properties-apigateway-domainname-endpointconfiguration-properties"></a>

`IpAddressType`  <a name="cfn-apigateway-domainname-endpointconfiguration-ipaddresstype"></a>
The IP address types that can invoke this DomainName. Use `ipv4` to allow only IPv4 addresses to invoke this DomainName, or use `dualstack` to allow both IPv4 and IPv6 addresses to invoke this DomainName. For the `PRIVATE` endpoint type, only `dualstack` is supported.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Types`  <a name="cfn-apigateway-domainname-endpointconfiguration-types"></a>
A list of endpoint types of an API (RestApi) or its custom domain name (DomainName). For an edge-optimized API and its custom domain name, the endpoint type is `"EDGE"`. For a regional API and its custom domain name, the endpoint type is `REGIONAL`. For a private API, the endpoint type is `PRIVATE`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-apigateway-domainname-endpointconfiguration--seealso"></a>
+ [DomainName](https://docs.aws.amazon.com/apigateway/latest/api/API_DomainName.html) in the *Amazon API Gateway REST API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
