---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotResourceGenerations.html
---

# ListBotResourceGenerations
<a name="API_ListBotResourceGenerations"></a>

Lists the generation requests made for a bot locale.

## Request Syntax
<a name="API_ListBotResourceGenerations_RequestSyntax"></a>

```
POST /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/generations HTTP/1.1
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
<a name="API_ListBotResourceGenerations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_ListBotResourceGenerations_RequestSyntax) **   <a name="lexv2-ListBotResourceGenerations-request-uri-botId"></a>
The unique identifier of the bot whose generation requests you want to view.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_ListBotResourceGenerations_RequestSyntax) **   <a name="lexv2-ListBotResourceGenerations-request-uri-botVersion"></a>
The version of the bot whose generation requests you want to view.
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: Yes

 ** [localeId](#API_ListBotResourceGenerations_RequestSyntax) **   <a name="lexv2-ListBotResourceGenerations-request-uri-localeId"></a>
The locale of the bot whose generation requests you want to view.
Required: Yes

## Request Body
<a name="API_ListBotResourceGenerations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListBotResourceGenerations_RequestSyntax) **   <a name="lexv2-ListBotResourceGenerations-request-maxResults"></a>
The maximum number of results to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListBotResourceGenerations_RequestSyntax) **   <a name="lexv2-ListBotResourceGenerations-request-nextToken"></a>
If the total number of results is greater than the number specified in the `maxResults`, the response returns a token in the `nextToken` field. Use this token when making a request to return the next batch of results.
Type: String
Required: No

 ** [sortBy](#API_ListBotResourceGenerations_RequestSyntax) **   <a name="lexv2-ListBotResourceGenerations-request-sortBy"></a>
An object containing information about the attribute and the method by which to sort the results
Type: [GenerationSortBy](API_GenerationSortBy.md) object
Required: No

## Response Syntax
<a name="API_ListBotResourceGenerations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "botVersion": "string",
   "generationSummaries": [
      {
         "creationDateTime": number,
         "generationId": "string",
         "generationStatus": "string",
         "lastUpdatedDateTime": number
      }
   ],
   "localeId": "string",
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBotResourceGenerations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_ListBotResourceGenerations_ResponseSyntax) **   <a name="lexv2-ListBotResourceGenerations-response-botId"></a>
The unique identifier of the bot for which the generation requests were made.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_ListBotResourceGenerations_ResponseSyntax) **   <a name="lexv2-ListBotResourceGenerations-response-botVersion"></a>
The version of the bot for which the generation requests were made.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`

 ** [generationSummaries](#API_ListBotResourceGenerations_ResponseSyntax) **   <a name="lexv2-ListBotResourceGenerations-response-generationSummaries"></a>
A list of objects, each containing information about a generation request for the bot locale.
Type: Array of [GenerationSummary](API_GenerationSummary.md) objects

 ** [localeId](#API_ListBotResourceGenerations_ResponseSyntax) **   <a name="lexv2-ListBotResourceGenerations-response-localeId"></a>
The locale of the bot for which the generation requests were made.
Type: String

 ** [nextToken](#API_ListBotResourceGenerations_ResponseSyntax) **   <a name="lexv2-ListBotResourceGenerations-response-nextToken"></a>
If the total number of results is greater than the number specified in the `maxResults`, the response returns a token in the `nextToken` field. Use this token when making a request to return the next batch of results.
Type: String

## Errors
<a name="API_ListBotResourceGenerations_Errors"></a>

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
<a name="API_ListBotResourceGenerations_Examples"></a>

### Example request
<a name="API_ListBotResourceGenerations_Example_1"></a>

This example illustrates one usage of ListBotResourceGenerations.

```
POST https://models-v2-lex.us-east-1.amazonaws.com/bots/BOT1234567/botversions/DRAFT/botlocales/en_GB/generations

Payload:
{
    "sortBy": {
        "attribute": "lastUpdatedTime",
        "order": "Descending"
    },
    "maxResults": 1
}
```

### Example response
<a name="API_ListBotResourceGenerations_Example_2"></a>

This example illustrates one usage of ListBotResourceGenerations.

```
{
    "botId": "BOT1234567",
    "botVersion": "DRAFT",
    "generationSummaries": [{
        "creationDateTime": 1.699570064977E9,
        "generationId": "GEN1234567",
        "generationStatus": "Complete",
        "lastUpdatedDateTime": 1.699570064977E9
    }],
    "localeId": "en_GB",
    "nextToken": null
}
```

## See Also
<a name="API_ListBotResourceGenerations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/ListBotResourceGenerations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/ListBotResourceGenerations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ListBotResourceGenerations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/ListBotResourceGenerations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ListBotResourceGenerations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/ListBotResourceGenerations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/ListBotResourceGenerations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/ListBotResourceGenerations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/ListBotResourceGenerations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ListBotResourceGenerations)
