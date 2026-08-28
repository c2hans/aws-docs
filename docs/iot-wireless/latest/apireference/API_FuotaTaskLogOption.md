---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_FuotaTaskLogOption.html
---

# FuotaTaskLogOption
<a name="API_FuotaTaskLogOption"></a>

The log options for FUOTA tasks and can be used to set log levels for a specific type of FUOTA task.

## Contents
<a name="API_FuotaTaskLogOption_Contents"></a>

 ** LogLevel **   <a name="iotwireless-Type-FuotaTaskLogOption-LogLevel"></a>
The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.
Type: String
Valid Values: `INFO | ERROR | DISABLED`
Required: Yes

 ** Type **   <a name="iotwireless-Type-FuotaTaskLogOption-Type"></a>
The FUOTA task type.
Type: String
Valid Values: `LoRaWAN`
Required: Yes

 ** Events **   <a name="iotwireless-Type-FuotaTaskLogOption-Events"></a>
The list of FUOTA task event log options.
Type: Array of [FuotaTaskEventLogOption](API_FuotaTaskEventLogOption.md) objects
Required: No

## See Also
<a name="API_FuotaTaskLogOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/FuotaTaskLogOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/FuotaTaskLogOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/FuotaTaskLogOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
