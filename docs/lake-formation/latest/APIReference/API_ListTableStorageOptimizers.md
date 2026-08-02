---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListTableStorageOptimizers.html
---

# ListTableStorageOptimizers
<a name="API_ListTableStorageOptimizers"></a>

Returns the configuration of all storage optimizers associated with a specified table.

## Request Syntax
<a name="API_ListTableStorageOptimizers_RequestSyntax"></a>

```
POST /ListTableStorageOptimizers HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StorageOptimizerType": "{{string}}",
   "TableName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListTableStorageOptimizers_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListTableStorageOptimizers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_ListTableStorageOptimizers_RequestSyntax) **   <a name="lakeformation-ListTableStorageOptimizers-request-CatalogId"></a>
The Catalog ID of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_ListTableStorageOptimizers_RequestSyntax) **   <a name="lakeformation-ListTableStorageOptimizers-request-DatabaseName"></a>
Name of the database where the table is present.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [MaxResults](#API_ListTableStorageOptimizers_RequestSyntax) **   <a name="lakeformation-ListTableStorageOptimizers-request-MaxResults"></a>
The number of storage optimizers to return on each call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListTableStorageOptimizers_RequestSyntax) **   <a name="lakeformation-ListTableStorageOptimizers-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

 ** [StorageOptimizerType](#API_ListTableStorageOptimizers_RequestSyntax) **   <a name="lakeformation-ListTableStorageOptimizers-request-StorageOptimizerType"></a>
The specific type of storage optimizers to list. The supported value is `compaction`.
Type: String
Valid Values: `COMPACTION | GARBAGE_COLLECTION | ALL`
Required: No

 ** [TableName](#API_ListTableStorageOptimizers_RequestSyntax) **   <a name="lakeformation-ListTableStorageOptimizers-request-TableName"></a>
Name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_ListTableStorageOptimizers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "StorageOptimizerList": [
      {
         "Config": {
            "string" : "string"
         },
         "ErrorMessage": "string",
         "LastRunDetails": "string",
         "StorageOptimizerType": "string",
         "Warnings": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTableStorageOptimizers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTableStorageOptimizers_ResponseSyntax) **   <a name="lakeformation-ListTableStorageOptimizers-response-NextToken"></a>
A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.
Type: String

 ** [StorageOptimizerList](#API_ListTableStorageOptimizers_ResponseSyntax) **   <a name="lakeformation-ListTableStorageOptimizers-response-StorageOptimizerList"></a>
A list of the storage optimizers associated with a table.
Type: Array of [StorageOptimizer](API_StorageOptimizer.md) objects

## Errors
<a name="API_ListTableStorageOptimizers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** EntityNotFoundException **
A specified entity does not exist.
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
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListTableStorageOptimizers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/ListTableStorageOptimizers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/ListTableStorageOptimizers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/ListTableStorageOptimizers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/ListTableStorageOptimizers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/ListTableStorageOptimizers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/ListTableStorageOptimizers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/ListTableStorageOptimizers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/ListTableStorageOptimizers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/ListTableStorageOptimizers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/ListTableStorageOptimizers)
