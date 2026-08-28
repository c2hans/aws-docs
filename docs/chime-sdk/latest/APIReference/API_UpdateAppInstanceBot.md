---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UpdateAppInstanceBot.html
---

# UpdateAppInstanceBot
<a name="API_UpdateAppInstanceBot"></a>

Updates the name and metadata of an `AppInstanceBot`.

## Request Syntax
<a name="API_UpdateAppInstanceBot_RequestSyntax"></a>

```
PUT /app-instance-bots/{{appInstanceBotArn}} HTTP/1.1
Content-type: application/json

{
   "Configuration": {
      "Lex": {
         "InvokedBy": {
            "StandardMessages": "{{string}}",
            "TargetedMessages": "{{string}}"
         },
         "LexBotAliasArn": "{{string}}",
         "LocaleId": "{{string}}",
         "RespondsTo": "{{string}}",
         "WelcomeIntent": "{{string}}"
      }
   },
   "Metadata": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAppInstanceBot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appInstanceBotArn](#API_UpdateAppInstanceBot_RequestSyntax) **   <a name="chimesdk-UpdateAppInstanceBot-request-uri-AppInstanceBotArn"></a>
The ARN of the `AppInstanceBot`.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_UpdateAppInstanceBot_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Configuration](#API_UpdateAppInstanceBot_RequestSyntax) **   <a name="chimesdk-UpdateAppInstanceBot-request-Configuration"></a>
The configuration for the bot update.
Type: [Configuration](API_Configuration.md) object
Required: No

 ** [Metadata](#API_UpdateAppInstanceBot_RequestSyntax) **   <a name="chimesdk-UpdateAppInstanceBot-request-Metadata"></a>
The metadata of the `AppInstanceBot`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: Yes

 ** [Name](#API_UpdateAppInstanceBot_RequestSyntax) **   <a name="chimesdk-UpdateAppInstanceBot-request-Name"></a>
The name of the `AppInstanceBot`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
Required: Yes

## Response Syntax
<a name="API_UpdateAppInstanceBot_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AppInstanceBotArn": "string"
}
```

## Response Elements
<a name="API_UpdateAppInstanceBot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppInstanceBotArn](#API_UpdateAppInstanceBot_ResponseSyntax) **   <a name="chimesdk-UpdateAppInstanceBot-response-AppInstanceBotArn"></a>
The ARN of the `AppInstanceBot`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

## Errors
<a name="API_UpdateAppInstanceBot_Errors"></a>

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
<a name="API_UpdateAppInstanceBot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-identity-2021-04-20/UpdateAppInstanceBot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-identity-2021-04-20/UpdateAppInstanceBot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/UpdateAppInstanceBot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-identity-2021-04-20/UpdateAppInstanceBot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/UpdateAppInstanceBot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-identity-2021-04-20/UpdateAppInstanceBot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-identity-2021-04-20/UpdateAppInstanceBot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-identity-2021-04-20/UpdateAppInstanceBot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-identity-2021-04-20/UpdateAppInstanceBot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/UpdateAppInstanceBot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
