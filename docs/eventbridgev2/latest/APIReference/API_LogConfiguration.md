---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_LogConfiguration.html
---

# LogConfiguration
<a name="API_LogConfiguration"></a>

Log configuration for a subscriber.

## Contents
<a name="API_LogConfiguration_Contents"></a>

 ** IncludePayload **   <a name="eventbridgev2-Type-LogConfiguration-IncludePayload"></a>
Whether the customer event payload is embedded in log records. Defaults to ON\_ERROR\_ONLY.
Type: String
Valid Values: `FULL | ON_ERROR_ONLY`
Required: No

 ** Level **   <a name="eventbridgev2-Type-LogConfiguration-Level"></a>
Minimum log level. Records below this level are not emitted. Defaults to OFF.
Type: String
Valid Values: `OFF | ERROR | INFO`
Required: No

## See Also
<a name="API_LogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/LogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/LogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/LogConfiguration)
