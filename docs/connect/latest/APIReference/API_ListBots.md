---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListBots.html
---

# ListBots
<a name="API_ListBots"></a>

This API is in preview release for Connect Customer and is subject to change.

For the specified version of Amazon Lex, returns a paginated list of all the Amazon Lex bots currently associated with the instance. Use this API to return both Amazon Lex V1 and V2 bots.

## Request Syntax
<a name="API_ListBots_RequestSyntax"></a>

```
GET /instance/{{InstanceId}}/bots?lexVersion={{LexVersion}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBots_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListBots_RequestSyntax) **   <a name="connect-ListBots-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [LexVersion](#API_ListBots_RequestSyntax) **   <a name="connect-ListBots-request-uri-LexVersion"></a>
The version of Amazon Lex or Amazon Lex V2.
Valid Values: `V1 | V2`
Required: Yes

 ** [MaxResults](#API_ListBots_RequestSyntax) **   <a name="connect-ListBots-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [NextToken](#API_ListBots_RequestSyntax) **   <a name="connect-ListBots-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListBots_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBots_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LexBots": [
      {
         "LexBot": {
            "LexRegion": "string",
            "Name": "string"
         },
         "LexV2Bot": {
            "AliasArn": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListBots_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LexBots](#API_ListBots_ResponseSyntax) **   <a name="connect-ListBots-response-LexBots"></a>
The names and AWS Regions of the Amazon Lex or Amazon Lex V2 bots associated with the specified instance.
Type: Array of [LexBotConfig](API_LexBotConfig.md) objects

 ** [NextToken](#API_ListBots_ResponseSyntax) **   <a name="connect-ListBots-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListBots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListBots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListBots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListBots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListBots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListBots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListBots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListBots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListBots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListBots)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListBots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListBots)
