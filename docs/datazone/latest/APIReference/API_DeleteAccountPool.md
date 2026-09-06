---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DeleteAccountPool.html
---

# DeleteAccountPool
<a name="API_DeleteAccountPool"></a>

Deletes an account pool.

## Request Syntax
<a name="API_DeleteAccountPool_RequestSyntax"></a>

```
DELETE /v2/domains/{{domainIdentifier}}/account-pools/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAccountPool_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_DeleteAccountPool_RequestSyntax) **   <a name="datazone-DeleteAccountPool-request-uri-domainIdentifier"></a>
The ID of the domain where the account pool is deleted.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_DeleteAccountPool_RequestSyntax) **   <a name="datazone-DeleteAccountPool-request-uri-identifier"></a>
The ID of the account pool to be deleted.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_DeleteAccountPool_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAccountPool_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteAccountPool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteAccountPool_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAccountPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/DeleteAccountPool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/DeleteAccountPool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DeleteAccountPool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/DeleteAccountPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DeleteAccountPool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/DeleteAccountPool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/DeleteAccountPool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/DeleteAccountPool)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/DeleteAccountPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DeleteAccountPool)
