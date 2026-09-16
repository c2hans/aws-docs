---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetAsset.html
---

# GetAsset
<a name="API_GetAsset"></a>

Gets an Amazon DataZone asset.

An asset is the fundamental building block in Amazon DataZone, representing any data resource that needs to be cataloged and managed. It can take many forms, from Amazon S3 buckets and database tables to dashboards and machine learning models. Each asset contains comprehensive metadata about the resource, including its location, schema, ownership, and lineage information. Assets are essential for organizing and managing data resources across an organization, making them discoverable and usable while maintaining proper governance.

Before using the Amazon DataZone GetAsset command, ensure the following prerequisites are met:
+ Domain identifier must exist and be valid
+ Asset identifier must exist
+ User must have the required permissions to perform the action

## Request Syntax
<a name="API_GetAsset_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/assets/{{identifier}}?revision={{revision}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAsset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetAsset_RequestSyntax) **   <a name="datazone-GetAsset-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain to which the asset belongs.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetAsset_RequestSyntax) **   <a name="datazone-GetAsset-request-uri-identifier"></a>
The ID of the Amazon DataZone asset.
This parameter supports either the value of `assetId` or `externalIdentifier` as input. If you are passing the value of `externalIdentifier`, you must prefix this value with `externalIdentifer%2F`.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [revision](#API_GetAsset_RequestSyntax) **   <a name="datazone-GetAsset-request-uri-revision"></a>
The revision of the Amazon DataZone asset.
Length Constraints: Minimum length of 1. Maximum length of 64.

## Request Body
<a name="API_GetAsset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAsset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
   "description": "string",
   "domainId": "string",
   "externalIdentifier": "string",
   "firstRevisionCreatedAt": number,
   "firstRevisionCreatedBy": "string",
   "formsOutput": [
      {
         "content": "string",
         "formName": "string",
         "typeName": "string",
         "typeRevision": "string"
      }
   ],
   "glossaryTerms": [ "string" ],
   "governedGlossaryTerms": [ "string" ],
   "id": "string",
   "latestTimeSeriesDataPointFormsOutput": [
      {
         "contentSummary": "string",
         "formName": "string",
         "id": "string",
         "timestamp": number,
         "typeIdentifier": "string",
         "typeRevision": "string"
      }
   ],
   "listing": {
      "listingId": "string",
      "listingStatus": "string"
   },
   "name": "string",
   "owningProjectId": "string",
   "readOnlyFormsOutput": [
      {
         "content": "string",
         "formName": "string",
         "typeName": "string",
         "typeRevision": "string"
      }
   ],
   "revision": "string",
   "typeIdentifier": "string",
   "typeRevision": "string"
}
```

## Response Elements
<a name="API_GetAsset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-createdAt"></a>
The timestamp of when the asset was created.
Type: Timestamp

 ** [createdBy](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-createdBy"></a>
The Amazon DataZone user who created the asset.
Type: String

 ** [description](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-description"></a>
The description of the Amazon DataZone asset.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-domainId"></a>
The ID of the Amazon DataZone domain to which the asset belongs.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [externalIdentifier](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-externalIdentifier"></a>
The external ID of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 600.

 ** [firstRevisionCreatedAt](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-firstRevisionCreatedAt"></a>
The timestamp of when the first revision of the asset was created.
Type: Timestamp

 ** [firstRevisionCreatedBy](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-firstRevisionCreatedBy"></a>
The Amazon DataZone user who created the first revision of the asset.
Type: String

 ** [formsOutput](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-formsOutput"></a>
The metadata forms attached to the asset.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [glossaryTerms](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-glossaryTerms"></a>
The business glossary terms attached to the asset.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [governedGlossaryTerms](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-governedGlossaryTerms"></a>
The restricted glossary terms attached to an asset.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-id"></a>
The ID of the asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [latestTimeSeriesDataPointFormsOutput](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-latestTimeSeriesDataPointFormsOutput"></a>
The latest data point that was imported into the time series form for the asset.
Type: Array of [TimeSeriesDataPointSummaryFormOutput](API_TimeSeriesDataPointSummaryFormOutput.md) objects

 ** [listing](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-listing"></a>
The listing of the asset.
Type: [AssetListingDetails](API_AssetListingDetails.md) object

 ** [name](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-name"></a>
The name of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [owningProjectId](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-owningProjectId"></a>
The ID of the project that owns the asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [readOnlyFormsOutput](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-readOnlyFormsOutput"></a>
The read-only metadata forms attached to the asset.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [revision](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-revision"></a>
The revision of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [typeIdentifier](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-typeIdentifier"></a>
The ID of the asset type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 513.
Pattern: `(?!\.)[\w\.]*\w`

 ** [typeRevision](#API_GetAsset_ResponseSyntax) **   <a name="datazone-GetAsset-response-typeRevision"></a>
The revision of the asset type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_GetAsset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

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
<a name="API_GetAsset_Examples"></a>

### Example
<a name="API_GetAsset_Example_1"></a>

Use the following command to retrieve an asset from Amazon DataZone:

#### Sample Request
<a name="API_GetAsset_Example_1_Request"></a>

```
aws datazone get-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "ast7k9mpq2xvn4w"
```

#### Sample Response
<a name="API_GetAsset_Example_1_Response"></a>

```
{
    "createdAt": 1752554243.917,
    "createdBy": "user_id_redacted",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1752554243.917,
    "firstRevisionCreatedBy": "user_id_redacted",
    "formsOutput": [{
        "content": "{\"bucketArn\":\"arn:aws:s3:::analytics-data-bucket\"}",
        "formName": "CustomerAnalyticsForm",
        "typeName": "amazon.datazone.S3ObjectCollectionFormType",
        "typeRevision": "7"
    }],
    "id": "ast7k9mpq2xvn4w",
    "latestTimeSeriesDataPointFormsOutput": [],
    "name": "CustomerAnalytics2023",
    "owningProjectId": "prj9vn4wxyz8k2m",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "amazon.datazone.S3ObjectCollectionAssetType",
    "typeRevision": "13"
}
```

### Example
<a name="API_GetAsset_Example_2"></a>

When the specified asset does not exist, the command will fail:

#### Sample Request
<a name="API_GetAsset_Example_2_Request"></a>

```
aws datazone get-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "astnonexistent2m4"
```

#### Sample Response
<a name="API_GetAsset_Example_2_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the GetAsset operation: The given Asset doesn't exist. Try creating Asset before accessing it.
```

### Example
<a name="API_GetAsset_Example_3"></a>

When a required parameter is missing, the command will fail:

#### Sample Request
<a name="API_GetAsset_Example_3_Request"></a>

```
aws datazone get-asset \
--domain-identifier "dzd_53ielnpxktdilj"
```

#### Sample Response
<a name="API_GetAsset_Example_3_Response"></a>

```
aws: error: the following arguments are required: —identifier
```

## See Also
<a name="API_GetAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetAsset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetAsset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetAsset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetAsset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetAsset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetAsset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetAsset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetAsset)
