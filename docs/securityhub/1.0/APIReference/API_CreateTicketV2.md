---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateTicketV2.html
---

# CreateTicketV2
<a name="API_CreateTicketV2"></a>

Grants permission to create a ticket in the chosen ITSM based on finding information for the provided finding metadata UID.

## Request Syntax
<a name="API_CreateTicketV2_RequestSyntax"></a>

```
POST /ticketsv2 HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "ConnectorId": "{{string}}",
   "FindingMetadataUid": "{{string}}",
   "Mode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateTicketV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTicketV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateTicketV2_RequestSyntax) **   <a name="securityhub-CreateTicketV2-request-ClientToken"></a>
The client idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[\x21-\x7E]{1,64}$`
Required: No

 ** [ConnectorId](#API_CreateTicketV2_RequestSyntax) **   <a name="securityhub-CreateTicketV2-request-ConnectorId"></a>
The UUID of the connectorV2 to identify connectorV2 resource.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [FindingMetadataUid](#API_CreateTicketV2_RequestSyntax) **   <a name="securityhub-CreateTicketV2-request-FindingMetadataUid"></a>
The the unique ID for the finding.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [Mode](#API_CreateTicketV2_RequestSyntax) **   <a name="securityhub-CreateTicketV2-request-Mode"></a>
The mode for ticket creation. When set to DRYRUN, the ticket is created using a Security Hub owned template test finding to verify the integration is working correctly.
Type: String
Valid Values: `DRYRUN`
Required: No

## Response Syntax
<a name="API_CreateTicketV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "TicketId": "string",
   "TicketSrcUrl": "string"
}
```

## Response Elements
<a name="API_CreateTicketV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TicketId](#API_CreateTicketV2_ResponseSyntax) **   <a name="securityhub-CreateTicketV2-response-TicketId"></a>
The ID for the ticketv2.
Type: String
Pattern: `.*\S.*`

 ** [TicketSrcUrl](#API_CreateTicketV2_ResponseSyntax) **   <a name="securityhub-CreateTicketV2-response-TicketSrcUrl"></a>
The url to the created ticket.
Type: String
Pattern: `.*\S.*`

## Errors
<a name="API_CreateTicketV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** ConflictException **
The request causes conflict with the current state of the service resource.
HTTP Status Code: 409

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_CreateTicketV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/CreateTicketV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/CreateTicketV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CreateTicketV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/CreateTicketV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CreateTicketV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/CreateTicketV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/CreateTicketV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/CreateTicketV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/CreateTicketV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CreateTicketV2)
