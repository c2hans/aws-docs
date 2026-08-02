---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_LogLocation.html
---

# LogLocation
<a name="API_LogLocation"></a>

The log location for a task, specifying where task execution logs are stored.

## Contents
<a name="API_LogLocation_Contents"></a>

 ** cloudWatchLog **   <a name="securityagent-Type-LogLocation-cloudWatchLog"></a>
The CloudWatch Logs location for the task logs.
Type: [CloudWatchLog](API_CloudWatchLog.md) object
Required: No

 ** logType **   <a name="securityagent-Type-LogLocation-logType"></a>
The type of log storage. Currently, only CLOUDWATCH is supported.
Type: String
Valid Values: `CLOUDWATCH`
Required: No

## See Also
<a name="API_LogLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/LogLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/LogLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/LogLocation)
