---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ListPrivateConnections.html
---

# ListPrivateConnections
<a name="API_ListPrivateConnections"></a>

Lists the private connections in your account.

## Request Syntax
<a name="API_ListPrivateConnections_RequestSyntax"></a>

```
POST /ListPrivateConnections HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListPrivateConnections_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListPrivateConnections_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListPrivateConnections_RequestSyntax) **   <a name="securityagent-ListPrivateConnections-request-maxResults"></a>
The maximum number of private connections to return in a single response.
Type: Integer
Required: No

 ** [nextToken](#API_ListPrivateConnections_RequestSyntax) **   <a name="securityagent-ListPrivateConnections-request-nextToken"></a>
The token for the next page of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListPrivateConnections_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "privateConnections": [
      {
         "certificateExpiryTime": "string",
         "dnsResolution": "string",
         "failureMessage": "string",
         "hostAddress": "string",
         "name": "string",
         "resourceConfigurationId": "string",
         "resourceGatewayId": "string",
         "status": "string",
         "tags": {
            "string" : "string"
         },
         "type": "string",
         "vpcId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPrivateConnections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPrivateConnections_ResponseSyntax) **   <a name="securityagent-ListPrivateConnections-response-nextToken"></a>
The token to use to retrieve the next page of results, if more results are available.
Type: String

 ** [privateConnections](#API_ListPrivateConnections_ResponseSyntax) **   <a name="securityagent-ListPrivateConnections-response-privateConnections"></a>
The list of private connections.
Type: Array of [PrivateConnectionSummary](API_PrivateConnectionSummary.md) objects

## Errors
<a name="API_ListPrivateConnections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** message **
Error description.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of your request.
 ** message **
Error description.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** message **
Error description.
 ** quotaCode **
Quota code for throttling limit.
 ** serviceCode **
Service code for throttling limit.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered during validation.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListPrivateConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/ListPrivateConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/ListPrivateConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ListPrivateConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/ListPrivateConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ListPrivateConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/ListPrivateConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/ListPrivateConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/ListPrivateConnections)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/ListPrivateConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ListPrivateConnections)
