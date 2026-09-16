---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SearchAssociatedTranscripts.html
---

# SearchAssociatedTranscripts
<a name="API_SearchAssociatedTranscripts"></a>

Search for associated transcripts that meet the specified criteria.

## Request Syntax
<a name="API_SearchAssociatedTranscripts_RequestSyntax"></a>

```
POST /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/botrecommendations/{{botRecommendationId}}/associatedtranscripts HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextIndex": {{number}},
   "searchOrder": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchAssociatedTranscripts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_SearchAssociatedTranscripts_RequestSyntax) **   <a name="lexv2-SearchAssociatedTranscripts-request-uri-botId"></a>
The unique identifier of the bot associated with the transcripts that you are searching.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botRecommendationId](#API_SearchAssociatedTranscripts_RequestSyntax) **   <a name="lexv2-SearchAssociatedTranscripts-request-uri-botRecommendationId"></a>
The unique identifier of the bot recommendation associated with the transcripts to search.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_SearchAssociatedTranscripts_RequestSyntax) **   <a name="lexv2-SearchAssociatedTranscripts-request-uri-botVersion"></a>
The version of the bot containing the transcripts that you are searching.
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: Yes

 ** [localeId](#API_SearchAssociatedTranscripts_RequestSyntax) **   <a name="lexv2-SearchAssociatedTranscripts-request-uri-localeId"></a>
The identifier of the language and locale of the transcripts to search. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html)
Required: Yes

## Request Body
<a name="API_SearchAssociatedTranscripts_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_SearchAssociatedTranscripts_RequestSyntax) **   <a name="lexv2-SearchAssociatedTranscripts-request-filters"></a>
A list of filter objects.
Type: Array of [AssociatedTranscriptFilter](API_AssociatedTranscriptFilter.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [maxResults](#API_SearchAssociatedTranscripts_RequestSyntax) **   <a name="lexv2-SearchAssociatedTranscripts-request-maxResults"></a>
The maximum number of bot recommendations to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextIndex](#API_SearchAssociatedTranscripts_RequestSyntax) **   <a name="lexv2-SearchAssociatedTranscripts-request-nextIndex"></a>
If the response from the SearchAssociatedTranscriptsRequest operation contains more results than specified in the maxResults parameter, an index is returned in the response. Use that index in the nextIndex parameter to return the next page of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000000.
Required: No

 ** [searchOrder](#API_SearchAssociatedTranscripts_RequestSyntax) **   <a name="lexv2-SearchAssociatedTranscripts-request-searchOrder"></a>
How SearchResults are ordered. Valid values are Ascending or Descending. The default is Descending.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_SearchAssociatedTranscripts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "associatedTranscripts": [
      {
         "transcript": "string"
      }
   ],
   "botId": "string",
   "botRecommendationId": "string",
   "botVersion": "string",
   "localeId": "string",
   "nextIndex": number,
   "totalResults": number
}
```

## Response Elements
<a name="API_SearchAssociatedTranscripts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associatedTranscripts](#API_SearchAssociatedTranscripts_ResponseSyntax) **   <a name="lexv2-SearchAssociatedTranscripts-response-associatedTranscripts"></a>
The object that contains the associated transcript that meet the criteria you specified.
Type: Array of [AssociatedTranscript](API_AssociatedTranscript.md) objects

 ** [botId](#API_SearchAssociatedTranscripts_ResponseSyntax) **   <a name="lexv2-SearchAssociatedTranscripts-response-botId"></a>
The unique identifier of the bot associated with the transcripts that you are searching.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botRecommendationId](#API_SearchAssociatedTranscripts_ResponseSyntax) **   <a name="lexv2-SearchAssociatedTranscripts-response-botRecommendationId"></a>
 The unique identifier of the bot recommendation associated with the transcripts to search.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_SearchAssociatedTranscripts_ResponseSyntax) **   <a name="lexv2-SearchAssociatedTranscripts-response-botVersion"></a>
The version of the bot containing the transcripts that you are searching.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`

 ** [localeId](#API_SearchAssociatedTranscripts_ResponseSyntax) **   <a name="lexv2-SearchAssociatedTranscripts-response-localeId"></a>
The identifier of the language and locale of the transcripts to search. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html)
Type: String

 ** [nextIndex](#API_SearchAssociatedTranscripts_ResponseSyntax) **   <a name="lexv2-SearchAssociatedTranscripts-response-nextIndex"></a>
A index that indicates whether there are more results to return in a response to the SearchAssociatedTranscripts operation. If the nextIndex field is present, you send the contents as the nextIndex parameter of a SearchAssociatedTranscriptsRequest operation to get the next page of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000000.

 ** [totalResults](#API_SearchAssociatedTranscripts_ResponseSyntax) **   <a name="lexv2-SearchAssociatedTranscripts-response-totalResults"></a>
The total number of transcripts returned by the search.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.

## Errors
<a name="API_SearchAssociatedTranscripts_Errors"></a>

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
<a name="API_SearchAssociatedTranscripts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/SearchAssociatedTranscripts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/SearchAssociatedTranscripts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SearchAssociatedTranscripts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/SearchAssociatedTranscripts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SearchAssociatedTranscripts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/SearchAssociatedTranscripts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/SearchAssociatedTranscripts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/SearchAssociatedTranscripts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/SearchAssociatedTranscripts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SearchAssociatedTranscripts)
