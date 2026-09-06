---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_StartProfileUpdateTask.html
---

# StartProfileUpdateTask
<a name="API_account_StartProfileUpdateTask"></a>

Initiates a profile update task to modify partner profile information asynchronously.

## Request Syntax
<a name="API_account_StartProfileUpdateTask_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "Identifier": "{{string}}",
   "TaskDetails": {
      "Description": "{{string}}",
      "DisplayName": "{{string}}",
      "Headquarters": {
         "CountryCode": "{{string}}",
         "SubdivisionCode": "{{string}}"
      },
      "IndustrySegments": [ "{{string}}" ],
      "LocalizedContents": [
         {
            "Description": "{{string}}",
            "DisplayName": "{{string}}",
            "Locale": "{{string}}",
            "LogoUrl": "{{string}}",
            "WebsiteUrl": "{{string}}"
         }
      ],
      "LogoUrl": "{{string}}",
      "PrimarySolutionType": "{{string}}",
      "TranslationSourceLocale": "{{string}}",
      "WebsiteUrl": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_account_StartProfileUpdateTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_account_StartProfileUpdateTask_RequestSyntax) **   <a name="AWSPartnerCentral-account_StartProfileUpdateTask-request-Catalog"></a>
The catalog identifier for the partner account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [Identifier](#API_account_StartProfileUpdateTask_RequestSyntax) **   <a name="AWSPartnerCentral-account_StartProfileUpdateTask-request-Identifier"></a>
The unique identifier of the partner account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(partner-[A-Za-z0-9]{13}|arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[A-Za-z-_]+/partner/partner-[A-Za-z0-9]{13})`
Required: Yes

 ** [TaskDetails](#API_account_StartProfileUpdateTask_RequestSyntax) **   <a name="AWSPartnerCentral-account_StartProfileUpdateTask-request-TaskDetails"></a>
The details of the profile updates to be performed.
Type: [TaskDetails](API_account_TaskDetails.md) object
Required: Yes

 ** [ClientToken](#API_account_StartProfileUpdateTask_RequestSyntax) **   <a name="AWSPartnerCentral-account_StartProfileUpdateTask-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: No

## Response Syntax
<a name="API_account_StartProfileUpdateTask_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "Catalog": "string",
   "EndedAt": "string",
   "ErrorDetailList": [
      {
         "Locale": "string",
         "Message": "string",
         "Reason": "string"
      }
   ],
   "Id": "string",
   "StartedAt": "string",
   "Status": "string",
   "TaskDetails": {
      "Description": "string",
      "DisplayName": "string",
      "Headquarters": {
         "CountryCode": "string",
         "SubdivisionCode": "string"
      },
      "IndustrySegments": [ "string" ],
      "LocalizedContents": [
         {
            "Description": "string",
            "DisplayName": "string",
            "Locale": "string",
            "LogoUrl": "string",
            "WebsiteUrl": "string"
         }
      ],
      "LogoUrl": "string",
      "PrimarySolutionType": "string",
      "TranslationSourceLocale": "string",
      "WebsiteUrl": "string"
   },
   "TaskId": "string"
}
```

## Response Elements
<a name="API_account_StartProfileUpdateTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_account_StartProfileUpdateTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartProfileUpdateTask-response-Arn"></a>
The Amazon Resource Name (ARN) of the started profile update task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[A-Za-z-_]+/partner/partner-[A-Za-z0-9]{13}`

 ** [Catalog](#API_account_StartProfileUpdateTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartProfileUpdateTask-response-Catalog"></a>
The catalog identifier for the partner account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [Id](#API_account_StartProfileUpdateTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartProfileUpdateTask-response-Id"></a>
The unique identifier of the partner account.
Type: String
Pattern: `partner-[A-Za-z0-9]{13}`

 ** [StartedAt](#API_account_StartProfileUpdateTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartProfileUpdateTask-response-StartedAt"></a>
The timestamp when the profile update task was started.
Type: Timestamp

 ** [Status](#API_account_StartProfileUpdateTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartProfileUpdateTask-response-Status"></a>
The current status of the profile update task (in progress).
Type: String
Valid Values: `IN_PROGRESS | CANCELED | SUCCEEDED | FAILED`

 ** [TaskDetails](#API_account_StartProfileUpdateTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartProfileUpdateTask-response-TaskDetails"></a>
The details of the profile update task that was started.
Type: [TaskDetails](API_account_TaskDetails.md) object

 ** [TaskId](#API_account_StartProfileUpdateTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartProfileUpdateTask-response-TaskId"></a>
The unique identifier of the started profile update task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `pprofiletask-[A-Za-z0-9]{13}`

 ** [EndedAt](#API_account_StartProfileUpdateTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartProfileUpdateTask-response-EndedAt"></a>
The timestamp when the profile update task ended (null for in-progress tasks).
Type: Timestamp

 ** [ErrorDetailList](#API_account_StartProfileUpdateTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartProfileUpdateTask-response-ErrorDetailList"></a>
A list of error details if any errors occurred during the profile update task.
Type: Array of [ErrorDetail](API_account_ErrorDetail.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

## Errors
<a name="API_account_StartProfileUpdateTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.
 ** Reason **
The specific reason for the access denial.
HTTP Status Code: 400

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.
 ** Reason **
The specific reason for the conflict.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.
 ** Reason **
The specific reason why the resource was not found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.
 ** Reason **
The specific reason for the service quota being exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.
 ** QuotaCode **
The quota code associated with the throttling error.
 ** ServiceCode **
The service code associated with the throttling error.
HTTP Status Code: 400

 ** ValidationException **
The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.
 ** ErrorDetails **
A list of detailed validation errors that occurred during request processing.
 ** Reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_account_StartProfileUpdateTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-account-2025-04-04/StartProfileUpdateTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-account-2025-04-04/StartProfileUpdateTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/StartProfileUpdateTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-account-2025-04-04/StartProfileUpdateTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/StartProfileUpdateTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-account-2025-04-04/StartProfileUpdateTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-account-2025-04-04/StartProfileUpdateTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-account-2025-04-04/StartProfileUpdateTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-account-2025-04-04/StartProfileUpdateTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/StartProfileUpdateTask)
