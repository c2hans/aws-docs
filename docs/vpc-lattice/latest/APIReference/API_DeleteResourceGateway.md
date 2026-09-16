---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteResourceGateway.html
---

# DeleteResourceGateway
<a name="API_DeleteResourceGateway"></a>

Deletes the specified resource gateway.

## Request Syntax
<a name="API_DeleteResourceGateway_RequestSyntax"></a>

```
DELETE /resourcegateways/{{resourceGatewayIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteResourceGateway_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceGatewayIdentifier](#API_DeleteResourceGateway_RequestSyntax) **   <a name="vpclattice-DeleteResourceGateway-request-uri-resourceGatewayIdentifier"></a>
The ID or ARN of the resource gateway.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((rgw-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourcegateway/rgw-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_DeleteResourceGateway_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteResourceGateway_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteResourceGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DeleteResourceGateway_ResponseSyntax) **   <a name="vpclattice-DeleteResourceGateway-response-arn"></a>
The Amazon Resource Name (ARN) of the resource gateway.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourcegateway/rgw-[0-9a-z]{17}`

 ** [id](#API_DeleteResourceGateway_ResponseSyntax) **   <a name="vpclattice-DeleteResourceGateway-response-id"></a>
The ID of the resource gateway.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rgw-[0-9a-z]{17}`

 ** [name](#API_DeleteResourceGateway_ResponseSyntax) **   <a name="vpclattice-DeleteResourceGateway-response-name"></a>
The name of the resource gateway.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!rgw-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [status](#API_DeleteResourceGateway_ResponseSyntax) **   <a name="vpclattice-DeleteResourceGateway-response-status"></a>
The status of the resource gateway.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`

## Errors
<a name="API_DeleteResourceGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
 ** serviceCode **
The service code.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** fieldList **
The fields that failed validation.
 ** reason **
The reason.
HTTP Status Code: 400

## See Also
<a name="API_DeleteResourceGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/DeleteResourceGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/DeleteResourceGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/DeleteResourceGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/DeleteResourceGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/DeleteResourceGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/DeleteResourceGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/DeleteResourceGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/DeleteResourceGateway)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/DeleteResourceGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/DeleteResourceGateway)
