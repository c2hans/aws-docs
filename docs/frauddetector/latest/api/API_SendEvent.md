---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_SendEvent.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# SendEvent
<a name="API_SendEvent"></a>

Stores events in Amazon Fraud Detector without generating fraud predictions for those events. For example, you can use `SendEvent` to upload a historical dataset, which you can then later use to train a model.

## Request Syntax
<a name="API_SendEvent_RequestSyntax"></a>

```
{
   "assignedLabel": "{{string}}",
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
   "labelTimestamp": "{{string}}"
}
```

## Request Parameters
<a name="API_SendEvent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [assignedLabel](#API_SendEvent_RequestSyntax) **   <a name="FraudDetector-SendEvent-request-assignedLabel"></a>
The label to associate with the event. Required if specifying `labelTimestamp`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** [entities](#API_SendEvent_RequestSyntax) **   <a name="FraudDetector-SendEvent-request-entities"></a>
An array of entities.
Type: Array of [Entity](API_Entity.md) objects
Required: Yes

 ** [eventId](#API_SendEvent_RequestSyntax) **   <a name="FraudDetector-SendEvent-request-eventId"></a>
The event ID to upload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [eventTimestamp](#API_SendEvent_RequestSyntax) **   <a name="FraudDetector-SendEvent-request-eventTimestamp"></a>
The timestamp that defines when the event under evaluation occurred. The timestamp must be specified using ISO 8601 standard in UTC.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 30.
Required: Yes

 ** [eventTypeName](#API_SendEvent_RequestSyntax) **   <a name="FraudDetector-SendEvent-request-eventTypeName"></a>
The event type name of the event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [eventVariables](#API_SendEvent_RequestSyntax) **   <a name="FraudDetector-SendEvent-request-eventVariables"></a>
Names of the event type's variables you defined in Amazon Fraud Detector to represent data elements and their corresponding values for the event you are sending for evaluation.
Type: String to string map
Map Entries: Maximum number of items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Value Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: Yes

 ** [labelTimestamp](#API_SendEvent_RequestSyntax) **   <a name="FraudDetector-SendEvent-request-labelTimestamp"></a>
The timestamp associated with the label. Required if specifying `assignedLabel`.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 30.
Required: No

## Response Elements
<a name="API_SendEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SendEvent_Errors"></a>

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

 ** ThrottlingException **
An exception indicating a throttling error.
HTTP Status Code: 400

 ** ValidationException **
An exception indicating a specified value is not allowed.
HTTP Status Code: 400

## See Also
<a name="API_SendEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/SendEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/SendEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/SendEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/SendEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/SendEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/SendEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/SendEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/SendEvent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/SendEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/SendEvent)
