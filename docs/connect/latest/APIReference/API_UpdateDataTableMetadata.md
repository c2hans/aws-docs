---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateDataTableMetadata.html
---

# UpdateDataTableMetadata
<a name="API_UpdateDataTableMetadata"></a>

Updates the metadata properties of a data table. Accepts all fields similar to CreateDataTable, except for fields and tags. There are no other granular update endpoints. It does not act as a patch operation - all properties must be provided or defaults will be used. Fields follow the same requirements as CreateDataTable.

## Request Syntax
<a name="API_UpdateDataTableMetadata_RequestSyntax"></a>

```
POST /data-tables/{{InstanceId}}/{{DataTableId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "TimeZone": "{{string}}",
   "ValueLockLevel": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDataTableMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataTableId](#API_UpdateDataTableMetadata_RequestSyntax) **   <a name="connect-UpdateDataTableMetadata-request-uri-DataTableId"></a>
The unique identifier for the data table. Must also accept the table ARN with or without a version alias. If the version is provided as part of the identifier or ARN, the version must be $LATEST. Providing any other alias fails with an error.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_UpdateDataTableMetadata_RequestSyntax) **   <a name="connect-UpdateDataTableMetadata-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateDataTableMetadata_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateDataTableMetadata_RequestSyntax) **   <a name="connect-UpdateDataTableMetadata-request-Description"></a>
The updated description for the data table. Must conform to Connect human readable string specification and have 0-250 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.
Pattern: `^[\\P{C}\r\n\t]+$`
Required: No

 ** [Name](#API_UpdateDataTableMetadata_RequestSyntax) **   <a name="connect-UpdateDataTableMetadata-request-Name"></a>
The updated name for the data table. Must conform to Connect human readable string specification and have 1-127 characters. Must be unique for the instance using case-insensitive comparison.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** [TimeZone](#API_UpdateDataTableMetadata_RequestSyntax) **   <a name="connect-UpdateDataTableMetadata-request-TimeZone"></a>
The updated IANA timezone identifier to use when resolving time based dynamic values.
Type: String
Required: Yes

 ** [ValueLockLevel](#API_UpdateDataTableMetadata_RequestSyntax) **   <a name="connect-UpdateDataTableMetadata-request-ValueLockLevel"></a>
The updated value lock level for the data table. One of DATA\_TABLE, PRIMARY\_VALUE, ATTRIBUTE, VALUE, and NONE.
Type: String
Valid Values: `NONE | DATA_TABLE | PRIMARY_VALUE | ATTRIBUTE | VALUE`
Required: Yes

## Response Syntax
<a name="API_UpdateDataTableMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LockVersion": {
      "Attribute": "string",
      "DataTable": "string",
      "PrimaryValues": "string",
      "Value": "string"
   }
}
```

## Response Elements
<a name="API_UpdateDataTableMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LockVersion](#API_UpdateDataTableMetadata_ResponseSyntax) **   <a name="connect-UpdateDataTableMetadata-response-LockVersion"></a>
The new lock version for the data table after the update.
Type: [DataTableLockVersion](API_DataTableLockVersion.md) object

## Errors
<a name="API_UpdateDataTableMetadata_Errors"></a>

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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateDataTableMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateDataTableMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateDataTableMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateDataTableMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateDataTableMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateDataTableMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateDataTableMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateDataTableMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateDataTableMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateDataTableMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateDataTableMetadata)
