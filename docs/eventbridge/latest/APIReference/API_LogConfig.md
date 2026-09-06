---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_LogConfig.html
---

# LogConfig
<a name="API_LogConfig"></a>

The logging configuration settings for the event bus.

For more information, see [Configuring logs for event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html) in the *EventBridge User Guide*.

## Contents
<a name="API_LogConfig_Contents"></a>

 ** IncludeDetail **   <a name="eventbridge-Type-LogConfig-IncludeDetail"></a>
Whether EventBridge include detailed event information in the records it generates. Detailed data can be useful for troubleshooting and debugging. This information includes details of the event itself, as well as target details.
For more information, see [Including detail data in event bus logs](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html#eb-event-logs-data) in the *EventBridge User Guide*.
Type: String
Valid Values: `NONE | FULL`
Required: No

 ** Level **   <a name="eventbridge-Type-LogConfig-Level"></a>
The level of logging detail to include. This applies to all log destinations for the event bus.
For more information, see [Specifying event bus log level](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html#eb-event-bus-logs-level) in the *EventBridge User Guide*.
Type: String
Valid Values: `OFF | ERROR | INFO | TRACE`
Required: No

## See Also
<a name="API_LogConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/LogConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/LogConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/LogConfig)
