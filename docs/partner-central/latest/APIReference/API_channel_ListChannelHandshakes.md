---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ListChannelHandshakes.html
---

# ListChannelHandshakes
<a name="API_channel_ListChannelHandshakes"></a>

Lists channel handshakes based on specified criteria.

## Request Syntax
<a name="API_channel_ListChannelHandshakes_RequestSyntax"></a>

```
{
   "associatedResourceIdentifiers": [ "{{string}}" ],
   "catalog": "{{string}}",
   "handshakeType": "{{string}}",
   "handshakeTypeFilters": { ... },
   "handshakeTypeSort": { ... },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "participantType": "{{string}}",
   "statuses": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_channel_ListChannelHandshakes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [catalog](#API_channel_ListChannelHandshakes_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListChannelHandshakes-request-catalog"></a>
The catalog identifier to filter handshakes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]*`
Required: Yes

 ** [handshakeType](#API_channel_ListChannelHandshakes_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListChannelHandshakes-request-handshakeType"></a>
Filter results by handshake type.
Type: String
Valid Values: `START_SERVICE_PERIOD | REVOKE_SERVICE_PERIOD | PROGRAM_MANAGEMENT_ACCOUNT`
Required: Yes

 ** [participantType](#API_channel_ListChannelHandshakes_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListChannelHandshakes-request-participantType"></a>
Filter by participant type (sender or receiver).
Type: String
Valid Values: `SENDER | RECEIVER`
Required: Yes

 ** [associatedResourceIdentifiers](#API_channel_ListChannelHandshakes_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListChannelHandshakes-request-associatedResourceIdentifiers"></a>
Filter by associated resource identifiers.
Type: Array of strings
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `((arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/program-management-account/pma-[a-z0-9]{13}(/relationship/rs-[a-z0-9]{13})?)|(pma|rs)-[a-z0-9]{13})`
Required: No

 ** [handshakeTypeFilters](#API_channel_ListChannelHandshakes_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListChannelHandshakes-request-handshakeTypeFilters"></a>
Type-specific filters for handshakes.
Type: [ListChannelHandshakesTypeFilters](API_channel_ListChannelHandshakesTypeFilters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [handshakeTypeSort](#API_channel_ListChannelHandshakes_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListChannelHandshakes-request-handshakeTypeSort"></a>
Type-specific sorting options for handshakes.
Type: [ListChannelHandshakesTypeSort](API_channel_ListChannelHandshakesTypeSort.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [maxResults](#API_channel_ListChannelHandshakes_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListChannelHandshakes-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_channel_ListChannelHandshakes_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListChannelHandshakes-request-nextToken"></a>
Token for retrieving the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\x00-\x1F\x7F\x20]*`
Required: No

 ** [statuses](#API_channel_ListChannelHandshakes_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListChannelHandshakes-request-statuses"></a>
Filter results by handshake status.
Type: Array of strings
Valid Values: `PENDING | ACCEPTED | REJECTED | CANCELED | EXPIRED`
Required: No

## Response Syntax
<a name="API_channel_ListChannelHandshakes_ResponseSyntax"></a>

```
{
   "items": [
      {
         "arn": "string",
         "associatedResourceId": "string",
         "catalog": "string",
         "createdAt": "string",
         "detail": { ... },
         "handshakeType": "string",
         "id": "string",
         "ownerAccountId": "string",
         "receiverAccountId": "string",
         "senderAccountId": "string",
         "senderDisplayName": "string",
         "status": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_channel_ListChannelHandshakes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_channel_ListChannelHandshakes_ResponseSyntax) **   <a name="AWSPartnerCentral-channel_ListChannelHandshakes-response-items"></a>
List of channel handshakes matching the criteria.
Type: Array of [ChannelHandshakeSummary](API_channel_ChannelHandshakeSummary.md) objects

 ** [nextToken](#API_channel_ListChannelHandshakes_ResponseSyntax) **   <a name="AWSPartnerCentral-channel_ListChannelHandshakes-response-nextToken"></a>
Token for retrieving the next page of results, if available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\x00-\x1F\x7F\x20]*`

## Errors
<a name="API_channel_ListChannelHandshakes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions.
 ** message **
A message describing the access denial.
 ** reason **
The reason for the access denial.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request.
 ** message **
A message describing the internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** message **
A message describing the resource not found error.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to too many requests being sent in a short period.
 ** message **
A message describing the throttling error.
 ** quotaCode **
The quota code associated with the throttling error.
 ** serviceCode **
The service code associated with the throttling error.
HTTP Status Code: 400

 ** ValidationException **
The request failed validation due to invalid input parameters.
 ** fieldList **
A list of fields that failed validation.
 ** message **
A message describing the validation error.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_channel_ListChannelHandshakes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-channel-2024-03-18/ListChannelHandshakes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-channel-2024-03-18/ListChannelHandshakes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/ListChannelHandshakes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-channel-2024-03-18/ListChannelHandshakes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/ListChannelHandshakes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-channel-2024-03-18/ListChannelHandshakes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-channel-2024-03-18/ListChannelHandshakes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-channel-2024-03-18/ListChannelHandshakes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-channel-2024-03-18/ListChannelHandshakes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/ListChannelHandshakes)
