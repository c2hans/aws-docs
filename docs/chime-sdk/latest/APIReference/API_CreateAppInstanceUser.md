---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstanceUser.html
---

# CreateAppInstanceUser
<a name="API_CreateAppInstanceUser"></a>

Creates a user under an Amazon Chime `AppInstance`. The request consists of a unique `appInstanceUserId` and `Name` for that user.

## Request Syntax
<a name="API_CreateAppInstanceUser_RequestSyntax"></a>

```
POST /app-instance-users HTTP/1.1
Content-type: application/json

{
   "AppInstanceArn": "{{string}}",
   "AppInstanceUserId": "{{string}}",
   "ClientRequestToken": "{{string}}",
   "ExpirationSettings": {
      "ExpirationCriterion": "{{string}}",
      "ExpirationDays": {{number}}
   },
   "Metadata": "{{string}}",
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateAppInstanceUser_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAppInstanceUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AppInstanceArn](#API_CreateAppInstanceUser_RequestSyntax) **   <a name="chimesdk-CreateAppInstanceUser-request-AppInstanceArn"></a>
The ARN of the `AppInstance` request.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [AppInstanceUserId](#API_CreateAppInstanceUser_RequestSyntax) **   <a name="chimesdk-CreateAppInstanceUser-request-AppInstanceUserId"></a>
The user ID of the `AppInstance`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9]([A-Za-z0-9\:\-\_\.\@]{0,62}[A-Za-z0-9])?`
Required: Yes

 ** [ClientRequestToken](#API_CreateAppInstanceUser_RequestSyntax) **   <a name="chimesdk-CreateAppInstanceUser-request-ClientRequestToken"></a>
The unique ID of the request. Use different tokens to request additional `AppInstances`.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[-_a-zA-Z0-9]*`
Required: Yes

 ** [ExpirationSettings](#API_CreateAppInstanceUser_RequestSyntax) **   <a name="chimesdk-CreateAppInstanceUser-request-ExpirationSettings"></a>
Settings that control the interval after which the `AppInstanceUser` is automatically deleted.
Type: [ExpirationSettings](API_ExpirationSettings.md) object
Required: No

 ** [Metadata](#API_CreateAppInstanceUser_RequestSyntax) **   <a name="chimesdk-CreateAppInstanceUser-request-Metadata"></a>
The request's metadata. Limited to a 1KB string in UTF-8.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** [Name](#API_CreateAppInstanceUser_RequestSyntax) **   <a name="chimesdk-CreateAppInstanceUser-request-Name"></a>
The user's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*\S.*`
Required: Yes

 ** [Tags](#API_CreateAppInstanceUser_RequestSyntax) **   <a name="chimesdk-CreateAppInstanceUser-request-Tags"></a>
Tags assigned to the `AppInstanceUser`.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateAppInstanceUser_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "AppInstanceUserArn": "string"
}
```

## Response Elements
<a name="API_CreateAppInstanceUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [AppInstanceUserArn](#API_CreateAppInstanceUser_ResponseSyntax) **   <a name="chimesdk-CreateAppInstanceUser-response-AppInstanceUserArn"></a>
The user's ARN.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

## Errors
<a name="API_CreateAppInstanceUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

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
<a name="API_CreateAppInstanceUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-identity-2021-04-20/CreateAppInstanceUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-identity-2021-04-20/CreateAppInstanceUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/CreateAppInstanceUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-identity-2021-04-20/CreateAppInstanceUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/CreateAppInstanceUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-identity-2021-04-20/CreateAppInstanceUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-identity-2021-04-20/CreateAppInstanceUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-identity-2021-04-20/CreateAppInstanceUser)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-identity-2021-04-20/CreateAppInstanceUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/CreateAppInstanceUser)
