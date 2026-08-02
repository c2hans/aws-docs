---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotVersionReplicas.html
---

# ListBotVersionReplicas
<a name="API_ListBotVersionReplicas"></a>

Contains information about all the versions replication statuses applicable for Global Resiliency.

## Request Syntax
<a name="API_ListBotVersionReplicas_RequestSyntax"></a>

```
POST /bots/{{botId}}/replicas/{{replicaRegion}}/botversions/ HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sortBy": {
      "attribute": "{{string}}",
      "order": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListBotVersionReplicas_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_ListBotVersionReplicas_RequestSyntax) **   <a name="lexv2-ListBotVersionReplicas-request-uri-botId"></a>
The request for the unique ID in the list of replicated bots.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [replicaRegion](#API_ListBotVersionReplicas_RequestSyntax) **   <a name="lexv2-ListBotVersionReplicas-request-uri-replicaRegion"></a>
The request for the region used in the list of replicated bots.
Length Constraints: Minimum length of 2. Maximum length of 25.
Required: Yes

## Request Body
<a name="API_ListBotVersionReplicas_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListBotVersionReplicas_RequestSyntax) **   <a name="lexv2-ListBotVersionReplicas-request-maxResults"></a>
The maximum results given in the list of replicated bots.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListBotVersionReplicas_RequestSyntax) **   <a name="lexv2-ListBotVersionReplicas-request-nextToken"></a>
The next token given in the list of replicated bots.
Type: String
Required: No

 ** [sortBy](#API_ListBotVersionReplicas_RequestSyntax) **   <a name="lexv2-ListBotVersionReplicas-request-sortBy"></a>
The requested sort category for the list of replicated bots.
Type: [BotVersionReplicaSortBy](API_BotVersionReplicaSortBy.md) object
Required: No

## Response Syntax
<a name="API_ListBotVersionReplicas_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "botVersionReplicaSummaries": [
      {
         "botVersion": "string",
         "botVersionReplicationStatus": "string",
         "creationDateTime": number,
         "failureReasons": [ "string" ]
      }
   ],
   "nextToken": "string",
   "replicaRegion": "string",
   "sourceRegion": "string"
}
```

## Response Elements
<a name="API_ListBotVersionReplicas_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_ListBotVersionReplicas_ResponseSyntax) **   <a name="lexv2-ListBotVersionReplicas-response-botId"></a>
The unique ID of the bots in the list of replicated bots.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersionReplicaSummaries](#API_ListBotVersionReplicas_ResponseSyntax) **   <a name="lexv2-ListBotVersionReplicas-response-botVersionReplicaSummaries"></a>
The information summary used for the replicated bots in the list of replicated bots.
Type: Array of [BotVersionReplicaSummary](API_BotVersionReplicaSummary.md) objects

 ** [nextToken](#API_ListBotVersionReplicas_ResponseSyntax) **   <a name="lexv2-ListBotVersionReplicas-response-nextToken"></a>
The next token used for the replicated bots in the list of replicated bots.
Type: String

 ** [replicaRegion](#API_ListBotVersionReplicas_ResponseSyntax) **   <a name="lexv2-ListBotVersionReplicas-response-replicaRegion"></a>
The region used for the replicated bots in the list of replicated bots.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.

 ** [sourceRegion](#API_ListBotVersionReplicas_ResponseSyntax) **   <a name="lexv2-ListBotVersionReplicas-response-sourceRegion"></a>
The source region used for the bots in the list of replicated bots.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.

## Errors
<a name="API_ListBotVersionReplicas_Errors"></a>

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
<a name="API_ListBotVersionReplicas_Examples"></a>

### This example illustrates one example input of ListBotVersionReplicas.
<a name="API_ListBotVersionReplicas_Example_1"></a>

This example illustrates one usage of ListBotVersionReplicas.

```
POST https://models-v2-lex.us-east-1.amazonaws.com/bots/BOT1234567/replicas/us-west-2/botversions
{
    "replicaRegion": "us-west-2",
    "maxResults": 50,
    "sortBy": {
        "attribute" : "BotVersion",
        "order" : "Ascending"
    }
}
```

### This example illustrates one example response of ListBotVersionReplicas.
<a name="API_ListBotVersionReplicas_Example_2"></a>

This example illustrates one usage of ListBotVersionReplicas.

```
{
    "botId": "BOT1234567",
    "botVersionReplicaSummaries": [{
            "botVersion": "0000000001",
            "botVersionReplicationStatus": "Available",
            "creationDateTime": 1.706822064378E9,
            "failureReasons": []
   }],
    "nextToken": null,
    "replicaRegion": "us-west-2",
    "sourceRegion": "us-east-1"
}
```

## See Also
<a name="API_ListBotVersionReplicas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/ListBotVersionReplicas)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/ListBotVersionReplicas)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ListBotVersionReplicas)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/ListBotVersionReplicas)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ListBotVersionReplicas)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/ListBotVersionReplicas)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/ListBotVersionReplicas)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/ListBotVersionReplicas)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/ListBotVersionReplicas)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ListBotVersionReplicas)
