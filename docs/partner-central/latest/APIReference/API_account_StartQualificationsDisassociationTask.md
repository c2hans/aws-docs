---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_StartQualificationsDisassociationTask.html
---

# StartQualificationsDisassociationTask
<a name="API_account_StartQualificationsDisassociationTask"></a>

Initiates an asynchronous task to disassociate your partner qualifications from a primary account. You must currently be associated and cannot disassociate if you are the primary partner. Use `GetQualificationsDisassociationTask` to monitor task progress.

## Request Syntax
<a name="API_account_StartQualificationsDisassociationTask_RequestSyntax"></a>

```
{
   "AssociatedPartner": {
      "AccountId": "{{string}}",
      "ProfileId": "{{string}}"
   },
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_account_StartQualificationsDisassociationTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AssociatedPartner](#API_account_StartQualificationsDisassociationTask_RequestSyntax) **   <a name="AWSPartnerCentral-account_StartQualificationsDisassociationTask-request-AssociatedPartner"></a>
The primary partner's profile and account identifier that you are currently associated with and will disassociate from. You must provide at least one of `ProfileId` or `AccountId`. The specified partner must match your current primary association.
Type: [QualificationsAssociationPartner](API_account_QualificationsAssociationPartner.md) object
Required: Yes

 ** [Catalog](#API_account_StartQualificationsDisassociationTask_RequestSyntax) **   <a name="AWSPartnerCentral-account_StartQualificationsDisassociationTask-request-Catalog"></a>
The catalog in which to perform the qualifications disassociation. Valid values: `AWS`, `Sandbox`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [Identifier](#API_account_StartQualificationsDisassociationTask_RequestSyntax) **   <a name="AWSPartnerCentral-account_StartQualificationsDisassociationTask-request-Identifier"></a>
Your partner identifier. You can provide either a partner ID (for example, `partner-abc123`) or a partner ARN. You must own this identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(partner-[A-Za-z0-9]{13}|arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[A-Za-z-_]+/partner/partner-[A-Za-z0-9]{13})`
Required: Yes

 ** [ClientToken](#API_account_StartQualificationsDisassociationTask_RequestSyntax) **   <a name="AWSPartnerCentral-account_StartQualificationsDisassociationTask-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: No

## Response Syntax
<a name="API_account_StartQualificationsDisassociationTask_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "AssociatedPartner": {
      "AccountId": "string",
      "ProfileId": "string"
   },
   "Catalog": "string",
   "Id": "string",
   "StartedAt": "string",
   "Status": "string",
   "TaskId": "string"
}
```

## Response Elements
<a name="API_account_StartQualificationsDisassociationTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_account_StartQualificationsDisassociationTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartQualificationsDisassociationTask-response-Arn"></a>
The Amazon Resource Name (ARN) that uniquely identifies your partner resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[A-Za-z-_]+/partner/partner-[A-Za-z0-9]{13}`

 ** [AssociatedPartner](#API_account_StartQualificationsDisassociationTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartQualificationsDisassociationTask-response-AssociatedPartner"></a>
The resolved primary partner's profile and account identifiers that the task is disassociating qualifications from.
Type: [QualificationsAssociationPartner](API_account_QualificationsAssociationPartner.md) object

 ** [Catalog](#API_account_StartQualificationsDisassociationTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartQualificationsDisassociationTask-response-Catalog"></a>
The catalog identifier echoed from the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [Id](#API_account_StartQualificationsDisassociationTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartQualificationsDisassociationTask-response-Id"></a>
Your unique partner identifier in the AWS Partner Network.
Type: String
Pattern: `partner-[A-Za-z0-9]{13}`

 ** [StartedAt](#API_account_StartQualificationsDisassociationTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartQualificationsDisassociationTask-response-StartedAt"></a>
The timestamp when the qualifications disassociation task started, in ISO 8601 format.
Type: Timestamp

 ** [Status](#API_account_StartQualificationsDisassociationTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartQualificationsDisassociationTask-response-Status"></a>
The current status of the qualifications disassociation task. The initial value is `IN_PROGRESS`.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED`

 ** [TaskId](#API_account_StartQualificationsDisassociationTask_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartQualificationsDisassociationTask-response-TaskId"></a>
The unique identifier of the started qualifications disassociation task, in the format `pqdtask-[a-z2-7]{13}`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `pqdtask-[A-Za-z0-9]{13}`

## Errors
<a name="API_account_StartQualificationsDisassociationTask_Errors"></a>

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
<a name="API_account_StartQualificationsDisassociationTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-account-2025-04-04/StartQualificationsDisassociationTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-account-2025-04-04/StartQualificationsDisassociationTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/StartQualificationsDisassociationTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-account-2025-04-04/StartQualificationsDisassociationTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/StartQualificationsDisassociationTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-account-2025-04-04/StartQualificationsDisassociationTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-account-2025-04-04/StartQualificationsDisassociationTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-account-2025-04-04/StartQualificationsDisassociationTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-account-2025-04-04/StartQualificationsDisassociationTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/StartQualificationsDisassociationTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
