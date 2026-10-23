---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_RevokeConnectionToken.html
---

# RevokeConnectionToken
<a name="API_RevokeConnectionToken"></a>

Revokes the specified connection token so that it can no longer connect to a stage. This operation disconnects any participant currently connected with the revoked token.

## Request Syntax
<a name="API_RevokeConnectionToken_RequestSyntax"></a>

```
POST /RevokeConnectionToken HTTP/1.1
Content-type: application/json

{
   "tokenId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RevokeConnectionToken_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RevokeConnectionToken_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tokenId](#API_RevokeConnectionToken_RequestSyntax) **   <a name="ivsrealtimeeapireference-RevokeConnectionToken-request-tokenId"></a>
The ID of the connection token to revoke.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

## Response Syntax
<a name="API_RevokeConnectionToken_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_RevokeConnectionToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RevokeConnectionToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_RevokeConnectionToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/RevokeConnectionToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/RevokeConnectionToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/RevokeConnectionToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/RevokeConnectionToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/RevokeConnectionToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/RevokeConnectionToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/RevokeConnectionToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/RevokeConnectionToken)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/RevokeConnectionToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/RevokeConnectionToken)
