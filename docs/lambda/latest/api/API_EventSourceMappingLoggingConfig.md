---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_EventSourceMappingLoggingConfig.html
---

# EventSourceMappingLoggingConfig
<a name="API_EventSourceMappingLoggingConfig"></a>

(Amazon MSK, and self-managed Apache Kafka only) The logging configuration for your event source. Use this configuration object to define the level of logs for your event source mapping.

## Contents
<a name="API_EventSourceMappingLoggingConfig_Contents"></a>

 ** SystemLogLevel **   <a name="lambda-Type-EventSourceMappingLoggingConfig-SystemLogLevel"></a>
 The log level you want your event source mapping to use. Lambda event poller only sends system logs at the selected level of detail and lower, where `DEBUG` is the highest level and `WARN` is the lowest. For more information about these metrics, see [ Event source mapping logging](https://docs.aws.amazon.com/lambda/latest/dg/esm-logging.html).
Type: String
Valid Values: `DEBUG | INFO | WARN`
Required: No

## See Also
<a name="API_EventSourceMappingLoggingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/EventSourceMappingLoggingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/EventSourceMappingLoggingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/EventSourceMappingLoggingConfig)
