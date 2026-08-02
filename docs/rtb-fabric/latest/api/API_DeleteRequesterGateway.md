---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_DeleteRequesterGateway.html
---

# DeleteRequesterGateway
<a name="API_DeleteRequesterGateway"></a>

Deletes a requester gateway.

## Request Syntax
<a name="API_DeleteRequesterGateway_RequestSyntax"></a>

```
DELETE /requester-gateway/{{gatewayId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteRequesterGateway_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayId](#API_DeleteRequesterGateway_RequestSyntax) **   <a name="rtbfabric-DeleteRequesterGateway-request-uri-gatewayId"></a>
The unique identifier of the gateway.
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

## Request Body
<a name="API_DeleteRequesterGateway_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteRequesterGateway_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "gatewayId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteRequesterGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [gatewayId](#API_DeleteRequesterGateway_ResponseSyntax) **   <a name="rtbfabric-DeleteRequesterGateway-response-gatewayId"></a>
The unique identifier of the gateway.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`

 ** [status](#API_DeleteRequesterGateway_ResponseSyntax) **   <a name="rtbfabric-DeleteRequesterGateway-response-status"></a>
The status of the request.
Type: String
Valid Values: `PENDING_CREATION | ACTIVE | PENDING_DELETION | DELETED | ERROR | PENDING_UPDATE | ISOLATED | PENDING_ISOLATION | PENDING_RESTORATION`

## Errors
<a name="API_DeleteRequesterGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed because of a conflict in the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request could not be completed because the resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteRequesterGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/DeleteRequesterGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/DeleteRequesterGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/DeleteRequesterGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/DeleteRequesterGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/DeleteRequesterGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/DeleteRequesterGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/DeleteRequesterGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/DeleteRequesterGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/DeleteRequesterGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/DeleteRequesterGateway)
