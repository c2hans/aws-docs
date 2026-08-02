---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateVpcLink.html
---

# UpdateVpcLink
<a name="API_UpdateVpcLink"></a>

Updates an existing VpcLink of a specified identifier.

## Request Syntax
<a name="API_UpdateVpcLink_RequestSyntax"></a>

```
PATCH /vpclinks/{{vpclink_id}} HTTP/1.1
Content-type: application/json

{
   "patchOperations": [
      {
         "from": "{{string}}",
         "op": "{{string}}",
         "path": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateVpcLink_RequestParameters"></a>

The request uses the following URI parameters.

 ** [vpclink\_id](#API_UpdateVpcLink_RequestSyntax) **   <a name="apigw-UpdateVpcLink-request-uri-vpcLinkId"></a>
The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.
Required: Yes

## Request Body
<a name="API_UpdateVpcLink_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [patchOperations](#API_UpdateVpcLink_RequestSyntax) **   <a name="apigw-UpdateVpcLink-request-patchOperations"></a>
For more information about supported patch operations, see [Patch Operations](patch-operations.md).
Type: Array of [PatchOperation](API_PatchOperation.md) objects
Required: No

## Response Syntax
<a name="API_UpdateVpcLink_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "description": "string",
   "id": "string",
   "name": "string",
   "status": "string",
   "statusMessage": "string",
   "tags": {
      "string" : "string"
   },
   "targetArns": [ "string" ]
}
```

## Response Elements
<a name="API_UpdateVpcLink_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_UpdateVpcLink_ResponseSyntax) **   <a name="apigw-UpdateVpcLink-response-description"></a>
The description of the VPC link.
Type: String

 ** [id](#API_UpdateVpcLink_ResponseSyntax) **   <a name="apigw-UpdateVpcLink-response-id"></a>
The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.
Type: String

 ** [name](#API_UpdateVpcLink_ResponseSyntax) **   <a name="apigw-UpdateVpcLink-response-name"></a>
The name used to label and identify the VPC link.
Type: String

 ** [status](#API_UpdateVpcLink_ResponseSyntax) **   <a name="apigw-UpdateVpcLink-response-status"></a>
The status of the VPC link. The valid values are `AVAILABLE`, `PENDING`, `DELETING`, or `FAILED`. Deploying an API will wait if the status is `PENDING` and will fail if the status is `DELETING`.
Type: String
Valid Values: `AVAILABLE | PENDING | DELETING | FAILED`

 ** [statusMessage](#API_UpdateVpcLink_ResponseSyntax) **   <a name="apigw-UpdateVpcLink-response-statusMessage"></a>
A description about the VPC link status.
Type: String

 ** [tags](#API_UpdateVpcLink_ResponseSyntax) **   <a name="apigw-UpdateVpcLink-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

 ** [targetArns](#API_UpdateVpcLink_ResponseSyntax) **   <a name="apigw-UpdateVpcLink-response-targetArns"></a>
The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same AWS account of the API owner.
Type: Array of strings

## Errors
<a name="API_UpdateVpcLink_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 409

 ** LimitExceededException **
The request exceeded the rate limit. Retry after the specified time period.
HTTP Status Code: 429

 ** NotFoundException **
The requested resource is not found. Make sure that the request URI is correct.
HTTP Status Code: 404

 ** TooManyRequestsException **
The request has reached its throttling limit. Retry after the specified time period.
HTTP Status Code: 429

 ** UnauthorizedException **
The request is denied because the caller has insufficient permissions.
HTTP Status Code: 401

## See Also
<a name="API_UpdateVpcLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/UpdateVpcLink)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/UpdateVpcLink)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/UpdateVpcLink)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/UpdateVpcLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/UpdateVpcLink)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/UpdateVpcLink)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/UpdateVpcLink)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/UpdateVpcLink)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/UpdateVpcLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/UpdateVpcLink)
