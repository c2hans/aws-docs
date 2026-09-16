---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogAnomalyDetector.html
---

# CreateLogAnomalyDetector
<a name="API_CreateLogAnomalyDetector"></a>

Creates an *anomaly detector* that regularly scans one or more log groups and look for patterns and anomalies in the logs.

An anomaly detector can help surface issues by automatically discovering anomalies in your log event traffic. An anomaly detector uses machine learning algorithms to scan log events and find *patterns*. A pattern is a shared text structure that recurs among your log fields. Patterns provide a useful tool for analyzing large sets of logs because a large number of log events can often be compressed into a few patterns.

The anomaly detector uses pattern recognition to find `anomalies`, which are unusual log events. It uses the `evaluationFrequency` to compare current log events and patterns with trained baselines.

Fields within a pattern are called *tokens*. Fields that vary within a pattern, such as a request ID or timestamp, are referred to as *dynamic tokens* and represented by `<*>`.

The following is an example of a pattern:

 `[INFO] Request time: <*> ms`

This pattern represents log events like `[INFO] Request time: 327 ms` and other similar log events that differ only by the number, in this csse 327. When the pattern is displayed, the different numbers are replaced by `<*>`

**Note**
Any parts of log events that are masked as sensitive data are not scanned for anomalies. For more information about masking sensitive data, see [Help protect sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html).

## Request Syntax
<a name="API_CreateLogAnomalyDetector_RequestSyntax"></a>

```
{
   "anomalyVisibilityTime": {{number}},
   "detectorName": "{{string}}",
   "evaluationFrequency": "{{string}}",
   "filterPattern": "{{string}}",
   "kmsKeyId": "{{string}}",
   "logGroupArnList": [ "{{string}}" ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateLogAnomalyDetector_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [anomalyVisibilityTime](#API_CreateLogAnomalyDetector_RequestSyntax) **   <a name="CWL-CreateLogAnomalyDetector-request-anomalyVisibilityTime"></a>
The number of days to have visibility on an anomaly. After this time period has elapsed for an anomaly, it will be automatically baselined and the anomaly detector will treat new occurrences of a similar anomaly as normal. Therefore, if you do not correct the cause of an anomaly during the time period specified in `anomalyVisibilityTime`, it will be considered normal going forward and will not be detected as an anomaly.
Type: Long
Valid Range: Minimum value of 7. Maximum value of 90.
Required: No

 ** [detectorName](#API_CreateLogAnomalyDetector_RequestSyntax) **   <a name="CWL-CreateLogAnomalyDetector-request-detectorName"></a>
A name for this anomaly detector.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [evaluationFrequency](#API_CreateLogAnomalyDetector_RequestSyntax) **   <a name="CWL-CreateLogAnomalyDetector-request-evaluationFrequency"></a>
Specifies how often the anomaly detector is to run and look for anomalies. Set this value according to the frequency that the log group receives new logs. For example, if the log group receives new log events every 10 minutes, then 15 minutes might be a good setting for `evaluationFrequency` .
Type: String
Valid Values: `ONE_MIN | FIVE_MIN | TEN_MIN | FIFTEEN_MIN | THIRTY_MIN | ONE_HOUR`
Required: No

 ** [filterPattern](#API_CreateLogAnomalyDetector_RequestSyntax) **   <a name="CWL-CreateLogAnomalyDetector-request-filterPattern"></a>
You can use this parameter to limit the anomaly detection model to examine only log events that match the pattern you specify here. For more information, see [Filter and Pattern Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [kmsKeyId](#API_CreateLogAnomalyDetector_RequestSyntax) **   <a name="CWL-CreateLogAnomalyDetector-request-kmsKeyId"></a>
Optionally assigns a AWS KMS key to secure this anomaly detector and its findings. If a key is assigned, the anomalies found and the model used by this detector are encrypted at rest with the key. If a key is assigned to an anomaly detector, a user must have permissions for both this key and for the anomaly detector to retrieve information about the anomalies that it finds.
 Make sure the value provided is a valid AWS KMS key ARN. For more information about using a AWS KMS key and to see the required IAM policy, see [Use a AWS KMS key with an anomaly detector](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection-KMS.html).
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^arn:aws[a-z\-]*:kms:[-a-z0-9]*:[0-9]*:key/[-a-z0-9]*$`
Required: No

 ** [logGroupArnList](#API_CreateLogAnomalyDetector_RequestSyntax) **   <a name="CWL-CreateLogAnomalyDetector-request-logGroupArnList"></a>
An array containing the ARN of the log group that this anomaly detector will watch. You can specify only one log group ARN.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: Yes

 ** [tags](#API_CreateLogAnomalyDetector_RequestSyntax) **   <a name="CWL-CreateLogAnomalyDetector-request-tags"></a>
An optional list of key-value pairs to associate with the resource.
For more information about tagging, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_CreateLogAnomalyDetector_ResponseSyntax"></a>

```
{
   "anomalyDetectorArn": "string"
}
```

## Response Elements
<a name="API_CreateLogAnomalyDetector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [anomalyDetectorArn](#API_CreateLogAnomalyDetector_ResponseSyntax) **   <a name="CWL-CreateLogAnomalyDetector-response-anomalyDetectorArn"></a>
The ARN of the log anomaly detector that you just created.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\w#+=/:,.@-]*`

## Errors
<a name="API_CreateLogAnomalyDetector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** LimitExceededException **
You have reached the maximum number of resources that can be created.
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
<a name="API_CreateLogAnomalyDetector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/CreateLogAnomalyDetector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/CreateLogAnomalyDetector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/CreateLogAnomalyDetector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/CreateLogAnomalyDetector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/CreateLogAnomalyDetector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/CreateLogAnomalyDetector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/CreateLogAnomalyDetector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/CreateLogAnomalyDetector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/CreateLogAnomalyDetector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/CreateLogAnomalyDetector)
