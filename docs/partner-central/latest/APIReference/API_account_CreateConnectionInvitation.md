---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_CreateConnectionInvitation.html
---

# CreateConnectionInvitation
<a name="API_account_CreateConnectionInvitation"></a>

Creates a new connection invitation to establish a partnership with another organization.

## Request Syntax
<a name="API_account_CreateConnectionInvitation_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "ConnectionType": "{{string}}",
   "Email": "{{string}}",
   "Message": "{{string}}",
   "Name": "{{string}}",
   "ReceiverIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_account_CreateConnectionInvitation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_account_CreateConnectionInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-request-Catalog"></a>
The catalog identifier where the connection invitation will be created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [ClientToken](#API_account_CreateConnectionInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

 ** [ConnectionType](#API_account_CreateConnectionInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-request-ConnectionType"></a>
The type of connection being requested (e.g., reseller, distributor, technology partner).
Type: String
Valid Values: `OPPORTUNITY_COLLABORATION | SUBSIDIARY`
Required: Yes

 ** [Email](#API_account_CreateConnectionInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-request-Email"></a>
The email address of the person to send the connection invitation to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 320.
Pattern: `[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*`
Required: Yes

 ** [Message](#API_account_CreateConnectionInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-request-Message"></a>
A custom message to include with the connection invitation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD\n]+`
Required: Yes

 ** [Name](#API_account_CreateConnectionInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-request-Name"></a>
The name of the person sending the connection invitation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

 ** [ReceiverIdentifier](#API_account_CreateConnectionInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-request-ReceiverIdentifier"></a>
The identifier of the organization or partner to invite for connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_account_CreateConnectionInvitation_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "Catalog": "string",
   "ConnectionId": "string",
   "ConnectionType": "string",
   "CreatedAt": "string",
   "ExpiresAt": "string",
   "Id": "string",
   "InvitationMessage": "string",
   "InviterEmail": "string",
   "InviterName": "string",
   "OtherParticipantIdentifier": "string",
   "ParticipantType": "string",
   "Status": "string",
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_account_CreateConnectionInvitation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_account_CreateConnectionInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-response-Arn"></a>
The Amazon Resource Name (ARN) of the created connection invitation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:[a-zA-Z0-9-]+:partnercentral:[a-z0-9\-]*::catalog/[a-zA-Z]+/connection-invitation/pacinv-[A-Za-z0-9]{13}`

 ** [Catalog](#API_account_CreateConnectionInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-response-Catalog"></a>
The catalog identifier where the connection invitation was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [ConnectionType](#API_account_CreateConnectionInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-response-ConnectionType"></a>
The type of connection being requested in the invitation.
Type: String
Valid Values: `OPPORTUNITY_COLLABORATION | SUBSIDIARY`

 ** [CreatedAt](#API_account_CreateConnectionInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-response-CreatedAt"></a>
The timestamp when the connection invitation was created.
Type: Timestamp

 ** [Id](#API_account_CreateConnectionInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-response-Id"></a>
The unique identifier of the created connection invitation.
Type: String
Pattern: `pacinv-[A-Za-z0-9]{13}`

 ** [InvitationMessage](#API_account_CreateConnectionInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-response-InvitationMessage"></a>
The custom message included with the connection invitation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD\n]+`

 ** [InviterEmail](#API_account_CreateConnectionInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-response-InviterEmail"></a>
The email address of the person who sent the connection invitation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 320.
Pattern: `[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*`

 ** [InviterName](#API_account_CreateConnectionInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-response-InviterName"></a>
The name of the person who sent the connection invitation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`

 ** [OtherParticipantIdentifier](#API_account_CreateConnectionInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-response-OtherParticipantIdentifier"></a>
The identifier of the organization or partner being invited.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`

 ** [ParticipantType](#API_account_CreateConnectionInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-response-ParticipantType"></a>
The type of participant (inviter or invitee) in the connection invitation.
Type: String
Valid Values: `SENDER | RECEIVER`

 ** [Status](#API_account_CreateConnectionInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-response-Status"></a>
The current status of the connection invitation (pending, accepted, rejected, etc.).
Type: String
Valid Values: `PENDING | ACCEPTED | REJECTED | CANCELED | EXPIRED`

 ** [UpdatedAt](#API_account_CreateConnectionInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-response-UpdatedAt"></a>
The timestamp when the connection invitation was last updated.
Type: Timestamp

 ** [ConnectionId](#API_account_CreateConnectionInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-response-ConnectionId"></a>
The identifier of the connection associated with this invitation.
Type: String
Pattern: `pac-[A-Za-z0-9]{13}`

 ** [ExpiresAt](#API_account_CreateConnectionInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreateConnectionInvitation-response-ExpiresAt"></a>
The timestamp when the connection invitation will expire if not responded to.
Type: Timestamp

## Errors
<a name="API_account_CreateConnectionInvitation_Errors"></a>

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
<a name="API_account_CreateConnectionInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-account-2025-04-04/CreateConnectionInvitation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-account-2025-04-04/CreateConnectionInvitation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/CreateConnectionInvitation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-account-2025-04-04/CreateConnectionInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/CreateConnectionInvitation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-account-2025-04-04/CreateConnectionInvitation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-account-2025-04-04/CreateConnectionInvitation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-account-2025-04-04/CreateConnectionInvitation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-account-2025-04-04/CreateConnectionInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/CreateConnectionInvitation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
