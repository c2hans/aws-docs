---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_GetQualificationsDisassociationTask.html
---

# GetQualificationsDisassociationTask
<a name="API_account_GetQualificationsDisassociationTask"></a>

Retrieves the status and details of the most recent qualifications disassociation task for your partner account. Use this operation to poll the progress of a disassociation task initiated by `StartQualificationsDisassociationTask`.

## Request Syntax
<a name="API_account_GetQualificationsDisassociationTask_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_account_GetQualificationsDisassociationTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_account_GetQualificationsDisassociationTask_RequestSyntax) **   <a name="AWSPartnerCentral-account_GetQualificationsDisassociationTask-request-Catalog"></a>
The catalog in which to look up the qualifications disassociation task. Valid values: `AWS`, `Sandbox`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [Identifier](#API_account_GetQualificationsDisassociationTask_RequestSyntax) **   <a name="AWSPartnerCentral-account_GetQualificationsDisassociationTask-request-Identifier"></a>
Your partner identifier. You can provide either a partner ID (for example, `partner-abc123`) or a partner ARN. You must own this identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(partner-[A-Za-z0-9]{13}|arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[A-Za-z-_]+/partner/partner-[A-Za-z0-9]{13})`
Required: Yes

## Response Syntax
<a name="API_account_GetQualificationsDisassociationTask_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "AssociatedPartner": {
      "AccountId": "string",
      "ProfileId": "string"
   },
   "Catalog": "string",
   "EndedAt": "string",
   "Id": "string",
   "StartedAt": "string",
   "Status": "string",
   "TaskId": "string"
}
```

## Response Elements
<a name="API_account_GetQualificationsDisassociationTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_account_GetQualificationsDisassociationTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetQualificationsDisassociationTask-response-Arn"></a>
The Amazon Resource Name (ARN) that uniquely identifies your partner resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[A-Za-z-_]+/partner/partner-[A-Za-z0-9]{13}`

 ** [AssociatedPartner](#API_account_GetQualificationsDisassociationTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetQualificationsDisassociationTask-response-AssociatedPartner"></a>
The primary partner's profile and account identifiers that the task is disassociating qualifications from.
Type: [QualificationsAssociationPartner](API_account_QualificationsAssociationPartner.md) object

 ** [Catalog](#API_account_GetQualificationsDisassociationTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetQualificationsDisassociationTask-response-Catalog"></a>
The catalog identifier echoed from the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [Id](#API_account_GetQualificationsDisassociationTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetQualificationsDisassociationTask-response-Id"></a>
Your unique partner identifier in the AWS Partner Network.
Type: String
Pattern: `partner-[A-Za-z0-9]{13}`

 ** [StartedAt](#API_account_GetQualificationsDisassociationTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetQualificationsDisassociationTask-response-StartedAt"></a>
The timestamp when the qualifications disassociation task started, in ISO 8601 format.
Type: Timestamp

 ** [Status](#API_account_GetQualificationsDisassociationTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetQualificationsDisassociationTask-response-Status"></a>
The current status of the qualifications disassociation task. Valid values: `IN_PROGRESS`, `SUCCEEDED`.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED`

 ** [TaskId](#API_account_GetQualificationsDisassociationTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetQualificationsDisassociationTask-response-TaskId"></a>
The unique identifier of the qualifications disassociation task, in the format `pqdtask-[a-z2-7]{13}`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `pqdtask-[A-Za-z0-9]{13}`

 ** [EndedAt](#API_account_GetQualificationsDisassociationTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetQualificationsDisassociationTask-response-EndedAt"></a>
The timestamp when the qualifications disassociation task ended, in ISO 8601 format. This field is present only when the status is `SUCCEEDED`.
Type: Timestamp

## Errors
<a name="API_account_GetQualificationsDisassociationTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.
 ** Reason **
The specific reason for the access denial.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.
 ** Reason **
The specific reason why the resource was not found.
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
<a name="API_account_GetQualificationsDisassociationTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-account-2025-04-04/GetQualificationsDisassociationTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-account-2025-04-04/GetQualificationsDisassociationTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/GetQualificationsDisassociationTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-account-2025-04-04/GetQualificationsDisassociationTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/GetQualificationsDisassociationTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-account-2025-04-04/GetQualificationsDisassociationTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-account-2025-04-04/GetQualificationsDisassociationTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-account-2025-04-04/GetQualificationsDisassociationTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-account-2025-04-04/GetQualificationsDisassociationTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/GetQualificationsDisassociationTask)
