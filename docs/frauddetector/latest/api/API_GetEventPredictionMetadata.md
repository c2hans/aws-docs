---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_GetEventPredictionMetadata.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# GetEventPredictionMetadata
<a name="API_GetEventPredictionMetadata"></a>

 Gets details of the past fraud predictions for the specified event ID, event type, detector ID, and detector version ID that was generated in the specified time period.

## Request Syntax
<a name="API_GetEventPredictionMetadata_RequestSyntax"></a>

```
{
   "detectorId": "{{string}}",
   "detectorVersionId": "{{string}}",
   "eventId": "{{string}}",
   "eventTypeName": "{{string}}",
   "predictionTimestamp": "{{string}}"
}
```

## Request Parameters
<a name="API_GetEventPredictionMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [detectorId](#API_GetEventPredictionMetadata_RequestSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-request-detectorId"></a>
 The detector ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [detectorVersionId](#API_GetEventPredictionMetadata_RequestSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-request-detectorVersionId"></a>
 The detector version ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^([1-9][0-9]*)$`
Required: Yes

 ** [eventId](#API_GetEventPredictionMetadata_RequestSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-request-eventId"></a>
 The event ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [eventTypeName](#API_GetEventPredictionMetadata_RequestSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-request-eventTypeName"></a>
 The event type associated with the detector specified for the prediction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [predictionTimestamp](#API_GetEventPredictionMetadata_RequestSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-request-predictionTimestamp"></a>
 The timestamp that defines when the prediction was generated. The timestamp must be specified using ISO 8601 standard in UTC.
We recommend calling [ListEventPredictions](https://docs.aws.amazon.com/frauddetector/latest/api/API_ListEventPredictions.html) first, and using the `predictionTimestamp` value in the response to provide an accurate prediction timestamp value.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: Yes

## Response Syntax
<a name="API_GetEventPredictionMetadata_ResponseSyntax"></a>

```
{
   "detectorId": "string",
   "detectorVersionId": "string",
   "detectorVersionStatus": "string",
   "entityId": "string",
   "entityType": "string",
   "evaluatedExternalModels": [
      {
         "inputVariables": {
            "string" : "string"
         },
         "modelEndpoint": "string",
         "outputVariables": {
            "string" : "string"
         },
         "useEventVariables": boolean
      }
   ],
   "evaluatedModelVersions": [
      {
         "evaluations": [
            {
               "evaluationScore": "string",
               "outputVariableName": "string",
               "predictionExplanations": {
                  "aggregatedVariablesImpactExplanations": [
                     {
                        "eventVariableNames": [ "string" ],
                        "logOddsImpact": number,
                        "relativeImpact": "string"
                     }
                  ],
                  "variableImpactExplanations": [
                     {
                        "eventVariableName": "string",
                        "logOddsImpact": number,
                        "relativeImpact": "string"
                     }
                  ]
               }
            }
         ],
         "modelId": "string",
         "modelType": "string",
         "modelVersion": "string"
      }
   ],
   "eventId": "string",
   "eventTimestamp": "string",
   "eventTypeName": "string",
   "eventVariables": [
      {
         "name": "string",
         "source": "string",
         "value": "string"
      }
   ],
   "outcomes": [ "string" ],
   "predictionTimestamp": "string",
   "ruleExecutionMode": "string",
   "rules": [
      {
         "evaluated": boolean,
         "expression": "string",
         "expressionWithValues": "string",
         "matched": boolean,
         "outcomes": [ "string" ],
         "ruleId": "string",
         "ruleVersion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetEventPredictionMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [detectorId](#API_GetEventPredictionMetadata_ResponseSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-response-detectorId"></a>
 The detector ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`

 ** [detectorVersionId](#API_GetEventPredictionMetadata_ResponseSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-response-detectorVersionId"></a>
 The detector version ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^([1-9][0-9]*)$`

 ** [detectorVersionStatus](#API_GetEventPredictionMetadata_ResponseSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-response-detectorVersionStatus"></a>
 The status of the detector version.
Type: String

 ** [entityId](#API_GetEventPredictionMetadata_ResponseSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-response-entityId"></a>
 The entity ID.
Type: String

 ** [entityType](#API_GetEventPredictionMetadata_ResponseSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-response-entityType"></a>
 The entity type.
Type: String

 ** [evaluatedExternalModels](#API_GetEventPredictionMetadata_ResponseSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-response-evaluatedExternalModels"></a>
 External (Amazon SageMaker) models that were evaluated for generating predictions.
Type: Array of [EvaluatedExternalModel](API_EvaluatedExternalModel.md) objects

 ** [evaluatedModelVersions](#API_GetEventPredictionMetadata_ResponseSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-response-evaluatedModelVersions"></a>
 Model versions that were evaluated for generating predictions.
Type: Array of [EvaluatedModelVersion](API_EvaluatedModelVersion.md) objects

 ** [eventId](#API_GetEventPredictionMetadata_ResponseSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-response-eventId"></a>
 The event ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`

 ** [eventTimestamp](#API_GetEventPredictionMetadata_ResponseSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-response-eventTimestamp"></a>
 The timestamp for when the prediction was generated for the associated event ID.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.

 ** [eventTypeName](#API_GetEventPredictionMetadata_ResponseSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-response-eventTypeName"></a>
 The event type associated with the detector specified for this prediction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`

 ** [eventVariables](#API_GetEventPredictionMetadata_ResponseSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-response-eventVariables"></a>
 A list of event variables that influenced the prediction scores.
Type: Array of [EventVariableSummary](API_EventVariableSummary.md) objects

 ** [outcomes](#API_GetEventPredictionMetadata_ResponseSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-response-outcomes"></a>
 The outcomes of the matched rule, based on the rule execution mode.
Type: Array of strings

 ** [predictionTimestamp](#API_GetEventPredictionMetadata_ResponseSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-response-predictionTimestamp"></a>
The timestamp that defines when the prediction was generated.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.

 ** [ruleExecutionMode](#API_GetEventPredictionMetadata_ResponseSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-response-ruleExecutionMode"></a>
 The execution mode of the rule used for evaluating variable values.
Type: String
Valid Values: `ALL_MATCHED | FIRST_MATCHED`

 ** [rules](#API_GetEventPredictionMetadata_ResponseSyntax) **   <a name="FraudDetector-GetEventPredictionMetadata-response-rules"></a>
 List of rules associated with the detector version that were used for evaluating variable values.
Type: Array of [EvaluatedRule](API_EvaluatedRule.md) objects

## Errors
<a name="API_GetEventPredictionMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as `PutExternalModel`, that specifies a role that is not in your account.
HTTP Status Code: 400

 ** InternalServerException **
An exception indicating an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception indicating the specified resource was not found.
HTTP Status Code: 400

 ** ThrottlingException **
An exception indicating a throttling error.
HTTP Status Code: 400

 ** ValidationException **
An exception indicating a specified value is not allowed.
HTTP Status Code: 400

## See Also
<a name="API_GetEventPredictionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/GetEventPredictionMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/GetEventPredictionMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/GetEventPredictionMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/GetEventPredictionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/GetEventPredictionMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/GetEventPredictionMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/GetEventPredictionMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/GetEventPredictionMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/GetEventPredictionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/GetEventPredictionMetadata)
