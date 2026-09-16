---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotRecommendations.html
---

# ListBotRecommendations
<a name="API_ListBotRecommendations"></a>

Get a list of bot recommendations that meet the specified criteria.

## Request Syntax
<a name="API_ListBotRecommendations_RequestSyntax"></a>

```
POST /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/botrecommendations/ HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListBotRecommendations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_ListBotRecommendations_RequestSyntax) **   <a name="lexv2-ListBotRecommendations-request-uri-botId"></a>
The unique identifier of the bot that contains the bot recommendation list.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_ListBotRecommendations_RequestSyntax) **   <a name="lexv2-ListBotRecommendations-request-uri-botVersion"></a>
The version of the bot that contains the bot recommendation list.
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`
Required: Yes

 ** [localeId](#API_ListBotRecommendations_RequestSyntax) **   <a name="lexv2-ListBotRecommendations-request-uri-localeId"></a>
The identifier of the language and locale of the bot recommendation list.
Required: Yes

## Request Body
<a name="API_ListBotRecommendations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListBotRecommendations_RequestSyntax) **   <a name="lexv2-ListBotRecommendations-request-maxResults"></a>
The maximum number of bot recommendations to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListBotRecommendations_RequestSyntax) **   <a name="lexv2-ListBotRecommendations-request-nextToken"></a>
If the response from the ListBotRecommendation operation contains more results than specified in the maxResults parameter, a token is returned in the response. Use that token in the nextToken parameter to return the next page of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListBotRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "botRecommendationSummaries": [
      {
         "botRecommendationId": "string",
         "botRecommendationStatus": "string",
         "creationDateTime": number,
         "lastUpdatedDateTime": number
      }
   ],
   "botVersion": "string",
   "localeId": "string",
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBotRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_ListBotRecommendations_ResponseSyntax) **   <a name="lexv2-ListBotRecommendations-response-botId"></a>
The unique identifier of the bot that contains the bot recommendation list.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botRecommendationSummaries](#API_ListBotRecommendations_ResponseSyntax) **   <a name="lexv2-ListBotRecommendations-response-botRecommendationSummaries"></a>
Summary information for the bot recommendations that meet the filter specified in this request. The length of the list is specified in the maxResults parameter of the request. If there are more bot recommendations available, the nextToken field contains a token to get the next page of results.
Type: Array of [BotRecommendationSummary](API_BotRecommendationSummary.md) objects

 ** [botVersion](#API_ListBotRecommendations_ResponseSyntax) **   <a name="lexv2-ListBotRecommendations-response-botVersion"></a>
The version of the bot that contains the bot recommendation list.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [localeId](#API_ListBotRecommendations_ResponseSyntax) **   <a name="lexv2-ListBotRecommendations-response-localeId"></a>
The identifier of the language and locale of the bot recommendation list.
Type: String

 ** [nextToken](#API_ListBotRecommendations_ResponseSyntax) **   <a name="lexv2-ListBotRecommendations-response-nextToken"></a>
A token that indicates whether there are more results to return in a response to the ListBotRecommendations operation. If the nextToken field is present, you send the contents as the nextToken parameter of a ListBotRecommendations operation request to get the next page of results.
Type: String

## Errors
<a name="API_ListBotRecommendations_Errors"></a>

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

## See Also
<a name="API_ListBotRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/ListBotRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/ListBotRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ListBotRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/ListBotRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ListBotRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/ListBotRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/ListBotRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/ListBotRecommendations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/ListBotRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ListBotRecommendations)
