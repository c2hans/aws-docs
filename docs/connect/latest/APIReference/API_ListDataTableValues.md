---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListDataTableValues.html
---

# ListDataTableValues
<a name="API_ListDataTableValues"></a>

Lists values stored in a data table with optional filtering by record IDs or primary attribute values. Returns the raw stored values along with metadata such as lock versions and modification timestamps.

## Request Syntax
<a name="API_ListDataTableValues_RequestSyntax"></a>

```
POST /data-tables/{{InstanceId}}/{{DataTableId}}/values/list?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "PrimaryAttributeValues": [
      {
         "AttributeName": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "RecordIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ListDataTableValues_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataTableId](#API_ListDataTableValues_RequestSyntax) **   <a name="connect-ListDataTableValues-request-uri-DataTableId"></a>
The unique identifier for the data table whose values should be listed.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_ListDataTableValues_RequestSyntax) **   <a name="connect-ListDataTableValues-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListDataTableValues_RequestSyntax) **   <a name="connect-ListDataTableValues-request-uri-MaxResults"></a>
The maximum number of data table values to return in one page of results.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListDataTableValues_RequestSyntax) **   <a name="connect-ListDataTableValues-request-uri-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.

## Request Body
<a name="API_ListDataTableValues_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PrimaryAttributeValues](#API_ListDataTableValues_RequestSyntax) **   <a name="connect-ListDataTableValues-request-PrimaryAttributeValues"></a>
Optional filter to retrieve values for records matching specific primary attribute criteria.
Type: Array of [PrimaryAttributeValueFilter](API_PrimaryAttributeValueFilter.md) objects
Required: No

 ** [RecordIds](#API_ListDataTableValues_RequestSyntax) **   <a name="connect-ListDataTableValues-request-RecordIds"></a>
Optional list of specific record IDs to retrieve values for.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_ListDataTableValues_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Values": [
      {
         "AttributeId": "string",
         "AttributeName": "string",
         "LastModifiedRegion": "string",
         "LastModifiedTime": number,
         "LockVersion": {
            "Attribute": "string",
            "DataTable": "string",
            "PrimaryValues": "string",
            "Value": "string"
         },
         "PrimaryValues": [
            {
               "AttributeId": "string",
               "AttributeName": "string",
               "Value": "string"
            }
         ],
         "RecordId": "string",
         "Value": "string",
         "ValueType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListDataTableValues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListDataTableValues_ResponseSyntax) **   <a name="connect-ListDataTableValues-response-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Type: String

 ** [Values](#API_ListDataTableValues_ResponseSyntax) **   <a name="connect-ListDataTableValues-response-Values"></a>
A list of data table values with their associated metadata, lock versions, and modification details.
Type: Array of [DataTableValueSummary](API_DataTableValueSummary.md) objects

## Errors
<a name="API_ListDataTableValues_Errors"></a>

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
<a name="API_ListDataTableValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListDataTableValues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListDataTableValues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListDataTableValues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListDataTableValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListDataTableValues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListDataTableValues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListDataTableValues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListDataTableValues)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListDataTableValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListDataTableValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
