---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetIamPortalLoginUrl.html
---

# GetIamPortalLoginUrl
<a name="API_GetIamPortalLoginUrl"></a>

Gets the data portal URL for the specified Amazon DataZone domain.

## Request Syntax
<a name="API_GetIamPortalLoginUrl_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/get-portal-login-url HTTP/1.1
```

## URI Request Parameters
<a name="API_GetIamPortalLoginUrl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetIamPortalLoginUrl_RequestSyntax) **   <a name="datazone-GetIamPortalLoginUrl-request-uri-domainIdentifier"></a>
the ID of the Amazon DataZone domain the data portal of which you want to get.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetIamPortalLoginUrl_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetIamPortalLoginUrl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "authCodeUrl": "string",
   "userProfileId": "string"
}
```

## Response Elements
<a name="API_GetIamPortalLoginUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [authCodeUrl](#API_GetIamPortalLoginUrl_ResponseSyntax) **   <a name="datazone-GetIamPortalLoginUrl-response-authCodeUrl"></a>
The data portal URL of the specified Amazon DataZone domain.
Type: String

 ** [userProfileId](#API_GetIamPortalLoginUrl_ResponseSyntax) **   <a name="datazone-GetIamPortalLoginUrl-response-userProfileId"></a>
The ID of the user profile.
Type: String

## Errors
<a name="API_GetIamPortalLoginUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

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
<a name="API_GetIamPortalLoginUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetIamPortalLoginUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetIamPortalLoginUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetIamPortalLoginUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetIamPortalLoginUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetIamPortalLoginUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetIamPortalLoginUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetIamPortalLoginUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetIamPortalLoginUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetIamPortalLoginUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetIamPortalLoginUrl)
