---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ListEntities.html
---

# ListEntities
<a name="API_ListEntities"></a>

Provides the list of entities of a given type.

## Request Syntax
<a name="API_ListEntities_RequestSyntax"></a>

```
POST /ListEntities HTTP/1.1
Content-type: application/json

{
   "Catalog": "{{string}}",
   "EntityType": "{{string}}",
   "EntityTypeFilters": { ... },
   "EntityTypeSort": { ... },
   "FilterList": [
      {
         "Name": "{{string}}",
         "ValueList": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OwnershipType": "{{string}}",
   "Sort": {
      "SortBy": "{{string}}",
      "SortOrder": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListEntities_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListEntities_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Catalog](#API_ListEntities_RequestSyntax) **   <a name="AWSMarketplaceService-ListEntities-request-Catalog"></a>
The catalog related to the request. Fixed value: `AWSMarketplace`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z]+$`
Required: Yes

 ** [EntityType](#API_ListEntities_RequestSyntax) **   <a name="AWSMarketplaceService-ListEntities-request-EntityType"></a>
The type of entities to retrieve. Valid values are: `AmiProduct`, `ContainerProduct`, `DataProduct`, `SaaSProduct`, `ProcurementPolicy`, `Experience`, `Audience`, `BrandingSettings`, `Offer`, `OfferSet`, `Seller`, `ResaleAuthorization`, `Solution`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z]+$`
Required: Yes

 ** [EntityTypeFilters](#API_ListEntities_RequestSyntax) **   <a name="AWSMarketplaceService-ListEntities-request-EntityTypeFilters"></a>
A Union object containing filter shapes for all `EntityType`s. Each `EntityTypeFilter` shape will have filters applicable for that `EntityType` that can be used to search or filter entities.
Type: [EntityTypeFilters](API_EntityTypeFilters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [EntityTypeSort](#API_ListEntities_RequestSyntax) **   <a name="AWSMarketplaceService-ListEntities-request-EntityTypeSort"></a>
A Union object containing `Sort` shapes for all `EntityType`s. Each `EntityTypeSort` shape will have `SortBy` and `SortOrder` applicable for fields on that `EntityType`. This can be used to sort the results of the filter query.
Type: [EntityTypeSort](API_EntityTypeSort.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [FilterList](#API_ListEntities_RequestSyntax) **   <a name="AWSMarketplaceService-ListEntities-request-FilterList"></a>
An array of filter objects. Each filter object contains two attributes, `filterName` and `filterValues`.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Required: No

 ** [MaxResults](#API_ListEntities_RequestSyntax) **   <a name="AWSMarketplaceService-ListEntities-request-MaxResults"></a>
Specifies the upper limit of the elements on a single page. If a value isn't provided, the default value is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListEntities_RequestSyntax) **   <a name="AWSMarketplaceService-ListEntities-request-NextToken"></a>
The value of the next token, if it exists. Null if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[\w+=.:@\-\/]$`
Required: No

 ** [OwnershipType](#API_ListEntities_RequestSyntax) **   <a name="AWSMarketplaceService-ListEntities-request-OwnershipType"></a>
Filters the returned set of entities based on their owner. The default is `SELF`. To list entities shared with you through AWS Resource Access Manager (AWS RAM), set to `SHARED`. Entities shared through the AWS Marketplace Catalog API `PutResourcePolicy` operation can't be discovered through the `SHARED` parameter.
Type: String
Valid Values: `SELF | SHARED`
Required: No

 ** [Sort](#API_ListEntities_RequestSyntax) **   <a name="AWSMarketplaceService-ListEntities-request-Sort"></a>
An object that contains two attributes, `SortBy` and `SortOrder`.
Type: [Sort](API_Sort.md) object
Required: No

## Response Syntax
<a name="API_ListEntities_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EntitySummaryList": [
      {
         "AmiProductSummary": {
            "ProductTitle": "string",
            "Visibility": "string"
         },
         "ContainerProductSummary": {
            "ProductTitle": "string",
            "Visibility": "string"
         },
         "DataProductSummary": {
            "ProductTitle": "string",
            "Visibility": "string"
         },
         "EntityArn": "string",
         "EntityId": "string",
         "EntityType": "string",
         "LastModifiedDate": "string",
         "MachineLearningProductSummary": {
            "ProductTitle": "string",
            "Visibility": "string"
         },
         "Name": "string",
         "OfferSetSummary": {
            "AssociatedOfferIds": [ "string" ],
            "Name": "string",
            "ReleaseDate": "string",
            "SolutionId": "string",
            "State": "string"
         },
         "OfferSummary": {
            "AvailabilityEndDate": "string",
            "BuyerAccounts": [ "string" ],
            "Name": "string",
            "OfferSetId": "string",
            "ProductId": "string",
            "ReleaseDate": "string",
            "ResaleAuthorizationId": "string",
            "State": "string",
            "Targeting": [ "string" ]
         },
         "ResaleAuthorizationSummary": {
            "AvailabilityEndDate": "string",
            "CreatedDate": "string",
            "ManufacturerAccountId": "string",
            "ManufacturerLegalName": "string",
            "Name": "string",
            "OfferExtendedStatus": "string",
            "ProductId": "string",
            "ProductName": "string",
            "ResellerAccountID": "string",
            "ResellerLegalName": "string",
            "Status": "string"
         },
         "SaaSProductSummary": {
            "ProductTitle": "string",
            "Visibility": "string"
         },
         "Visibility": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEntities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EntitySummaryList](#API_ListEntities_ResponseSyntax) **   <a name="AWSMarketplaceService-ListEntities-response-EntitySummaryList"></a>
Array of `EntitySummary` objects.
Type: Array of [EntitySummary](API_EntitySummary.md) objects

 ** [NextToken](#API_ListEntities_ResponseSyntax) **   <a name="AWSMarketplaceService-ListEntities-response-NextToken"></a>
The value of the next token if it exists. Null if there is no more result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[\w+=.:@\-\/]$`

## Errors
<a name="API_ListEntities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP status code: 403
HTTP Status Code: 403

 ** InternalServiceException **
There was an internal service exception.
HTTP status code: 500
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource wasn't found.
HTTP status code: 404
HTTP Status Code: 404

 ** ThrottlingException **
Too many requests.
HTTP status code: 429
HTTP Status Code: 429

 ** ValidationException **
An error occurred during validation.
HTTP status code: 422
HTTP Status Code: 422

## See Also
<a name="API_ListEntities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-catalog-2018-09-17/ListEntities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-catalog-2018-09-17/ListEntities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ListEntities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-catalog-2018-09-17/ListEntities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ListEntities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-catalog-2018-09-17/ListEntities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-catalog-2018-09-17/ListEntities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-catalog-2018-09-17/ListEntities)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/ListEntities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ListEntities)
