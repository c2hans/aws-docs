---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBot.html
---

# DeleteBot
<a name="API_DeleteBot"></a>

Deletes all versions of a bot, including the `Draft` version. To delete a specific version, use the `DeleteBotVersion` operation.

When you delete a bot, all of the resources contained in the bot are also deleted. Deleting a bot removes all locales, intents, slot, and slot types defined for the bot.

If a bot has an alias, the `DeleteBot` operation returns a `ResourceInUseException` exception. If you want to delete the bot and the alias, set the `skipResourceInUseCheck` parameter to `true`.

## Request Syntax
<a name="API_DeleteBot_RequestSyntax"></a>

```
DELETE /bots/{{botId}}/?skipResourceInUseCheck={{skipResourceInUseCheck}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteBot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_DeleteBot_RequestSyntax) **   <a name="lexv2-DeleteBot-request-uri-botId"></a>
The identifier of the bot to delete.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [skipResourceInUseCheck](#API_DeleteBot_RequestSyntax) **   <a name="lexv2-DeleteBot-request-uri-skipResourceInUseCheck"></a>
By default, Amazon Lex checks if any other resource, such as an alias or bot network, is using the bot version before it is deleted and throws a `ResourceInUseException` exception if the bot is being used by another resource. Set this parameter to `true` to skip this check and remove the bot even if it is being used by another resource.

## Request Body
<a name="API_DeleteBot_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteBot_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "botId": "string",
   "botStatus": "string"
}
```

## Response Elements
<a name="API_DeleteBot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_DeleteBot_ResponseSyntax) **   <a name="lexv2-DeleteBot-response-botId"></a>
The unique identifier of the bot that Amazon Lex is deleting.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botStatus](#API_DeleteBot_ResponseSyntax) **   <a name="lexv2-DeleteBot-response-botStatus"></a>
The current status of the bot. The status is `Deleting` while the bot and its associated resources are being deleted.
Type: String
Valid Values: `Creating | Available | Inactive | Deleting | Failed | Versioning | Importing | Updating`

## Errors
<a name="API_DeleteBot_Errors"></a>

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
<a name="API_DeleteBot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DeleteBot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DeleteBot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DeleteBot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DeleteBot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DeleteBot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DeleteBot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DeleteBot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DeleteBot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DeleteBot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DeleteBot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
