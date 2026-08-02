---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateAssetType.html
---

# CreateAssetType
<a name="API_CreateAssetType"></a>

Creates a custom asset type.

Prerequisites:
+ The `formsInput` field is required, however, can be passed as empty (e.g. `-forms-input {})`.
+ You must have `CreateAssetType` permissions.
+ The domain-identifier and owning-project-identifier must be valid and active.
+ The name of the asset type must be unique within the domain — duplicate names will cause failure.
+ JSON input must be valid — incorrect formatting causes Invalid JSON errors.

## Request Syntax
<a name="API_CreateAssetType_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/asset-types HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "formsInput": {
      "{{string}}" : {
         "required": {{boolean}},
         "typeIdentifier": "{{string}}",
         "typeRevision": "{{string}}"
      }
   },
   "name": "{{string}}",
   "owningProjectIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAssetType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateAssetType_RequestSyntax) **   <a name="datazone-CreateAssetType-request-uri-domainIdentifier"></a>
The unique identifier of the Amazon DataZone domain where the custom asset type is being created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateAssetType_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateAssetType_RequestSyntax) **   <a name="datazone-CreateAssetType-request-description"></a>
The descripton of the custom asset type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [formsInput](#API_CreateAssetType_RequestSyntax) **   <a name="datazone-CreateAssetType-request-formsInput"></a>
The metadata forms that are to be attached to the custom asset type.
Type: String to [FormEntryInput](API_FormEntryInput.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*`
Required: Yes

 ** [name](#API_CreateAssetType_RequestSyntax) **   <a name="datazone-CreateAssetType-request-name"></a>
The name of the custom asset type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\.]*.*`
Required: Yes

 ** [owningProjectIdentifier](#API_CreateAssetType_RequestSyntax) **   <a name="datazone-CreateAssetType-request-owningProjectIdentifier"></a>
The identifier of the Amazon DataZone project that is to own the custom asset type.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Response Syntax
<a name="API_CreateAssetType_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
   "description": "string",
   "domainId": "string",
   "formsOutput": {
      "string" : {
         "required": boolean,
         "typeName": "string",
         "typeRevision": "string"
      }
   },
   "name": "string",
   "originDomainId": "string",
   "originProjectId": "string",
   "owningProjectId": "string",
   "revision": "string",
   "updatedAt": number,
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_CreateAssetType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateAssetType_ResponseSyntax) **   <a name="datazone-CreateAssetType-response-createdAt"></a>
The timestamp of when the asset type is to be created.
Type: Timestamp

 ** [createdBy](#API_CreateAssetType_ResponseSyntax) **   <a name="datazone-CreateAssetType-response-createdBy"></a>
The Amazon DataZone user who creates this custom asset type.
Type: String

 ** [description](#API_CreateAssetType_ResponseSyntax) **   <a name="datazone-CreateAssetType-response-description"></a>
The description of the custom asset type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_CreateAssetType_ResponseSyntax) **   <a name="datazone-CreateAssetType-response-domainId"></a>
The ID of the Amazon DataZone domain in which the asset type was created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [formsOutput](#API_CreateAssetType_ResponseSyntax) **   <a name="datazone-CreateAssetType-response-formsOutput"></a>
The metadata forms that are attached to the asset type.
Type: String to [FormEntryOutput](API_FormEntryOutput.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*`

 ** [name](#API_CreateAssetType_ResponseSyntax) **   <a name="datazone-CreateAssetType-response-name"></a>
The name of the asset type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\.]*.*`

 ** [originDomainId](#API_CreateAssetType_ResponseSyntax) **   <a name="datazone-CreateAssetType-response-originDomainId"></a>
The ID of the Amazon DataZone domain where the asset type was originally created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [originProjectId](#API_CreateAssetType_ResponseSyntax) **   <a name="datazone-CreateAssetType-response-originProjectId"></a>
The ID of the Amazon DataZone project where the asset type was originally created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [owningProjectId](#API_CreateAssetType_ResponseSyntax) **   <a name="datazone-CreateAssetType-response-owningProjectId"></a>
The ID of the Amazon DataZone project that currently owns this asset type.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [revision](#API_CreateAssetType_ResponseSyntax) **   <a name="datazone-CreateAssetType-response-revision"></a>
The revision of the custom asset type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [updatedAt](#API_CreateAssetType_ResponseSyntax) **   <a name="datazone-CreateAssetType-response-updatedAt"></a>
The timestamp of when the custom type was created.
Type: Timestamp

 ** [updatedBy](#API_CreateAssetType_ResponseSyntax) **   <a name="datazone-CreateAssetType-response-updatedBy"></a>
The Amazon DataZone user that created the custom asset type.
Type: String

## Errors
<a name="API_CreateAssetType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

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
<a name="API_CreateAssetType_Examples"></a>

### Example
<a name="API_CreateAssetType_Example_1"></a>

This example illustrates one usage of CreateAssetType.

#### Sample Request
<a name="API_CreateAssetType_Example_1_Request"></a>

```
aws datazone create-asset-type \ --domain-identifier "dzd_53ielnpxktdilj" \ --owning-project-identifier "prj9vn4wxyz8k2m" \ --name "DataProductAssetType" \ --forms-input '{ "DataProductMetadataForm": { "required": true, "typeIdentifier": "DataProductMetadataForm", "typeRevision": "1" } }'
```

#### Sample Response
<a name="API_CreateAssetType_Example_1_Response"></a>

```
{
    "description": "Asset type for Data Product using DataProductMetadataForm",
    "domainId": "dzd_53ielnpxktdilj",
    "formsOutput": {
        "AssetCommonDetailsForm": {
            "required": false,
            "typeName": "amazon.datazone.AssetCommonDetailsFormType",
            "typeRevision": "6"
        },
        "DataProductMetadataForm": {
            "required": true,
            "typeName": "DataProductMetadataForm",
            "typeRevision": "1"
        }
    },
    "name": "DataProductAssetType",
    "revision": "1"
}
```

### Example
<a name="API_CreateAssetType_Example_2"></a>

Failure case - missing `--forms-input`:

#### Sample Request
<a name="API_CreateAssetType_Example_2_Request"></a>

```
aws datazone create-asset-type \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "CustomerDataAssetType"
```

#### Sample Response
<a name="API_CreateAssetType_Example_2_Response"></a>

```
aws: error: the following arguments are required: —forms-input
```

### Example
<a name="API_CreateAssetType_Example_3"></a>

Failure case - invalid `typeIdentifier`:

#### Sample Request
<a name="API_CreateAssetType_Example_3_Request"></a>

```
aws datazone create-asset-type \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "CustomerDataAssetType" \
--forms-input '{
    "CustomerProfileForm": {
        "required": true,
        "typeIdentifier": "NonExistentFormType",
        "typeRevision": "1"
    }
}'
```

#### Sample Response
<a name="API_CreateAssetType_Example_3_Response"></a>

```
An error occurred (ValidationException) when calling the CreateAssetType operation: {"message":"Object type Form#dzd_53ielnpxktdilj#NonExistentFormType with version 1 not found"}
```

### Example
<a name="API_CreateAssetType_Example_4"></a>

Failure case - invalid JSON:

#### Sample Request
<a name="API_CreateAssetType_Example_4_Request"></a>

```
aws datazone create-asset-type \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "CustomerDataAssetType" \
--forms-input '{"CustomerProfileForm": {"required": true, "typeIdentifier": "CustomerProfileFormType", "typeRevision": 1'
```

#### Sample Response
<a name="API_CreateAssetType_Example_4_Response"></a>

```
Error parsing parameter '--forms-input': Invalid JSON: Expecting ',' delimiter: line 1 column 77 (char 76)
JSON received: {"CustomerProfileForm": {"required": true, "typeIdentifier": "CustomerProfileFormType", "typeRevision": 1
```

## See Also
<a name="API_CreateAssetType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateAssetType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateAssetType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateAssetType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateAssetType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateAssetType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateAssetType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateAssetType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateAssetType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateAssetType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateAssetType)
