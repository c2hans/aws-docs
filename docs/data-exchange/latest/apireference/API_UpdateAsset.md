---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_UpdateAsset.html
---

# UpdateAsset
<a name="API_UpdateAsset"></a>

This operation updates an asset.

## Request Syntax
<a name="API_UpdateAsset_RequestSyntax"></a>

```
PATCH /v1/data-sets/{{DataSetId}}/revisions/{{RevisionId}}/assets/{{AssetId}} HTTP/1.1
Content-type: application/json

{
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAsset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssetId](#API_UpdateAsset_RequestSyntax) **   <a name="dataexchange-UpdateAsset-request-uri-AssetId"></a>
The unique identifier for an asset.
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** [DataSetId](#API_UpdateAsset_RequestSyntax) **   <a name="dataexchange-UpdateAsset-request-uri-DataSetId"></a>
The unique identifier for a data set.
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** [RevisionId](#API_UpdateAsset_RequestSyntax) **   <a name="dataexchange-UpdateAsset-request-uri-RevisionId"></a>
The unique identifier for a revision.
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

## Request Body
<a name="API_UpdateAsset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_UpdateAsset_RequestSyntax) **   <a name="dataexchange-UpdateAsset-request-Name"></a>
The name of the asset. When importing from Amazon S3, the Amazon S3 object key is used as the asset name. When exporting to Amazon S3, the asset name is used as default target Amazon S3 object key. When importing from Amazon API Gateway API, the API name is used as the asset name. When importing from Amazon Redshift, the datashare name is used as the asset name. When importing from AWS Lake Formation, the static values of "Database(s) included in the LF-tag policy" or "Table(s) included in LF-tag policy" are used as the name.
Type: String
Required: Yes

## Response Syntax
<a name="API_UpdateAsset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "AssetDetails": {
      "ApiGatewayApiAsset": {
         "ApiDescription": "string",
         "ApiEndpoint": "string",
         "ApiId": "string",
         "ApiKey": "string",
         "ApiName": "string",
         "ApiSpecificationDownloadUrl": "string",
         "ApiSpecificationDownloadUrlExpiresAt": "string",
         "ProtocolType": "string",
         "Stage": "string"
      },
      "LakeFormationDataPermissionAsset": {
         "LakeFormationDataPermissionDetails": {
            "LFTagPolicy": {
               "CatalogId": "string",
               "ResourceDetails": {
                  "Database": {
                     "Expression": [
                        {
                           "TagKey": "string",
                           "TagValues": [ "string" ]
                        }
                     ]
                  },
                  "Table": {
                     "Expression": [
                        {
                           "TagKey": "string",
                           "TagValues": [ "string" ]
                        }
                     ]
                  }
               },
               "ResourceType": "string"
            }
         },
         "LakeFormationDataPermissionType": "string",
         "Permissions": [ "string" ],
         "RoleArn": "string"
      },
      "RedshiftDataShareAsset": {
         "Arn": "string"
      },
      "S3DataAccessAsset": {
         "Bucket": "string",
         "KeyPrefixes": [ "string" ],
         "Keys": [ "string" ],
         "KmsKeysToGrant": [
            {
               "KmsKeyArn": "string"
            }
         ],
         "S3AccessPointAlias": "string",
         "S3AccessPointArn": "string"
      },
      "S3SnapshotAsset": {
         "Size": number
      }
   },
   "AssetType": "string",
   "CreatedAt": "string",
   "DataSetId": "string",
   "Id": "string",
   "Name": "string",
   "RevisionId": "string",
   "SourceId": "string",
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_UpdateAsset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateAsset_ResponseSyntax) **   <a name="dataexchange-UpdateAsset-response-Arn"></a>
The ARN for the asset.
Type: String

 ** [AssetDetails](#API_UpdateAsset_ResponseSyntax) **   <a name="dataexchange-UpdateAsset-response-AssetDetails"></a>
Details about the asset.
Type: [AssetDetails](API_AssetDetails.md) object

 ** [AssetType](#API_UpdateAsset_ResponseSyntax) **   <a name="dataexchange-UpdateAsset-response-AssetType"></a>
The type of asset that is added to a data set.
Type: String
Valid Values: `S3_SNAPSHOT | REDSHIFT_DATA_SHARE | API_GATEWAY_API | S3_DATA_ACCESS | LAKE_FORMATION_DATA_PERMISSION`

 ** [CreatedAt](#API_UpdateAsset_ResponseSyntax) **   <a name="dataexchange-UpdateAsset-response-CreatedAt"></a>
The date and time that the asset was created, in ISO 8601 format.
Type: Timestamp

 ** [DataSetId](#API_UpdateAsset_ResponseSyntax) **   <a name="dataexchange-UpdateAsset-response-DataSetId"></a>
The unique identifier for the data set associated with this asset.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [Id](#API_UpdateAsset_ResponseSyntax) **   <a name="dataexchange-UpdateAsset-response-Id"></a>
The unique identifier for the asset.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [Name](#API_UpdateAsset_ResponseSyntax) **   <a name="dataexchange-UpdateAsset-response-Name"></a>
The name of the asset. When importing from Amazon S3, the Amazon S3 object key is used as the asset name. When exporting to Amazon S3, the asset name is used as default target Amazon S3 object key. When importing from Amazon API Gateway API, the API name is used as the asset name. When importing from Amazon Redshift, the datashare name is used as the asset name. When importing from AWS Lake Formation, the static values of "Database(s) included in the LF-tag policy"- or "Table(s) included in LF-tag policy" are used as the asset name.
Type: String

 ** [RevisionId](#API_UpdateAsset_ResponseSyntax) **   <a name="dataexchange-UpdateAsset-response-RevisionId"></a>
The unique identifier for the revision associated with this asset.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [SourceId](#API_UpdateAsset_ResponseSyntax) **   <a name="dataexchange-UpdateAsset-response-SourceId"></a>
The asset ID of the owned asset corresponding to the entitled asset being viewed. This parameter is returned when an asset owner is viewing the entitled copy of its owned asset.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [UpdatedAt](#API_UpdateAsset_ResponseSyntax) **   <a name="dataexchange-UpdateAsset-response-UpdatedAt"></a>
The date and time that the asset was last updated, in ISO 8601 format.
Type: Timestamp

## Errors
<a name="API_UpdateAsset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the resource is denied.
 ** Message **
Access to the resource is denied.
HTTP Status Code: 403

 ** ConflictException **
The request couldn't be completed because it conflicted with the current state of the resource.
 ** Message **
The request couldn't be completed because it conflicted with the current state of the resource.
 ** ResourceId **
The unique identifier for the resource with the conflict.
 ** ResourceType **
The type of the resource with the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An exception occurred with the service.
 ** Message **
The message identifying the service exception that occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
 ** Message **
The resource couldn't be found.
 ** ResourceId **
The unique identifier for the resource that couldn't be found.
 ** ResourceType **
The type of resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** Message **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request was invalid.
 ** ExceptionCause **
The unique identifier for the resource that couldn't be found.
 ** Message **
The message that informs you about what was invalid about the request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/UpdateAsset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/UpdateAsset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/UpdateAsset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/UpdateAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/UpdateAsset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/UpdateAsset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/UpdateAsset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/UpdateAsset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/UpdateAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/UpdateAsset)
