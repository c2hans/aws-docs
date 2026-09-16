---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetPrivateGraphEndpoint.html
---

# GetPrivateGraphEndpoint
<a name="API_GetPrivateGraphEndpoint"></a>

Retrieves information about a specified private endpoint.

## Request Syntax
<a name="API_GetPrivateGraphEndpoint_RequestSyntax"></a>

```
GET /graphs/{{graphIdentifier}}/endpoints/{{vpcId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPrivateGraphEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [graphIdentifier](#API_GetPrivateGraphEndpoint_RequestSyntax) **   <a name="neptunegraph-GetPrivateGraphEndpoint-request-uri-graphIdentifier"></a>
The unique identifier of the Neptune Analytics graph.
Pattern: `g-[a-z0-9]{10}`
Required: Yes

 ** [vpcId](#API_GetPrivateGraphEndpoint_RequestSyntax) **   <a name="neptunegraph-GetPrivateGraphEndpoint-request-uri-vpcId"></a>
The ID of the VPC where the private endpoint is located.
Pattern: `vpc-[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_GetPrivateGraphEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPrivateGraphEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string",
   "subnetIds": [ "string" ],
   "vpcEndpointId": "string",
   "vpcId": "string"
}
```

## Response Elements
<a name="API_GetPrivateGraphEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_GetPrivateGraphEndpoint_ResponseSyntax) **   <a name="neptunegraph-GetPrivateGraphEndpoint-response-status"></a>
The current status of the private endpoint.
Type: String
Valid Values: `CREATING | AVAILABLE | DELETING | FAILED`

 ** [subnetIds](#API_GetPrivateGraphEndpoint_ResponseSyntax) **   <a name="neptunegraph-GetPrivateGraphEndpoint-response-subnetIds"></a>
The subnet IDs involved.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Pattern: `subnet-[a-z0-9]+`

 ** [vpcEndpointId](#API_GetPrivateGraphEndpoint_ResponseSyntax) **   <a name="neptunegraph-GetPrivateGraphEndpoint-response-vpcEndpointId"></a>
The ID of the private endpoint.
Type: String
Pattern: `vpce-[0-9a-f]{17}`

 ** [vpcId](#API_GetPrivateGraphEndpoint_ResponseSyntax) **   <a name="neptunegraph-GetPrivateGraphEndpoint-response-vpcId"></a>
The ID of the VPC where the private endpoint is located.
Type: String
Pattern: `vpc-[a-z0-9]+`

## Errors
<a name="API_GetPrivateGraphEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
A failure occurred on the server.
 ** message **
A message describing the problem.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A specified resource could not be located.
 ** message **
A message describing the problem.
HTTP Status Code: 404

 ** ThrottlingException **
The exception was interrupted by throttling.
 ** message **
A message describing the problem.
HTTP Status Code: 429

 ** ValidationException **
A resource could not be validated.
 ** message **
A message describing the problem.
 ** reason **
The reason that the resource could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_GetPrivateGraphEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/GetPrivateGraphEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/GetPrivateGraphEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/GetPrivateGraphEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/GetPrivateGraphEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/GetPrivateGraphEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/GetPrivateGraphEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/GetPrivateGraphEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/GetPrivateGraphEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/GetPrivateGraphEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/GetPrivateGraphEndpoint)
