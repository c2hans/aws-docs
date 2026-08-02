---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateDataTable.html
---

# CreateDataTable
<a name="API_CreateDataTable"></a>

Creates a new data table with the specified properties. Supports the creation of all table properties except for attributes and values. A table with no attributes and values is a valid state for a table. The number of tables per instance is limited to 100 per instance. Customers can request an increase by using AWS Service Quotas.

## Request Syntax
<a name="API_CreateDataTable_RequestSyntax"></a>

```
PUT /data-tables/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Status": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "TimeZone": "{{string}}",
   "ValueLockLevel": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDataTable_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateDataTable_RequestSyntax) **   <a name="connect-CreateDataTable-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance where the data table will be created.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateDataTable_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateDataTable_RequestSyntax) **   <a name="connect-CreateDataTable-request-Description"></a>
An optional description for the data table. Must conform to Connect human readable string specification and have 0-250 characters. Whitespace must be trimmed first.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.
Pattern: `^[\\P{C}\r\n\t]+$`
Required: No

 ** [Name](#API_CreateDataTable_RequestSyntax) **   <a name="connect-CreateDataTable-request-Name"></a>
The name for the data table. Must conform to Connect human readable string specification and have 1-127 characters. Whitespace must be trimmed first. Must not start with the reserved case insensitive values 'connect:' and 'aws:'. Must be unique for the instance using case-insensitive comparison.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** [Status](#API_CreateDataTable_RequestSyntax) **   <a name="connect-CreateDataTable-request-Status"></a>
The status of the data table. One of PUBLISHED or SAVED. Required parameter that determines the initial state of the table.
Type: String
Valid Values: `PUBLISHED`
Required: Yes

 ** [Tags](#API_CreateDataTable_RequestSyntax) **   <a name="connect-CreateDataTable-request-Tags"></a>
Key value pairs for attribute based access control (TBAC or ABAC). Optional tags to apply to the data table for organization and access control purposes.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [TimeZone](#API_CreateDataTable_RequestSyntax) **   <a name="connect-CreateDataTable-request-TimeZone"></a>
The IANA timezone identifier to use when resolving time based dynamic values. Required even if no time slices are specified.
Type: String
Required: Yes

 ** [ValueLockLevel](#API_CreateDataTable_RequestSyntax) **   <a name="connect-CreateDataTable-request-ValueLockLevel"></a>
The data level that concurrent value edits are locked on. One of DATA\_TABLE, PRIMARY\_VALUE, ATTRIBUTE, VALUE, and NONE. NONE is the default if unspecified. This determines how concurrent edits are handled when multiple users attempt to modify values simultaneously.
Type: String
Valid Values: `NONE | DATA_TABLE | PRIMARY_VALUE | ATTRIBUTE | VALUE`
Required: Yes

## Response Syntax
<a name="API_CreateDataTable_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Id": "string",
   "LockVersion": {
      "Attribute": "string",
      "DataTable": "string",
      "PrimaryValues": "string",
      "Value": "string"
   }
}
```

## Response Elements
<a name="API_CreateDataTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateDataTable_ResponseSyntax) **   <a name="connect-CreateDataTable-response-Arn"></a>
The Amazon Resource Name (ARN) for the created data table. Does not include the version alias.
Type: String

 ** [Id](#API_CreateDataTable_ResponseSyntax) **   <a name="connect-CreateDataTable-response-Id"></a>
The unique identifier for the created data table. Does not include the version alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [LockVersion](#API_CreateDataTable_ResponseSyntax) **   <a name="connect-CreateDataTable-response-LockVersion"></a>
The lock version information for the created data table, used for optimistic locking and table versioning.
Type: [DataTableLockVersion](API_DataTableLockVersion.md) object

## Errors
<a name="API_CreateDataTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Operation cannot be performed at this time as there is a conflict with another operation or contact state.
HTTP Status Code: 409

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateDataTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateDataTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateDataTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateDataTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateDataTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateDataTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateDataTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateDataTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateDataTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateDataTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateDataTable)
