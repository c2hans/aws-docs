---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListDataTablePrimaryValues.html
---

# ListDataTablePrimaryValues
<a name="API_ListDataTablePrimaryValues"></a>

Lists all primary value combinations for a given data table. Returns the unique combinations of primary attribute values that identify records in the table. Up to 100 records are returned per request.

## Request Syntax
<a name="API_ListDataTablePrimaryValues_RequestSyntax"></a>

```
POST /data-tables/{{InstanceId}}/{{DataTableId}}/values/list-primary?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
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
<a name="API_ListDataTablePrimaryValues_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataTableId](#API_ListDataTablePrimaryValues_RequestSyntax) **   <a name="connect-ListDataTablePrimaryValues-request-uri-DataTableId"></a>
The unique identifier for the data table whose primary values should be listed.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_ListDataTablePrimaryValues_RequestSyntax) **   <a name="connect-ListDataTablePrimaryValues-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListDataTablePrimaryValues_RequestSyntax) **   <a name="connect-ListDataTablePrimaryValues-request-uri-MaxResults"></a>
The maximum number of data table primary values to return in one page of results.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListDataTablePrimaryValues_RequestSyntax) **   <a name="connect-ListDataTablePrimaryValues-request-uri-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.

## Request Body
<a name="API_ListDataTablePrimaryValues_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PrimaryAttributeValues](#API_ListDataTablePrimaryValues_RequestSyntax) **   <a name="connect-ListDataTablePrimaryValues-request-PrimaryAttributeValues"></a>
Optional filter to retrieve primary values matching specific criteria.
Type: Array of [PrimaryAttributeValueFilter](API_PrimaryAttributeValueFilter.md) objects
Required: No

 ** [RecordIds](#API_ListDataTablePrimaryValues_RequestSyntax) **   <a name="connect-ListDataTablePrimaryValues-request-RecordIds"></a>
Optional list of specific record IDs to retrieve. Used for CloudFormation to effectively describe records by ID. If NextToken is provided, this parameter is ignored.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_ListDataTablePrimaryValues_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "PrimaryValuesList": [
      {
         "LastModifiedRegion": "string",
         "LastModifiedTime": number,
         "PrimaryValues": [
            {
               "AttributeId": "string",
               "AttributeName": "string",
               "Value": "string"
            }
         ],
         "RecordId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListDataTablePrimaryValues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListDataTablePrimaryValues_ResponseSyntax) **   <a name="connect-ListDataTablePrimaryValues-response-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Type: String

 ** [PrimaryValuesList](#API_ListDataTablePrimaryValues_ResponseSyntax) **   <a name="connect-ListDataTablePrimaryValues-response-PrimaryValuesList"></a>
A list of primary value combinations with their record IDs and modification metadata.
Type: Array of [RecordPrimaryValue](API_RecordPrimaryValue.md) objects

## Errors
<a name="API_ListDataTablePrimaryValues_Errors"></a>

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
<a name="API_ListDataTablePrimaryValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListDataTablePrimaryValues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListDataTablePrimaryValues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListDataTablePrimaryValues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListDataTablePrimaryValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListDataTablePrimaryValues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListDataTablePrimaryValues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListDataTablePrimaryValues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListDataTablePrimaryValues)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListDataTablePrimaryValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListDataTablePrimaryValues)
