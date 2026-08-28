---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListDataCellsFilter.html
---

# ListDataCellsFilter
<a name="API_ListDataCellsFilter"></a>

Lists all the data cell filters on a table.

## Request Syntax
<a name="API_ListDataCellsFilter_RequestSyntax"></a>

```
POST /ListDataCellsFilter HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Table": {
      "CatalogId": "{{string}}",
      "DatabaseName": "{{string}}",
      "Name": "{{string}}",
      "TableWildcard": {
      }
   }
}
```

## URI Request Parameters
<a name="API_ListDataCellsFilter_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListDataCellsFilter_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListDataCellsFilter_RequestSyntax) **   <a name="lakeformation-ListDataCellsFilter-request-MaxResults"></a>
The maximum size of the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListDataCellsFilter_RequestSyntax) **   <a name="lakeformation-ListDataCellsFilter-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

 ** [Table](#API_ListDataCellsFilter_RequestSyntax) **   <a name="lakeformation-ListDataCellsFilter-request-Table"></a>
A table in the AWS Glue Data Catalog.
Type: [TableResource](API_TableResource.md) object
Required: No

## Response Syntax
<a name="API_ListDataCellsFilter_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DataCellsFilters": [
      {
         "ColumnNames": [ "string" ],
         "ColumnWildcard": {
            "ExcludedColumnNames": [ "string" ]
         },
         "DatabaseName": "string",
         "Name": "string",
         "RowFilter": {
            "AllRowsWildcard": {
            },
            "FilterExpression": "string"
         },
         "TableCatalogId": "string",
         "TableName": "string",
         "VersionId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDataCellsFilter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataCellsFilters](#API_ListDataCellsFilter_ResponseSyntax) **   <a name="lakeformation-ListDataCellsFilter-response-DataCellsFilters"></a>
A list of `DataCellFilter` structures.
Type: Array of [DataCellsFilter](API_DataCellsFilter.md) objects

 ** [NextToken](#API_ListDataCellsFilter_ResponseSyntax) **   <a name="lakeformation-ListDataCellsFilter-response-NextToken"></a>
A continuation token, if not all requested data cell filters have been returned.
Type: String

## Errors
<a name="API_ListDataCellsFilter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

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

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListDataCellsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/ListDataCellsFilter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/ListDataCellsFilter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/ListDataCellsFilter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/ListDataCellsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/ListDataCellsFilter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/ListDataCellsFilter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/ListDataCellsFilter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/ListDataCellsFilter)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/ListDataCellsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/ListDataCellsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
