---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteUtterances.html
---

# DeleteUtterances
<a name="API_DeleteUtterances"></a>

Deletes stored utterances.

Amazon Lex stores the utterances that users send to your bot. Utterances are stored for 15 days for use with the [ListAggregatedUtterances](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html) operation, and then stored indefinitely for use in improving the ability of your bot to respond to user input..

Use the `DeleteUtterances` operation to manually delete utterances for a specific session. When you use the `DeleteUtterances` operation, utterances stored for improving your bot's ability to respond to user input are deleted immediately. Utterances stored for use with the `ListAggregatedUtterances` operation are deleted after 15 days.

## Request Syntax
<a name="API_DeleteUtterances_RequestSyntax"></a>

```
DELETE /bots/{{botId}}/utterances/?localeId={{localeId}}&sessionId={{sessionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteUtterances_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_DeleteUtterances_RequestSyntax) **   <a name="lexv2-DeleteUtterances-request-uri-botId"></a>
The unique identifier of the bot that contains the utterances.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [localeId](#API_DeleteUtterances_RequestSyntax) **   <a name="lexv2-DeleteUtterances-request-uri-localeId"></a>
The identifier of the language and locale where the utterances were collected. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).

 ** [sessionId](#API_DeleteUtterances_RequestSyntax) **   <a name="lexv2-DeleteUtterances-request-uri-sessionId"></a>
The unique identifier of the session with the user. The ID is returned in the response from the [RecognizeText](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeText.html) and [RecognizeUtterance](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeUtterance.html) operations.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[0-9a-zA-Z._:-]+`

## Request Body
<a name="API_DeleteUtterances_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteUtterances_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteUtterances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteUtterances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_DeleteUtterances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DeleteUtterances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DeleteUtterances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DeleteUtterances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DeleteUtterances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DeleteUtterances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DeleteUtterances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DeleteUtterances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DeleteUtterances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DeleteUtterances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DeleteUtterances)
