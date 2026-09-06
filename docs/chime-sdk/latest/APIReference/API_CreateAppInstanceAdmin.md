---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstanceAdmin.html
---

# CreateAppInstanceAdmin
<a name="API_CreateAppInstanceAdmin"></a>

Promotes an `AppInstanceUser` or `AppInstanceBot` to an `AppInstanceAdmin`. The promoted entity can perform the following actions.
+  `ChannelModerator` actions across all channels in the `AppInstance`.
+  `DeleteChannelMessage` actions.

Only an `AppInstanceUser` and `AppInstanceBot` can be promoted to an `AppInstanceAdmin` role.

## Request Syntax
<a name="API_CreateAppInstanceAdmin_RequestSyntax"></a>

```
POST /app-instances/{{appInstanceArn}}/admins HTTP/1.1
Content-type: application/json

{
   "AppInstanceAdminArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAppInstanceAdmin_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appInstanceArn](#API_CreateAppInstanceAdmin_RequestSyntax) **   <a name="chimesdk-CreateAppInstanceAdmin-request-uri-AppInstanceArn"></a>
The ARN of the `AppInstance`.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_CreateAppInstanceAdmin_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AppInstanceAdminArn](#API_CreateAppInstanceAdmin_RequestSyntax) **   <a name="chimesdk-CreateAppInstanceAdmin-request-AppInstanceAdminArn"></a>
The ARN of an existing instance user or bot, to be promoted to the administrator of the current AppInstance.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Response Syntax
<a name="API_CreateAppInstanceAdmin_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "AppInstanceAdmin": {
      "Arn": "string",
      "Name": "string"
   },
   "AppInstanceArn": "string"
}
```

## Response Elements
<a name="API_CreateAppInstanceAdmin_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [AppInstanceAdmin](#API_CreateAppInstanceAdmin_ResponseSyntax) **   <a name="chimesdk-CreateAppInstanceAdmin-response-AppInstanceAdmin"></a>
The ARN and name of the administrator, the ARN of the `AppInstance`, and the created and last-updated timestamps. All timestamps use epoch milliseconds.
Type: [Identity](API_Identity.md) object

 ** [AppInstanceArn](#API_CreateAppInstanceAdmin_ResponseSyntax) **   <a name="chimesdk-CreateAppInstanceAdmin-response-AppInstanceArn"></a>
The ARN of the of the admin for the `AppInstance`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

## Errors
<a name="API_CreateAppInstanceAdmin_Errors"></a>

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
<a name="API_CreateAppInstanceAdmin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-identity-2021-04-20/CreateAppInstanceAdmin)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-identity-2021-04-20/CreateAppInstanceAdmin)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/CreateAppInstanceAdmin)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-identity-2021-04-20/CreateAppInstanceAdmin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/CreateAppInstanceAdmin)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-identity-2021-04-20/CreateAppInstanceAdmin)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-identity-2021-04-20/CreateAppInstanceAdmin)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-identity-2021-04-20/CreateAppInstanceAdmin)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-identity-2021-04-20/CreateAppInstanceAdmin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/CreateAppInstanceAdmin)
