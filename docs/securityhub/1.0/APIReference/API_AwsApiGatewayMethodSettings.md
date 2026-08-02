---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsApiGatewayMethodSettings.html
---

# AwsApiGatewayMethodSettings
<a name="API_AwsApiGatewayMethodSettings"></a>

Defines settings for a method for the stage.

## Contents
<a name="API_AwsApiGatewayMethodSettings_Contents"></a>

 ** CacheDataEncrypted **   <a name="securityhub-Type-AwsApiGatewayMethodSettings-CacheDataEncrypted"></a>
Indicates whether the cached responses are encrypted.
Type: Boolean
Required: No

 ** CacheTtlInSeconds **   <a name="securityhub-Type-AwsApiGatewayMethodSettings-CacheTtlInSeconds"></a>
Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL, the longer the response is cached.
Type: Integer
Required: No

 ** CachingEnabled **   <a name="securityhub-Type-AwsApiGatewayMethodSettings-CachingEnabled"></a>
Indicates whether responses are cached and returned for requests. For responses to be cached, a cache cluster must be enabled on the stage.
Type: Boolean
Required: No

 ** DataTraceEnabled **   <a name="securityhub-Type-AwsApiGatewayMethodSettings-DataTraceEnabled"></a>
Indicates whether data trace logging is enabled for the method. Data trace logging affects the log entries that are pushed to CloudWatch Logs.
Type: Boolean
Required: No

 ** HttpMethod **   <a name="securityhub-Type-AwsApiGatewayMethodSettings-HttpMethod"></a>
The HTTP method. You can use an asterisk (\*) as a wildcard to apply method settings to multiple methods.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LoggingLevel **   <a name="securityhub-Type-AwsApiGatewayMethodSettings-LoggingLevel"></a>
The logging level for this method. The logging level affects the log entries that are pushed to CloudWatch Logs.
If the logging level is `ERROR`, then the logs only include error-level entries.
If the logging level is `INFO`, then the logs include both `ERROR` events and extra informational events.
Valid values: `OFF` \| `ERROR` \| `INFO`
Type: String
Pattern: `.*\S.*`
Required: No

 ** MetricsEnabled **   <a name="securityhub-Type-AwsApiGatewayMethodSettings-MetricsEnabled"></a>
Indicates whether CloudWatch metrics are enabled for the method.
Type: Boolean
Required: No

 ** RequireAuthorizationForCacheControl **   <a name="securityhub-Type-AwsApiGatewayMethodSettings-RequireAuthorizationForCacheControl"></a>
Indicates whether authorization is required for a cache invalidation request.
Type: Boolean
Required: No

 ** ResourcePath **   <a name="securityhub-Type-AwsApiGatewayMethodSettings-ResourcePath"></a>
The resource path for this method. Forward slashes (/) are encoded as \~1 . The initial slash must include a forward slash.
For example, the path value `/resource/subresource` must be encoded as `/~1resource~1subresource`.
To specify the root path, use only a slash (/). You can use an asterisk (\*) as a wildcard to apply method settings to multiple methods.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ThrottlingBurstLimit **   <a name="securityhub-Type-AwsApiGatewayMethodSettings-ThrottlingBurstLimit"></a>
The throttling burst limit for the method.
Type: Integer
Required: No

 ** ThrottlingRateLimit **   <a name="securityhub-Type-AwsApiGatewayMethodSettings-ThrottlingRateLimit"></a>
The throttling rate limit for the method.
Type: Double
Required: No

 ** UnauthorizedCacheControlHeaderStrategy **   <a name="securityhub-Type-AwsApiGatewayMethodSettings-UnauthorizedCacheControlHeaderStrategy"></a>
Indicates how to handle unauthorized requests for cache invalidation.
Valid values: `FAIL_WITH_403` \| `SUCCEED_WITH_RESPONSE_HEADER` \| `SUCCEED_WITHOUT_RESPONSE_HEADER`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsApiGatewayMethodSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsApiGatewayMethodSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsApiGatewayMethodSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsApiGatewayMethodSettings)
