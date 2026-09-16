---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_ListAppInstanceBots.html
---

# ListAppInstanceBots
<a name="API_ListAppInstanceBots"></a>

Lists all `AppInstanceBots` created under a single `AppInstance`.

## Request Syntax
<a name="API_ListAppInstanceBots_RequestSyntax"></a>

```
GET /app-instance-bots?app-instance-arn={{AppInstanceArn}}&max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAppInstanceBots_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AppInstanceArn](#API_ListAppInstanceBots_RequestSyntax) **   <a name="chimesdk-ListAppInstanceBots-request-uri-AppInstanceArn"></a>
The ARN of the `AppInstance`.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [MaxResults](#API_ListAppInstanceBots_RequestSyntax) **   <a name="chimesdk-ListAppInstanceBots-request-uri-MaxResults"></a>
The maximum number of requests to return.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListAppInstanceBots_RequestSyntax) **   <a name="chimesdk-ListAppInstanceBots-request-uri-NextToken"></a>
The token passed by previous API calls until all requested bots are returned.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

## Request Body
<a name="API_ListAppInstanceBots_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAppInstanceBots_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AppInstanceArn": "string",
   "AppInstanceBots": [
      {
         "AppInstanceBotArn": "string",
         "Metadata": "string",
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAppInstanceBots_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppInstanceArn](#API_ListAppInstanceBots_ResponseSyntax) **   <a name="chimesdk-ListAppInstanceBots-response-AppInstanceArn"></a>
The ARN of the AppInstance.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [AppInstanceBots](#API_ListAppInstanceBots_ResponseSyntax) **   <a name="chimesdk-ListAppInstanceBots-response-AppInstanceBots"></a>
The information for each requested `AppInstanceBot`.
Type: Array of [AppInstanceBotSummary](API_AppInstanceBotSummary.md) objects

 ** [NextToken](#API_ListAppInstanceBots_ResponseSyntax) **   <a name="chimesdk-ListAppInstanceBots-response-NextToken"></a>
The token passed by previous API calls until all requested bots are returned.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

## Errors
<a name="API_ListAppInstanceBots_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
HTTP Status Code: 400

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

## See Also
<a name="API_ListAppInstanceBots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-identity-2021-04-20/ListAppInstanceBots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-identity-2021-04-20/ListAppInstanceBots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/ListAppInstanceBots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-identity-2021-04-20/ListAppInstanceBots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/ListAppInstanceBots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-identity-2021-04-20/ListAppInstanceBots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-identity-2021-04-20/ListAppInstanceBots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-identity-2021-04-20/ListAppInstanceBots)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-identity-2021-04-20/ListAppInstanceBots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/ListAppInstanceBots)
