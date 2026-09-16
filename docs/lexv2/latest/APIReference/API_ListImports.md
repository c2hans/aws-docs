---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListImports.html
---

# ListImports
<a name="API_ListImports"></a>

Lists the imports for a bot, bot locale, or custom vocabulary. Imports are kept in the list for 7 days.

## Request Syntax
<a name="API_ListImports_RequestSyntax"></a>

```
POST /imports/ HTTP/1.1
Content-type: application/json

{
   "botId": "{{string}}",
   "botVersion": "{{string}}",
   "filters": [
      {
         "name": "{{string}}",
         "operator": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "localeId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sortBy": {
      "attribute": "{{string}}",
      "order": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListImports_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListImports_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [botId](#API_ListImports_RequestSyntax) **   <a name="lexv2-ListImports-request-botId"></a>
The unique identifier that Amazon Lex assigned to the bot.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: No

 ** [botVersion](#API_ListImports_RequestSyntax) **   <a name="lexv2-ListImports-request-botVersion"></a>
The version of the bot to list imports for.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`
Required: No

 ** [filters](#API_ListImports_RequestSyntax) **   <a name="lexv2-ListImports-request-filters"></a>
Provides the specification of a filter used to limit the bots in the response to only those that match the filter specification. You can only specify one filter and one string to filter on.
Type: Array of [ImportFilter](API_ImportFilter.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [localeId](#API_ListImports_RequestSyntax) **   <a name="lexv2-ListImports-request-localeId"></a>
Specifies the locale that should be present in the list. If you don't specify a resource type in the `filters` parameter, the list contains both bot locales and custom vocabularies.
Type: String
Required: No

 ** [maxResults](#API_ListImports_RequestSyntax) **   <a name="lexv2-ListImports-request-maxResults"></a>
The maximum number of imports to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListImports_RequestSyntax) **   <a name="lexv2-ListImports-request-nextToken"></a>
If the response from the `ListImports` operation contains more results than specified in the `maxResults` parameter, a token is returned in the response.
Use the returned token in the `nextToken` parameter of a `ListImports` request to return the next page of results. For a complete set of results, call the `ListImports` operation until the `nextToken` returned in the response is null.
Type: String
Required: No

 ** [sortBy](#API_ListImports_RequestSyntax) **   <a name="lexv2-ListImports-request-sortBy"></a>
Determines the field that the list of imports is sorted by. You can sort by the `LastUpdatedDateTime` field in ascending or descending order.
Type: [ImportSortBy](API_ImportSortBy.md) object
Required: No

## Response Syntax
<a name="API_ListImports_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "botVersion": "string",
   "importSummaries": [
      {
         "creationDateTime": number,
         "importedResourceId": "string",
         "importedResourceName": "string",
         "importedResourceType": "string",
         "importId": "string",
         "importStatus": "string",
         "lastUpdatedDateTime": number,
         "mergeStrategy": "string"
      }
   ],
   "localeId": "string",
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListImports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_ListImports_ResponseSyntax) **   <a name="lexv2-ListImports-response-botId"></a>
The unique identifier assigned by Amazon Lex to the bot.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_ListImports_ResponseSyntax) **   <a name="lexv2-ListImports-response-botVersion"></a>
The version of the bot that was imported. It will always be `DRAFT`.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [importSummaries](#API_ListImports_ResponseSyntax) **   <a name="lexv2-ListImports-response-importSummaries"></a>
Summary information for the imports that meet the filter criteria specified in the request. The length of the list is specified in the `maxResults` parameter. If there are more imports available, the `nextToken` field contains a token to get the next page of results.
Type: Array of [ImportSummary](API_ImportSummary.md) objects

 ** [localeId](#API_ListImports_ResponseSyntax) **   <a name="lexv2-ListImports-response-localeId"></a>
The locale specified in the request.
Type: String

 ** [nextToken](#API_ListImports_ResponseSyntax) **   <a name="lexv2-ListImports-response-nextToken"></a>
A token that indicates whether there are more results to return in a response to the `ListImports` operation. If the `nextToken` field is present, you send the contents as the `nextToken` parameter of a `ListImports` operation request to get the next page of results.
Type: String

## Errors
<a name="API_ListImports_Errors"></a>

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
<a name="API_ListImports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/ListImports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/ListImports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ListImports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/ListImports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ListImports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/ListImports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/ListImports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/ListImports)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/ListImports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ListImports)
