---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigateway-domainnamev2-endpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::DomainNameV2 EndpointConfiguration
<a name="aws-properties-apigateway-domainnamev2-endpointconfiguration"></a>

The endpoint configuration to indicate the types of endpoints an API (RestApi) or its custom domain name (DomainName) has and the IP address types that can invoke it.

## Syntax
<a name="aws-properties-apigateway-domainnamev2-endpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigateway-domainnamev2-endpointconfiguration-syntax.json"></a>

```
{
  "[IpAddressType](#cfn-apigateway-domainnamev2-endpointconfiguration-ipaddresstype)" : {{String}},
  "[Types](#cfn-apigateway-domainnamev2-endpointconfiguration-types)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-apigateway-domainnamev2-endpointconfiguration-syntax.yaml"></a>

```
  [IpAddressType](#cfn-apigateway-domainnamev2-endpointconfiguration-ipaddresstype): {{String}}
  [Types](#cfn-apigateway-domainnamev2-endpointconfiguration-types): {{
    - String}}
```

## Properties
<a name="aws-properties-apigateway-domainnamev2-endpointconfiguration-properties"></a>

`IpAddressType`  <a name="cfn-apigateway-domainnamev2-endpointconfiguration-ipaddresstype"></a>
The IP address types that can invoke an API (RestApi) or a DomainName. Use `ipv4` to allow only IPv4 addresses to invoke an API or DomainName, or use `dualstack` to allow both IPv4 and IPv6 addresses to invoke an API or a DomainName. For the `PRIVATE` endpoint type, only `dualstack` is supported.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | dualstack`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Types`  <a name="cfn-apigateway-domainnamev2-endpointconfiguration-types"></a>
A list of endpoint types of an API (RestApi) or its custom domain name (DomainName). For an edge-optimized API and its custom domain name, the endpoint type is `"EDGE"`. For a regional API and its custom domain name, the endpoint type is `REGIONAL`. For a private API, the endpoint type is `PRIVATE`.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
