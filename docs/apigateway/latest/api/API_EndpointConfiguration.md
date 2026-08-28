---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_EndpointConfiguration.html
---

# EndpointConfiguration
<a name="API_EndpointConfiguration"></a>

The endpoint configuration to indicate the types of endpoints an API (RestApi) or its custom domain name (DomainName) has and the IP address types that can invoke it.

## Contents
<a name="API_EndpointConfiguration_Contents"></a>

 ** ipAddressType **   <a name="apigw-Type-EndpointConfiguration-ipAddressType"></a>
The IP address types that can invoke an API (RestApi) or a DomainName. Use `ipv4` to allow only IPv4 addresses to invoke an API or DomainName, or use `dualstack` to allow both IPv4 and IPv6 addresses to invoke an API or a DomainName. For the `PRIVATE` endpoint type, only `dualstack` is supported.
Type: String
Valid Values: `ipv4 | dualstack`
Required: No

 ** types **   <a name="apigw-Type-EndpointConfiguration-types"></a>
A list of endpoint types of an API (RestApi) or its custom domain name (DomainName). For an edge-optimized API and its custom domain name, the endpoint type is `"EDGE"`. For a regional API and its custom domain name, the endpoint type is `REGIONAL`. For a private API, the endpoint type is `PRIVATE`.
Type: Array of strings
Valid Values: `REGIONAL | EDGE | PRIVATE`
Required: No

 ** vpcEndpointIds **   <a name="apigw-Type-EndpointConfiguration-vpcEndpointIds"></a>
A list of VpcEndpointIds of an API (RestApi) against which to create Route53 ALIASes. It is only supported for `PRIVATE` endpoint type.
Type: Array of strings
Required: No

## See Also
<a name="API_EndpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/EndpointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/EndpointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/EndpointConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
