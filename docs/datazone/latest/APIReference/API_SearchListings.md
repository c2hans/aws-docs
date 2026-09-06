---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SearchListings.html
---

# SearchListings
<a name="API_SearchListings"></a>

Searches listings in Amazon DataZone.

SearchListings is a powerful capability that enables users to discover and explore published assets and data products across their organization. It provides both basic and advanced search functionality, allowing users to find resources based on names, descriptions, metadata, and other attributes. SearchListings also supports filtering using various criteria such as creation date, owner, or status. This API is essential for making the wealth of data resources in an organization discoverable and usable, helping users find the right data for their needs quickly and efficiently.

SearchListings returns results in a paginated format. When the result set is large, the response will include a nextToken, which can be used to retrieve the next page of results.

The SearchListings API gives users flexibility in specifying what kind of search is run.

To run a standard free-text search, the `searchText` parameter must be supplied. By default, all searchable fields are indexed for semantic search and will return semantic matches for SearchListings queries. To prevent semantic search indexing for a custom form attribute, see the [CreateFormType API documentation](https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateFormType.html). To run a lexical search query, enclose the query with double quotes (""). This will disable semantic search even for fields that have semantic search enabled and will only return results that contain the keywords wrapped by double quotes (order of tokens in the query is not enforced). Free-text search is supported for all attributes annotated with @amazon.datazone\#searchable.

To run a filtered search, provide filter clause using the `filters` parameter. To filter on glossary terms, use the special attribute `__DataZoneGlossaryTerms`. To filter on an indexed numeric attribute (i.e., a numeric attribute annotated with `@amazon.datazone#sortable`), provide a filter using the `intValue` parameter. The filters parameter can also be used to run more advanced free-text searches that target specific attributes (attributes must be annotated with `@amazon.datazone#searchable` for free-text search). Create/update timestamp filtering is supported using the special `creationTime`/`lastUpdatedTime` attributes. Filter types can be mixed and matched to power complex queries.

 To find out whether an attribute has been annotated and indexed for a given search type, use the GetFormType API to retrieve the form containing the attribute.

## Request Syntax
<a name="API_SearchListings_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/listings/search HTTP/1.1
Content-type: application/json

{
   "additionalAttributes": [ "{{string}}" ],
   "aggregations": [
      {
         "attribute": "{{string}}",
         "displayValue": "{{string}}"
      }
   ],
   "filters": { ... },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "searchIn": [
      {
         "attribute": "{{string}}"
      }
   ],
   "searchText": "{{string}}",
   "sort": {
      "attribute": "{{string}}",
      "order": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_SearchListings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_SearchListings_RequestSyntax) **   <a name="datazone-SearchListings-request-uri-domainIdentifier"></a>
The identifier of the domain in which to search listings.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_SearchListings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [additionalAttributes](#API_SearchListings_RequestSyntax) **   <a name="datazone-SearchListings-request-additionalAttributes"></a>
Specifies additional attributes for the search.
Type: Array of strings
Valid Values: `FORMS | TIME_SERIES_DATA_POINT_FORMS | TEXT_MATCH_RATIONALE`
Required: No

 ** [aggregations](#API_SearchListings_RequestSyntax) **   <a name="datazone-SearchListings-request-aggregations"></a>
Enables you to specify one or more attributes to compute and return counts grouped by field values.
Type: Array of [AggregationListItem](API_AggregationListItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [filters](#API_SearchListings_RequestSyntax) **   <a name="datazone-SearchListings-request-filters"></a>
Specifies the filters for the search of listings.
Type: [FilterClause](API_FilterClause.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [maxResults](#API_SearchListings_RequestSyntax) **   <a name="datazone-SearchListings-request-maxResults"></a>
The maximum number of results to return in a single call to `SearchListings`. When the number of results to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `SearchListings` to list the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_SearchListings_RequestSyntax) **   <a name="datazone-SearchListings-request-nextToken"></a>
When the number of results is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of results, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `SearchListings` to list the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** [searchIn](#API_SearchListings_RequestSyntax) **   <a name="datazone-SearchListings-request-searchIn"></a>
The details of the search.
Type: Array of [SearchInItem](API_SearchInItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [searchText](#API_SearchListings_RequestSyntax) **   <a name="datazone-SearchListings-request-searchText"></a>
Specifies the text for which to search.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** [sort](#API_SearchListings_RequestSyntax) **   <a name="datazone-SearchListings-request-sort"></a>
Specifies the way for sorting the search results.
Type: [SearchSort](API_SearchSort.md) object
Required: No

## Response Syntax
<a name="API_SearchListings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "aggregates": [
      {
         "attribute": "string",
         "displayValue": "string",
         "items": [
            {
               "count": number,
               "displayValue": "string",
               "value": "string"
            }
         ]
      }
   ],
   "items": [
      { ... }
   ],
   "nextToken": "string",
   "totalMatchCount": number
}
```

## Response Elements
<a name="API_SearchListings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aggregates](#API_SearchListings_ResponseSyntax) **   <a name="datazone-SearchListings-response-aggregates"></a>
Contains computed counts grouped by field values based on the requested aggregation attributes for the matching listings.
Type: Array of [AggregationOutput](API_AggregationOutput.md) objects

 ** [items](#API_SearchListings_ResponseSyntax) **   <a name="datazone-SearchListings-response-items"></a>
The results of the `SearchListings` action.
Type: Array of [SearchResultItem](API_SearchResultItem.md) objects

 ** [nextToken](#API_SearchListings_ResponseSyntax) **   <a name="datazone-SearchListings-response-nextToken"></a>
When the number of results is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of results, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `SearchListings` to list the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [totalMatchCount](#API_SearchListings_ResponseSyntax) **   <a name="datazone-SearchListings-response-totalMatchCount"></a>
Total number of search results.
Type: Integer

## Errors
<a name="API_SearchListings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## Examples
<a name="API_SearchListings_Examples"></a>

### Example
<a name="API_SearchListings_Example_1"></a>

This example illustrates a lexical search.

#### Sample Request
<a name="API_SearchListings_Example_1_Request"></a>

```
aws datazone search-listings \
--domain-identifier "dzd_4q2el0k35ngqa8" \
--search-in '[{"attribute":"DataProductMetadataForm.name"}]' \
--search-text "\"car\"" \
--additional-attributes '["FORMS"]'
```

#### Sample Response
<a name="API_SearchListings_Example_1_Response"></a>

```
{
    "items": [
        {
            "assetListing": {
                "additionalAttributes": {
                    "forms": "{\"S3ObjectCollectionForm\":{\"bucketArn\":\"arn:aws:s3:::bucket/prefix\"},\"DataProductMetadataForm\":{\"name\":\"car\"}}"
                },
                "createdAt": "2025-08-28T21:41:17.026000+00:00",
                "entityId": "asl5ff7g6psoi8",
                "entityRevision": "4",
                "entityType": "S3ObjectCollectionAssetType",
                "glossaryTerms": [],
                "listingCreatedBy": "f697efa1-8b40-41c1-b1ef-977412f9d3d4",
                "listingId": "3tgx25pz22pic0",
                "listingRevision": "6",
                "listingUpdatedBy": "f697efa1-8b40-41c1-b1ef-977412f9d3d4",
                "name": "test",
                "owningProjectId": "4mo2oiauaqbrtc"
            }
        }
    ],
    "totalMatchCount": 1
}
```

### Example
<a name="API_SearchListings_Example_2"></a>

This example illustrates the filtering capabilities of the SearchListings APIs. Note: `__DataZoneGlossaryTerms` is a special keyword for getting all aggregated glossary terms across assets, custom metadata forms and columns.

#### Sample Request
<a name="API_SearchListings_Example_2_Request"></a>

```
aws datazone search-listings \
    --domain-identifier "dzd_4q2el0k35ngqa8" \
    --filters '{ "or": [
        { "filter": { "attribute": "__DataZoneGlossaryTerms", "value": "cxjyge917oaaa8" } },
        { "filter": { "attribute": "__DataZoneGlossaryTerms", "value": "46i8vpwe0s0t9j" } }
    ] }'
```

#### Sample Response
<a name="API_SearchListings_Example_2_Response"></a>

```
{
    "items": [
        {
            "assetListing": {
                "createdAt": "2025-09-05T16:53:55.563000+00:00",
                "entityId": "dgutcpgqbkbcsw",
                "entityRevision": "2",
                "entityType": "S3ObjectCollectionAssetType",
                "glossaryTerms": [
                    {
                        "name": "artist"
                    }
                ],
                "listingCreatedBy": "f697efa1-8b40-41c1-b1ef-977412f9d3d4",
                "listingId": "anj2uue0h4qd1s",
                "listingRevision": "2",
                "listingUpdatedBy": "f697efa1-8b40-41c1-b1ef-977412f9d3d4",
                "name": "blab",
                "owningProjectId": "4mo2oiauaqbrtc"
            }
        }
    ],
    "totalMatchCount": 1
}
```

### Example
<a name="API_SearchListings_Example_3"></a>

This example illustrates the numeric filtering capabilities of the SearchListing API. In this case, only listings which have an attribute value between the specified filter values will be returned. Only numeric attributes annotated with `@amazon.datazone#sortable` may be used for numeric filtering.

#### Sample Request
<a name="API_SearchListings_Example_3_Request"></a>

```
aws datazone search-listings \
    --domain-identifier "dzd_4q2el0k35ngqa8" \
    --filters '{ "and": [
        { "filter": { "attribute": "MyCustomForm.numericAttribute", "intValue": 5, "operator": "LT" } },
        { "filter": { "attribute": "MyCustomForm.numericAttribute", "intValue": 2, "operator": "GT" } }
    ] }'
```

### Example
<a name="API_SearchListings_Example_4"></a>

This example illustrates the advanced free-text search capabilities of the SearchListing API via filter clauses. In this example, only listings that match the respective search clauses in both attributes will be returned. Only string attributes annotated with `@amazon.datazone#searchable` may be used for free-text search.

#### Sample Request
<a name="API_SearchListings_Example_4_Request"></a>

```
aws datazone search-listings \
    --domain-identifier "dzd_4q2el0k35ngqa8" \
    --filters '{ "and": [
        { "filter": { "attribute": "MyCustomForm.attr1", "value": "rat", "operator": "TEXT_SEARCH" } },
        { "filter": { "attribute": "MyCustomForm.attr2", "value": "reproductive study", "operator": "TEXT_SEARCH" } }
    ] }'
```

### Example
<a name="API_SearchListings_Example_5"></a>

This example illustrates timestamp filtering using the SearchListing API. In this example, only listings that have been updated since the provided epoch ms timestamp are returned. Currently, only `creationTime`/`lastUpdatedTime` attributes are supported for timestamp filtering.

#### Sample Request
<a name="API_SearchListings_Example_5_Request"></a>

```
aws datazone search-listings \
    --domain-identifier "dzd_4q2el0k35ngqa8" \
    --filters '{ "filter": { "attribute": "lastUpdatedAt", "intValue": 1768437337867, "operator": "GE" } }'
```

## See Also
<a name="API_SearchListings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/SearchListings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/SearchListings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SearchListings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/SearchListings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SearchListings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/SearchListings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/SearchListings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/SearchListings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/SearchListings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SearchListings)
