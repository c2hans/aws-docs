---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_ListAppInstanceUserEndpoints.html
---

# ListAppInstanceUserEndpoints
<a name="API_ListAppInstanceUserEndpoints"></a>

Lists all the `AppInstanceUserEndpoints` created under a single `AppInstanceUser`.

## Request Syntax
<a name="API_ListAppInstanceUserEndpoints_RequestSyntax"></a>

```
GET /app-instance-users/{{appInstanceUserArn}}/endpoints?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAppInstanceUserEndpoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appInstanceUserArn](#API_ListAppInstanceUserEndpoints_RequestSyntax) **   <a name="chimesdk-ListAppInstanceUserEndpoints-request-uri-AppInstanceUserArn"></a>
The ARN of the `AppInstanceUser`.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [MaxResults](#API_ListAppInstanceUserEndpoints_RequestSyntax) **   <a name="chimesdk-ListAppInstanceUserEndpoints-request-uri-MaxResults"></a>
The maximum number of endpoints that you want to return.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListAppInstanceUserEndpoints_RequestSyntax) **   <a name="chimesdk-ListAppInstanceUserEndpoints-request-uri-NextToken"></a>
The token passed by previous API calls until all requested endpoints are returned.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

## Request Body
<a name="API_ListAppInstanceUserEndpoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAppInstanceUserEndpoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AppInstanceUserEndpoints": [
      {
         "AllowMessages": "string",
         "AppInstanceUserArn": "string",
         "EndpointId": "string",
         "EndpointState": {
            "Status": "string",
            "StatusReason": "string"
         },
         "Name": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAppInstanceUserEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppInstanceUserEndpoints](#API_ListAppInstanceUserEndpoints_ResponseSyntax) **   <a name="chimesdk-ListAppInstanceUserEndpoints-response-AppInstanceUserEndpoints"></a>
The information for each requested `AppInstanceUserEndpoint`.
Type: Array of [AppInstanceUserEndpointSummary](API_AppInstanceUserEndpointSummary.md) objects

 ** [NextToken](#API_ListAppInstanceUserEndpoints_ResponseSyntax) **   <a name="chimesdk-ListAppInstanceUserEndpoints-response-NextToken"></a>
The token passed by previous API calls until all requested endpoints are returned.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

## Errors
<a name="API_ListAppInstanceUserEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

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
<a name="API_ListAppInstanceUserEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-identity-2021-04-20/ListAppInstanceUserEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-identity-2021-04-20/ListAppInstanceUserEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/ListAppInstanceUserEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-identity-2021-04-20/ListAppInstanceUserEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/ListAppInstanceUserEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-identity-2021-04-20/ListAppInstanceUserEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-identity-2021-04-20/ListAppInstanceUserEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-identity-2021-04-20/ListAppInstanceUserEndpoints)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-identity-2021-04-20/ListAppInstanceUserEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/ListAppInstanceUserEndpoints)
