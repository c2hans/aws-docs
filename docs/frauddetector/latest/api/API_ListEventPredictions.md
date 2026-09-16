---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_ListEventPredictions.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# ListEventPredictions
<a name="API_ListEventPredictions"></a>

Gets a list of past predictions. The list can be filtered by detector ID, detector version ID, event ID, event type, or by specifying a time period. If filter is not specified, the most recent prediction is returned.

For example, the following filter lists all past predictions for `xyz` event type - `{ "eventType":{ "value": "xyz" }” } `

This is a paginated API. If you provide a null `maxResults`, this action will retrieve a maximum of 10 records per page. If you provide a `maxResults`, the value must be between 50 and 100. To get the next page results, provide the `nextToken` from the response as part of your request. A null `nextToken` fetches the records from the beginning.

## Request Syntax
<a name="API_ListEventPredictions_RequestSyntax"></a>

```
{
   "detectorId": {
      "value": "{{string}}"
   },
   "detectorVersionId": {
      "value": "{{string}}"
   },
   "eventId": {
      "value": "{{string}}"
   },
   "eventType": {
      "value": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "predictionTimeRange": {
      "endTime": "{{string}}",
      "startTime": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ListEventPredictions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [detectorId](#API_ListEventPredictions_RequestSyntax) **   <a name="FraudDetector-ListEventPredictions-request-detectorId"></a>
 The detector ID.
Type: [FilterCondition](API_FilterCondition.md) object
Required: No

 ** [detectorVersionId](#API_ListEventPredictions_RequestSyntax) **   <a name="FraudDetector-ListEventPredictions-request-detectorVersionId"></a>
 The detector version ID.
Type: [FilterCondition](API_FilterCondition.md) object
Required: No

 ** [eventId](#API_ListEventPredictions_RequestSyntax) **   <a name="FraudDetector-ListEventPredictions-request-eventId"></a>
 The event ID.
Type: [FilterCondition](API_FilterCondition.md) object
Required: No

 ** [eventType](#API_ListEventPredictions_RequestSyntax) **   <a name="FraudDetector-ListEventPredictions-request-eventType"></a>
 The event type associated with the detector.
Type: [FilterCondition](API_FilterCondition.md) object
Required: No

 ** [maxResults](#API_ListEventPredictions_RequestSyntax) **   <a name="FraudDetector-ListEventPredictions-request-maxResults"></a>
 The maximum number of predictions to return for the request.
Type: Integer
Valid Range: Minimum value of 50. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListEventPredictions_RequestSyntax) **   <a name="FraudDetector-ListEventPredictions-request-nextToken"></a>
 Identifies the next page of results to return. Use the token to make the call again to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.
Type: String
Required: No

 ** [predictionTimeRange](#API_ListEventPredictions_RequestSyntax) **   <a name="FraudDetector-ListEventPredictions-request-predictionTimeRange"></a>
 The time period for when the predictions were generated.
Type: [PredictionTimeRange](API_PredictionTimeRange.md) object
Required: No

## Response Syntax
<a name="API_ListEventPredictions_ResponseSyntax"></a>

```
{
   "eventPredictionSummaries": [
      {
         "detectorId": "string",
         "detectorVersionId": "string",
         "eventId": "string",
         "eventTimestamp": "string",
         "eventTypeName": "string",
         "predictionTimestamp": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEventPredictions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [eventPredictionSummaries](#API_ListEventPredictions_ResponseSyntax) **   <a name="FraudDetector-ListEventPredictions-response-eventPredictionSummaries"></a>
 The summary of the past predictions.
Type: Array of [EventPredictionSummary](API_EventPredictionSummary.md) objects

 ** [nextToken](#API_ListEventPredictions_ResponseSyntax) **   <a name="FraudDetector-ListEventPredictions-response-nextToken"></a>
 Identifies the next page of results to return. Use the token to make the call again to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.
Type: String

## Errors
<a name="API_ListEventPredictions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as `PutExternalModel`, that specifies a role that is not in your account.
HTTP Status Code: 400

 ** InternalServerException **
An exception indicating an internal server error.
HTTP Status Code: 500

 ** ThrottlingException **
An exception indicating a throttling error.
HTTP Status Code: 400

 ** ValidationException **
An exception indicating a specified value is not allowed.
HTTP Status Code: 400

## See Also
<a name="API_ListEventPredictions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/ListEventPredictions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/ListEventPredictions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/ListEventPredictions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/ListEventPredictions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/ListEventPredictions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/ListEventPredictions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/ListEventPredictions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/ListEventPredictions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/ListEventPredictions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/ListEventPredictions)
