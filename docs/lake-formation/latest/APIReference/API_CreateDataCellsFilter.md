---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_CreateDataCellsFilter.html
---

# CreateDataCellsFilter
<a name="API_CreateDataCellsFilter"></a>

Creates a data cell filter to allow one to grant access to certain columns on certain rows.

## Request Syntax
<a name="API_CreateDataCellsFilter_RequestSyntax"></a>

```
POST /CreateDataCellsFilter HTTP/1.1
Content-type: application/json

{
   "TableData": {
      "ColumnNames": [ "{{string}}" ],
      "ColumnWildcard": {
         "ExcludedColumnNames": [ "{{string}}" ]
      },
      "DatabaseName": "{{string}}",
      "Name": "{{string}}",
      "RowFilter": {
         "AllRowsWildcard": {
         },
         "FilterExpression": "{{string}}"
      },
      "TableCatalogId": "{{string}}",
      "TableName": "{{string}}",
      "VersionId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDataCellsFilter_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDataCellsFilter_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TableData](#API_CreateDataCellsFilter_RequestSyntax) **   <a name="lakeformation-CreateDataCellsFilter-request-TableData"></a>
A `DataCellsFilter` structure containing information about the data cells filter.
Type: [DataCellsFilter](API_DataCellsFilter.md) object
Required: Yes

## Response Syntax
<a name="API_CreateDataCellsFilter_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreateDataCellsFilter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateDataCellsFilter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

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

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_CreateDataCellsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/CreateDataCellsFilter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/CreateDataCellsFilter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/CreateDataCellsFilter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/CreateDataCellsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/CreateDataCellsFilter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/CreateDataCellsFilter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/CreateDataCellsFilter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/CreateDataCellsFilter)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/CreateDataCellsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/CreateDataCellsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
