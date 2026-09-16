---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StartContactConversationalAnalyticsJob.html
---

# StartContactConversationalAnalyticsJob
<a name="API_StartContactConversationalAnalyticsJob"></a>

Starts a Contact Lens post-call analytics job for the specified contact. This API runs Conversational Analytics post-contact analysis on a voice recording that is already attached to the contact, generating transcription, sentiment analysis, redaction, and summarization results based on the provided configuration.

**Important**
A voice recording must already be attached to the contact before calling this API. Use `CreateAttachedFile` to attach a recording from an S3 source URI.

**Note**
For example, you can call `CreateContact`, then `CreateAttachedFile`, then `StartContactConversationalAnalyticsJob` to create a contact, attach a recording, and run post-call analytics.

## Request Syntax
<a name="API_StartContactConversationalAnalyticsJob_RequestSyntax"></a>

```
POST /contact/start-conversational-analytics-job/{{InstanceId}}/{{ContactId}} HTTP/1.1
Content-type: application/json

{
   "AnalyticsConfiguration": {
      "LanguageConfiguration": {
         "LanguageLocale": "{{string}}"
      },
      "RedactionConfiguration": {
         "Behavior": "{{string}}",
         "Entities": [ "{{string}}" ],
         "MaskMode": "{{string}}",
         "Policy": "{{string}}"
      },
      "RulesConfiguration": {
         "Behavior": "{{string}}"
      },
      "SentimentConfiguration": {
         "Behavior": "{{string}}"
      },
      "SummaryConfiguration": {
         "SummaryModes": [ "{{string}}" ]
      }
   },
   "AnalyticsModes": [ "{{string}}" ],
   "ClientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartContactConversationalAnalyticsJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactId](#API_StartContactConversationalAnalyticsJob_RequestSyntax) **   <a name="connect-StartContactConversationalAnalyticsJob-request-uri-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_StartContactConversationalAnalyticsJob_RequestSyntax) **   <a name="connect-StartContactConversationalAnalyticsJob-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_StartContactConversationalAnalyticsJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AnalyticsConfiguration](#API_StartContactConversationalAnalyticsJob_RequestSyntax) **   <a name="connect-StartContactConversationalAnalyticsJob-request-AnalyticsConfiguration"></a>
The configuration for the conversational analytics job.
Type: [AnalyticsConfiguration](API_AnalyticsConfiguration.md) object
Required: Yes

 ** [AnalyticsModes](#API_StartContactConversationalAnalyticsJob_RequestSyntax) **   <a name="connect-StartContactConversationalAnalyticsJob-request-AnalyticsModes"></a>
The analytics modes to run for the contact. Valid values: `PostContact`.
Type: Array of strings
Valid Values: `PostContact | RealTime | ContactLens | AutomatedInteraction`
Required: Yes

 ** [ClientToken](#API_StartContactConversationalAnalyticsJob_RequestSyntax) **   <a name="connect-StartContactConversationalAnalyticsJob-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

## Response Syntax
<a name="API_StartContactConversationalAnalyticsJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactId": "string",
   "InstanceId": "string"
}
```

## Response Elements
<a name="API_StartContactConversationalAnalyticsJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactId](#API_StartContactConversationalAnalyticsJob_ResponseSyntax) **   <a name="connect-StartContactConversationalAnalyticsJob-response-ContactId"></a>
The identifier of the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [InstanceId](#API_StartContactConversationalAnalyticsJob_ResponseSyntax) **   <a name="connect-StartContactConversationalAnalyticsJob-response-InstanceId"></a>
The identifier of the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

## Errors
<a name="API_StartContactConversationalAnalyticsJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** IdempotencyException **
An entity with the same name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_StartContactConversationalAnalyticsJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/StartContactConversationalAnalyticsJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/StartContactConversationalAnalyticsJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StartContactConversationalAnalyticsJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/StartContactConversationalAnalyticsJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StartContactConversationalAnalyticsJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/StartContactConversationalAnalyticsJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/StartContactConversationalAnalyticsJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/StartContactConversationalAnalyticsJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/StartContactConversationalAnalyticsJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StartContactConversationalAnalyticsJob)
