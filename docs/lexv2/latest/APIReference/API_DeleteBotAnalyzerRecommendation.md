---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBotAnalyzerRecommendation.html
---

# DeleteBotAnalyzerRecommendation
<a name="API_DeleteBotAnalyzerRecommendation"></a>

Permanently deletes the recommendations and analysis results for a specific bot analysis request. This operation is provided for GDPR compliance and cannot be undone.

After deletion, the analysis results cannot be retrieved. The analysis request ID will still appear in the history list, but attempting to describe the recommendations will return a `ResourceNotFoundException`.

## Request Syntax
<a name="API_DeleteBotAnalyzerRecommendation_RequestSyntax"></a>

```
DELETE /bots/{{botId}}/botanalyzer/{{botAnalyzerRequestId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteBotAnalyzerRecommendation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botAnalyzerRequestId](#API_DeleteBotAnalyzerRecommendation_RequestSyntax) **   <a name="lexv2-DeleteBotAnalyzerRecommendation-request-uri-botAnalyzerRequestId"></a>
The unique identifier of the analysis request whose recommendations should be deleted.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [botId](#API_DeleteBotAnalyzerRecommendation_RequestSyntax) **   <a name="lexv2-DeleteBotAnalyzerRecommendation-request-uri-botId"></a>
The unique identifier of the bot.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_DeleteBotAnalyzerRecommendation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteBotAnalyzerRecommendation_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteBotAnalyzerRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteBotAnalyzerRecommendation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## Examples
<a name="API_DeleteBotAnalyzerRecommendation_Examples"></a>

### Example request
<a name="API_DeleteBotAnalyzerRecommendation_Example_1"></a>

This example illustrates one usage of DeleteBotAnalyzerRecommendation.

```
DELETE https://models-v2-lex.us-east-1.amazonaws.com/bots/<BotId>/botanalyzer/<RequestId>/
```

### Example response
<a name="API_DeleteBotAnalyzerRecommendation_Example_2"></a>

This example illustrates one usage of DeleteBotAnalyzerRecommendation.

```
HTTP/1.1 204 No Content
```

## See Also
<a name="API_DeleteBotAnalyzerRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DeleteBotAnalyzerRecommendation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DeleteBotAnalyzerRecommendation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DeleteBotAnalyzerRecommendation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DeleteBotAnalyzerRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DeleteBotAnalyzerRecommendation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DeleteBotAnalyzerRecommendation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DeleteBotAnalyzerRecommendation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DeleteBotAnalyzerRecommendation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DeleteBotAnalyzerRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DeleteBotAnalyzerRecommendation)
