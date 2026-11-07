---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_PutAsset.html
---

# PutAsset
<a name="API_PutAsset"></a>

Creates or updates an asset in AWS Glue Data Catalog. If the asset already exists, this operation updates it; otherwise, a new asset is created.

## Request Syntax
<a name="API_PutAsset_RequestSyntax"></a>

```
{
   "AssetTypeId": "{{string}}",
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "Forms": {
      "{{string}}" : {
         "Content": "{{string}}",
         "FormTypeId": "{{string}}"
      }
   },
   "Identifier": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_PutAsset_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssetTypeId](#API_PutAsset_RequestSyntax) **   <a name="Glue-PutAsset-request-AssetTypeId"></a>
The identifier of the asset type for the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [ClientToken](#API_PutAsset_RequestSyntax) **   <a name="Glue-PutAsset-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Description](#API_PutAsset_RequestSyntax) **   <a name="Glue-PutAsset-request-Description"></a>
The description of the asset.
Type: String
Required: No

 ** [Forms](#API_PutAsset_RequestSyntax) **   <a name="Glue-PutAsset-request-Forms"></a>
The forms to set on the asset, keyed by form name. Each entry specifies the form type and its JSON content.
Type: String to [AssetFormEntry](API_AssetFormEntry.md) object map
Required: Yes

 ** [Identifier](#API_PutAsset_RequestSyntax) **   <a name="Glue-PutAsset-request-Identifier"></a>
The unique identifier of the asset. If an asset with this identifier already exists, it is updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Pattern: `[a-zA-Z0-9\-\:\/\.\_\*]+`
Required: Yes

 ** [Name](#API_PutAsset_RequestSyntax) **   <a name="Glue-PutAsset-request-Name"></a>
The name of the asset.
Type: String
Required: Yes

## Response Syntax
<a name="API_PutAsset_ResponseSyntax"></a>

```
{
   "CreatedAt": number,
   "Description": "string",
   "Forms": {
      "string" : {
         "Content": "string",
         "FormTypeId": "string"
      }
   },
   "Id": "string",
   "Name": "string"
}
```

## Response Elements
<a name="API_PutAsset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_PutAsset_ResponseSyntax) **   <a name="Glue-PutAsset-response-CreatedAt"></a>
The timestamp at which the asset was created.
Type: Timestamp

 ** [Description](#API_PutAsset_ResponseSyntax) **   <a name="Glue-PutAsset-response-Description"></a>
The description of the asset.
Type: String

 ** [Forms](#API_PutAsset_ResponseSyntax) **   <a name="Glue-PutAsset-response-Forms"></a>
The forms attached to the asset, keyed by form name.
Type: String to [AssetFormEntry](API_AssetFormEntry.md) object map

 ** [Id](#API_PutAsset_ResponseSyntax) **   <a name="Glue-PutAsset-response-Id"></a>
The unique identifier of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Pattern: `[a-zA-Z0-9\-\:\/\.\_\*]+`

 ** [Name](#API_PutAsset_ResponseSyntax) **   <a name="Glue-PutAsset-response-Name"></a>
The name of the asset.
Type: String

## Errors
<a name="API_PutAsset_Errors"></a>

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
<a name="API_PutAsset_Examples"></a>

### Example
<a name="API_PutAsset_Example_1"></a>

The following example creates an asset with a form.

```
aws glue put-asset \
    --asset-type-id DataSet \
    --identifier quarterly-sales-2026q1 \
    --name "Quarterly Sales 2026 Q1" \
    --description "Aggregated quarterly sales metrics" \
    --forms '{"DataClassification":{"FormTypeId":"DataClassification","Content":"{\"classification\":\"internal\",\"owner\":\"data-platform-team\"}"}}'

{
    "Id": "quarterly-sales-2026q1",
    "Name": "Quarterly Sales 2026 Q1",
    "Description": "Aggregated quarterly sales metrics",
    "CreatedAt": "2026-06-16T06:42:00.442Z",
    "Forms": {
        "DataClassification": {
            "FormTypeId": "DataClassification",
            "Content": "{\"classification\":\"internal\",\"owner\":\"data-platform-team\"}"
        }
    }
}
```

## See Also
<a name="API_PutAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/PutAsset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/PutAsset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/PutAsset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/PutAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/PutAsset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/PutAsset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/PutAsset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/PutAsset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/PutAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/PutAsset)
