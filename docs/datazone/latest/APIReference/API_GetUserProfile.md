---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetUserProfile.html
---

# GetUserProfile
<a name="API_GetUserProfile"></a>

Gets a user profile in Amazon DataZone.

## Request Syntax
<a name="API_GetUserProfile_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/user-profiles/{{userIdentifier}}?sessionName={{sessionName}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetUserProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetUserProfile_RequestSyntax) **   <a name="datazone-GetUserProfile-request-uri-domainIdentifier"></a>
the ID of the Amazon DataZone domain the data portal of which you want to get.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [sessionName](#API_GetUserProfile_RequestSyntax) **   <a name="datazone-GetUserProfile-request-uri-sessionName"></a>
The session name for IAM role sessions.
Length Constraints: Minimum length of 2. Maximum length of 64.

 ** [type](#API_GetUserProfile_RequestSyntax) **   <a name="datazone-GetUserProfile-request-uri-type"></a>
The type of the user profile.
Valid Values: `IAM | SSO`

 ** [userIdentifier](#API_GetUserProfile_RequestSyntax) **   <a name="datazone-GetUserProfile-request-uri-userIdentifier"></a>
The identifier of the user for which you want to get the user profile.
Pattern: `.*(^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$|^[a-zA-Z_0-9+=,.@-]+$|^arn:aws:iam::\d{12}:.+$).*`
Required: Yes

## Request Body
<a name="API_GetUserProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetUserProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "details": { ... },
   "domainId": "string",
   "id": "string",
   "status": "string",
   "type": "string"
}
```

## Response Elements
<a name="API_GetUserProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [details](#API_GetUserProfile_ResponseSyntax) **   <a name="datazone-GetUserProfile-response-details"></a>
The user profile details.
Type: [UserProfileDetails](API_UserProfileDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [domainId](#API_GetUserProfile_ResponseSyntax) **   <a name="datazone-GetUserProfile-response-domainId"></a>
the identifier of the Amazon DataZone domain of which you want to get the user profile.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetUserProfile_ResponseSyntax) **   <a name="datazone-GetUserProfile-response-id"></a>
The identifier of the user profile.
Type: String
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`

 ** [status](#API_GetUserProfile_ResponseSyntax) **   <a name="datazone-GetUserProfile-response-status"></a>
The status of the user profile.
Type: String
Valid Values: `ASSIGNED | NOT_ASSIGNED | ACTIVATED | DEACTIVATED`

 ** [type](#API_GetUserProfile_ResponseSyntax) **   <a name="datazone-GetUserProfile-response-type"></a>
The type of the user profile.
Type: String
Valid Values: `IAM | SSO`

## Errors
<a name="API_GetUserProfile_Errors"></a>

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
<a name="API_GetUserProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetUserProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetUserProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetUserProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetUserProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetUserProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetUserProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetUserProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetUserProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetUserProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetUserProfile)
