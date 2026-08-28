---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_MethodSetting.html
---

# MethodSetting
<a name="API_MethodSetting"></a>

Specifies the method setting properties.

## Contents
<a name="API_MethodSetting_Contents"></a>

 ** cacheDataEncrypted **   <a name="apigw-Type-MethodSetting-cacheDataEncrypted"></a>
Specifies whether the cached responses are encrypted.
Type: Boolean
Required: No

 ** cacheTtlInSeconds **   <a name="apigw-Type-MethodSetting-cacheTtlInSeconds"></a>
Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL, the longer the response will be cached.
Type: Integer
Required: No

 ** cachingEnabled **   <a name="apigw-Type-MethodSetting-cachingEnabled"></a>
Specifies whether responses should be cached and returned for requests. A cache cluster must be enabled on the stage for responses to be cached.
Type: Boolean
Required: No

 ** dataTraceEnabled **   <a name="apigw-Type-MethodSetting-dataTraceEnabled"></a>
Specifies whether data trace logging is enabled for this method, which affects the log entries pushed to Amazon CloudWatch Logs. This can be useful to troubleshoot APIs, but can result in logging sensitive data. We recommend that you don't enable this option for production APIs.
Type: Boolean
Required: No

 ** loggingLevel **   <a name="apigw-Type-MethodSetting-loggingLevel"></a>
Specifies the logging level for this method, which affects the log entries pushed to Amazon CloudWatch Logs. Valid values are `OFF`, `ERROR`, and `INFO`. Choose `ERROR` to write only error-level entries to CloudWatch Logs, or choose `INFO` to include all `ERROR` events as well as extra informational events.
Type: String
Required: No

 ** metricsEnabled **   <a name="apigw-Type-MethodSetting-metricsEnabled"></a>
Specifies whether Amazon CloudWatch metrics are enabled for this method.
Type: Boolean
Required: No

 ** requireAuthorizationForCacheControl **   <a name="apigw-Type-MethodSetting-requireAuthorizationForCacheControl"></a>
Specifies whether authorization is required for a cache invalidation request.
Type: Boolean
Required: No

 ** throttlingBurstLimit **   <a name="apigw-Type-MethodSetting-throttlingBurstLimit"></a>
Specifies the throttling burst limit.
Type: Integer
Required: No

 ** throttlingRateLimit **   <a name="apigw-Type-MethodSetting-throttlingRateLimit"></a>
Specifies the throttling rate limit.
Type: Double
Required: No

 ** unauthorizedCacheControlHeaderStrategy **   <a name="apigw-Type-MethodSetting-unauthorizedCacheControlHeaderStrategy"></a>
Specifies how to handle unauthorized requests for cache invalidation.
Type: String
Valid Values: `FAIL_WITH_403 | SUCCEED_WITH_RESPONSE_HEADER | SUCCEED_WITHOUT_RESPONSE_HEADER`
Required: No

## See Also
<a name="API_MethodSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/MethodSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/MethodSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/MethodSetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
