---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceConnectAccessLogConfiguration.html
---

# ServiceConnectAccessLogConfiguration
<a name="API_ServiceConnectAccessLogConfiguration"></a>

Configuration for Service Connect access logging. Access logs provide detailed information about requests made to your service, including request patterns, response codes, and timing data for debugging and monitoring purposes.

**Note**
To enable access logs, you must also specify a `logConfiguration` in the `serviceConnectConfiguration`.

## Contents
<a name="API_ServiceConnectAccessLogConfiguration_Contents"></a>

 ** format **   <a name="ECS-Type-ServiceConnectAccessLogConfiguration-format"></a>
The format for Service Connect access log output. Choose TEXT for human-readable logs or JSON for structured data that integrates well with log analysis tools.
Type: String
Valid Values: `TEXT | JSON`
Required: Yes

 ** includeQueryParameters **   <a name="ECS-Type-ServiceConnectAccessLogConfiguration-includeQueryParameters"></a>
Specifies whether to include query parameters in Service Connect access logs.
When enabled, query parameters from HTTP requests are included in the access logs. Consider security and privacy implications when enabling this feature, as query parameters may contain sensitive information such as request IDs and tokens. By default, this parameter is `DISABLED`.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

## See Also
<a name="API_ServiceConnectAccessLogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceConnectAccessLogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceConnectAccessLogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceConnectAccessLogConfiguration)
