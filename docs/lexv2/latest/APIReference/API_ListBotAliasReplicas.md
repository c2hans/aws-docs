---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotAliasReplicas.html
---

# ListBotAliasReplicas
<a name="API_ListBotAliasReplicas"></a>

The action to list the replicated bots created from the source bot alias.

## Request Syntax
<a name="API_ListBotAliasReplicas_RequestSyntax"></a>

```
POST /bots/{{botId}}/replicas/{{replicaRegion}}/botaliases/ HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListBotAliasReplicas_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_ListBotAliasReplicas_RequestSyntax) **   <a name="lexv2-ListBotAliasReplicas-request-uri-botId"></a>
The request for the unique bot ID of the replicated bot created from the source bot alias.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [replicaRegion](#API_ListBotAliasReplicas_RequestSyntax) **   <a name="lexv2-ListBotAliasReplicas-request-uri-replicaRegion"></a>
The request for the secondary region of the replicated bot created from the source bot alias.
Length Constraints: Minimum length of 2. Maximum length of 25.
Required: Yes

## Request Body
<a name="API_ListBotAliasReplicas_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListBotAliasReplicas_RequestSyntax) **   <a name="lexv2-ListBotAliasReplicas-request-maxResults"></a>
The request for maximum results to list the replicated bots created from the source bot alias.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListBotAliasReplicas_RequestSyntax) **   <a name="lexv2-ListBotAliasReplicas-request-nextToken"></a>
The request for the next token for the replicated bot created from the source bot alias.
Type: String
Required: No

## Response Syntax
<a name="API_ListBotAliasReplicas_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botAliasReplicaSummaries": [
      {
         "botAliasId": "string",
         "botAliasReplicationStatus": "string",
         "botVersion": "string",
         "creationDateTime": number,
         "failureReasons": [ "string" ],
         "lastUpdatedDateTime": number
      }
   ],
   "botId": "string",
   "nextToken": "string",
   "replicaRegion": "string",
   "sourceRegion": "string"
}
```

## Response Elements
<a name="API_ListBotAliasReplicas_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botAliasReplicaSummaries](#API_ListBotAliasReplicas_ResponseSyntax) **   <a name="lexv2-ListBotAliasReplicas-response-botAliasReplicaSummaries"></a>
The summary information of the replicated bot created from the source bot alias.
Type: Array of [BotAliasReplicaSummary](API_BotAliasReplicaSummary.md) objects

 ** [botId](#API_ListBotAliasReplicas_ResponseSyntax) **   <a name="lexv2-ListBotAliasReplicas-response-botId"></a>
The unique bot ID of the replicated bot created from the source bot alias.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [nextToken](#API_ListBotAliasReplicas_ResponseSyntax) **   <a name="lexv2-ListBotAliasReplicas-response-nextToken"></a>
The next token for the replicated bots created from the source bot alias.
Type: String

 ** [replicaRegion](#API_ListBotAliasReplicas_ResponseSyntax) **   <a name="lexv2-ListBotAliasReplicas-response-replicaRegion"></a>
The secondary region of the replicated bot created from the source bot alias.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.

 ** [sourceRegion](#API_ListBotAliasReplicas_ResponseSyntax) **   <a name="lexv2-ListBotAliasReplicas-response-sourceRegion"></a>
The source region of the replicated bot created from the source bot alias.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.

## Errors
<a name="API_ListBotAliasReplicas_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

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

## Examples
<a name="API_ListBotAliasReplicas_Examples"></a>

### This example illustrates one example input of ListBotAliasReplicas.
<a name="API_ListBotAliasReplicas_Example_1"></a>

This example illustrates one usage of ListBotAliasReplicas.

```
POST https://models-v2-lex.us-east-1.amazonaws.com/bots/BOT1234567/replicas/us-west-2/botaliases
{
    "replicaRegion": "us-west-2",
    "maxResults": 50
}
```

### This example illustrates one example response of ListBotAliasReplicas.
<a name="API_ListBotAliasReplicas_Example_2"></a>

This example illustrates one usage of ListBotAliasReplicas.

```
{
    "botAliasReplicaSummaries": [{
        "botAliasId": "ALIAS12345",
        "botAliasReplicationStatus": "Available",
        "botVersion": "0000000001",
        "creationDateTime": 1.706822183021E9,
        "failureReasons": [],
        "lastUpdatedDateTime": 1.706822187379E9
   }],
    "botId": "BOT1234567",
    "nextToken": null,
    "replicaRegion": "us-west-2",
    "sourceRegion": "us-east-1"
}
```

## See Also
<a name="API_ListBotAliasReplicas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/ListBotAliasReplicas)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/ListBotAliasReplicas)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ListBotAliasReplicas)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/ListBotAliasReplicas)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ListBotAliasReplicas)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/ListBotAliasReplicas)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/ListBotAliasReplicas)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/ListBotAliasReplicas)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/ListBotAliasReplicas)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ListBotAliasReplicas)
