---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListCrawls.html
---

# ListCrawls
<a name="API_ListCrawls"></a>

Returns all the crawls of a specified crawler. Returns only the crawls that have occurred since the launch date of the crawler history feature, and only retains up to 12 months of crawls. Older crawls will not be returned.

You may use this API to:
+ Retrive all the crawls of a specified crawler.
+ Retrieve all the crawls of a specified crawler within a limited count.
+ Retrieve all the crawls of a specified crawler in a specific time range.
+ Retrieve all the crawls of a specified crawler with a particular state, crawl ID, or DPU hour value.

## Request Syntax
<a name="API_ListCrawls_RequestSyntax"></a>

```
{
   "CrawlerName": "{{string}}",
   "Filters": [
      {
         "FieldName": "{{string}}",
         "FieldValue": "{{string}}",
         "FilterOperator": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCrawls_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CrawlerName](#API_ListCrawls_RequestSyntax) **   <a name="Glue-ListCrawls-request-CrawlerName"></a>
The name of the crawler whose runs you want to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Filters](#API_ListCrawls_RequestSyntax) **   <a name="Glue-ListCrawls-request-Filters"></a>
Filters the crawls by the criteria you specify in a list of `CrawlsFilter` objects.
Type: Array of [CrawlsFilter](API_CrawlsFilter.md) objects
Required: No

 ** [MaxResults](#API_ListCrawls_RequestSyntax) **   <a name="Glue-ListCrawls-request-MaxResults"></a>
The maximum number of results to return. The default is 20, and maximum is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListCrawls_RequestSyntax) **   <a name="Glue-ListCrawls-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

## Response Syntax
<a name="API_ListCrawls_ResponseSyntax"></a>

```
{
   "Crawls": [
      {
         "CrawlId": "string",
         "DPUHour": number,
         "EndTime": number,
         "ErrorMessage": "string",
         "LogGroup": "string",
         "LogStream": "string",
         "MessagePrefix": "string",
         "StartTime": number,
         "State": "string",
         "Summary": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCrawls_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Crawls](#API_ListCrawls_ResponseSyntax) **   <a name="Glue-ListCrawls-response-Crawls"></a>
A list of `CrawlerHistory` objects representing the crawl runs that meet your criteria.
Type: Array of [CrawlerHistory](API_CrawlerHistory.md) objects

 ** [NextToken](#API_ListCrawls_ResponseSyntax) **   <a name="Glue-ListCrawls-response-NextToken"></a>
A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.
Type: String

## Errors
<a name="API_ListCrawls_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListCrawls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListCrawls)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListCrawls)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListCrawls)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListCrawls)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListCrawls)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListCrawls)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListCrawls)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListCrawls)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListCrawls)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListCrawls)
