---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_PutAssetType.html
---

# PutAssetType
<a name="API_PutAssetType"></a>

Creates or updates an asset type in AWS Glue Data Catalog. An asset type defines the structure of assets by specifying which forms they include. If an asset type with the given name already exists, it is updated.

## Request Syntax
<a name="API_PutAssetType_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Forms": {
      "{{string}}" : {
         "FormTypeIdentifier": "{{string}}"
      }
   },
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_PutAssetType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_PutAssetType_RequestSyntax) **   <a name="Glue-PutAssetType-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Forms](#API_PutAssetType_RequestSyntax) **   <a name="Glue-PutAssetType-request-Forms"></a>
The forms that make up the asset type, keyed by form name. Each entry references the form type that defines the form's schema.
Type: String to [AssetTypeFormReference](API_AssetTypeFormReference.md) object map
Map Entries: Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*$`
Required: Yes

 ** [Name](#API_PutAssetType_RequestSyntax) **   <a name="Glue-PutAssetType-request-Name"></a>
The name of the asset type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*$`
Required: Yes

## Response Syntax
<a name="API_PutAssetType_ResponseSyntax"></a>

```
{
   "Forms": {
      "string" : {
         "FormTypeIdentifier": "string"
      }
   },
   "Id": "string",
   "Name": "string"
}
```

## Response Elements
<a name="API_PutAssetType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Forms](#API_PutAssetType_ResponseSyntax) **   <a name="Glue-PutAssetType-response-Forms"></a>
The forms that make up the asset type, keyed by form name.
Type: String to [AssetTypeFormReference](API_AssetTypeFormReference.md) object map
Map Entries: Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*$`

 ** [Id](#API_PutAssetType_ResponseSyntax) **   <a name="Glue-PutAssetType-response-Id"></a>
The identifier of the asset type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [Name](#API_PutAssetType_ResponseSyntax) **   <a name="Glue-PutAssetType-response-Name"></a>
The name of the asset type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*$`

## Errors
<a name="API_PutAssetType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
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
<a name="API_PutAssetType_Examples"></a>

### Example
<a name="API_PutAssetType_Example_1"></a>

The following example creates an asset type that references a form type.

```
aws glue put-asset-type \
    --name DataSet \
    --forms '{"DataClassification":{"FormTypeIdentifier":"DataClassification"}}'

{
    "Id": "DataSet",
    "Name": "DataSet",
    "Forms": {
        "DataClassification": {
            "FormTypeIdentifier": "DataClassification"
        }
    }
}
```

## See Also
<a name="API_PutAssetType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/PutAssetType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/PutAssetType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/PutAssetType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/PutAssetType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/PutAssetType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/PutAssetType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/PutAssetType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/PutAssetType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/PutAssetType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/PutAssetType)
