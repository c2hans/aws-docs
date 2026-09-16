---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateLogAnomalyDetector.html
---

# UpdateLogAnomalyDetector
<a name="API_UpdateLogAnomalyDetector"></a>

Updates an existing log anomaly detector.

## Request Syntax
<a name="API_UpdateLogAnomalyDetector_RequestSyntax"></a>

```
{
   "anomalyDetectorArn": "{{string}}",
   "anomalyVisibilityTime": {{number}},
   "enabled": {{boolean}},
   "evaluationFrequency": "{{string}}",
   "filterPattern": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateLogAnomalyDetector_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [anomalyDetectorArn](#API_UpdateLogAnomalyDetector_RequestSyntax) **   <a name="CWL-UpdateLogAnomalyDetector-request-anomalyDetectorArn"></a>
The ARN of the anomaly detector that you want to update.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\w#+=/:,.@-]*`
Required: Yes

 ** [anomalyVisibilityTime](#API_UpdateLogAnomalyDetector_RequestSyntax) **   <a name="CWL-UpdateLogAnomalyDetector-request-anomalyVisibilityTime"></a>
The number of days to use as the life cycle of anomalies. After this time, anomalies are automatically baselined and the anomaly detector model will treat new occurrences of similar event as normal. Therefore, if you do not correct the cause of an anomaly during this time, it will be considered normal going forward and will not be detected.
Type: Long
Valid Range: Minimum value of 7. Maximum value of 90.
Required: No

 ** [enabled](#API_UpdateLogAnomalyDetector_RequestSyntax) **   <a name="CWL-UpdateLogAnomalyDetector-request-enabled"></a>
Use this parameter to pause or restart the anomaly detector.
Type: Boolean
Required: Yes

 ** [evaluationFrequency](#API_UpdateLogAnomalyDetector_RequestSyntax) **   <a name="CWL-UpdateLogAnomalyDetector-request-evaluationFrequency"></a>
Specifies how often the anomaly detector runs and look for anomalies. Set this value according to the frequency that the log group receives new logs. For example, if the log group receives new log events every 10 minutes, then setting `evaluationFrequency` to `FIFTEEN_MIN` might be appropriate.
Type: String
Valid Values: `ONE_MIN | FIVE_MIN | TEN_MIN | FIFTEEN_MIN | THIRTY_MIN | ONE_HOUR`
Required: No

 ** [filterPattern](#API_UpdateLogAnomalyDetector_RequestSyntax) **   <a name="CWL-UpdateLogAnomalyDetector-request-filterPattern"></a>
A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event can contain timestamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## Response Elements
<a name="API_UpdateLogAnomalyDetector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLogAnomalyDetector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** OperationAbortedException **
Multiple concurrent requests to update the same resource were in conflict.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## See Also
<a name="API_UpdateLogAnomalyDetector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/UpdateLogAnomalyDetector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/UpdateLogAnomalyDetector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/UpdateLogAnomalyDetector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/UpdateLogAnomalyDetector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/UpdateLogAnomalyDetector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/UpdateLogAnomalyDetector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/UpdateLogAnomalyDetector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/UpdateLogAnomalyDetector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/UpdateLogAnomalyDetector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/UpdateLogAnomalyDetector)
