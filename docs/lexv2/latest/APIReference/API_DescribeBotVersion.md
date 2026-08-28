---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBotVersion.html
---

# DescribeBotVersion
<a name="API_DescribeBotVersion"></a>

Provides metadata about a version of a bot.

## Request Syntax
<a name="API_DescribeBotVersion_RequestSyntax"></a>

```
GET /bots/{{botId}}/botversions/{{botVersion}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeBotVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_DescribeBotVersion_RequestSyntax) **   <a name="lexv2-DescribeBotVersion-request-uri-botId"></a>
The identifier of the bot containing the version to return metadata for.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_DescribeBotVersion_RequestSyntax) **   <a name="lexv2-DescribeBotVersion-request-uri-botVersion"></a>
The version of the bot to return metadata for.
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^[0-9]+$`
Required: Yes

## Request Body
<a name="API_DescribeBotVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeBotVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
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
   "botVersion": "string",
   "creationDateTime": number,
   "dataPrivacy": {
      "childDirected": boolean
   },
   "description": "string",
   "failureReasons": [ "string" ],
   "idleSessionTTLInSeconds": number,
   "parentBotNetworks": [
      {
         "botId": "string",
         "botVersion": "string"
      }
   ],
   "roleArn": "string"
}
```

## Response Elements
<a name="API_DescribeBotVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_DescribeBotVersion_ResponseSyntax) **   <a name="lexv2-DescribeBotVersion-response-botId"></a>
The identifier of the bot that contains the version.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botMembers](#API_DescribeBotVersion_ResponseSyntax) **   <a name="lexv2-DescribeBotVersion-response-botMembers"></a>
The members of bot network in the version that was described.
Type: Array of [BotMember](API_BotMember.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [botName](#API_DescribeBotVersion_ResponseSyntax) **   <a name="lexv2-DescribeBotVersion-response-botName"></a>
The name of the bot that contains the version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

 ** [botStatus](#API_DescribeBotVersion_ResponseSyntax) **   <a name="lexv2-DescribeBotVersion-response-botStatus"></a>
The current status of the bot. When the status is `Available`, the bot version is ready for use.
Type: String
Valid Values: `Creating | Available | Inactive | Deleting | Failed | Versioning | Importing | Updating`

 ** [botType](#API_DescribeBotVersion_ResponseSyntax) **   <a name="lexv2-DescribeBotVersion-response-botType"></a>
The type of the bot in the version that was described.
Type: String
Valid Values: `Bot | BotNetwork`

 ** [botVersion](#API_DescribeBotVersion_ResponseSyntax) **   <a name="lexv2-DescribeBotVersion-response-botVersion"></a>
The version of the bot that was described.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^[0-9]+$`

 ** [creationDateTime](#API_DescribeBotVersion_ResponseSyntax) **   <a name="lexv2-DescribeBotVersion-response-creationDateTime"></a>
A timestamp of the date and time that the bot version was created.
Type: Timestamp

 ** [dataPrivacy](#API_DescribeBotVersion_ResponseSyntax) **   <a name="lexv2-DescribeBotVersion-response-dataPrivacy"></a>
Data privacy settings for the bot version.
Type: [DataPrivacy](API_DataPrivacy.md) object

 ** [description](#API_DescribeBotVersion_ResponseSyntax) **   <a name="lexv2-DescribeBotVersion-response-description"></a>
The description specified for the bot.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [failureReasons](#API_DescribeBotVersion_ResponseSyntax) **   <a name="lexv2-DescribeBotVersion-response-failureReasons"></a>
If the `botStatus` is `Failed`, this contains a list of reasons that the version couldn't be built.
Type: Array of strings

 ** [idleSessionTTLInSeconds](#API_DescribeBotVersion_ResponseSyntax) **   <a name="lexv2-DescribeBotVersion-response-idleSessionTTLInSeconds"></a>
The number of seconds that a session with the bot remains active before it is discarded by Amazon Lex.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 86400.

 ** [parentBotNetworks](#API_DescribeBotVersion_ResponseSyntax) **   <a name="lexv2-DescribeBotVersion-response-parentBotNetworks"></a>
A list of the networks to which the bot version you described belongs.
Type: Array of [ParentBotNetwork](API_ParentBotNetwork.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.

 ** [roleArn](#API_DescribeBotVersion_ResponseSyntax) **   <a name="lexv2-DescribeBotVersion-response-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that has permission to access the bot version.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.*$`

## Errors
<a name="API_DescribeBotVersion_Errors"></a>

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
<a name="API_DescribeBotVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DescribeBotVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DescribeBotVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescribeBotVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DescribeBotVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescribeBotVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DescribeBotVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DescribeBotVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DescribeBotVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DescribeBotVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescribeBotVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
