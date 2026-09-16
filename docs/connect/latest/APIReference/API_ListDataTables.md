---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListDataTables.html
---

# ListDataTables
<a name="API_ListDataTables"></a>

Lists all data tables for the specified Amazon Connect instance. Returns summary information for each table including basic metadata and modification details.

## Request Syntax
<a name="API_ListDataTables_RequestSyntax"></a>

```
GET /data-tables/{{InstanceId}}?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataTables_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListDataTables_RequestSyntax) **   <a name="connect-ListDataTables-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance whose data tables should be listed.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListDataTables_RequestSyntax) **   <a name="connect-ListDataTables-request-uri-MaxResults"></a>
The maximum number of data tables to return in one page of results.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListDataTables_RequestSyntax) **   <a name="connect-ListDataTables-request-uri-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.

## Request Body
<a name="API_ListDataTables_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataTables_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DataTableSummaryList": [
      {
         "Arn": "string",
         "Id": "string",
         "LastModifiedRegion": "string",
         "LastModifiedTime": number,
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDataTables_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataTableSummaryList](#API_ListDataTables_ResponseSyntax) **   <a name="connect-ListDataTables-response-DataTableSummaryList"></a>
A list of data table summaries containing basic information about each table including ID, ARN, name, and modification details.
Type: Array of [DataTableSummary](API_DataTableSummary.md) objects

 ** [NextToken](#API_ListDataTables_ResponseSyntax) **   <a name="connect-ListDataTables-response-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Type: String

## Errors
<a name="API_ListDataTables_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListDataTables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListDataTables)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListDataTables)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListDataTables)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListDataTables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListDataTables)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListDataTables)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListDataTables)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListDataTables)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListDataTables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListDataTables)
