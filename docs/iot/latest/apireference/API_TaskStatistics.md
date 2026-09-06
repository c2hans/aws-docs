---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_TaskStatistics.html
---

# TaskStatistics
<a name="API_TaskStatistics"></a>

Statistics for the checks performed during the audit.

## Contents
<a name="API_TaskStatistics_Contents"></a>

 ** canceledChecks **   <a name="iot-Type-TaskStatistics-canceledChecks"></a>
The number of checks that did not run because the audit was canceled.
Type: Integer
Required: No

 ** compliantChecks **   <a name="iot-Type-TaskStatistics-compliantChecks"></a>
The number of checks that found compliant resources.
Type: Integer
Required: No

 ** failedChecks **   <a name="iot-Type-TaskStatistics-failedChecks"></a>
The number of checks.
Type: Integer
Required: No

 ** inProgressChecks **   <a name="iot-Type-TaskStatistics-inProgressChecks"></a>
The number of checks in progress.
Type: Integer
Required: No

 ** nonCompliantChecks **   <a name="iot-Type-TaskStatistics-nonCompliantChecks"></a>
The number of checks that found noncompliant resources.
Type: Integer
Required: No

 ** totalChecks **   <a name="iot-Type-TaskStatistics-totalChecks"></a>
The number of checks in this audit.
Type: Integer
Required: No

 ** waitingForDataCollectionChecks **   <a name="iot-Type-TaskStatistics-waitingForDataCollectionChecks"></a>
The number of checks waiting for data collection.
Type: Integer
Required: No

## See Also
<a name="API_TaskStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/TaskStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/TaskStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/TaskStatistics)
