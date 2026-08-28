---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetDataCellsFilter.html
---

# GetDataCellsFilter
<a name="API_GetDataCellsFilter"></a>

Returns a data cells filter.

## Request Syntax
<a name="API_GetDataCellsFilter_RequestSyntax"></a>

```
POST /GetDataCellsFilter HTTP/1.1
Content-type: application/json

{
   "DatabaseName": "{{string}}",
   "Name": "{{string}}",
   "TableCatalogId": "{{string}}",
   "TableName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetDataCellsFilter_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetDataCellsFilter_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DatabaseName](#API_GetDataCellsFilter_RequestSyntax) **   <a name="lakeformation-GetDataCellsFilter-request-DatabaseName"></a>
A database in the AWS Glue Data Catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Name](#API_GetDataCellsFilter_RequestSyntax) **   <a name="lakeformation-GetDataCellsFilter-request-Name"></a>
The name given by the user to the data filter cell.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TableCatalogId](#API_GetDataCellsFilter_RequestSyntax) **   <a name="lakeformation-GetDataCellsFilter-request-TableCatalogId"></a>
The ID of the catalog to which the table belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TableName](#API_GetDataCellsFilter_RequestSyntax) **   <a name="lakeformation-GetDataCellsFilter-request-TableName"></a>
A table in the database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetDataCellsFilter_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DataCellsFilter": {
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
}
```

## Response Elements
<a name="API_GetDataCellsFilter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataCellsFilter](#API_GetDataCellsFilter_ResponseSyntax) **   <a name="lakeformation-GetDataCellsFilter-response-DataCellsFilter"></a>
A structure that describes certain columns on certain rows.
Type: [DataCellsFilter](API_DataCellsFilter.md) object

## Errors
<a name="API_GetDataCellsFilter_Errors"></a>

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

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetDataCellsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/GetDataCellsFilter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/GetDataCellsFilter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/GetDataCellsFilter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/GetDataCellsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/GetDataCellsFilter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/GetDataCellsFilter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/GetDataCellsFilter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/GetDataCellsFilter)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/GetDataCellsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/GetDataCellsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
