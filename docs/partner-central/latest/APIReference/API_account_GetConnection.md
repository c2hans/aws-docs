---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_GetConnection.html
---

# GetConnection
<a name="API_account_GetConnection"></a>

Retrieves detailed information about a specific connection between partners.

## Request Syntax
<a name="API_account_GetConnection_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_account_GetConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_account_GetConnection_RequestSyntax) **   <a name="AWSPartnerCentral-account_GetConnection-request-Catalog"></a>
The catalog identifier where the connection exists.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [Identifier](#API_account_GetConnection_RequestSyntax) **   <a name="AWSPartnerCentral-account_GetConnection-request-Identifier"></a>
The unique identifier of the connection to retrieve.
Type: String
Pattern: `pac-[A-Za-z0-9]{13}`
Required: Yes

## Response Syntax
<a name="API_account_GetConnection_ResponseSyntax"></a>

```
{
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
```

## Response Elements
<a name="API_account_GetConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_account_GetConnection_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetConnection-response-Arn"></a>
The Amazon Resource Name (ARN) of the connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:[a-zA-Z0-9-]+:partnercentral:[a-z0-9\-]*::catalog/[a-zA-Z]+/connection/pac-[A-Za-z0-9]{13}`

 ** [Catalog](#API_account_GetConnection_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetConnection-response-Catalog"></a>
The catalog identifier where the connection exists.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [ConnectionTypes](#API_account_GetConnection_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetConnection-response-ConnectionTypes"></a>
The list of connection types active between the partners.
Type: String to [ConnectionTypeDetail](API_account_ConnectionTypeDetail.md) object map
Valid Keys: `OPPORTUNITY_COLLABORATION | SUBSIDIARY`

 ** [Id](#API_account_GetConnection_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetConnection-response-Id"></a>
The unique identifier of the connection.
Type: String
Pattern: `pac-[A-Za-z0-9]{13}`

 ** [OtherParticipantAccountId](#API_account_GetConnection_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetConnection-response-OtherParticipantAccountId"></a>
The AWS account ID of the other participant in the connection.
Type: String
Pattern: `[0-9]{12}`

 ** [UpdatedAt](#API_account_GetConnection_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetConnection-response-UpdatedAt"></a>
The timestamp when the connection was last updated.
Type: Timestamp

## Errors
<a name="API_account_GetConnection_Errors"></a>

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
<a name="API_account_GetConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-account-2025-04-04/GetConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-account-2025-04-04/GetConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/GetConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-account-2025-04-04/GetConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/GetConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-account-2025-04-04/GetConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-account-2025-04-04/GetConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-account-2025-04-04/GetConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-account-2025-04-04/GetConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/GetConnection)
