---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SearchAssets.html
---

# SearchAssets
<a name="API_SearchAssets"></a>

Searches for assets in AWS Glue Data Catalog using full-text search, filters, sorting, and aggregations. Returns matching assets with relevance-ranked results.

## Request Syntax
<a name="API_SearchAssets_RequestSyntax"></a>

```
{
   "FilterClause": { ... },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchText": "{{string}}",
   "Sort": {
      "Attribute": "{{string}}",
      "Order": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_SearchAssets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FilterClause](#API_SearchAssets_RequestSyntax) **   <a name="Glue-SearchAssets-request-FilterClause"></a>
The filter clause to apply to the search. Supports nested AND/OR logic with attribute-level and map-level filters.
Type: [SearchFilterClause](API_SearchFilterClause.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [MaxResults](#API_SearchAssets_RequestSyntax) **   <a name="Glue-SearchAssets-request-MaxResults"></a>
The maximum number of results to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchAssets_RequestSyntax) **   <a name="Glue-SearchAssets-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

 ** [SearchText](#API_SearchAssets_RequestSyntax) **   <a name="Glue-SearchAssets-request-SearchText"></a>
The text to search for. At least one of `searchText` or `filterClause` must be provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** [Sort](#API_SearchAssets_RequestSyntax) **   <a name="Glue-SearchAssets-request-Sort"></a>
The sort criteria for the search results.
Type: [SearchSort](API_SearchSort.md) object
Required: No

## Response Syntax
<a name="API_SearchAssets_ResponseSyntax"></a>

```
{
   "Items": [
      {
         "AssetDescription": "string",
         "AssetName": "string",
         "AssetTypeId": "string",
         "Id": "string",
         "UpdatedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchAssets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_SearchAssets_ResponseSyntax) **   <a name="Glue-SearchAssets-response-Items"></a>
The list of assets matching the search criteria.
Type: Array of [SearchResultItem](API_SearchResultItem.md) objects

 ** [NextToken](#API_SearchAssets_ResponseSyntax) **   <a name="Glue-SearchAssets-response-NextToken"></a>
A continuation token, present if the current segment is not the last.
Type: String

## Errors
<a name="API_SearchAssets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ThrottlingException **
The throttling threshhold was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## Examples
<a name="API_SearchAssets_Examples"></a>

### Example
<a name="API_SearchAssets_Example_1"></a>

The following example runs a full-text search for assets.

```
aws glue search-assets --search-text "sales" --max-results 10

{
    "Items": [
        {
            "Id": "quarterly-sales-2026q1",
            "AssetName": "Quarterly Sales 2026 Q1",
            "AssetDescription": "Aggregated quarterly sales metrics",
            "UpdatedAt": "2026-06-16T06:42:00.442Z",
            "AssetTypeId": "DataSet"
        }
    ]
}
```

### Example
<a name="API_SearchAssets_Example_2"></a>

The following example searches with a filter clause and sort order.

```
aws glue search-assets \
    --search-text "sales" \
    --max-results 10 \
    --filter-clause '{"AttributeFilter":{"Attribute":"AssetTypeId","Operator":"equals","Value":{"StringValue":"DataSet"}}}' \
    --sort '{"Attribute":"name","Order":"ASCENDING"}'

{
    "Items": [
        {
            "Id": "quarterly-sales-2026q1",
            "AssetName": "Quarterly Sales 2026 Q1",
            "AssetDescription": "Aggregated quarterly sales metrics",
            "UpdatedAt": "2026-06-16T06:42:00.442Z",
            "AssetTypeId": "DataSet"
        }
    ]
}
```

## See Also
<a name="API_SearchAssets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/SearchAssets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/SearchAssets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SearchAssets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/SearchAssets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SearchAssets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/SearchAssets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/SearchAssets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/SearchAssets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/SearchAssets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SearchAssets)
