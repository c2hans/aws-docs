---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_GetEventPrediction.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# GetEventPrediction
<a name="API_GetEventPrediction"></a>

Evaluates an event against a detector version. If a version ID is not provided, the detector’s (`ACTIVE`) version is used.

## Request Syntax
<a name="API_GetEventPrediction_RequestSyntax"></a>

```
{
   "detectorId": "{{string}}",
   "detectorVersionId": "{{string}}",
   "entities": [
      {
         "entityId": "{{string}}",
         "entityType": "{{string}}"
      }
   ],
   "eventId": "{{string}}",
   "eventTimestamp": "{{string}}",
   "eventTypeName": "{{string}}",
   "eventVariables": {
      "{{string}}" : "{{string}}"
   },
   "externalModelEndpointDataBlobs": {
      "{{string}}" : {
         "byteBuffer": {{blob}},
         "contentType": "{{string}}"
      }
   }
}
```

## Request Parameters
<a name="API_GetEventPrediction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [detectorId](#API_GetEventPrediction_RequestSyntax) **   <a name="FraudDetector-GetEventPrediction-request-detectorId"></a>
The detector ID.
Type: String
Required: Yes

 ** [detectorVersionId](#API_GetEventPrediction_RequestSyntax) **   <a name="FraudDetector-GetEventPrediction-request-detectorVersionId"></a>
The detector version ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^([1-9][0-9]*)$`
Required: No

 ** [entities](#API_GetEventPrediction_RequestSyntax) **   <a name="FraudDetector-GetEventPrediction-request-entities"></a>
The entity type (associated with the detector's event type) and specific entity ID representing who performed the event. If an entity id is not available, use "UNKNOWN."
Type: Array of [Entity](API_Entity.md) objects
Required: Yes

 ** [eventId](#API_GetEventPrediction_RequestSyntax) **   <a name="FraudDetector-GetEventPrediction-request-eventId"></a>
The unique ID used to identify the event.
Type: String
Required: Yes

 ** [eventTimestamp](#API_GetEventPrediction_RequestSyntax) **   <a name="FraudDetector-GetEventPrediction-request-eventTimestamp"></a>
Timestamp that defines when the event under evaluation occurred. The timestamp must be specified using ISO 8601 standard in UTC.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 30.
Required: Yes

 ** [eventTypeName](#API_GetEventPrediction_RequestSyntax) **   <a name="FraudDetector-GetEventPrediction-request-eventTypeName"></a>
The event type associated with the detector specified for the prediction.
Type: String
Required: Yes

 ** [eventVariables](#API_GetEventPrediction_RequestSyntax) **   <a name="FraudDetector-GetEventPrediction-request-eventVariables"></a>
Names of the event type's variables you defined in Amazon Fraud Detector to represent data elements and their corresponding values for the event you are sending for evaluation.
You must provide at least one eventVariable
To ensure most accurate fraud prediction and to simplify your data preparation, Amazon Fraud Detector will replace all missing variables or values as follows:
 **For Amazon Fraud Detector trained models:**
If a null value is provided explicitly for a variable or if a variable is missing, model will replace the null value or the missing variable (no variable name in the eventVariables map) with calculated default mean/medians for numeric variables and with special values for categorical variables.
 **For imported SageMaker models:**
If a null value is provided explicitly for a variable, the model and rules will use “null” as the value. If a variable is not provided (no variable name in the eventVariables map), model and rules will use the default value that is provided for the variable.
Type: String to string map
Map Entries: Maximum number of items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Value Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: Yes

 ** [externalModelEndpointDataBlobs](#API_GetEventPrediction_RequestSyntax) **   <a name="FraudDetector-GetEventPrediction-request-externalModelEndpointDataBlobs"></a>
The Amazon SageMaker model endpoint input data blobs.
Type: String to [ModelEndpointDataBlob](API_ModelEndpointDataBlob.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 63.
Key Pattern: `^[0-9A-Za-z_-]+$`
Required: No

## Response Syntax
<a name="API_GetEventPrediction_ResponseSyntax"></a>

```
{
   "externalModelOutputs": [
      {
         "externalModel": {
            "modelEndpoint": "string",
            "modelSource": "string"
         },
         "outputs": {
            "string" : "string"
         }
      }
   ],
   "modelScores": [
      {
         "modelVersion": {
            "arn": "string",
            "modelId": "string",
            "modelType": "string",
            "modelVersionNumber": "string"
         },
         "scores": {
            "string" : number
         }
      }
   ],
   "ruleResults": [
      {
         "outcomes": [ "string" ],
         "ruleId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetEventPrediction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [externalModelOutputs](#API_GetEventPrediction_ResponseSyntax) **   <a name="FraudDetector-GetEventPrediction-response-externalModelOutputs"></a>
The model scores for Amazon SageMaker models.
Type: Array of [ExternalModelOutputs](API_ExternalModelOutputs.md) objects

 ** [modelScores](#API_GetEventPrediction_ResponseSyntax) **   <a name="FraudDetector-GetEventPrediction-response-modelScores"></a>
The model scores. Amazon Fraud Detector generates model scores between 0 and 1000, where 0 is low fraud risk and 1000 is high fraud risk. Model scores are directly related to the false positive rate (FPR). For example, a score of 600 corresponds to an estimated 10% false positive rate whereas a score of 900 corresponds to an estimated 2% false positive rate.
Type: Array of [ModelScores](API_ModelScores.md) objects

 ** [ruleResults](#API_GetEventPrediction_ResponseSyntax) **   <a name="FraudDetector-GetEventPrediction-response-ruleResults"></a>
The results from the rules.
Type: Array of [RuleResult](API_RuleResult.md) objects

## Errors
<a name="API_GetEventPrediction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as `PutExternalModel`, that specifies a role that is not in your account.
HTTP Status Code: 400

 ** ConflictException **
An exception indicating there was a conflict during a delete operation.
HTTP Status Code: 400

 ** InternalServerException **
An exception indicating an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception indicating the specified resource was not found.
HTTP Status Code: 400

 ** ResourceUnavailableException **
An exception indicating that the attached customer-owned (external) model threw an exception when Amazon Fraud Detector invoked the model.
HTTP Status Code: 400

 ** ThrottlingException **
An exception indicating a throttling error.
HTTP Status Code: 400

 ** ValidationException **
An exception indicating a specified value is not allowed.
HTTP Status Code: 400

## See Also
<a name="API_GetEventPrediction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/GetEventPrediction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/GetEventPrediction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/GetEventPrediction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/GetEventPrediction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/GetEventPrediction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/GetEventPrediction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/GetEventPrediction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/GetEventPrediction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/GetEventPrediction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/GetEventPrediction)
