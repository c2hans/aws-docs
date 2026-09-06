---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetAssetType.html
---

# GetAssetType
<a name="API_GetAssetType"></a>

Gets an Amazon DataZone asset type.

Asset types define the categories and characteristics of different kinds of data assets within Amazon DataZone.. They determine what metadata fields are required, what operations are possible, and how the asset integrates with other AWS services. Asset types can range from built-in types like Amazon S3 buckets and AWS Glue tables to custom types defined for specific organizational needs. Understanding asset types is crucial for properly organizing and managing different kinds of data resources.

Prerequisites:
+ The asset type with identifier must exist in the domain. ResourceNotFoundException.
+ You must have the GetAssetType permission.
+ Ensure the domain-identifier value is correct and accessible.

## Request Syntax
<a name="API_GetAssetType_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/asset-types/{{identifier}}?revision={{revision}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAssetType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetAssetType_RequestSyntax) **   <a name="datazone-GetAssetType-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the asset type exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetAssetType_RequestSyntax) **   <a name="datazone-GetAssetType-request-uri-identifier"></a>
The ID of the asset type.
Length Constraints: Minimum length of 1. Maximum length of 513.
Pattern: `(?!\.)[\w\.]*\w`
Required: Yes

 ** [revision](#API_GetAssetType_RequestSyntax) **   <a name="datazone-GetAssetType-request-uri-revision"></a>
The revision of the asset type.
Length Constraints: Minimum length of 1. Maximum length of 64.

## Request Body
<a name="API_GetAssetType_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAssetType_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetAssetType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetAssetType_ResponseSyntax) **   <a name="datazone-GetAssetType-response-createdAt"></a>
The timestamp of when the asset type was created.
Type: Timestamp

 ** [createdBy](#API_GetAssetType_ResponseSyntax) **   <a name="datazone-GetAssetType-response-createdBy"></a>
The Amazon DataZone user who created the asset type.
Type: String

 ** [description](#API_GetAssetType_ResponseSyntax) **   <a name="datazone-GetAssetType-response-description"></a>
The description of the asset type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_GetAssetType_ResponseSyntax) **   <a name="datazone-GetAssetType-response-domainId"></a>
The ID of the Amazon DataZone domain in which the asset type exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [formsOutput](#API_GetAssetType_ResponseSyntax) **   <a name="datazone-GetAssetType-response-formsOutput"></a>
The metadata forms attached to the asset type.
Type: String to [FormEntryOutput](API_FormEntryOutput.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*`

 ** [name](#API_GetAssetType_ResponseSyntax) **   <a name="datazone-GetAssetType-response-name"></a>
The name of the asset type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\.]*.*`

 ** [originDomainId](#API_GetAssetType_ResponseSyntax) **   <a name="datazone-GetAssetType-response-originDomainId"></a>
The ID of the Amazon DataZone domain in which the asset type was originally created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [originProjectId](#API_GetAssetType_ResponseSyntax) **   <a name="datazone-GetAssetType-response-originProjectId"></a>
The ID of the Amazon DataZone project in which the asset type was originally created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [owningProjectId](#API_GetAssetType_ResponseSyntax) **   <a name="datazone-GetAssetType-response-owningProjectId"></a>
The ID of the Amazon DataZone project that owns the asset type.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [revision](#API_GetAssetType_ResponseSyntax) **   <a name="datazone-GetAssetType-response-revision"></a>
The revision of the asset type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [updatedAt](#API_GetAssetType_ResponseSyntax) **   <a name="datazone-GetAssetType-response-updatedAt"></a>
The timestamp of when the asset type was updated.
Type: Timestamp

 ** [updatedBy](#API_GetAssetType_ResponseSyntax) **   <a name="datazone-GetAssetType-response-updatedBy"></a>
The Amazon DataZone user that updated the asset type.
Type: String

## Errors
<a name="API_GetAssetType_Errors"></a>

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
<a name="API_GetAssetType_Examples"></a>

### Example
<a name="API_GetAssetType_Example_1"></a>

This example illustrates one usage of GetAssetType.

#### Sample Request
<a name="API_GetAssetType_Example_1_Request"></a>

```
aws datazone get-asset-type \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "customerAnalyticsType"
```

#### Sample Response
<a name="API_GetAssetType_Example_1_Response"></a>

```
{
    "createdAt": 1752576607.833,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "formsOutput": {
        "AssetCommonDetailsForm": {
            "required": false,
            "typeName": "amazon.datazone.AssetCommonDetailsFormType",
            "typeRevision": "6"
        }
    },
    "name": "customerAnalyticsType",
    "owningProjectId": "prj7nx82mkl",
    "revision": "1",
    "updatedAt": 1752576607.833,
    "updatedBy": "usr7nx82mkl"
}
```

### Example
<a name="API_GetAssetType_Example_2"></a>

Failure case - missing required parameter: `--identifier`

#### Sample Request
<a name="API_GetAssetType_Example_2_Request"></a>

```
aws datazone get-asset-type \
--domain-identifier "dzd_53ielnpxktdilj"
```

#### Sample Response
<a name="API_GetAssetType_Example_2_Response"></a>

```
aws: error: the following arguments are required: —identifier
```

## See Also
<a name="API_GetAssetType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetAssetType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetAssetType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetAssetType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetAssetType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetAssetType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetAssetType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetAssetType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetAssetType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetAssetType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetAssetType)
