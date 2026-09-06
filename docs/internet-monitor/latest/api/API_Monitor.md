---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_Monitor.html
---

# Monitor
<a name="API_Monitor"></a>

The description of and information about a monitor in Internet Monitor.

## Contents
<a name="API_Monitor_Contents"></a>

 ** MonitorArn **   <a name="internetmonitor-Type-Monitor-MonitorArn"></a>
The Amazon Resource Name (ARN) of the monitor.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 512.
Pattern: `arn:.*`
Required: Yes

 ** MonitorName **   <a name="internetmonitor-Type-Monitor-MonitorName"></a>
The name of the monitor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** Status **   <a name="internetmonitor-Type-Monitor-Status"></a>
The status of a monitor.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR`
Required: Yes

 ** ProcessingStatus **   <a name="internetmonitor-Type-Monitor-ProcessingStatus"></a>
The health of data processing for the monitor.
Type: String
Valid Values: `OK | INACTIVE | COLLECTING_DATA | INSUFFICIENT_DATA | FAULT_SERVICE | FAULT_ACCESS_CLOUDWATCH`
Required: No

## See Also
<a name="API_Monitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/Monitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/Monitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/Monitor)
