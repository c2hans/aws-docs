---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBotVersion.html
---

# CreateBotVersion
<a name="API_CreateBotVersion"></a>

Creates an immutable version of the bot. When you create the first version of a bot, Amazon Lex sets the version number to 1. Subsequent bot versions increase in an increment of 1. The version number will always represent the total number of versions created of the bot, not the current number of versions. If a bot version is deleted, that bot version number will not be reused.

## Request Syntax
<a name="API_CreateBotVersion_RequestSyntax"></a>

```
PUT /bots/{{botId}}/botversions/ HTTP/1.1
Content-type: application/json

{
   "botVersionLocaleSpecification": {
      "{{string}}" : {
         "sourceBotVersion": "{{string}}"
      }
   },
   "description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateBotVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_CreateBotVersion_RequestSyntax) **   <a name="lexv2-CreateBotVersion-request-uri-botId"></a>
The identifier of the bot to create the version for.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_CreateBotVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [botVersionLocaleSpecification](#API_CreateBotVersion_RequestSyntax) **   <a name="lexv2-CreateBotVersion-request-botVersionLocaleSpecification"></a>
Specifies the locales that Amazon Lex adds to this version. You can choose the `Draft` version or any other previously published version for each locale. When you specify a source version, the locale data is copied from the source version to the new version.
Type: String to [BotVersionLocaleDetails](API_BotVersionLocaleDetails.md) object map
Map Entries: Maximum number of items.
Required: Yes

 ** [description](#API_CreateBotVersion_RequestSyntax) **   <a name="lexv2-CreateBotVersion-request-description"></a>
A description of the version. Use the description to help identify the version in lists.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_CreateBotVersion_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "botId": "string",
   "botStatus": "string",
   "botVersion": "string",
   "botVersionLocaleSpecification": {
      "string" : {
         "sourceBotVersion": "string"
      }
   },
   "creationDateTime": number,
   "description": "string"
}
```

## Response Elements
<a name="API_CreateBotVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_CreateBotVersion_ResponseSyntax) **   <a name="lexv2-CreateBotVersion-response-botId"></a>
The bot identifier specified in the request.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botStatus](#API_CreateBotVersion_ResponseSyntax) **   <a name="lexv2-CreateBotVersion-response-botStatus"></a>
When you send a request to create or update a bot, Amazon Lex sets the status response element to `Creating`. After Amazon Lex builds the bot, it sets status to `Available`. If Amazon Lex can't build the bot, it sets status to `Failed`.
Type: String
Valid Values: `Creating | Available | Inactive | Deleting | Failed | Versioning | Importing | Updating`

 ** [botVersion](#API_CreateBotVersion_ResponseSyntax) **   <a name="lexv2-CreateBotVersion-response-botVersion"></a>
The version number assigned to the version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^[0-9]+$`

 ** [botVersionLocaleSpecification](#API_CreateBotVersion_ResponseSyntax) **   <a name="lexv2-CreateBotVersion-response-botVersionLocaleSpecification"></a>
The source versions used for each locale in the new version.
Type: String to [BotVersionLocaleDetails](API_BotVersionLocaleDetails.md) object map
Map Entries: Maximum number of items.

 ** [creationDateTime](#API_CreateBotVersion_ResponseSyntax) **   <a name="lexv2-CreateBotVersion-response-creationDateTime"></a>
A timestamp of the date and time that the version was created.
Type: Timestamp

 ** [description](#API_CreateBotVersion_ResponseSyntax) **   <a name="lexv2-CreateBotVersion-response-description"></a>
The description of the version specified in the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

## Errors
<a name="API_CreateBotVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** PreconditionFailedException **
Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.
HTTP Status Code: 412

 ** ServiceQuotaExceededException **
You have reached a quota for your bot.
HTTP Status Code: 402

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_CreateBotVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/CreateBotVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/CreateBotVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/CreateBotVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/CreateBotVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/CreateBotVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/CreateBotVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/CreateBotVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/CreateBotVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/CreateBotVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/CreateBotVersion)
