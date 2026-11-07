---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetIterableForms.html
---

# BatchGetIterableForms
<a name="API_BatchGetIterableForms"></a>

Retrieves multiple items from an iterable form on an asset in AWS Glue Data Catalog in a single request.

## Request Syntax
<a name="API_BatchGetIterableForms_RequestSyntax"></a>

```
{
   "AssetIdentifier": "{{string}}",
   "ItemIdentifiers": [ "{{string}}" ],
   "IterableFormName": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchGetIterableForms_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssetIdentifier](#API_BatchGetIterableForms_RequestSyntax) **   <a name="Glue-BatchGetIterableForms-request-AssetIdentifier"></a>
The unique identifier of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Pattern: `[a-zA-Z0-9\-\:\/\.\_\*]+`
Required: Yes

 ** [ItemIdentifiers](#API_BatchGetIterableForms_RequestSyntax) **   <a name="Glue-BatchGetIterableForms-request-ItemIdentifiers"></a>
The list of item identifiers to retrieve. Each identifier can be an item ID or item name.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 1087.
Required: Yes

 ** [IterableFormName](#API_BatchGetIterableForms_RequestSyntax) **   <a name="Glue-BatchGetIterableForms-request-IterableFormName"></a>
The name of the iterable form to retrieve items from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*(::[a-zA-Z][a-zA-Z0-9_]*)?$`
Required: Yes

## Response Syntax
<a name="API_BatchGetIterableForms_ResponseSyntax"></a>

```
{
   "Errors": [
      {
         "Code": "string",
         "ItemIdentifier": "string",
         "Message": "string"
      }
   ],
   "Items": [
      {
         "Attachments": {
            "string" : {
               "Content": "string",
               "FormTypeId": "string"
            }
         },
         "Forms": {
            "string" : {
               "Content": "string",
               "FormTypeId": "string"
            }
         },
         "GlossaryTerms": [ "string" ],
         "ItemId": "string",
         "ItemName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetIterableForms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchGetIterableForms_ResponseSyntax) **   <a name="Glue-BatchGetIterableForms-response-Errors"></a>
The list of errors for items that could not be retrieved.
Type: Array of [ItemError](API_ItemError.md) objects

 ** [Items](#API_BatchGetIterableForms_ResponseSyntax) **   <a name="Glue-BatchGetIterableForms-response-Items"></a>
The list of retrieved iterable form items.
Type: Array of [IterableFormItem](API_IterableFormItem.md) objects

## Errors
<a name="API_BatchGetIterableForms_Errors"></a>

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
<a name="API_BatchGetIterableForms_Examples"></a>

### Example
<a name="API_BatchGetIterableForms_Example_1"></a>

The following example retrieves specific columns by identifier.

```
aws glue batch-get-iterable-forms \
    --asset-identifier quarterly-sales-2026q1 \
    --iterable-form-name columns \
    --item-identifiers region amount

{
    "Items": [
        {
            "ItemId": "quarterly-sales-2026q1#region",
            "ItemName": "region",
            "GlossaryTerms": [],
            "Forms": {
                "columns": {
                    "FormTypeId": "amazon.glue::Column",
                    "Content": "{\"type\":\"string\"}"
                }
            },
            "Attachments": {}
        },
        {
            "ItemId": "quarterly-sales-2026q1#amount",
            "ItemName": "amount",
            "GlossaryTerms": [],
            "Forms": {
                "columns": {
                    "FormTypeId": "amazon.glue::Column",
                    "Content": "{\"type\":\"double\"}"
                }
            },
            "Attachments": {}
        }
    ],
    "Errors": []
}
```

## See Also
<a name="API_BatchGetIterableForms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchGetIterableForms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchGetIterableForms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchGetIterableForms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchGetIterableForms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchGetIterableForms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchGetIterableForms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchGetIterableForms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchGetIterableForms)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchGetIterableForms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchGetIterableForms)
