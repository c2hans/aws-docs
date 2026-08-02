---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteListener.html
---

# DeleteListener
<a name="API_DeleteListener"></a>

Deletes the specified listener.

## Request Syntax
<a name="API_DeleteListener_RequestSyntax"></a>

```
DELETE /services/{{serviceIdentifier}}/listeners/{{listenerIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteListener_RequestParameters"></a>

The request uses the following URI parameters.

 ** [listenerIdentifier](#API_DeleteListener_RequestSyntax) **   <a name="vpclattice-DeleteListener-request-uri-listenerIdentifier"></a>
The ID or ARN of the listener.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((listener-[0-9a-z]{17})|(^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}$))`
Required: Yes

 ** [serviceIdentifier](#API_DeleteListener_RequestSyntax) **   <a name="vpclattice-DeleteListener-request-uri-serviceIdentifier"></a>
The ID or ARN of the service.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((svc-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_DeleteListener_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteListener_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteListener_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteListener_Errors"></a>

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
<a name="API_DeleteListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/DeleteListener)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/DeleteListener)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/DeleteListener)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/DeleteListener)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/DeleteListener)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/DeleteListener)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/DeleteListener)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/DeleteListener)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/DeleteListener)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/DeleteListener)
