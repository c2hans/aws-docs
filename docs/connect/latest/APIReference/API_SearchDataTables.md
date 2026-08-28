---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchDataTables.html
---

# SearchDataTables
<a name="API_SearchDataTables"></a>

Searches for data tables based on the table's ID, name, and description. In the future, this operation can support searching on attribute names and possibly primary values. Follows other search operations closely and supports both search criteria and filters.

## Request Syntax
<a name="API_SearchDataTables_RequestSyntax"></a>

```
POST /search-data-tables HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "DataTableSearchCriteria"
      ],
      "OrConditions": [
         "DataTableSearchCriteria"
      ],
      "StringCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}",
         "Value": "{{string}}"
      }
   },
   "SearchFilter": {
      "AttributeFilter": {
         "AndCondition": {
            "TagConditions": [
               {
                  "TagKey": "{{string}}",
                  "TagValue": "{{string}}"
               }
            ]
         },
         "OrConditions": [
            {
               "TagConditions": [
                  {
                     "TagKey": "{{string}}",
                     "TagValue": "{{string}}"
                  }
               ]
            }
         ],
         "TagCondition": {
            "TagKey": "{{string}}",
            "TagValue": "{{string}}"
         }
      }
   }
}
```

## URI Request Parameters
<a name="API_SearchDataTables_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchDataTables_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchDataTables_RequestSyntax) **   <a name="connect-SearchDataTables-request-InstanceId"></a>
The unique identifier for the Amazon Connect instance to search within.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchDataTables_RequestSyntax) **   <a name="connect-SearchDataTables-request-MaxResults"></a>
The maximum number of data tables to return in one page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_SearchDataTables_RequestSyntax) **   <a name="connect-SearchDataTables-request-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Type: String
Required: No

 ** [SearchCriteria](#API_SearchDataTables_RequestSyntax) **   <a name="connect-SearchDataTables-request-SearchCriteria"></a>
Search criteria including string conditions for matching table names, descriptions, or resource IDs. Supports STARTS\_WITH, CONTAINS, and EXACT comparison types.
Type: [DataTableSearchCriteria](API_DataTableSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchDataTables_RequestSyntax) **   <a name="connect-SearchDataTables-request-SearchFilter"></a>
Optional filters to apply to the search results, such as tag-based filtering for attribute-based access control.
Type: [DataTableSearchFilter](API_DataTableSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchDataTables_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "DataTables": [
      {
         "Arn": "string",
         "CreatedTime": number,
         "Description": "string",
         "Id": "string",
         "LastModifiedRegion": "string",
         "LastModifiedTime": number,
         "LockVersion": {
            "Attribute": "string",
            "DataTable": "string",
            "PrimaryValues": "string",
            "Value": "string"
         },
         "Name": "string",
         "Status": "string",
         "Tags": {
            "string" : "string"
         },
         "TimeZone": "string",
         "ValueLockLevel": "string",
         "Version": "string",
         "VersionDescription": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchDataTables_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchDataTables_ResponseSyntax) **   <a name="connect-SearchDataTables-response-ApproximateTotalCount"></a>
The approximate number of data tables that matched the search criteria.
Type: Long

 ** [DataTables](#API_SearchDataTables_ResponseSyntax) **   <a name="connect-SearchDataTables-response-DataTables"></a>
An array of data tables matching the search criteria with the same structure as DescribeTable except Version, VersionDescription, and LockVersion are omitted.
Type: Array of [DataTable](API_DataTable.md) objects

 ** [NextToken](#API_SearchDataTables_ResponseSyntax) **   <a name="connect-SearchDataTables-response-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Type: String

## Errors
<a name="API_SearchDataTables_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_SearchDataTables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchDataTables)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchDataTables)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchDataTables)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchDataTables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchDataTables)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchDataTables)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchDataTables)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchDataTables)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchDataTables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchDataTables)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
