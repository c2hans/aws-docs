---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_CancelSolNetworkOperation.html
---

# CancelSolNetworkOperation
<a name="API_CancelSolNetworkOperation"></a>

Cancels a network operation.

A network operation is any operation that is done to your network, such as network instance instantiation or termination.

## Request Syntax
<a name="API_CancelSolNetworkOperation_RequestSyntax"></a>

```
POST /sol/nslcm/v1/ns_lcm_op_occs/{{nsLcmOpOccId}}/cancel HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelSolNetworkOperation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [nsLcmOpOccId](#API_CancelSolNetworkOperation_RequestSyntax) **   <a name="TNB-CancelSolNetworkOperation-request-uri-nsLcmOpOccId"></a>
The identifier of the network operation.
Pattern: `no-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_CancelSolNetworkOperation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelSolNetworkOperation_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_CancelSolNetworkOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_CancelSolNetworkOperation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Insufficient permissions to make request.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error occurred. Problem on the server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource that doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
Exception caused by throttling.
HTTP Status Code: 429

 ** ValidationException **
Unable to process the request because the client provided input failed to satisfy request constraints.
HTTP Status Code: 400

## See Also
<a name="API_CancelSolNetworkOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/CancelSolNetworkOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/CancelSolNetworkOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/CancelSolNetworkOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/CancelSolNetworkOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/CancelSolNetworkOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/CancelSolNetworkOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/CancelSolNetworkOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/CancelSolNetworkOperation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/CancelSolNetworkOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/CancelSolNetworkOperation)
