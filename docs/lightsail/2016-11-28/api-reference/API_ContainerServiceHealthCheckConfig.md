---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ContainerServiceHealthCheckConfig.html
---

# ContainerServiceHealthCheckConfig
<a name="API_ContainerServiceHealthCheckConfig"></a>

Describes the health check configuration of an Amazon Lightsail container service.

## Contents
<a name="API_ContainerServiceHealthCheckConfig_Contents"></a>

 ** healthyThreshold **   <a name="Lightsail-Type-ContainerServiceHealthCheckConfig-healthyThreshold"></a>
The number of consecutive health checks successes required before moving the container to the `Healthy` state. The default value is `2`.
Type: Integer
Required: No

 ** intervalSeconds **   <a name="Lightsail-Type-ContainerServiceHealthCheckConfig-intervalSeconds"></a>
The approximate interval, in seconds, between health checks of an individual container. You can specify between 5 and 300 seconds. The default value is `5`.
Type: Integer
Required: No

 ** path **   <a name="Lightsail-Type-ContainerServiceHealthCheckConfig-path"></a>
The path on the container on which to perform the health check. The default value is `/`.
Type: String
Required: No

 ** successCodes **   <a name="Lightsail-Type-ContainerServiceHealthCheckConfig-successCodes"></a>
The HTTP codes to use when checking for a successful response from a container. You can specify values between `200` and `499`. You can specify multiple values (for example, `200,202`) or a range of values (for example, `200-299`).
Type: String
Required: No

 ** timeoutSeconds **   <a name="Lightsail-Type-ContainerServiceHealthCheckConfig-timeoutSeconds"></a>
The amount of time, in seconds, during which no response means a failed health check. You can specify between 2 and 60 seconds. The default value is `2`.
Type: Integer
Required: No

 ** unhealthyThreshold **   <a name="Lightsail-Type-ContainerServiceHealthCheckConfig-unhealthyThreshold"></a>
The number of consecutive health check failures required before moving the container to the `Unhealthy` state. The default value is `2`.
Type: Integer
Required: No

## See Also
<a name="API_ContainerServiceHealthCheckConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/ContainerServiceHealthCheckConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/ContainerServiceHealthCheckConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/ContainerServiceHealthCheckConfig)
