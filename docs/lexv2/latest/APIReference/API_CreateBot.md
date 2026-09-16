---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html
---

# CreateBot
<a name="API_CreateBot"></a>

Creates an Amazon Lex conversational bot.

## Request Syntax
<a name="API_CreateBot_RequestSyntax"></a>

```
PUT /bots/ HTTP/1.1
Content-type: application/json

{
   "botMembers": [
      {
         "botMemberAliasId": "{{string}}",
         "botMemberAliasName": "{{string}}",
         "botMemberId": "{{string}}",
         "botMemberName": "{{string}}",
         "botMemberVersion": "{{string}}"
      }
   ],
   "botName": "{{string}}",
   "botTags": {
      "{{string}}" : "{{string}}"
   },
   "botType": "{{string}}",
   "dataPrivacy": {
      "childDirected": {{boolean}}
   },
   "description": "{{string}}",
   "errorLogSettings": {
      "enabled": {{boolean}}
   },
   "idleSessionTTLInSeconds": {{number}},
   "roleArn": "{{string}}",
   "testBotAliasTags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateBot_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateBot_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [botMembers](#API_CreateBot_RequestSyntax) **   <a name="lexv2-CreateBot-request-botMembers"></a>
The list of bot members in a network to be created.
Type: Array of [BotMember](API_BotMember.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [botName](#API_CreateBot_RequestSyntax) **   <a name="lexv2-CreateBot-request-botName"></a>
The name of the bot. The bot name must be unique in the account that creates the bot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** [botTags](#API_CreateBot_RequestSyntax) **   <a name="lexv2-CreateBot-request-botTags"></a>
A list of tags to add to the bot. You can only add tags when you create a bot. You can't use the `UpdateBot` operation to update tags. To update tags, use the `TagResource` operation.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [botType](#API_CreateBot_RequestSyntax) **   <a name="lexv2-CreateBot-request-botType"></a>
The type of a bot to create.
Type: String
Valid Values: `Bot | BotNetwork`
Required: No

 ** [dataPrivacy](#API_CreateBot_RequestSyntax) **   <a name="lexv2-CreateBot-request-dataPrivacy"></a>
Provides information on additional privacy protections Amazon Lex should use with the bot's data.
Type: [DataPrivacy](API_DataPrivacy.md) object
Required: Yes

 ** [description](#API_CreateBot_RequestSyntax) **   <a name="lexv2-CreateBot-request-description"></a>
A description of the bot. It appears in lists to help you identify a particular bot.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** [errorLogSettings](#API_CreateBot_RequestSyntax) **   <a name="lexv2-CreateBot-request-errorLogSettings"></a>
Specifies the configuration for error logging during bot creation.
Type: [ErrorLogSettings](API_ErrorLogSettings.md) object
Required: No

 ** [idleSessionTTLInSeconds](#API_CreateBot_RequestSyntax) **   <a name="lexv2-CreateBot-request-idleSessionTTLInSeconds"></a>
The time, in seconds, that Amazon Lex should keep information about a user's conversation with the bot.
A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.
You can specify between 60 (1 minute) and 86,400 (24 hours) seconds.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 86400.
Required: Yes

 ** [roleArn](#API_CreateBot_RequestSyntax) **   <a name="lexv2-CreateBot-request-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that has permission to access the bot.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.*$`
Required: Yes

 ** [testBotAliasTags](#API_CreateBot_RequestSyntax) **   <a name="lexv2-CreateBot-request-testBotAliasTags"></a>
A list of tags to add to the test alias for a bot. You can only add tags when you create a bot. You can't use the `UpdateAlias` operation to update tags. To update tags on the test alias, use the `TagResource` operation.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateBot_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "botId": "string",
   "botMembers": [
      {
         "botMemberAliasId": "string",
         "botMemberAliasName": "string",
         "botMemberId": "string",
         "botMemberName": "string",
         "botMemberVersion": "string"
      }
   ],
   "botName": "string",
   "botStatus": "string",
   "botTags": {
      "string" : "string"
   },
   "botType": "string",
   "creationDateTime": number,
   "dataPrivacy": {
      "childDirected": boolean
   },
   "description": "string",
   "errorLogSettings": {
      "enabled": boolean
   },
   "idleSessionTTLInSeconds": number,
   "roleArn": "string",
   "testBotAliasTags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateBot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_CreateBot_ResponseSyntax) **   <a name="lexv2-CreateBot-response-botId"></a>
A unique identifier for a particular bot. You use this to identify the bot when you call other Amazon Lex API operations.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botMembers](#API_CreateBot_ResponseSyntax) **   <a name="lexv2-CreateBot-response-botMembers"></a>
The list of bots in a network that was created.
Type: Array of [BotMember](API_BotMember.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [botName](#API_CreateBot_ResponseSyntax) **   <a name="lexv2-CreateBot-response-botName"></a>
The name specified for the bot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

 ** [botStatus](#API_CreateBot_ResponseSyntax) **   <a name="lexv2-CreateBot-response-botStatus"></a>
Shows the current status of the bot. The bot is first in the `Creating` status. Once the bot is read for use, it changes to the `Available` status. After the bot is created, you can use the `DRAFT` version of the bot.
Type: String
Valid Values: `Creating | Available | Inactive | Deleting | Failed | Versioning | Importing | Updating`

 ** [botTags](#API_CreateBot_ResponseSyntax) **   <a name="lexv2-CreateBot-response-botTags"></a>
A list of tags associated with the bot.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [botType](#API_CreateBot_ResponseSyntax) **   <a name="lexv2-CreateBot-response-botType"></a>
The type of a bot that was created.
Type: String
Valid Values: `Bot | BotNetwork`

 ** [creationDateTime](#API_CreateBot_ResponseSyntax) **   <a name="lexv2-CreateBot-response-creationDateTime"></a>
A timestamp indicating the date and time that the bot was created.
Type: Timestamp

 ** [dataPrivacy](#API_CreateBot_ResponseSyntax) **   <a name="lexv2-CreateBot-response-dataPrivacy"></a>
The data privacy settings specified for the bot.
Type: [DataPrivacy](API_DataPrivacy.md) object

 ** [description](#API_CreateBot_ResponseSyntax) **   <a name="lexv2-CreateBot-response-description"></a>
The description specified for the bot.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [errorLogSettings](#API_CreateBot_ResponseSyntax) **   <a name="lexv2-CreateBot-response-errorLogSettings"></a>
Specifies configuration settings for delivering error logs to Cloudwatch Logs in an Amazon Lex bot response.
Type: [ErrorLogSettings](API_ErrorLogSettings.md) object

 ** [idleSessionTTLInSeconds](#API_CreateBot_ResponseSyntax) **   <a name="lexv2-CreateBot-response-idleSessionTTLInSeconds"></a>
The session idle time specified for the bot.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 86400.

 ** [roleArn](#API_CreateBot_ResponseSyntax) **   <a name="lexv2-CreateBot-response-roleArn"></a>
The IAM role specified for the bot.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.*$`

 ** [testBotAliasTags](#API_CreateBot_ResponseSyntax) **   <a name="lexv2-CreateBot-response-testBotAliasTags"></a>
A list of tags associated with the test alias for the bot.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateBot_Errors"></a>

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
<a name="API_CreateBot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/CreateBot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/CreateBot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/CreateBot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/CreateBot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/CreateBot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/CreateBot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/CreateBot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/CreateBot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/CreateBot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/CreateBot)
