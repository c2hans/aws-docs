---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ListManagedThingSchemas.html
---

# ListManagedThingSchemas
<a name="API_ListManagedThingSchemas"></a>

List schemas associated with a managed thing.

## Request Syntax
<a name="API_ListManagedThingSchemas_RequestSyntax"></a>

```
GET /managed-thing-schemas/{{Identifier}}?CapabilityIdFilter={{CapabilityIdFilter}}&EndpointIdFilter={{EndpointIdFilter}}&MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListManagedThingSchemas_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CapabilityIdFilter](#API_ListManagedThingSchemas_RequestSyntax) **   <a name="managedintegrations-ListManagedThingSchemas-request-uri-CapabilityIdFilter"></a>
Filter on a capability id.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9./]+(@\d+\.\d+)?`

 ** [EndpointIdFilter](#API_ListManagedThingSchemas_RequestSyntax) **   <a name="managedintegrations-ListManagedThingSchemas-request-uri-EndpointIdFilter"></a>
Filter on an endpoint id.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`

 ** [Identifier](#API_ListManagedThingSchemas_RequestSyntax) **   <a name="managedintegrations-ListManagedThingSchemas-request-uri-Identifier"></a>
The managed thing id.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: Yes

 ** [MaxResults](#API_ListManagedThingSchemas_RequestSyntax) **   <a name="managedintegrations-ListManagedThingSchemas-request-uri-MaxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListManagedThingSchemas_RequestSyntax) **   <a name="managedintegrations-ListManagedThingSchemas-request-uri-NextToken"></a>
A token that can be used to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

## Request Body
<a name="API_ListManagedThingSchemas_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListManagedThingSchemas_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "CapabilityId": "string",
         "EndpointId": "string",
         "Schema": JSON value
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListManagedThingSchemas_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListManagedThingSchemas_ResponseSyntax) **   <a name="managedintegrations-ListManagedThingSchemas-response-Items"></a>
The list of managed thing schemas.
Type: Array of [ManagedThingSchemaListItem](API_ManagedThingSchemaListItem.md) objects

 ** [NextToken](#API_ListManagedThingSchemas_ResponseSyntax) **   <a name="managedintegrations-ListManagedThingSchemas-response-NextToken"></a>
A token that can be used to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

## Errors
<a name="API_ListManagedThingSchemas_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** UnauthorizedException **
You are not authorized to perform this operation.
HTTP Status Code: 401

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_ListManagedThingSchemas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/ListManagedThingSchemas)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/ListManagedThingSchemas)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ListManagedThingSchemas)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/ListManagedThingSchemas)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ListManagedThingSchemas)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/ListManagedThingSchemas)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/ListManagedThingSchemas)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/ListManagedThingSchemas)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/ListManagedThingSchemas)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ListManagedThingSchemas)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
