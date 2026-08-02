---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_EndpointRequest.html
---

# EndpointRequest
<a name="API_EndpointRequest"></a>

Describes the settings of a public endpoint for an Amazon Lightsail container service.

## Contents
<a name="API_EndpointRequest_Contents"></a>

 ** containerName **   <a name="Lightsail-Type-EndpointRequest-containerName"></a>
The name of the container for the endpoint.
Type: String
Required: Yes

 ** containerPort **   <a name="Lightsail-Type-EndpointRequest-containerPort"></a>
The port of the container to which traffic is forwarded to.
Type: Integer
Required: Yes

 ** healthCheck **   <a name="Lightsail-Type-EndpointRequest-healthCheck"></a>
An object that describes the health check configuration of the container.
Type: [ContainerServiceHealthCheckConfig](API_ContainerServiceHealthCheckConfig.md) object
Required: No

## See Also
<a name="API_EndpointRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/EndpointRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/EndpointRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/EndpointRequest)
