---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_DeleteAccessToken.html
---

# DeleteAccessToken
<a name="API_DeleteAccessToken"></a>

Deletes a specified personal access token (PAT). A personal access token can only be deleted by the user who created it.

## Request Syntax
<a name="API_DeleteAccessToken_RequestSyntax"></a>

```
DELETE /v1/accessTokens/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAccessToken_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_DeleteAccessToken_RequestSyntax) **   <a name="codecatalyst-DeleteAccessToken-request-uri-id"></a>
The ID of the personal access token to delete. You can find the IDs of all PATs associated with your AWS Builder ID in a space by calling [ListAccessTokens](API_ListAccessTokens.md).
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

## Request Body
<a name="API_DeleteAccessToken_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAccessToken_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteAccessToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAccessToken_Errors"></a>

 ** AccessDeniedException **
The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.
HTTP Status Code: 403

 ** ConflictException **
The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.
HTTP Status Code: 400

## Examples
<a name="API_DeleteAccessToken_Examples"></a>

### Example
<a name="API_DeleteAccessToken_Example_1"></a>

The following example illustrates using DeleteAccessToken to delete the personal access token with the ID of *a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb*. To get the ID of a personal access token, use [ListAccessTokens](API_ListAccessTokens.md).

#### Sample Request
<a name="API_DeleteAccessToken_Example_1_Request"></a>

```
DELETE https://codecatalyst.global.api.aws/v1/accessTokens/a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb
Host: codecatalyst.global.api.aws
Accept-Encoding: identity
User-Agent: aws-cli/2.7.31 Python/3.10.8 Darwin/21.6.0 source/x86_64 prompt/off command/codecatalyst.delete-access-token
Content-Type: application/x-amz-json-1.1
Authorization: Bearer AKIAI44QH8DHBEXAMPLE
Content-Length: 0
```

#### Sample Response
<a name="API_DeleteAccessToken_Example_1_Response"></a>

```
200 OK 2b
Content-Type: application/json; charset=utf-8
Date: Sat, 05 Nov 2022 13:20:05 GMT

{}
```

## See Also
<a name="API_DeleteAccessToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/DeleteAccessToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/DeleteAccessToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/DeleteAccessToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/DeleteAccessToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/DeleteAccessToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/DeleteAccessToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/DeleteAccessToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/DeleteAccessToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/DeleteAccessToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/DeleteAccessToken)
