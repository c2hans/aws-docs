---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_AcceptConnectionInvitation.html
---

# AcceptConnectionInvitation
<a name="API_account_AcceptConnectionInvitation"></a>

Accepts a connection invitation from another partner, establishing a formal partnership connection between the two parties.

## Request Syntax
<a name="API_account_AcceptConnectionInvitation_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_account_AcceptConnectionInvitation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_account_AcceptConnectionInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-account_AcceptConnectionInvitation-request-Catalog"></a>
The catalog identifier where the connection invitation exists.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [ClientToken](#API_account_AcceptConnectionInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-account_AcceptConnectionInvitation-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

 ** [Identifier](#API_account_AcceptConnectionInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-account_AcceptConnectionInvitation-request-Identifier"></a>
The unique identifier of the connection invitation to accept.
Type: String
Pattern: `pacinv-[A-Za-z0-9]{13}`
Required: Yes

## Response Syntax
<a name="API_account_AcceptConnectionInvitation_ResponseSyntax"></a>

```
{
   "Connection": {
      "Arn": "string",
      "Catalog": "string",
      "ConnectionTypes": {
         "string" : {
            "CanceledAt": "string",
            "CanceledBy": "string",
            "CreatedAt": "string",
            "InviterEmail": "string",
            "InviterName": "string",
            "OtherParticipant": { ... },
            "Status": "string"
         }
      },
      "Id": "string",
      "OtherParticipantAccountId": "string",
      "UpdatedAt": "string"
   }
}
```

## Response Elements
<a name="API_account_AcceptConnectionInvitation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connection](#API_account_AcceptConnectionInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-account_AcceptConnectionInvitation-response-Connection"></a>
The details of the accepted connection between the two partners.
Type: [Connection](API_account_Connection.md) object

## Errors
<a name="API_account_AcceptConnectionInvitation_Errors"></a>

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
<a name="API_account_AcceptConnectionInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-account-2025-04-04/AcceptConnectionInvitation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-account-2025-04-04/AcceptConnectionInvitation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/AcceptConnectionInvitation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-account-2025-04-04/AcceptConnectionInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/AcceptConnectionInvitation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-account-2025-04-04/AcceptConnectionInvitation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-account-2025-04-04/AcceptConnectionInvitation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-account-2025-04-04/AcceptConnectionInvitation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-account-2025-04-04/AcceptConnectionInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/AcceptConnectionInvitation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
