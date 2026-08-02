---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ContainerServiceEndpoint.html
---

# ContainerServiceEndpoint
<a name="API_ContainerServiceEndpoint"></a>

Describes the public endpoint configuration of a deployment of an Amazon Lightsail container service.

## Contents
<a name="API_ContainerServiceEndpoint_Contents"></a>

 ** containerName **   <a name="Lightsail-Type-ContainerServiceEndpoint-containerName"></a>
The name of the container entry of the deployment that the endpoint configuration applies to.
Type: String
Required: No

 ** containerPort **   <a name="Lightsail-Type-ContainerServiceEndpoint-containerPort"></a>
The port of the specified container to which traffic is forwarded to.
Type: Integer
Required: No

 ** healthCheck **   <a name="Lightsail-Type-ContainerServiceEndpoint-healthCheck"></a>
An object that describes the health check configuration of the container.
Type: [ContainerServiceHealthCheckConfig](API_ContainerServiceHealthCheckConfig.md) object
Required: No

## See Also
<a name="API_ContainerServiceEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/ContainerServiceEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/ContainerServiceEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/ContainerServiceEndpoint)
