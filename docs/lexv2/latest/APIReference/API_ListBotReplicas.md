---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotReplicas.html
---

# ListBotReplicas
<a name="API_ListBotReplicas"></a>

The action to list the replicated bots.

## Request Syntax
<a name="API_ListBotReplicas_RequestSyntax"></a>

```
POST /bots/{{botId}}/replicas/ HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBotReplicas_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_ListBotReplicas_RequestSyntax) **   <a name="lexv2-ListBotReplicas-request-uri-botId"></a>
The request for the unique bot IDs in the list of replicated bots.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_ListBotReplicas_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBotReplicas_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "botReplicaSummaries": [
      {
         "botReplicaStatus": "string",
         "creationDateTime": number,
         "failureReasons": [ "string" ],
         "replicaRegion": "string"
      }
   ],
   "sourceRegion": "string"
}
```

## Response Elements
<a name="API_ListBotReplicas_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_ListBotReplicas_ResponseSyntax) **   <a name="lexv2-ListBotReplicas-response-botId"></a>
the unique bot IDs in the list of replicated bots.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botReplicaSummaries](#API_ListBotReplicas_ResponseSyntax) **   <a name="lexv2-ListBotReplicas-response-botReplicaSummaries"></a>
The summary details for the replicated bots.
Type: Array of [BotReplicaSummary](API_BotReplicaSummary.md) objects

 ** [sourceRegion](#API_ListBotReplicas_ResponseSyntax) **   <a name="lexv2-ListBotReplicas-response-sourceRegion"></a>
The source region of the source bots in the list of replicated bots.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.

## Errors
<a name="API_ListBotReplicas_Errors"></a>

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
<a name="API_ListBotReplicas_Examples"></a>

### This example illustrates one example input of ListBotReplicas.
<a name="API_ListBotReplicas_Example_1"></a>

This example illustrates one usage of ListBotReplicas.

```
POST https://models-v2-lex.us-east-1.amazonaws.com/bots/BOT1234567/replicas/
{
}
```

### This example illustrates one example response of ListBotReplicas.
<a name="API_ListBotReplicas_Example_2"></a>

This example illustrates one usage of ListBotReplicas.

```
{
    "botId": "BOT1234567",
    "botReplicaSummaries": [{
        "botReplicaStatus": "Enabled",
        "creationDateTime": 1.706821927692E9,
        "failureReasons": null,
        "replicaRegion": "us-west-2"
    }],
    "sourceRegion": "us-east-1"
}
```

## See Also
<a name="API_ListBotReplicas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/ListBotReplicas)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/ListBotReplicas)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ListBotReplicas)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/ListBotReplicas)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ListBotReplicas)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/ListBotReplicas)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/ListBotReplicas)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/ListBotReplicas)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/ListBotReplicas)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ListBotReplicas)
