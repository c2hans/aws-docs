---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateDataTablePrimaryValues.html
---

# UpdateDataTablePrimaryValues
<a name="API_UpdateDataTablePrimaryValues"></a>

Updates the primary values for a record. This operation affects all existing values that are currently associated to the record and its primary values. Users that have restrictions on attributes and/or primary values are not authorized to use this endpoint. The combination of new primary values must be unique within the table.

## Request Syntax
<a name="API_UpdateDataTablePrimaryValues_RequestSyntax"></a>

```
POST /data-tables/{{InstanceId}}/{{DataTableId}}/values/update-primary HTTP/1.1
Content-type: application/json

{
   "LockVersion": {
      "Attribute": "{{string}}",
      "DataTable": "{{string}}",
      "PrimaryValues": "{{string}}",
      "Value": "{{string}}"
   },
   "NewPrimaryValues": [
      {
         "AttributeName": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "PrimaryValues": [
      {
         "AttributeName": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateDataTablePrimaryValues_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataTableId](#API_UpdateDataTablePrimaryValues_RequestSyntax) **   <a name="connect-UpdateDataTablePrimaryValues-request-uri-DataTableId"></a>
The unique identifier for the data table. Must also accept the table ARN with or without a version alias. If the version is provided as part of the identifier or ARN, the version must be one of the two available system managed aliases, $SAVED or $LATEST.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_UpdateDataTablePrimaryValues_RequestSyntax) **   <a name="connect-UpdateDataTablePrimaryValues-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateDataTablePrimaryValues_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [LockVersion](#API_UpdateDataTablePrimaryValues_RequestSyntax) **   <a name="connect-UpdateDataTablePrimaryValues-request-LockVersion"></a>
The lock version information required for optimistic locking to prevent concurrent modifications.
Type: [DataTableLockVersion](API_DataTableLockVersion.md) object
Required: Yes

 ** [NewPrimaryValues](#API_UpdateDataTablePrimaryValues_RequestSyntax) **   <a name="connect-UpdateDataTablePrimaryValues-request-NewPrimaryValues"></a>
The new primary values for the record. Required and must include values for all primary attributes. The combination must be unique within the table.
Type: Array of [PrimaryValue](API_PrimaryValue.md) objects
Required: Yes

 ** [PrimaryValues](#API_UpdateDataTablePrimaryValues_RequestSyntax) **   <a name="connect-UpdateDataTablePrimaryValues-request-PrimaryValues"></a>
The current primary values for the record. Required and must include values for all primary attributes. Fails if the table has primary attributes and some primary values are omitted.
Type: Array of [PrimaryValue](API_PrimaryValue.md) objects
Required: Yes

## Response Syntax
<a name="API_UpdateDataTablePrimaryValues_ResponseSyntax"></a>

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
<a name="API_UpdateDataTablePrimaryValues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LockVersion](#API_UpdateDataTablePrimaryValues_ResponseSyntax) **   <a name="connect-UpdateDataTablePrimaryValues-response-LockVersion"></a>
The updated lock version information for the data table and affected components after the primary values change.
Type: [DataTableLockVersion](API_DataTableLockVersion.md) object

## Errors
<a name="API_UpdateDataTablePrimaryValues_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Operation cannot be performed at this time as there is a conflict with another operation or contact state.
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
<a name="API_UpdateDataTablePrimaryValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateDataTablePrimaryValues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateDataTablePrimaryValues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateDataTablePrimaryValues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateDataTablePrimaryValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateDataTablePrimaryValues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateDataTablePrimaryValues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateDataTablePrimaryValues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateDataTablePrimaryValues)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateDataTablePrimaryValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateDataTablePrimaryValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
