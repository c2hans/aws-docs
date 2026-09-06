---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_ListAppInstanceAdmins.html
---

# ListAppInstanceAdmins
<a name="API_ListAppInstanceAdmins"></a>

Returns a list of the administrators in the `AppInstance`.

## Request Syntax
<a name="API_ListAppInstanceAdmins_RequestSyntax"></a>

```
GET /app-instances/{{appInstanceArn}}/admins?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAppInstanceAdmins_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appInstanceArn](#API_ListAppInstanceAdmins_RequestSyntax) **   <a name="chimesdk-ListAppInstanceAdmins-request-uri-AppInstanceArn"></a>
The ARN of the `AppInstance`.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [MaxResults](#API_ListAppInstanceAdmins_RequestSyntax) **   <a name="chimesdk-ListAppInstanceAdmins-request-uri-MaxResults"></a>
The maximum number of administrators that you want to return.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListAppInstanceAdmins_RequestSyntax) **   <a name="chimesdk-ListAppInstanceAdmins-request-uri-NextToken"></a>
The token returned from previous API requests until the number of administrators is reached.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

## Request Body
<a name="API_ListAppInstanceAdmins_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAppInstanceAdmins_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AppInstanceAdmins": [
      {
         "Admin": {
            "Arn": "string",
            "Name": "string"
         }
      }
   ],
   "AppInstanceArn": "string",
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAppInstanceAdmins_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppInstanceAdmins](#API_ListAppInstanceAdmins_ResponseSyntax) **   <a name="chimesdk-ListAppInstanceAdmins-response-AppInstanceAdmins"></a>
The information for each administrator.
Type: Array of [AppInstanceAdminSummary](API_AppInstanceAdminSummary.md) objects

 ** [AppInstanceArn](#API_ListAppInstanceAdmins_ResponseSyntax) **   <a name="chimesdk-ListAppInstanceAdmins-response-AppInstanceArn"></a>
The ARN of the `AppInstance`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [NextToken](#API_ListAppInstanceAdmins_ResponseSyntax) **   <a name="chimesdk-ListAppInstanceAdmins-response-NextToken"></a>
The token returned from previous API requests until the number of administrators is reached.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

## Errors
<a name="API_ListAppInstanceAdmins_Errors"></a>

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
<a name="API_ListAppInstanceAdmins_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-identity-2021-04-20/ListAppInstanceAdmins)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-identity-2021-04-20/ListAppInstanceAdmins)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/ListAppInstanceAdmins)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-identity-2021-04-20/ListAppInstanceAdmins)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/ListAppInstanceAdmins)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-identity-2021-04-20/ListAppInstanceAdmins)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-identity-2021-04-20/ListAppInstanceAdmins)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-identity-2021-04-20/ListAppInstanceAdmins)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-identity-2021-04-20/ListAppInstanceAdmins)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/ListAppInstanceAdmins)
