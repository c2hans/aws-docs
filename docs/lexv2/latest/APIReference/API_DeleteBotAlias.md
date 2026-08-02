---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBotAlias.html
---

# DeleteBotAlias
<a name="API_DeleteBotAlias"></a>

Deletes the specified bot alias.

## Request Syntax
<a name="API_DeleteBotAlias_RequestSyntax"></a>

```
DELETE /bots/{{botId}}/botaliases/{{botAliasId}}/?skipResourceInUseCheck={{skipResourceInUseCheck}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteBotAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botAliasId](#API_DeleteBotAlias_RequestSyntax) **   <a name="lexv2-DeleteBotAlias-request-uri-botAliasId"></a>
The unique identifier of the bot alias to delete.
Length Constraints: Fixed length of 10.
Pattern: `^(\bTSTALIASID\b|[0-9a-zA-Z]+)$`
Required: Yes

 ** [botId](#API_DeleteBotAlias_RequestSyntax) **   <a name="lexv2-DeleteBotAlias-request-uri-botId"></a>
The unique identifier of the bot associated with the alias to delete.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [skipResourceInUseCheck](#API_DeleteBotAlias_RequestSyntax) **   <a name="lexv2-DeleteBotAlias-request-uri-skipResourceInUseCheck"></a>
By default, Amazon Lex checks if any other resource, such as a bot network, is using the bot alias before it is deleted and throws a `ResourceInUseException` exception if the alias is being used by another resource. Set this parameter to `true` to skip this check and remove the alias even if it is being used by another resource.

## Request Body
<a name="API_DeleteBotAlias_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteBotAlias_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "botAliasId": "string",
   "botAliasStatus": "string",
   "botId": "string"
}
```

## Response Elements
<a name="API_DeleteBotAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [botAliasId](#API_DeleteBotAlias_ResponseSyntax) **   <a name="lexv2-DeleteBotAlias-response-botAliasId"></a>
The unique identifier of the bot alias to delete.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^(\bTSTALIASID\b|[0-9a-zA-Z]+)$`

 ** [botAliasStatus](#API_DeleteBotAlias_ResponseSyntax) **   <a name="lexv2-DeleteBotAlias-response-botAliasStatus"></a>
The current status of the alias. The status is `Deleting` while the alias is in the process of being deleted. Once the alias is deleted, it will no longer appear in the list of aliases returned by the `ListBotAliases` operation.
Type: String
Valid Values: `Creating | Available | Deleting | Failed`

 ** [botId](#API_DeleteBotAlias_ResponseSyntax) **   <a name="lexv2-DeleteBotAlias-response-botId"></a>
The unique identifier of the bot that contains the alias to delete.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

## Errors
<a name="API_DeleteBotAlias_Errors"></a>

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
<a name="API_DeleteBotAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DeleteBotAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DeleteBotAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DeleteBotAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DeleteBotAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DeleteBotAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DeleteBotAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DeleteBotAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DeleteBotAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DeleteBotAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DeleteBotAlias)
