---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_UpdateConnectionPreferences.html
---

# UpdateConnectionPreferences
<a name="API_account_UpdateConnectionPreferences"></a>

Updates the connection preferences for a partner account, modifying access settings and exclusions.

## Request Syntax
<a name="API_account_UpdateConnectionPreferences_RequestSyntax"></a>

```
{
   "AccessType": "{{string}}",
   "Catalog": "{{string}}",
   "ExcludedParticipantIdentifiers": [ "{{string}}" ],
   "Revision": {{number}}
}
```

## Request Parameters
<a name="API_account_UpdateConnectionPreferences_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AccessType](#API_account_UpdateConnectionPreferences_RequestSyntax) **   <a name="AWSPartnerCentral-account_UpdateConnectionPreferences-request-AccessType"></a>
The access type setting for connections (e.g., open, restricted, invitation-only).
Type: String
Valid Values: `ALLOW_ALL | DENY_ALL | ALLOW_BY_DEFAULT_DENY_SOME`
Required: Yes

 ** [Catalog](#API_account_UpdateConnectionPreferences_RequestSyntax) **   <a name="AWSPartnerCentral-account_UpdateConnectionPreferences-request-Catalog"></a>
The catalog identifier for the partner account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [Revision](#API_account_UpdateConnectionPreferences_RequestSyntax) **   <a name="AWSPartnerCentral-account_UpdateConnectionPreferences-request-Revision"></a>
The revision number of the connection preferences for optimistic locking.
Type: Long
Required: Yes

 ** [ExcludedParticipantIdentifiers](#API_account_UpdateConnectionPreferences_RequestSyntax) **   <a name="AWSPartnerCentral-account_UpdateConnectionPreferences-request-ExcludedParticipantIdentifiers"></a>
The updated list of participant identifiers to exclude from connections.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: No

## Response Syntax
<a name="API_account_UpdateConnectionPreferences_ResponseSyntax"></a>

```
{
   "AccessType": "string",
   "Arn": "string",
   "Catalog": "string",
   "ExcludedParticipantIds": [ "string" ],
   "Revision": number,
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_account_UpdateConnectionPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessType](#API_account_UpdateConnectionPreferences_ResponseSyntax) **   <a name="AWSPartnerCentral-account_UpdateConnectionPreferences-response-AccessType"></a>
The updated access type setting for connections.
Type: String
Valid Values: `ALLOW_ALL | DENY_ALL | ALLOW_BY_DEFAULT_DENY_SOME`

 ** [Arn](#API_account_UpdateConnectionPreferences_ResponseSyntax) **   <a name="AWSPartnerCentral-account_UpdateConnectionPreferences-response-Arn"></a>
The Amazon Resource Name (ARN) of the updated connection preferences.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:[a-zA-Z0-9-]+:partnercentral:[a-z0-9\-]*:[0-9]{12}:catalog/[a-zA-Z]+/connection-preferences`

 ** [Catalog](#API_account_UpdateConnectionPreferences_ResponseSyntax) **   <a name="AWSPartnerCentral-account_UpdateConnectionPreferences-response-Catalog"></a>
The catalog identifier for the partner account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [Revision](#API_account_UpdateConnectionPreferences_ResponseSyntax) **   <a name="AWSPartnerCentral-account_UpdateConnectionPreferences-response-Revision"></a>
The updated revision number of the connection preferences.
Type: Long

 ** [UpdatedAt](#API_account_UpdateConnectionPreferences_ResponseSyntax) **   <a name="AWSPartnerCentral-account_UpdateConnectionPreferences-response-UpdatedAt"></a>
The timestamp when the connection preferences were last updated.
Type: Timestamp

 ** [ExcludedParticipantIds](#API_account_UpdateConnectionPreferences_ResponseSyntax) **   <a name="AWSPartnerCentral-account_UpdateConnectionPreferences-response-ExcludedParticipantIds"></a>
A list of participant IDs that are excluded from connection requests or interactions.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`

## Errors
<a name="API_account_UpdateConnectionPreferences_Errors"></a>

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
<a name="API_account_UpdateConnectionPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-account-2025-04-04/UpdateConnectionPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-account-2025-04-04/UpdateConnectionPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/UpdateConnectionPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-account-2025-04-04/UpdateConnectionPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/UpdateConnectionPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-account-2025-04-04/UpdateConnectionPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-account-2025-04-04/UpdateConnectionPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-account-2025-04-04/UpdateConnectionPreferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-account-2025-04-04/UpdateConnectionPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/UpdateConnectionPreferences)
