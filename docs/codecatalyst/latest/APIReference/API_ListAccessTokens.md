---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListAccessTokens.html
---

# ListAccessTokens
<a name="API_ListAccessTokens"></a>

Lists all personal access tokens (PATs) associated with the user who calls the API. You can only list PATs associated with your AWS Builder ID.

## Request Syntax
<a name="API_ListAccessTokens_RequestSyntax"></a>

```
POST /v1/accessTokens HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListAccessTokens_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListAccessTokens_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListAccessTokens_RequestSyntax) **   <a name="codecatalyst-ListAccessTokens-request-maxResults"></a>
The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a `NextToken` element, which you can use to obtain additional results.
Type: Integer
Valid Range: Maximum value of 10.
Required: No

 ** [nextToken](#API_ListAccessTokens_RequestSyntax) **   <a name="codecatalyst-ListAccessTokens-request-nextToken"></a>
A token returned from a call to this API to indicate the next batch of results to return, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: No

## Response Syntax
<a name="API_ListAccessTokens_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "expiresTime": "string",
         "id": "string",
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAccessTokens_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListAccessTokens_ResponseSyntax) **   <a name="codecatalyst-ListAccessTokens-response-items"></a>
A list of personal access tokens (PATs) associated with the calling user identity.
Type: Array of [AccessTokenSummary](API_AccessTokenSummary.md) objects

 ** [nextToken](#API_ListAccessTokens_ResponseSyntax) **   <a name="codecatalyst-ListAccessTokens-response-nextToken"></a>
A token returned from a call to this API to indicate the next batch of results to return, if any.
Type: String

## Errors
<a name="API_ListAccessTokens_Errors"></a>

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
<a name="API_ListAccessTokens_Examples"></a>

### Example
<a name="API_ListAccessTokens_Example_1"></a>

This example illustrates one usage of ListAccessTokens.

#### Sample Request
<a name="API_ListAccessTokens_Example_1_Request"></a>

```
POST https://codecatalyst.global.api.aws/v1/accessTokens
Host: codecatalyst.global.api.aws
Accept-Encoding: identity
User-Agent: aws-cli/2.7.31 Python/3.10.8 Darwin/21.6.0 source/x86_64 prompt/off command/codecatalyst.list-access-tokens
Content-Type: application/x-amz-json-1.1
Authorization: Bearer AKIAI44QH8DHBEXAMPLE
```

#### Sample Response
<a name="API_ListAccessTokens_Example_1_Response"></a>

```
200 OK 411b
Content-Type: application/json; charset=utf-8
Date: Sat, 05 Nov 2022 13:16:05 GMT

{
    "items": [
        {
            "accessTokenId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
            "expiresTime": "2023-02-16T14:50:02.114Z",
            "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
            "issued": "2022-02-16T14:50:03.863Z",
            "name": "marymajor-22222EXAMPLE"
        },
        {
            "accessTokenId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
            "expiresTime": "2023-02-16T14:50:02.114Z",
            "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
            "issued": "2022-03-16T14:50:03.863Z",
            "name": "marymajor-11111EXAMPLE"
        }
    ]
}
```

## See Also
<a name="API_ListAccessTokens_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/ListAccessTokens)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/ListAccessTokens)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/ListAccessTokens)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/ListAccessTokens)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/ListAccessTokens)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/ListAccessTokens)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/ListAccessTokens)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/ListAccessTokens)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/ListAccessTokens)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/ListAccessTokens)
