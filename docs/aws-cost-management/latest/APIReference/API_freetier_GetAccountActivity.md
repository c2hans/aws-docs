---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_GetAccountActivity.html
---

# GetAccountActivity
<a name="API_freetier_GetAccountActivity"></a>

 Returns a specific activity record that is available to the customer.

## Request Syntax
<a name="API_freetier_GetAccountActivity_RequestSyntax"></a>

```
{
   "activityId": "{{string}}",
   "languageCode": "{{string}}"
}
```

## Request Parameters
<a name="API_freetier_GetAccountActivity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [activityId](#API_freetier_GetAccountActivity_RequestSyntax) **   <a name="awscostmanagement-freetier_GetAccountActivity-request-activityId"></a>
 A unique identifier that identifies the activity.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** [languageCode](#API_freetier_GetAccountActivity_RequestSyntax) **   <a name="awscostmanagement-freetier_GetAccountActivity-request-languageCode"></a>
 The language code used to return translated title and description fields.
Type: String
Valid Values: `en-US | en-GB | id-ID | de-DE | es-ES | fr-FR | ja-JP | it-IT | pt-PT | ko-KR | zh-CN | zh-TW | tr-TR`
Required: No

## Response Syntax
<a name="API_freetier_GetAccountActivity_ResponseSyntax"></a>

```
{
   "activityId": "string",
   "completedAt": "string",
   "description": "string",
   "estimatedTimeToCompleteInMinutes": number,
   "expiresAt": "string",
   "instructionsUrl": "string",
   "reward": { ... },
   "startedAt": "string",
   "status": "string",
   "title": "string"
}
```

## Response Elements
<a name="API_freetier_GetAccountActivity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [activityId](#API_freetier_GetAccountActivity_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetAccountActivity-response-activityId"></a>
 A unique identifier that identifies the activity.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-zA-Z0-9]+`

 ** [completedAt](#API_freetier_GetAccountActivity_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetAccountActivity-response-completedAt"></a>
 The timestamp when the activity is completed. This field appears only for activities in the `COMPLETED` state.
Type: Timestamp

 ** [description](#API_freetier_GetAccountActivity_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetAccountActivity-response-description"></a>
 Provides detailed information about the activity and its expected outcomes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`

 ** [estimatedTimeToCompleteInMinutes](#API_freetier_GetAccountActivity_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetAccountActivity-response-estimatedTimeToCompleteInMinutes"></a>
 The estimated time to complete the activity. This is the duration in minutes.
Type: Integer

 ** [expiresAt](#API_freetier_GetAccountActivity_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetAccountActivity-response-expiresAt"></a>
 The time by which the activity must be completed to receive a reward.
Type: Timestamp

 ** [instructionsUrl](#API_freetier_GetAccountActivity_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetAccountActivity-response-instructionsUrl"></a>
 The URL resource that provides guidance on activity requirements and completion.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`

 ** [reward](#API_freetier_GetAccountActivity_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetAccountActivity-response-reward"></a>
 A reward granted upon activity completion.
Type: [ActivityReward](API_freetier_ActivityReward.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [startedAt](#API_freetier_GetAccountActivity_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetAccountActivity-response-startedAt"></a>
 The timestamp when the activity started. This field appears only for activities in the `IN_PROGRESS` or `COMPLETED` states.
Type: Timestamp

 ** [status](#API_freetier_GetAccountActivity_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetAccountActivity-response-status"></a>
 The current activity status.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED | EXPIRING`

 ** [title](#API_freetier_GetAccountActivity_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetAccountActivity-response-title"></a>
 A short activity title.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`

## Errors
<a name="API_freetier_GetAccountActivity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred during the processing of your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 This exception is thrown when the requested resource cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_freetier_GetAccountActivity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/freetier-2023-09-07/GetAccountActivity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/freetier-2023-09-07/GetAccountActivity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/freetier-2023-09-07/GetAccountActivity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/freetier-2023-09-07/GetAccountActivity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/freetier-2023-09-07/GetAccountActivity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/freetier-2023-09-07/GetAccountActivity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/freetier-2023-09-07/GetAccountActivity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/freetier-2023-09-07/GetAccountActivity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/freetier-2023-09-07/GetAccountActivity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/freetier-2023-09-07/GetAccountActivity)
