---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeDataTable.html
---

# DescribeDataTable
<a name="API_DescribeDataTable"></a>

Returns all properties for a data table except for attributes and values. All properties from CreateDataTable are returned as well as properties for region replication, versioning, and system tables. "Describe" is a deprecated term but is allowed to maintain consistency with existing operations.

## Request Syntax
<a name="API_DescribeDataTable_RequestSyntax"></a>

```
GET /data-tables/{{InstanceId}}/{{DataTableId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDataTable_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataTableId](#API_DescribeDataTable_RequestSyntax) **   <a name="connect-DescribeDataTable-request-uri-DataTableId"></a>
The unique identifier for the data table. Must also accept the table ARN with or without a version alias. If no alias is provided, the default behavior is identical to providing the $LATEST alias.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_DescribeDataTable_RequestSyntax) **   <a name="connect-DescribeDataTable-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DescribeDataTable_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDataTable_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DataTable": {
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
}
```

## Response Elements
<a name="API_DescribeDataTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataTable](#API_DescribeDataTable_ResponseSyntax) **   <a name="connect-DescribeDataTable-response-DataTable"></a>
The complete data table information including metadata, configuration, and versioning details.
Type: [DataTable](API_DataTable.md) object

## Errors
<a name="API_DescribeDataTable_Errors"></a>

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
<a name="API_DescribeDataTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeDataTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeDataTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeDataTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeDataTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeDataTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeDataTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeDataTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeDataTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeDataTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeDataTable)
