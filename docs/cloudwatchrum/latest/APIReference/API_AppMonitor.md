---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_AppMonitor.html
---

# AppMonitor
<a name="API_AppMonitor"></a>

A RUM app monitor collects telemetry data from your application and sends that data to RUM. The data includes performance and reliability information such as page load time, client-side errors, and user behavior.

## Contents
<a name="API_AppMonitor_Contents"></a>

 ** AppMonitorConfiguration **   <a name="cloudwatchrum-Type-AppMonitor-AppMonitorConfiguration"></a>
A structure that contains much of the configuration data for the app monitor.
Type: [AppMonitorConfiguration](API_AppMonitorConfiguration.md) object
Required: No

 ** Created **   <a name="cloudwatchrum-Type-AppMonitor-Created"></a>
The date and time that this app monitor was created.
Type: String
Length Constraints: Fixed length of 19.
Required: No

 ** CustomEvents **   <a name="cloudwatchrum-Type-AppMonitor-CustomEvents"></a>
Specifies whether this app monitor allows the web client to define and send custom events.
For more information about custom events, see [Send custom events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-custom-events.html).
Type: [CustomEvents](API_CustomEvents.md) object
Required: No

 ** DataStorage **   <a name="cloudwatchrum-Type-AppMonitor-DataStorage"></a>
A structure that contains information about whether this app monitor stores a copy of the telemetry data that RUM collects using CloudWatch Logs.
Type: [DataStorage](API_DataStorage.md) object
Required: No

 ** DeobfuscationConfiguration **   <a name="cloudwatchrum-Type-AppMonitor-DeobfuscationConfiguration"></a>
 A structure that contains the configuration for how an app monitor can deobfuscate stack traces.
Type: [DeobfuscationConfiguration](API_DeobfuscationConfiguration.md) object
Required: No

 ** Domain **   <a name="cloudwatchrum-Type-AppMonitor-Domain"></a>
The top-level internet domain name for which your application has administrative authority.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(localhost)$|^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|(?=^[a-zA-Z0-9\.\*-]{4,253}$)(?!.*\.-)(?!.*-\.)(?!.*\.\.)(?!.*[^\.]{64,})^(\*\.)?(?![-\.\*])[^\*]{1,}\.(\*|(?!.*--)(?=.*[a-zA-Z])[^\*]{1,}[^\*-])`
Required: No

 ** DomainList **   <a name="cloudwatchrum-Type-AppMonitor-DomainList"></a>
 List the domain names for which your application has administrative authority.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(localhost)$|^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|(?=^[a-zA-Z0-9\.\*-]{4,253}$)(?!.*\.-)(?!.*-\.)(?!.*\.\.)(?!.*[^\.]{64,})^(\*\.)?(?![-\.\*])[^\*]{1,}\.(\*|(?!.*--)(?=.*[a-zA-Z])[^\*]{1,}[^\*-])`
Required: No

 ** Id **   <a name="cloudwatchrum-Type-AppMonitor-Id"></a>
The unique ID of this app monitor.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: No

 ** LastModified **   <a name="cloudwatchrum-Type-AppMonitor-LastModified"></a>
The date and time of the most recent changes to this app monitor's configuration.
Type: String
Length Constraints: Fixed length of 19.
Required: No

 ** Name **   <a name="cloudwatchrum-Type-AppMonitor-Name"></a>
The name of the app monitor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!\.)[\.\-_#A-Za-z0-9]+`
Required: No

 ** State **   <a name="cloudwatchrum-Type-AppMonitor-State"></a>
The current state of the app monitor.
Type: String
Valid Values: `CREATED | DELETING | ACTIVE`
Required: No

 ** Tags **   <a name="cloudwatchrum-Type-AppMonitor-Tags"></a>
The list of tag keys and values associated with this app monitor.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_AppMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/AppMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/AppMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/AppMonitor)
