---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBotReplica.html
---

# DeleteBotReplica
<a name="API_DeleteBotReplica"></a>

The action to delete the replicated bot in the secondary region.

## Request Syntax
<a name="API_DeleteBotReplica_RequestSyntax"></a>

```
DELETE /bots/{{botId}}/replicas/{{replicaRegion}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteBotReplica_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_DeleteBotReplica_RequestSyntax) **   <a name="lexv2-DeleteBotReplica-request-uri-botId"></a>
The unique ID of the replicated bot to be deleted from the secondary region
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [replicaRegion](#API_DeleteBotReplica_RequestSyntax) **   <a name="lexv2-DeleteBotReplica-request-uri-replicaRegion"></a>
The secondary region of the replicated bot that will be deleted.
Length Constraints: Minimum length of 2. Maximum length of 25.
Required: Yes

## Request Body
<a name="API_DeleteBotReplica_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteBotReplica_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "botId": "string",
   "botReplicaStatus": "string",
   "replicaRegion": "string"
}
```

## Response Elements
<a name="API_DeleteBotReplica_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_DeleteBotReplica_ResponseSyntax) **   <a name="lexv2-DeleteBotReplica-response-botId"></a>
The unique bot ID of the replicated bot generated.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botReplicaStatus](#API_DeleteBotReplica_ResponseSyntax) **   <a name="lexv2-DeleteBotReplica-response-botReplicaStatus"></a>
The operational status of the replicated bot generated.
Type: String
Valid Values: `Enabling | Enabled | Deleting | Failed`

 ** [replicaRegion](#API_DeleteBotReplica_ResponseSyntax) **   <a name="lexv2-DeleteBotReplica-response-replicaRegion"></a>
The region of the replicated bot generated.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.

## Errors
<a name="API_DeleteBotReplica_Errors"></a>

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

## Examples
<a name="API_DeleteBotReplica_Examples"></a>

### This example illustrates one example input of DeleteBotReplica.
<a name="API_DeleteBotReplica_Example_1"></a>

This example illustrates one usage of DeleteBotReplica.

```
DELETE https://models-v2-lex.us-east-1.amazonaws.com/bots/BOT1234567/replicas/us-west-2
{
    "replicaRegion": "us-west-2"
}
```

### This example illustrates one example response of DeleteBotReplica.
<a name="API_DeleteBotReplica_Example_2"></a>

This example illustrates one usage of DeleteBotReplica.

```
{
    "botId": "BOT1234567",
    "botReplicaStatus": "Deleting",
    "replicaRegion": "us-west-2"
}
```

## See Also
<a name="API_DeleteBotReplica_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DeleteBotReplica)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DeleteBotReplica)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DeleteBotReplica)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DeleteBotReplica)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DeleteBotReplica)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DeleteBotReplica)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DeleteBotReplica)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DeleteBotReplica)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DeleteBotReplica)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DeleteBotReplica)
