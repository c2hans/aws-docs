---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBotReplica.html
---

# DescribeBotReplica
<a name="API_DescribeBotReplica"></a>

Monitors the bot replication status through the UI console.

## Request Syntax
<a name="API_DescribeBotReplica_RequestSyntax"></a>

```
GET /bots/{{botId}}/replicas/{{replicaRegion}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeBotReplica_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_DescribeBotReplica_RequestSyntax) **   <a name="lexv2-DescribeBotReplica-request-uri-botId"></a>
The request for the unique bot ID of the replicated bot being monitored.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [replicaRegion](#API_DescribeBotReplica_RequestSyntax) **   <a name="lexv2-DescribeBotReplica-request-uri-replicaRegion"></a>
The request for the region of the replicated bot being monitored.
Length Constraints: Minimum length of 2. Maximum length of 25.
Required: Yes

## Request Body
<a name="API_DescribeBotReplica_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeBotReplica_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "botReplicaStatus": "string",
   "creationDateTime": number,
   "failureReasons": [ "string" ],
   "replicaRegion": "string",
   "sourceRegion": "string"
}
```

## Response Elements
<a name="API_DescribeBotReplica_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_DescribeBotReplica_ResponseSyntax) **   <a name="lexv2-DescribeBotReplica-response-botId"></a>
The unique bot ID of the replicated bot being monitored.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botReplicaStatus](#API_DescribeBotReplica_ResponseSyntax) **   <a name="lexv2-DescribeBotReplica-response-botReplicaStatus"></a>
The operational status of the replicated bot being monitored.
Type: String
Valid Values: `Enabling | Enabled | Deleting | Failed`

 ** [creationDateTime](#API_DescribeBotReplica_ResponseSyntax) **   <a name="lexv2-DescribeBotReplica-response-creationDateTime"></a>
The creation date and time of the replicated bot being monitored.
Type: Timestamp

 ** [failureReasons](#API_DescribeBotReplica_ResponseSyntax) **   <a name="lexv2-DescribeBotReplica-response-failureReasons"></a>
The failure reasons the bot being monitored failed to replicate.
Type: Array of strings

 ** [replicaRegion](#API_DescribeBotReplica_ResponseSyntax) **   <a name="lexv2-DescribeBotReplica-response-replicaRegion"></a>
The region of the replicated bot being monitored.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.

 ** [sourceRegion](#API_DescribeBotReplica_ResponseSyntax) **   <a name="lexv2-DescribeBotReplica-response-sourceRegion"></a>
The source region of the replicated bot being monitored.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.

## Errors
<a name="API_DescribeBotReplica_Errors"></a>

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

## Examples
<a name="API_DescribeBotReplica_Examples"></a>

### This example illustrates one example input of DescribeBotReplica
<a name="API_DescribeBotReplica_Example_1"></a>

This example illustrates one usage of DescribeBotReplica.

```
GET https://models-v2-lex.us-east-1.amazonaws.com/bots/BOT1234567/replicas/us-west-2
{
    "replicaRegion": "us-west-2"
}
```

### This example illustrates one example response of DescribeBotReplica.
<a name="API_DescribeBotReplica_Example_2"></a>

This example illustrates one usage of DescribeBotReplica.

```
{
    "botId": "BOT1234567",
    "botReplicaStatus": "Enabled",
    "creationDateTime": 1.706821927692E9,
    "failureReasons": null,
    "replicaRegion": "us-west-2",
    "sourceRegion": "us-east-1"
}
```

## See Also
<a name="API_DescribeBotReplica_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DescribeBotReplica)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DescribeBotReplica)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescribeBotReplica)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DescribeBotReplica)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescribeBotReplica)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DescribeBotReplica)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DescribeBotReplica)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DescribeBotReplica)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DescribeBotReplica)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescribeBotReplica)
