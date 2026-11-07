---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetAsset.html
---

# GetAsset
<a name="API_GetAsset"></a>

Retrieves the metadata for an asset in AWS Glue Data Catalog, including its forms, additional attachments, and associated glossary terms.

## Request Syntax
<a name="API_GetAsset_RequestSyntax"></a>

```
{
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAsset_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Identifier](#API_GetAsset_RequestSyntax) **   <a name="Glue-GetAsset-request-Identifier"></a>
The unique identifier of the asset to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Pattern: `[a-zA-Z0-9\-\:\/\.\_\*]+`
Required: Yes

## Response Syntax
<a name="API_GetAsset_ResponseSyntax"></a>

```
{
   "AssetTypeId": "string",
   "Attachments": {
      "string" : {
         "Content": "string",
         "FormTypeId": "string"
      }
   },
   "CreatedAt": number,
   "Description": "string",
   "Forms": {
      "string" : {
         "Content": "string",
         "FormTypeId": "string"
      }
   },
   "GlossaryTerms": [ "string" ],
   "Id": "string",
   "IterableForms": {
      "string" : {
         "FormTypeId": "string"
      }
   },
   "Name": "string",
   "UpdatedAt": number
}
```

## Response Elements
<a name="API_GetAsset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssetTypeId](#API_GetAsset_ResponseSyntax) **   <a name="Glue-GetAsset-response-AssetTypeId"></a>
The identifier of the asset type for this asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [Attachments](#API_GetAsset_ResponseSyntax) **   <a name="Glue-GetAsset-response-Attachments"></a>
Additional attachments on the asset for more context, keyed by attachment name.
Type: String to [AssetFormEntry](API_AssetFormEntry.md) object map

 ** [CreatedAt](#API_GetAsset_ResponseSyntax) **   <a name="Glue-GetAsset-response-CreatedAt"></a>
The timestamp at which the asset was created.
Type: Timestamp

 ** [Description](#API_GetAsset_ResponseSyntax) **   <a name="Glue-GetAsset-response-Description"></a>
The description of the asset.
Type: String

 ** [Forms](#API_GetAsset_ResponseSyntax) **   <a name="Glue-GetAsset-response-Forms"></a>
The forms on the asset, keyed by form name.
Type: String to [AssetFormEntry](API_AssetFormEntry.md) object map

 ** [GlossaryTerms](#API_GetAsset_ResponseSyntax) **   <a name="Glue-GetAsset-response-GlossaryTerms"></a>
The identifiers of the glossary terms associated with the asset.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [Id](#API_GetAsset_ResponseSyntax) **   <a name="Glue-GetAsset-response-Id"></a>
The unique identifier of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Pattern: `[a-zA-Z0-9\-\:\/\.\_\*]+`

 ** [IterableForms](#API_GetAsset_ResponseSyntax) **   <a name="Glue-GetAsset-response-IterableForms"></a>
The iterable forms available on the asset, keyed by form name (for example, `columns`). Use the form name with `ListIterableForms` or `BatchGetIterableForms` to retrieve the form's items.
Type: String to [IterableFormEntry](API_IterableFormEntry.md) object map

 ** [Name](#API_GetAsset_ResponseSyntax) **   <a name="Glue-GetAsset-response-Name"></a>
The name of the asset.
Type: String

 ** [UpdatedAt](#API_GetAsset_ResponseSyntax) **   <a name="Glue-GetAsset-response-UpdatedAt"></a>
The timestamp at which the asset was last updated.
Type: Timestamp

## Errors
<a name="API_GetAsset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
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
<a name="API_GetAsset_Examples"></a>

### Example
<a name="API_GetAsset_Example_1"></a>

The following example retrieves an asset by its identifier.

```
aws glue get-asset --identifier quarterly-sales-2026q1

{
    "Id": "quarterly-sales-2026q1",
    "Name": "Quarterly Sales 2026 Q1",
    "Description": "Aggregated quarterly sales metrics",
    "CreatedAt": "2026-06-16T06:42:00.442Z",
    "AssetTypeId": "DataSet",
    "GlossaryTerms": [],
    "Forms": {
        "DataClassification": {
            "FormTypeId": "DataClassification",
            "Content": "{\"classification\":\"internal\",\"owner\":\"data-platform-team\"}"
        }
    },
    "Attachments": {},
    "IterableForms": {}
}
```

## See Also
<a name="API_GetAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetAsset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetAsset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetAsset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetAsset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetAsset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetAsset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetAsset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetAsset)
