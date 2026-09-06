---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ListChangeSets.html
---

# ListChangeSets
<a name="API_ListChangeSets"></a>

Returns the list of change sets owned by the account being used to make the call. You can filter this list by providing any combination of `entityId`, `ChangeSetName`, and status. If you provide more than one filter, the API operation applies a logical AND between the filters.

You can describe a change during the 60-day request history retention period for API calls.

## Request Syntax
<a name="API_ListChangeSets_RequestSyntax"></a>

```
POST /ListChangeSets HTTP/1.1
Content-type: application/json

{
   "Catalog": "{{string}}",
   "FilterList": [
      {
         "Name": "{{string}}",
         "ValueList": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Sort": {
      "SortBy": "{{string}}",
      "SortOrder": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListChangeSets_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListChangeSets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Catalog](#API_ListChangeSets_RequestSyntax) **   <a name="AWSMarketplaceService-ListChangeSets-request-Catalog"></a>
The catalog related to the request. Fixed value: `AWSMarketplace`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z]+$`
Required: Yes

 ** [FilterList](#API_ListChangeSets_RequestSyntax) **   <a name="AWSMarketplaceService-ListChangeSets-request-FilterList"></a>
An array of filter objects.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Required: No

 ** [MaxResults](#API_ListChangeSets_RequestSyntax) **   <a name="AWSMarketplaceService-ListChangeSets-request-MaxResults"></a>
The maximum number of results returned by a single call. This value must be provided in the next call to retrieve the next set of results. By default, this value is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** [NextToken](#API_ListChangeSets_RequestSyntax) **   <a name="AWSMarketplaceService-ListChangeSets-request-NextToken"></a>
The token value retrieved from a previous call to access the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^[\w+=.:@\-\/]+$`
Required: No

 ** [Sort](#API_ListChangeSets_RequestSyntax) **   <a name="AWSMarketplaceService-ListChangeSets-request-Sort"></a>
An object that contains two attributes, `SortBy` and `SortOrder`.
Type: [Sort](API_Sort.md) object
Required: No

## Response Syntax
<a name="API_ListChangeSets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChangeSetSummaryList": [
      {
         "ChangeSetArn": "string",
         "ChangeSetId": "string",
         "ChangeSetName": "string",
         "EndTime": "string",
         "EntityIdList": [ "string" ],
         "FailureCode": "string",
         "StartTime": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListChangeSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeSetSummaryList](#API_ListChangeSets_ResponseSyntax) **   <a name="AWSMarketplaceService-ListChangeSets-response-ChangeSetSummaryList"></a>
 Array of `ChangeSetSummaryListItem` objects.
Type: Array of [ChangeSetSummaryListItem](API_ChangeSetSummaryListItem.md) objects

 ** [NextToken](#API_ListChangeSets_ResponseSyntax) **   <a name="AWSMarketplaceService-ListChangeSets-response-NextToken"></a>
The value of the next token, if it exists. Null if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^[\w+=.:@\-\/]+$`

## Errors
<a name="API_ListChangeSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP status code: 403
HTTP Status Code: 403

 ** InternalServiceException **
There was an internal service exception.
HTTP status code: 500
HTTP Status Code: 500

 ** ThrottlingException **
Too many requests.
HTTP status code: 429
HTTP Status Code: 429

 ** ValidationException **
An error occurred during validation.
HTTP status code: 422
HTTP Status Code: 422

## See Also
<a name="API_ListChangeSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-catalog-2018-09-17/ListChangeSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-catalog-2018-09-17/ListChangeSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ListChangeSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-catalog-2018-09-17/ListChangeSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ListChangeSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-catalog-2018-09-17/ListChangeSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-catalog-2018-09-17/ListChangeSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-catalog-2018-09-17/ListChangeSets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/ListChangeSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ListChangeSets)
