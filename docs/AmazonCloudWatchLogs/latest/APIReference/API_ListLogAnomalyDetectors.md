---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListLogAnomalyDetectors.html
---

# ListLogAnomalyDetectors
<a name="API_ListLogAnomalyDetectors"></a>

Retrieves a list of the log anomaly detectors in the account.

## Request Syntax
<a name="API_ListLogAnomalyDetectors_RequestSyntax"></a>

```
{
   "filterLogGroupArn": "{{string}}",
   "limit": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListLogAnomalyDetectors_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filterLogGroupArn](#API_ListLogAnomalyDetectors_RequestSyntax) **   <a name="CWL-ListLogAnomalyDetectors-request-filterLogGroupArn"></a>
Use this to optionally filter the results to only include anomaly detectors that are associated with the specified log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: No

 ** [limit](#API_ListLogAnomalyDetectors_RequestSyntax) **   <a name="CWL-ListLogAnomalyDetectors-request-limit"></a>
The maximum number of items to return. If you don't specify a value, the default maximum value of 50 items is used.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_ListLogAnomalyDetectors_RequestSyntax) **   <a name="CWL-ListLogAnomalyDetectors-request-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_ListLogAnomalyDetectors_ResponseSyntax"></a>

```
{
   "anomalyDetectors": [
      {
         "anomalyDetectorArn": "string",
         "anomalyDetectorStatus": "string",
         "anomalyVisibilityTime": number,
         "creationTimeStamp": number,
         "detectorName": "string",
         "evaluationFrequency": "string",
         "filterPattern": "string",
         "kmsKeyId": "string",
         "lastModifiedTimeStamp": number,
         "logGroupArnList": [ "string" ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListLogAnomalyDetectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [anomalyDetectors](#API_ListLogAnomalyDetectors_ResponseSyntax) **   <a name="CWL-ListLogAnomalyDetectors-response-anomalyDetectors"></a>
An array of structures, where each structure in the array contains information about one anomaly detector.
Type: Array of [AnomalyDetector](API_AnomalyDetector.md) objects

 ** [nextToken](#API_ListLogAnomalyDetectors_ResponseSyntax) **   <a name="CWL-ListLogAnomalyDetectors-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListLogAnomalyDetectors_Errors"></a>

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
<a name="API_ListLogAnomalyDetectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/ListLogAnomalyDetectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/ListLogAnomalyDetectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ListLogAnomalyDetectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/ListLogAnomalyDetectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ListLogAnomalyDetectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/ListLogAnomalyDetectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/ListLogAnomalyDetectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/ListLogAnomalyDetectors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/ListLogAnomalyDetectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ListLogAnomalyDetectors)
