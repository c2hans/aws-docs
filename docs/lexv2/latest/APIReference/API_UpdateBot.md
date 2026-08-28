---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateBot.html
---

# UpdateBot
<a name="API_UpdateBot"></a>

Updates the configuration of an existing bot.

## Request Syntax
<a name="API_UpdateBot_RequestSyntax"></a>

```
PUT /bots/{{botId}}/ HTTP/1.1
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
   "botType": "{{string}}",
   "dataPrivacy": {
      "childDirected": {{boolean}}
   },
   "description": "{{string}}",
   "errorLogSettings": {
      "enabled": {{boolean}}
   },
   "idleSessionTTLInSeconds": {{number}},
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateBot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_UpdateBot_RequestSyntax) **   <a name="lexv2-UpdateBot-request-uri-botId"></a>
The unique identifier of the bot to update. This identifier is returned by the [CreateBot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html) operation.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_UpdateBot_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [botMembers](#API_UpdateBot_RequestSyntax) **   <a name="lexv2-UpdateBot-request-botMembers"></a>
The list of bot members in the network associated with the update action.
Type: Array of [BotMember](API_BotMember.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [botName](#API_UpdateBot_RequestSyntax) **   <a name="lexv2-UpdateBot-request-botName"></a>
The new name of the bot. The name must be unique in the account that creates the bot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** [botType](#API_UpdateBot_RequestSyntax) **   <a name="lexv2-UpdateBot-request-botType"></a>
The type of the bot to be updated.
Type: String
Valid Values: `Bot | BotNetwork`
Required: No

 ** [dataPrivacy](#API_UpdateBot_RequestSyntax) **   <a name="lexv2-UpdateBot-request-dataPrivacy"></a>
Provides information on additional privacy protections Amazon Lex should use with the bot's data.
Type: [DataPrivacy](API_DataPrivacy.md) object
Required: Yes

 ** [description](#API_UpdateBot_RequestSyntax) **   <a name="lexv2-UpdateBot-request-description"></a>
A description of the bot.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** [errorLogSettings](#API_UpdateBot_RequestSyntax) **   <a name="lexv2-UpdateBot-request-errorLogSettings"></a>
Allows you to modify how Amazon Lex logs errors during bot interactions, including destinations for error logs and the types of errors to be captured.
Type: [ErrorLogSettings](API_ErrorLogSettings.md) object
Required: No

 ** [idleSessionTTLInSeconds](#API_UpdateBot_RequestSyntax) **   <a name="lexv2-UpdateBot-request-idleSessionTTLInSeconds"></a>
The time, in seconds, that Amazon Lex should keep information about a user's conversation with the bot.
A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.
You can specify between 60 (1 minute) and 86,400 (24 hours) seconds.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 86400.
Required: Yes

 ** [roleArn](#API_UpdateBot_RequestSyntax) **   <a name="lexv2-UpdateBot-request-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that has permissions to access the bot.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.*$`
Required: Yes

## Response Syntax
<a name="API_UpdateBot_ResponseSyntax"></a>

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
   "lastUpdatedDateTime": number,
   "roleArn": "string"
}
```

## Response Elements
<a name="API_UpdateBot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_UpdateBot_ResponseSyntax) **   <a name="lexv2-UpdateBot-response-botId"></a>
The unique identifier of the bot that was updated.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botMembers](#API_UpdateBot_ResponseSyntax) **   <a name="lexv2-UpdateBot-response-botMembers"></a>
The list of bot members in the network that was updated.
Type: Array of [BotMember](API_BotMember.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [botName](#API_UpdateBot_ResponseSyntax) **   <a name="lexv2-UpdateBot-response-botName"></a>
The name of the bot after the update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

 ** [botStatus](#API_UpdateBot_ResponseSyntax) **   <a name="lexv2-UpdateBot-response-botStatus"></a>
Shows the current status of the bot. The bot is first in the `Creating` status. Once the bot is read for use, it changes to the `Available` status. After the bot is created, you can use the `DRAFT` version of the bot.
Type: String
Valid Values: `Creating | Available | Inactive | Deleting | Failed | Versioning | Importing | Updating`

 ** [botType](#API_UpdateBot_ResponseSyntax) **   <a name="lexv2-UpdateBot-response-botType"></a>
The type of the bot that was updated.
Type: String
Valid Values: `Bot | BotNetwork`

 ** [creationDateTime](#API_UpdateBot_ResponseSyntax) **   <a name="lexv2-UpdateBot-response-creationDateTime"></a>
A timestamp of the date and time that the bot was created.
Type: Timestamp

 ** [dataPrivacy](#API_UpdateBot_ResponseSyntax) **   <a name="lexv2-UpdateBot-response-dataPrivacy"></a>
The data privacy settings for the bot after the update.
Type: [DataPrivacy](API_DataPrivacy.md) object

 ** [description](#API_UpdateBot_ResponseSyntax) **   <a name="lexv2-UpdateBot-response-description"></a>
The description of the bot after the update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [errorLogSettings](#API_UpdateBot_ResponseSyntax) **   <a name="lexv2-UpdateBot-response-errorLogSettings"></a>
Settings for managing error logs within the response of an update bot operation.
Type: [ErrorLogSettings](API_ErrorLogSettings.md) object

 ** [idleSessionTTLInSeconds](#API_UpdateBot_ResponseSyntax) **   <a name="lexv2-UpdateBot-response-idleSessionTTLInSeconds"></a>
The session timeout, in seconds, for the bot after the update.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 86400.

 ** [lastUpdatedDateTime](#API_UpdateBot_ResponseSyntax) **   <a name="lexv2-UpdateBot-response-lastUpdatedDateTime"></a>
A timestamp of the date and time that the bot was last updated.
Type: Timestamp

 ** [roleArn](#API_UpdateBot_ResponseSyntax) **   <a name="lexv2-UpdateBot-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used by the bot after the update.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.*$`

## Errors
<a name="API_UpdateBot_Errors"></a>

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
<a name="API_UpdateBot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/UpdateBot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/UpdateBot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UpdateBot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/UpdateBot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UpdateBot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/UpdateBot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/UpdateBot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/UpdateBot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/UpdateBot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UpdateBot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
