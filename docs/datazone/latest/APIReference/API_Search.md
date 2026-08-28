---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_Search.html
---

# Search
<a name="API_Search"></a>

Searches for assets in Amazon DataZone.

Search in Amazon DataZone is a powerful capability that enables users to discover and explore data assets, glossary terms, and data products across their organization. It provides both basic and advanced search functionality, allowing users to find resources based on names, descriptions, metadata, and other attributes. Search can be scoped to specific types of resources (like assets, glossary terms, or data products) and can be filtered using various criteria such as creation date, owner, or status. The search functionality is essential for making the wealth of data resources in an organization discoverable and usable, helping users find the right data for their needs quickly and efficiently.

Many search commands in Amazon DataZone are paginated, including `search` and `search-types`. When the result set is large, Amazon DataZone returns a `nextToken` in the response. This token can be used to retrieve the next page of results.

Prerequisites:
+ The --domain-identifier must refer to an existing Amazon DataZone domain.
+ --search-scope must be one of: ASSET, GLOSSARY\_TERM, DATA\_PRODUCT, or GLOSSARY.
+ The user must have search permissions in the specified domain.
+ If using --filters, ensure that the JSON is well-formed and that each filter includes valid attribute and value keys.
+ For paginated results, be prepared to use --next-token to fetch additional pages.

To run a standard free-text search, the `searchText` parameter must be supplied. By default, all searchable fields are indexed for semantic search and will return semantic matches for SearchListings queries. To prevent semantic search indexing for a custom form attribute, see the [CreateFormType API documentation](https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateFormType.html). To run a lexical search query, enclose the query with double quotes (""). This will disable semantic search even for fields that have semantic search enabled and will only return results that contain the keywords wrapped by double quotes (order of tokens in the query is not enforced). Free-text search is supported for all attributes annotated with @amazon.datazone\#searchable.

To run a filtered search, provide filter clause using the `filters` parameter. To filter on glossary terms, use the special attribute `__DataZoneGlossaryTerms`. To filter on an indexed numeric attribute (i.e., a numeric attribute annotated with `@amazon.datazone#sortable`), provide a filter using the `intValue` parameter. The filters parameter can also be used to run more advanced free-text searches that target specific attributes (attributes must be annotated with `@amazon.datazone#searchable` for free-text search). Create/update timestamp filtering is supported using the special `creationTime`/`lastUpdatedTime` attributes. Filter types can be mixed and matched to power complex queries.

 To find out whether an attribute has been annotated and indexed for a given search type, use the GetFormType API to retrieve the form containing the attribute.

## Request Syntax
<a name="API_Search_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/search HTTP/1.1
Content-type: application/json

{
   "additionalAttributes": [ "{{string}}" ],
   "filters": { ... },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "owningProjectIdentifier": "{{string}}",
   "searchIn": [
      {
         "attribute": "{{string}}"
      }
   ],
   "searchScope": "{{string}}",
   "searchText": "{{string}}",
   "sort": {
      "attribute": "{{string}}",
      "order": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_Search_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_Search_RequestSyntax) **   <a name="datazone-Search-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_Search_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [additionalAttributes](#API_Search_RequestSyntax) **   <a name="datazone-Search-request-additionalAttributes"></a>
Specifies additional attributes for the `Search` action.
Type: Array of strings
Valid Values: `FORMS | TIME_SERIES_DATA_POINT_FORMS | TEXT_MATCH_RATIONALE`
Required: No

 ** [filters](#API_Search_RequestSyntax) **   <a name="datazone-Search-request-filters"></a>
Specifies the search filters.
Type: [FilterClause](API_FilterClause.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [maxResults](#API_Search_RequestSyntax) **   <a name="datazone-Search-request-maxResults"></a>
The maximum number of results to return in a single call to `Search`. When the number of results to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `Search` to list the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_Search_RequestSyntax) **   <a name="datazone-Search-request-nextToken"></a>
When the number of results is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of results, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `Search` to list the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** [owningProjectIdentifier](#API_Search_RequestSyntax) **   <a name="datazone-Search-request-owningProjectIdentifier"></a>
The identifier of the owning project specified for the search.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** [searchIn](#API_Search_RequestSyntax) **   <a name="datazone-Search-request-searchIn"></a>
The details of the search.
Type: Array of [SearchInItem](API_SearchInItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [searchScope](#API_Search_RequestSyntax) **   <a name="datazone-Search-request-searchScope"></a>
The scope of the search.
Type: String
Valid Values: `ASSET | GLOSSARY | GLOSSARY_TERM | DATA_PRODUCT`
Required: Yes

 ** [searchText](#API_Search_RequestSyntax) **   <a name="datazone-Search-request-searchText"></a>
Specifies the text for which to search.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [sort](#API_Search_RequestSyntax) **   <a name="datazone-Search-request-sort"></a>
Specifies the way in which the search results are to be sorted.
Type: [SearchSort](API_SearchSort.md) object
Required: No

## Response Syntax
<a name="API_Search_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      { ... }
   ],
   "nextToken": "string",
   "totalMatchCount": number
}
```

## Response Elements
<a name="API_Search_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_Search_ResponseSyntax) **   <a name="datazone-Search-response-items"></a>
The results of the `Search` action.
Type: Array of [SearchInventoryResultItem](API_SearchInventoryResultItem.md) objects

 ** [nextToken](#API_Search_ResponseSyntax) **   <a name="datazone-Search-response-nextToken"></a>
When the number of results is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of results, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `Search` to list the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [totalMatchCount](#API_Search_ResponseSyntax) **   <a name="datazone-Search-response-totalMatchCount"></a>
Total number of search results.
Type: Integer

## Errors
<a name="API_Search_Errors"></a>

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
<a name="API_Search_Examples"></a>

### Example
<a name="API_Search_Example_1"></a>

This example illustrates one usage of Search.

#### Sample Request
<a name="API_Search_Example_1_Request"></a>

```
 aws datazone search \
--domain-identifier "dzd_53ielnpxktdilj" \
--search-scope "GLOSSARY_TERM"
```

#### Sample Response
<a name="API_Search_Example_1_Response"></a>

```
{
    "items": [
        {
            "glossaryTermItem": {
                "createdAt": 1752766662.222,
                "createdBy": "usr7nx82mkl",
                "domainId": "dzd_53ielnpxktdilj",
                "glossaryId": "gls8m3nqx2wkfp",
                "id": "trm9k4pq7xwnmh",
                "name": "CustomerLifetimeValue",
                "status": "ENABLED",
                "updatedAt": 1752766662.222,
                "updatedBy": "usr7nx82mkl"
            }
        },
        {
            "glossaryTermItem": {
                "createdAt": 1752674736.91,
                "createdBy": "usr7nx82mkl",
                "domainId": "dzd_53ielnpxktdilj",
                "glossaryId": "gls8m3nqx2wkfp",
                "id": "trm8p2mq3xvn5",
                "name": "ChurnRisk",
                "status": "ENABLED",
                "updatedAt": 1752766697.481,
                "updatedBy": "usr7nx82mkl"
            }
        }
    ],
    "totalMatchCount": 2
}
```

### Example
<a name="API_Search_Example_2"></a>

Failure case - missing parameter:

#### Sample Request
<a name="API_Search_Example_2_Request"></a>

```
aws datazone search \
--search-scope "GLOSSARY_TERM"
```

#### Sample Response
<a name="API_Search_Example_2_Response"></a>

```
aws: error: the following arguments are required: —domain-identifier
```

### Example
<a name="API_Search_Example_3"></a>

Failure case - invalid input:

#### Sample Request
<a name="API_Search_Example_3_Request"></a>

```
aws datazone search \
--domain-identifier "dzd_53ielnpxktdilj" \
--search-scope "INVALID_SCOPE"
```

#### Sample Response
<a name="API_Search_Example_3_Response"></a>

```
An error occurred (ValidationException) when calling the Search operation: 1 validation error detected: Value at 'searchScope' failed to satisfy constraint: Member must satisfy enum value set: [GLOSSARY_TERM, ASSET, DATA_PRODUCT, GLOSSARY]
```

### Example
<a name="API_Search_Example_4"></a>

Failure case - invalid JSON:

#### Sample Request
<a name="API_Search_Example_4_Request"></a>

```
aws datazone search \
--domain-identifier "dzd_53ielnpxktdilj" \
--search-scope "GLOSSARY_TERM" \
--filters '[{attribute:"NAME",value:"Term"}]'
```

#### Sample Response
<a name="API_Search_Example_4_Response"></a>

```
Error parsing parameter '--filters': Invalid JSON:
[{attribute:"NAME",value:"Term"}]
```

### Example
<a name="API_Search_Example_5"></a>

This example illustrates a technical identifier search (assuming the `technicalField` attribute is indexed for TECHNICAL search). For more information, see [https://aws.amazon.com/blogs/big-data/streamline-data-discovery-with-precise-technical-identifier-search-in-amazon-sagemaker-unified-studio/](https://aws.amazon.com/blogs/big-data/streamline-data-discovery-with-precise-technical-identifier-search-in-amazon-sagemaker-unified-studio/).

#### Sample Request
<a name="API_Search_Example_5_Request"></a>

```
aws datazone search \
--domain-identifier "dzd_4q2el0k35ngqa8" \
--search-in '[{"attribute":"name"}]' \
--search-text "\"blab\"" \
--search-scope "ASSET" \
--owning-project-identifier "4mo2oiauaqbrtc"
```

#### Sample Response
<a name="API_Search_Example_5_Response"></a>

```
{
    "items": [
        {
            "assetItem": {
                "createdAt": "2025-09-05T16:54:05.078000+00:00",
                "createdBy": "f697efa1-8b40-41c1-b1ef-977412f9d3d4",
                "firstRevisionCreatedAt": "2025-09-05T16:53:55.563000+00:00",
                "firstRevisionCreatedBy": "f697efa1-8b40-41c1-b1ef-977412f9d3d4",
                "glossaryTerms": [
                    "cxjyge917oaaa8"
                ],
                "identifier": "dgutcpgqbkbcsw",
                "name": "blab",
                "owningProjectId": "4mo2oiauaqbrtc",
                "typeIdentifier": "amazon.datazone.S3ObjectCollectionAssetType",
                "typeRevision": "14"
            }
        }
    ],
    "totalMatchCount": 1
}
```

### Example
<a name="API_Search_Example_6"></a>

This example illustrates the numeric filtering capabilities of the Search API. In this case only assets which have an attribute value between the specified filter values will be returned. Only numeric attributes annotated with `@amazon.datazone#sortable` may be used for numeric filtering.

#### Sample Request
<a name="API_Search_Example_6_Request"></a>

```
aws datazone search \
--domain-identifier "dzd_4q2el0k35ngqa8" \
--search-scope "ASSET" \
--owning-project-identifier "4mo2oiauaqbrtc" \
--filters '{ "and": [
        { "filter": { "attribute": "MyCustomForm.numericAttribute", "intValue": 5, "operator": "LT" } },
        { "filter": { "attribute": "MyCustomForm.numericAttribute", "intValue": 2, "operator": "GT" } }
    ] }'
```

### Example
<a name="API_Search_Example_7"></a>

This example illustrates the advanced free-text search capabilities of the Search API via filter clauses. In this example, only assets that match the respective search clauses in both attributes will be returned. Only string attributes annotated with `@amazon.datazone#searchable` may be used for free-text search.

#### Sample Request
<a name="API_Search_Example_7_Request"></a>

```
aws datazone search \
--domain-identifier "dzd_4q2el0k35ngqa8" \
--search-scope "ASSET" \
--owning-project-identifier "4mo2oiauaqbrtc" \
--filters '{ "and": [
        { "filter": { "attribute": "MyCustomForm.attr1", "value": "rat", "operator": "TEXT_SEARCH" } },
        { "filter": { "attribute": "MyCustomForm.attr2", "value": "reproductive study", "operator": "TEXT_SEARCH" } }
    ] }'
```

### Example
<a name="API_Search_Example_8"></a>

This example illustrates timestamp filtering using the Search API. In this example, only assets that have been updated since the provided epoch ms timestamp are returned. Currently, only `creationTime`/`lastUpdatedTime` attributes are supported for timestamp filtering.

#### Sample Request
<a name="API_Search_Example_8_Request"></a>

```
aws datazone search \
--domain-identifier "dzd_4q2el0k35ngqa8" \
--search-scope "ASSET" \
--owning-project-identifier "4mo2oiauaqbrtc" \
--filters '{ "filter": { "attribute": "lastUpdatedAt", "intValue": 1768437337867, "operator": "GE" } }'
```

## See Also
<a name="API_Search_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/Search)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/Search)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/Search)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/Search)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/Search)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/Search)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/Search)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/Search)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/Search)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/Search)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
