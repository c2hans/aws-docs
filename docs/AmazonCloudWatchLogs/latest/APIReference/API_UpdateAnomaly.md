---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateAnomaly.html
---

# UpdateAnomaly
<a name="API_UpdateAnomaly"></a>

Use this operation to *suppress* anomaly detection for a specified anomaly or pattern. If you suppress an anomaly, CloudWatch Logs won't report new occurrences of that anomaly and won't update that anomaly with new data. If you suppress a pattern, CloudWatch Logs won't report any anomalies related to that pattern.

You must specify either `anomalyId` or `patternId`, but you can't specify both parameters in the same operation.

If you have previously used this operation to suppress detection of a pattern or anomaly, you can use it again to cause CloudWatch Logs to end the suppression. To do this, use this operation and specify the anomaly or pattern to stop suppressing, and omit the `suppressionType` and `suppressionPeriod` parameters.

## Request Syntax
<a name="API_UpdateAnomaly_RequestSyntax"></a>

```
{
   "anomalyDetectorArn": "{{string}}",
   "anomalyId": "{{string}}",
   "baseline": {{boolean}},
   "patternId": "{{string}}",
   "suppressionPeriod": {
      "suppressionUnit": "{{string}}",
      "value": {{number}}
   },
   "suppressionType": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateAnomaly_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [anomalyDetectorArn](#API_UpdateAnomaly_RequestSyntax) **   <a name="CWL-UpdateAnomaly-request-anomalyDetectorArn"></a>
The ARN of the anomaly detector that this operation is to act on.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\w#+=/:,.@-]*`
Required: Yes

 ** [anomalyId](#API_UpdateAnomaly_RequestSyntax) **   <a name="CWL-UpdateAnomaly-request-anomalyId"></a>
If you are suppressing or unsuppressing an anomaly, specify its unique ID here. You can find anomaly IDs by using the [ListAnomalies](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListAnomalies.html) operation.
Type: String
Length Constraints: Fixed length of 36.
Required: No

 ** [baseline](#API_UpdateAnomaly_RequestSyntax) **   <a name="CWL-UpdateAnomaly-request-baseline"></a>
Set this to `true` to prevent CloudWatch Logs from displaying this behavior as an anomaly in the future. The behavior is then treated as baseline behavior. However, if similar but more severe occurrences of this behavior occur in the future, those will still be reported as anomalies.
The default is `false`
Type: Boolean
Required: No

 ** [patternId](#API_UpdateAnomaly_RequestSyntax) **   <a name="CWL-UpdateAnomaly-request-patternId"></a>
If you are suppressing or unsuppressing an pattern, specify its unique ID here. You can find pattern IDs by using the [ListAnomalies](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListAnomalies.html) operation.
Type: String
Length Constraints: Fixed length of 32.
Required: No

 ** [suppressionPeriod](#API_UpdateAnomaly_RequestSyntax) **   <a name="CWL-UpdateAnomaly-request-suppressionPeriod"></a>
If you are temporarily suppressing an anomaly or pattern, use this structure to specify how long the suppression is to last.
Type: [SuppressionPeriod](API_SuppressionPeriod.md) object
Required: No

 ** [suppressionType](#API_UpdateAnomaly_RequestSyntax) **   <a name="CWL-UpdateAnomaly-request-suppressionType"></a>
Use this to specify whether the suppression to be temporary or infinite. If you specify `LIMITED`, you must also specify a `suppressionPeriod`. If you specify `INFINITE`, any value for `suppressionPeriod` is ignored.
Type: String
Valid Values: `LIMITED | INFINITE`
Required: No

## Response Elements
<a name="API_UpdateAnomaly_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateAnomaly_Errors"></a>

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
<a name="API_UpdateAnomaly_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/UpdateAnomaly)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/UpdateAnomaly)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/UpdateAnomaly)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/UpdateAnomaly)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/UpdateAnomaly)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/UpdateAnomaly)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/UpdateAnomaly)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/UpdateAnomaly)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/UpdateAnomaly)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/UpdateAnomaly)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
