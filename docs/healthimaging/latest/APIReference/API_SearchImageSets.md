---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_SearchImageSets.html
---

# SearchImageSets
<a name="API_SearchImageSets"></a>

Search image sets based on defined input attributes.

**Note**
 `SearchImageSets` accepts a single search query parameter and returns a paginated response of all image sets that have the matching criteria. All date range queries must be input as `(lowerBound, upperBound)`.
By default, `SearchImageSets` uses the `updatedAt` field for sorting in descending order from newest to oldest.

## Request Syntax
<a name="API_SearchImageSets_RequestSyntax"></a>

```
POST /datastore/{{datastoreId}}/searchImageSets?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "operator": "{{string}}",
         "values": [
            { ... }
         ]
      }
   ],
   "sort": {
      "sortField": "{{string}}",
      "sortOrder": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_SearchImageSets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datastoreId](#API_SearchImageSets_RequestSyntax) **   <a name="healthimaging-SearchImageSets-request-uri-datastoreId"></a>
The identifier of the data store where the image sets reside.
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** [maxResults](#API_SearchImageSets_RequestSyntax) **   <a name="healthimaging-SearchImageSets-request-uri-maxResults"></a>
The maximum number of results that can be returned in a search.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_SearchImageSets_RequestSyntax) **   <a name="healthimaging-SearchImageSets-request-uri-nextToken"></a>
The token used for pagination of results returned in the response. Use the token returned from the previous request to continue results where the previous request ended.
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `\p{ASCII}{0,8192}`

## Request Body
<a name="API_SearchImageSets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_SearchImageSets_RequestSyntax) **   <a name="healthimaging-SearchImageSets-request-filters"></a>
The filters for the search criteria.
Type: Array of [SearchFilter](API_SearchFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** [sort](#API_SearchImageSets_RequestSyntax) **   <a name="healthimaging-SearchImageSets-request-sort"></a>
The sort input for search criteria.
Type: [Sort](API_Sort.md) object
Required: No

## Response Syntax
<a name="API_SearchImageSets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "imageSetsMetadataSummaries": [
      {
         "createdAt": number,
         "DICOMTags": {
            "DICOMAccessionNumber": "string",
            "DICOMNumberOfStudyRelatedInstances": number,
            "DICOMNumberOfStudyRelatedSeries": number,
            "DICOMPatientBirthDate": "string",
            "DICOMPatientId": "string",
            "DICOMPatientName": "string",
            "DICOMPatientSex": "string",
            "DICOMSeriesBodyPart": "string",
            "DICOMSeriesInstanceUID": "string",
            "DICOMSeriesModality": "string",
            "DICOMSeriesNumber": number,
            "DICOMStudyDate": "string",
            "DICOMStudyDescription": "string",
            "DICOMStudyId": "string",
            "DICOMStudyInstanceUID": "string",
            "DICOMStudyTime": "string"
         },
         "imageSetId": "string",
         "isPrimary": boolean,
         "lastAccessedAt": number,
         "storageTier": "string",
         "updatedAt": number,
         "version": number
      }
   ],
   "nextToken": "string",
   "sort": {
      "sortField": "string",
      "sortOrder": "string"
   }
}
```

## Response Elements
<a name="API_SearchImageSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageSetsMetadataSummaries](#API_SearchImageSets_ResponseSyntax) **   <a name="healthimaging-SearchImageSets-response-imageSetsMetadataSummaries"></a>
The model containing the image set results.
Type: Array of [ImageSetsMetadataSummary](API_ImageSetsMetadataSummary.md) objects

 ** [nextToken](#API_SearchImageSets_ResponseSyntax) **   <a name="healthimaging-SearchImageSets-response-nextToken"></a>
The token for pagination results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `\p{ASCII}{0,8192}`

 ** [sort](#API_SearchImageSets_ResponseSyntax) **   <a name="healthimaging-SearchImageSets-response-sort"></a>
The sort order for image set search results.
Type: [Sort](API_Sort.md) object

## Errors
<a name="API_SearchImageSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during processing of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource which does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints set by the service.
HTTP Status Code: 400

## See Also
<a name="API_SearchImageSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/medical-imaging-2023-07-19/SearchImageSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/medical-imaging-2023-07-19/SearchImageSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/SearchImageSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/medical-imaging-2023-07-19/SearchImageSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/SearchImageSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/medical-imaging-2023-07-19/SearchImageSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/medical-imaging-2023-07-19/SearchImageSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/medical-imaging-2023-07-19/SearchImageSets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/medical-imaging-2023-07-19/SearchImageSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/SearchImageSets)
