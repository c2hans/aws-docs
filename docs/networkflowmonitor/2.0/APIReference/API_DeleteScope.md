---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_DeleteScope.html
---

# DeleteScope
<a name="API_DeleteScope"></a>

Deletes a scope that has been defined.

## Request Syntax
<a name="API_DeleteScope_RequestSyntax"></a>

```
DELETE /scopes/{{scopeId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteScope_RequestParameters"></a>

The request uses the following URI parameters.

 ** [scopeId](#API_DeleteScope_RequestSyntax) **   <a name="networkflowmonitor-DeleteScope-request-uri-scopeId"></a>
The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.
Required: Yes

## Request Body
<a name="API_DeleteScope_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteScope_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteScope_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteScope_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The requested resource is in use.
HTTP Status Code: 409

 ** InternalServerException **
An internal error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request specifies a resource that doesn't exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeded a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
Invalid request.
HTTP Status Code: 400

## See Also
<a name="API_DeleteScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/DeleteScope)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/DeleteScope)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/DeleteScope)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/DeleteScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/DeleteScope)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/DeleteScope)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/DeleteScope)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/DeleteScope)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/DeleteScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/DeleteScope)
