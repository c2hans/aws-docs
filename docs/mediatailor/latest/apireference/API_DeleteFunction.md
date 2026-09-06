---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DeleteFunction.html
---

# DeleteFunction
<a name="API_DeleteFunction"></a>

Deletes a function. MediaTailor prevents deletion of a function that is still referenced by a playback configuration or by another function. Remove all references before deleting. For more information about functions, see [Working with functions](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the *MediaTailor User Guide*.

## Request Syntax
<a name="API_DeleteFunction_RequestSyntax"></a>

```
DELETE /function/{{FunctionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteFunction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionId](#API_DeleteFunction_RequestSyntax) **   <a name="mediatailor-DeleteFunction-request-uri-FunctionId"></a>
The identifier of the function to delete.
Required: Yes

## Request Body
<a name="API_DeleteFunction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteFunction_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteFunction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DeleteFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/DeleteFunction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/DeleteFunction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/DeleteFunction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/DeleteFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/DeleteFunction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/DeleteFunction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/DeleteFunction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/DeleteFunction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/DeleteFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/DeleteFunction)
