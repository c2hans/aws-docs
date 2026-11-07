---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListIterableForms.html
---

# ListIterableForms
<a name="API_ListIterableForms"></a>

Lists the items in an iterable form on an asset in AWS Glue Data Catalog. For example, lists the columns of a table asset.

## Request Syntax
<a name="API_ListIterableForms_RequestSyntax"></a>

```
{
   "AssetIdentifier": "{{string}}",
   "IterableFormName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListIterableForms_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssetIdentifier](#API_ListIterableForms_RequestSyntax) **   <a name="Glue-ListIterableForms-request-AssetIdentifier"></a>
The unique identifier of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Pattern: `[a-zA-Z0-9\-\:\/\.\_\*]+`
Required: Yes

 ** [IterableFormName](#API_ListIterableForms_RequestSyntax) **   <a name="Glue-ListIterableForms-request-IterableFormName"></a>
The name of the iterable form to list items from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*(::[a-zA-Z][a-zA-Z0-9_]*)?$`
Required: Yes

 ** [MaxResults](#API_ListIterableForms_RequestSyntax) **   <a name="Glue-ListIterableForms-request-MaxResults"></a>
The maximum number of results to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListIterableForms_RequestSyntax) **   <a name="Glue-ListIterableForms-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

## Response Syntax
<a name="API_ListIterableForms_ResponseSyntax"></a>

```
{
   "Items": [
      {
         "Description": "string",
         "GlossaryTerms": [ "string" ],
         "ItemId": "string",
         "ItemName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListIterableForms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListIterableForms_ResponseSyntax) **   <a name="Glue-ListIterableForms-response-Items"></a>
The list of iterable form items.
Type: Array of [IterableFormListItem](API_IterableFormListItem.md) objects

 ** [NextToken](#API_ListIterableForms_ResponseSyntax) **   <a name="Glue-ListIterableForms-response-NextToken"></a>
A continuation token, present if the current segment is not the last.
Type: String

## Errors
<a name="API_ListIterableForms_Errors"></a>

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
<a name="API_ListIterableForms_Examples"></a>

### Example
<a name="API_ListIterableForms_Example_1"></a>

The following example lists the columns of an asset.

```
aws glue list-iterable-forms \
    --asset-identifier quarterly-sales-2026q1 \
    --iterable-form-name columns \
    --max-results 20

{
    "AssetId": "quarterly-sales-2026q1",
    "IterableFormName": "columns",
    "Items": [
        {
            "ItemId": "quarterly-sales-2026q1#region",
            "ItemName": "region",
            "Description": "AWS region of the sales record",
            "GlossaryTerms": []
        },
        {
            "ItemId": "quarterly-sales-2026q1#amount",
            "ItemName": "amount",
            "Description": "Sales amount in USD",
            "GlossaryTerms": []
        }
    ]
}
```

## See Also
<a name="API_ListIterableForms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListIterableForms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListIterableForms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListIterableForms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListIterableForms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListIterableForms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListIterableForms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListIterableForms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListIterableForms)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListIterableForms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListIterableForms)
