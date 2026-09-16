---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreatePrivateGraphEndpoint.html
---

# CreatePrivateGraphEndpoint
<a name="API_CreatePrivateGraphEndpoint"></a>

Create a private graph endpoint to allow private access from to the graph from within a VPC. You can attach security groups to the private graph endpoint.

**Note**
VPC endpoint charges apply.

## Request Syntax
<a name="API_CreatePrivateGraphEndpoint_RequestSyntax"></a>

```
POST /graphs/{{graphIdentifier}}/endpoints/ HTTP/1.1
Content-type: application/json

{
   "subnetIds": [ "{{string}}" ],
   "vpcId": "{{string}}",
   "vpcSecurityGroupIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_CreatePrivateGraphEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [graphIdentifier](#API_CreatePrivateGraphEndpoint_RequestSyntax) **   <a name="neptunegraph-CreatePrivateGraphEndpoint-request-uri-graphIdentifier"></a>
The unique identifier of the Neptune Analytics graph.
Pattern: `g-[a-z0-9]{10}`
Required: Yes

## Request Body
<a name="API_CreatePrivateGraphEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [subnetIds](#API_CreatePrivateGraphEndpoint_RequestSyntax) **   <a name="neptunegraph-CreatePrivateGraphEndpoint-request-subnetIds"></a>
Subnets in which private graph endpoint ENIs are created.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Pattern: `subnet-[a-z0-9]+`
Required: No

 ** [vpcId](#API_CreatePrivateGraphEndpoint_RequestSyntax) **   <a name="neptunegraph-CreatePrivateGraphEndpoint-request-vpcId"></a>
 The VPC in which the private graph endpoint needs to be created.
Type: String
Pattern: `vpc-[a-z0-9]+`
Required: No

 ** [vpcSecurityGroupIds](#API_CreatePrivateGraphEndpoint_RequestSyntax) **   <a name="neptunegraph-CreatePrivateGraphEndpoint-request-vpcSecurityGroupIds"></a>
Security groups to be attached to the private graph endpoint..
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `sg-[a-z0-9]+`
Required: No

## Response Syntax
<a name="API_CreatePrivateGraphEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "status": "string",
   "subnetIds": [ "string" ],
   "vpcEndpointId": "string",
   "vpcId": "string"
}
```

## Response Elements
<a name="API_CreatePrivateGraphEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [status](#API_CreatePrivateGraphEndpoint_ResponseSyntax) **   <a name="neptunegraph-CreatePrivateGraphEndpoint-response-status"></a>
Status of the private graph endpoint.
Type: String
Valid Values: `CREATING | AVAILABLE | DELETING | FAILED`

 ** [subnetIds](#API_CreatePrivateGraphEndpoint_ResponseSyntax) **   <a name="neptunegraph-CreatePrivateGraphEndpoint-response-subnetIds"></a>
Subnets in which the private graph endpoint ENIs are created.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Pattern: `subnet-[a-z0-9]+`

 ** [vpcEndpointId](#API_CreatePrivateGraphEndpoint_ResponseSyntax) **   <a name="neptunegraph-CreatePrivateGraphEndpoint-response-vpcEndpointId"></a>
Endpoint ID of the prviate grpah endpoint.
Type: String
Pattern: `vpce-[0-9a-f]{17}`

 ** [vpcId](#API_CreatePrivateGraphEndpoint_ResponseSyntax) **   <a name="neptunegraph-CreatePrivateGraphEndpoint-response-vpcId"></a>
VPC in which the private graph endpoint is created.
Type: String
Pattern: `vpc-[a-z0-9]+`

## Errors
<a name="API_CreatePrivateGraphEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Raised when a conflict is encountered.
 ** message **
A message describing the problem.
 ** reason **
The reason for the conflict exception.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
A service quota was exceeded.
 ** quotaCode **
Service quota code of the resource for which quota was exceeded.
 ** resourceId **
The identifier of the resource that exceeded quota.
 ** resourceType **
The type of the resource that exceeded quota. Ex: Graph, Snapshot
 ** serviceCode **
The service code that exceeded quota.
HTTP Status Code: 402

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
<a name="API_CreatePrivateGraphEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/CreatePrivateGraphEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/CreatePrivateGraphEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/CreatePrivateGraphEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/CreatePrivateGraphEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/CreatePrivateGraphEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/CreatePrivateGraphEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/CreatePrivateGraphEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/CreatePrivateGraphEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/CreatePrivateGraphEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/CreatePrivateGraphEndpoint)
