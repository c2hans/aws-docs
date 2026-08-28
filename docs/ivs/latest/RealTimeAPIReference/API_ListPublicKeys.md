---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListPublicKeys.html
---

# ListPublicKeys
<a name="API_ListPublicKeys"></a>

Gets summary information about all public keys in your account, in the AWS region where the API request is processed.

## Request Syntax
<a name="API_ListPublicKeys_RequestSyntax"></a>

```
POST /ListPublicKeys HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListPublicKeys_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListPublicKeys_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListPublicKeys_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListPublicKeys-request-maxResults"></a>
Maximum number of results to return. Default: 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListPublicKeys_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListPublicKeys-request-nextToken"></a>
The first public key to retrieve. This is used for pagination; see the `nextToken` response field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`
Required: No

## Response Syntax
<a name="API_ListPublicKeys_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "publicKeys": [
      {
         "arn": "string",
         "name": "string",
         "tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListPublicKeys_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPublicKeys_ResponseSyntax) **   <a name="ivsrealtimeeapireference-ListPublicKeys-response-nextToken"></a>
If there are more public keys than `maxResults`, use `nextToken` in the request to get the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`

 ** [publicKeys](#API_ListPublicKeys_ResponseSyntax) **   <a name="ivsrealtimeeapireference-ListPublicKeys-response-publicKeys"></a>
List of the matching public keys (summary information only).
Type: Array of [PublicKeySummary](API_PublicKeySummary.md) objects

## Errors
<a name="API_ListPublicKeys_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** exceptionMessage **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ValidationException **

 ** exceptionMessage **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListPublicKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/ListPublicKeys)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/ListPublicKeys)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/ListPublicKeys)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/ListPublicKeys)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/ListPublicKeys)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/ListPublicKeys)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/ListPublicKeys)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/ListPublicKeys)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/ListPublicKeys)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/ListPublicKeys)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
