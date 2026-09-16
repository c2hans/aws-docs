---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBotAlias.html
---

# DescribeBotAlias
<a name="API_DescribeBotAlias"></a>

Get information about a specific bot alias.

## Request Syntax
<a name="API_DescribeBotAlias_RequestSyntax"></a>

```
GET /bots/{{botId}}/botaliases/{{botAliasId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeBotAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botAliasId](#API_DescribeBotAlias_RequestSyntax) **   <a name="lexv2-DescribeBotAlias-request-uri-botAliasId"></a>
The identifier of the bot alias to describe.
Length Constraints: Fixed length of 10.
Pattern: `^(\bTSTALIASID\b|[0-9a-zA-Z]+)$`
Required: Yes

 ** [botId](#API_DescribeBotAlias_RequestSyntax) **   <a name="lexv2-DescribeBotAlias-request-uri-botId"></a>
The identifier of the bot associated with the bot alias to describe.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_DescribeBotAlias_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeBotAlias_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botAliasHistoryEvents": [
      {
         "botVersion": "string",
         "endDate": number,
         "startDate": number
      }
   ],
   "botAliasId": "string",
   "botAliasLocaleSettings": {
      "string" : {
         "codeHookSpecification": {
            "lambdaCodeHook": {
               "codeHookInterfaceVersion": "string",
               "lambdaARN": "string"
            }
         },
         "enabled": boolean
      }
   },
   "botAliasName": "string",
   "botAliasStatus": "string",
   "botId": "string",
   "botVersion": "string",
   "conversationLogSettings": {
      "audioLogSettings": [
         {
            "destination": {
               "s3Bucket": {
                  "kmsKeyArn": "string",
                  "logPrefix": "string",
                  "s3BucketArn": "string"
               }
            },
            "enabled": boolean,
            "selectiveLoggingEnabled": boolean
         }
      ],
      "textLogSettings": [
         {
            "destination": {
               "cloudWatch": {
                  "cloudWatchLogGroupArn": "string",
                  "logPrefix": "string"
               }
            },
            "enabled": boolean,
            "selectiveLoggingEnabled": boolean
         }
      ]
   },
   "creationDateTime": number,
   "description": "string",
   "lastUpdatedDateTime": number,
   "parentBotNetworks": [
      {
         "botId": "string",
         "botVersion": "string"
      }
   ],
   "sentimentAnalysisSettings": {
      "detectSentiment": boolean
   }
}
```

## Response Elements
<a name="API_DescribeBotAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botAliasHistoryEvents](#API_DescribeBotAlias_ResponseSyntax) **   <a name="lexv2-DescribeBotAlias-response-botAliasHistoryEvents"></a>
A list of events that affect a bot alias. For example, an event is recorded when the version that the alias points to changes.
Type: Array of [BotAliasHistoryEvent](API_BotAliasHistoryEvent.md) objects

 ** [botAliasId](#API_DescribeBotAlias_ResponseSyntax) **   <a name="lexv2-DescribeBotAlias-response-botAliasId"></a>
The identifier of the bot alias.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^(\bTSTALIASID\b|[0-9a-zA-Z]+)$`

 ** [botAliasLocaleSettings](#API_DescribeBotAlias_ResponseSyntax) **   <a name="lexv2-DescribeBotAlias-response-botAliasLocaleSettings"></a>
The locale settings that are unique to the alias.
Type: String to [BotAliasLocaleSettings](API_BotAliasLocaleSettings.md) object map
Map Entries: Maximum number of items.

 ** [botAliasName](#API_DescribeBotAlias_ResponseSyntax) **   <a name="lexv2-DescribeBotAlias-response-botAliasName"></a>
The name of the bot alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

 ** [botAliasStatus](#API_DescribeBotAlias_ResponseSyntax) **   <a name="lexv2-DescribeBotAlias-response-botAliasStatus"></a>
The current status of the alias. When the alias is `Available`, the alias is ready for use with your bot.
Type: String
Valid Values: `Creating | Available | Deleting | Failed`

 ** [botId](#API_DescribeBotAlias_ResponseSyntax) **   <a name="lexv2-DescribeBotAlias-response-botId"></a>
The identifier of the bot associated with the bot alias.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_DescribeBotAlias_ResponseSyntax) **   <a name="lexv2-DescribeBotAlias-response-botVersion"></a>
The version of the bot associated with the bot alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`

 ** [conversationLogSettings](#API_DescribeBotAlias_ResponseSyntax) **   <a name="lexv2-DescribeBotAlias-response-conversationLogSettings"></a>
Specifics of how Amazon Lex logs text and audio conversations with the bot associated with the alias.
Type: [ConversationLogSettings](API_ConversationLogSettings.md) object

 ** [creationDateTime](#API_DescribeBotAlias_ResponseSyntax) **   <a name="lexv2-DescribeBotAlias-response-creationDateTime"></a>
A timestamp of the date and time that the alias was created.
Type: Timestamp

 ** [description](#API_DescribeBotAlias_ResponseSyntax) **   <a name="lexv2-DescribeBotAlias-response-description"></a>
The description of the bot alias.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [lastUpdatedDateTime](#API_DescribeBotAlias_ResponseSyntax) **   <a name="lexv2-DescribeBotAlias-response-lastUpdatedDateTime"></a>
A timestamp of the date and time that the alias was last updated.
Type: Timestamp

 ** [parentBotNetworks](#API_DescribeBotAlias_ResponseSyntax) **   <a name="lexv2-DescribeBotAlias-response-parentBotNetworks"></a>
A list of the networks to which the bot alias you described belongs.
Type: Array of [ParentBotNetwork](API_ParentBotNetwork.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.

 ** [sentimentAnalysisSettings](#API_DescribeBotAlias_ResponseSyntax) **   <a name="lexv2-DescribeBotAlias-response-sentimentAnalysisSettings"></a>
Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.
Type: [SentimentAnalysisSettings](API_SentimentAnalysisSettings.md) object

## Errors
<a name="API_DescribeBotAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

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
<a name="API_DescribeBotAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DescribeBotAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DescribeBotAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescribeBotAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DescribeBotAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescribeBotAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DescribeBotAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DescribeBotAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DescribeBotAlias)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DescribeBotAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescribeBotAlias)
