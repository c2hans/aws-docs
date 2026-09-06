---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_LogEventConfiguration.html
---

# LogEventConfiguration
<a name="API_LogEventConfiguration"></a>

 Configuration for event-based logging that specifies which event types to log and their logging settings. Used for account-level logging overrides.

## Contents
<a name="API_LogEventConfiguration_Contents"></a>

 ** eventType **   <a name="iot-Type-LogEventConfiguration-eventType"></a>
 The type of event to log. These include event types like Connect, Publish, and Disconnect.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** logDestination **   <a name="iot-Type-LogEventConfiguration-logDestination"></a>
 CloudWatch Log Group for event-based logging. Specifies where log events should be sent. The log destination for event-based logging overrides default Log Group for the specified event type and applies to all resources associated with that event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[.\-_/#A-Za-z0-9]+$`
Required: No

 ** logLevel **   <a name="iot-Type-LogEventConfiguration-logLevel"></a>
 The logging level for the specified event type. Determines the verbosity of log messages generated for this event type.
Type: String
Valid Values: `DEBUG | INFO | ERROR | WARN | DISABLED`
Required: No

## See Also
<a name="API_LogEventConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/LogEventConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/LogEventConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/LogEventConfiguration)
