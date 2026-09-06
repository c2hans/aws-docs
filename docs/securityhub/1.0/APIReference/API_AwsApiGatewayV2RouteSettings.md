---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsApiGatewayV2RouteSettings.html
---

# AwsApiGatewayV2RouteSettings
<a name="API_AwsApiGatewayV2RouteSettings"></a>

Contains route settings for a stage.

## Contents
<a name="API_AwsApiGatewayV2RouteSettings_Contents"></a>

 ** DataTraceEnabled **   <a name="securityhub-Type-AwsApiGatewayV2RouteSettings-DataTraceEnabled"></a>
Indicates whether data trace logging is enabled. Data trace logging affects the log entries that are pushed to CloudWatch Logs. Supported only for WebSocket APIs.
Type: Boolean
Required: No

 ** DetailedMetricsEnabled **   <a name="securityhub-Type-AwsApiGatewayV2RouteSettings-DetailedMetricsEnabled"></a>
Indicates whether detailed metrics are enabled.
Type: Boolean
Required: No

 ** LoggingLevel **   <a name="securityhub-Type-AwsApiGatewayV2RouteSettings-LoggingLevel"></a>
The logging level. The logging level affects the log entries that are pushed to CloudWatch Logs. Supported only for WebSocket APIs.
If the logging level is `ERROR`, then the logs only include error-level entries.
If the logging level is `INFO`, then the logs include both `ERROR` events and extra informational events.
Valid values: `OFF` \| `ERROR` \| `INFO`
Type: String
Pattern: `.*\S.*`
Required: No

 ** ThrottlingBurstLimit **   <a name="securityhub-Type-AwsApiGatewayV2RouteSettings-ThrottlingBurstLimit"></a>
The throttling burst limit.
Type: Integer
Required: No

 ** ThrottlingRateLimit **   <a name="securityhub-Type-AwsApiGatewayV2RouteSettings-ThrottlingRateLimit"></a>
The throttling rate limit.
Type: Double
Required: No

## See Also
<a name="API_AwsApiGatewayV2RouteSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsApiGatewayV2RouteSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsApiGatewayV2RouteSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsApiGatewayV2RouteSettings)
