---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_ListConnectionInvitations.html
---

# ListConnectionInvitations
<a name="API_account_ListConnectionInvitations"></a>

Lists connection invitations for the partner account, with optional filtering by status, type, and other criteria.

## Request Syntax
<a name="API_account_ListConnectionInvitations_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ConnectionType": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OtherParticipantIdentifiers": [ "{{string}}" ],
   "ParticipantType": "{{string}}",
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_account_ListConnectionInvitations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_account_ListConnectionInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-account_ListConnectionInvitations-request-Catalog"></a>
The catalog identifier for the partner account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [ConnectionType](#API_account_ListConnectionInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-account_ListConnectionInvitations-request-ConnectionType"></a>
Filter results by connection type (e.g., reseller, distributor, technology partner).
Type: String
Valid Values: `OPPORTUNITY_COLLABORATION | SUBSIDIARY`
Required: No

 ** [MaxResults](#API_account_ListConnectionInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-account_ListConnectionInvitations-request-MaxResults"></a>
The maximum number of connection invitations to return in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_account_ListConnectionInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-account_ListConnectionInvitations-request-NextToken"></a>
The token for retrieving the next page of results in paginated responses.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** [OtherParticipantIdentifiers](#API_account_ListConnectionInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-account_ListConnectionInvitations-request-OtherParticipantIdentifiers"></a>
Filter results by specific participant identifiers.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [ParticipantType](#API_account_ListConnectionInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-account_ListConnectionInvitations-request-ParticipantType"></a>
Filter results by participant type (inviter or invitee).
Type: String
Valid Values: `SENDER | RECEIVER`
Required: No

 ** [Status](#API_account_ListConnectionInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-account_ListConnectionInvitations-request-Status"></a>
Filter results by invitation status (pending, accepted, rejected, canceled, expired).
Type: String
Valid Values: `PENDING | ACCEPTED | REJECTED | CANCELED | EXPIRED`
Required: No

## Response Syntax
<a name="API_account_ListConnectionInvitations_ResponseSyntax"></a>

```
{
   "ConnectionInvitationSummaries": [
      {
         "Arn": "string",
         "Catalog": "string",
         "ConnectionId": "string",
         "ConnectionType": "string",
         "CreatedAt": "string",
         "ExpiresAt": "string",
         "Id": "string",
         "OtherParticipantIdentifier": "string",
         "ParticipantType": "string",
         "Status": "string",
         "UpdatedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_account_ListConnectionInvitations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionInvitationSummaries](#API_account_ListConnectionInvitations_ResponseSyntax) **   <a name="AWSPartnerCentral-account_ListConnectionInvitations-response-ConnectionInvitationSummaries"></a>
A list of connection invitation summaries matching the specified criteria.
Type: Array of [ConnectionInvitationSummary](API_account_ConnectionInvitationSummary.md) objects

 ** [NextToken](#API_account_ListConnectionInvitations_ResponseSyntax) **   <a name="AWSPartnerCentral-account_ListConnectionInvitations-response-NextToken"></a>
The token for retrieving the next page of results if more results are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\S]+`

## Errors
<a name="API_account_ListConnectionInvitations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.
 ** Reason **
The specific reason for the access denial.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.
HTTP Status Code: 500

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
<a name="API_account_ListConnectionInvitations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-account-2025-04-04/ListConnectionInvitations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-account-2025-04-04/ListConnectionInvitations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/ListConnectionInvitations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-account-2025-04-04/ListConnectionInvitations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/ListConnectionInvitations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-account-2025-04-04/ListConnectionInvitations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-account-2025-04-04/ListConnectionInvitations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-account-2025-04-04/ListConnectionInvitations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-account-2025-04-04/ListConnectionInvitations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/ListConnectionInvitations)
