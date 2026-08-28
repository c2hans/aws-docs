---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_PutEventType.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# PutEventType
<a name="API_PutEventType"></a>

Creates or updates an event type. An event is a business activity that is evaluated for fraud risk. With Amazon Fraud Detector, you generate fraud predictions for events. An event type defines the structure for an event sent to Amazon Fraud Detector. This includes the variables sent as part of the event, the entity performing the event (such as a customer), and the labels that classify the event. Example event types include online payment transactions, account registrations, and authentications.

## Request Syntax
<a name="API_PutEventType_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "entityTypes": [ "{{string}}" ],
   "eventIngestion": "{{string}}",
   "eventOrchestration": {
      "eventBridgeEnabled": {{boolean}}
   },
   "eventVariables": [ "{{string}}" ],
   "labels": [ "{{string}}" ],
   "name": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutEventType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_PutEventType_RequestSyntax) **   <a name="FraudDetector-PutEventType-request-description"></a>
The description of the event type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [entityTypes](#API_PutEventType_RequestSyntax) **   <a name="FraudDetector-PutEventType-request-entityTypes"></a>
The entity type for the event type. Example entity types: customer, merchant, account.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: Yes

 ** [eventIngestion](#API_PutEventType_RequestSyntax) **   <a name="FraudDetector-PutEventType-request-eventIngestion"></a>
Specifies if ingestion is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [eventOrchestration](#API_PutEventType_RequestSyntax) **   <a name="FraudDetector-PutEventType-request-eventOrchestration"></a>
Enables or disables event orchestration. If enabled, you can send event predictions to select AWS services for downstream processing of the events.
Type: [EventOrchestration](API_EventOrchestration.md) object
Required: No

 ** [eventVariables](#API_PutEventType_RequestSyntax) **   <a name="FraudDetector-PutEventType-request-eventVariables"></a>
The event type variables.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: Yes

 ** [labels](#API_PutEventType_RequestSyntax) **   <a name="FraudDetector-PutEventType-request-labels"></a>
The event type labels.
Type: Array of strings
Required: No

 ** [name](#API_PutEventType_RequestSyntax) **   <a name="FraudDetector-PutEventType-request-name"></a>
The name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [tags](#API_PutEventType_RequestSyntax) **   <a name="FraudDetector-PutEventType-request-tags"></a>
A collection of key and value pairs.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Elements
<a name="API_PutEventType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutEventType_Errors"></a>

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

 ** ThrottlingException **
An exception indicating a throttling error.
HTTP Status Code: 400

 ** ValidationException **
An exception indicating a specified value is not allowed.
HTTP Status Code: 400

## See Also
<a name="API_PutEventType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/PutEventType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/PutEventType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/PutEventType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/PutEventType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/PutEventType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/PutEventType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/PutEventType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/PutEventType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/PutEventType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/PutEventType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
