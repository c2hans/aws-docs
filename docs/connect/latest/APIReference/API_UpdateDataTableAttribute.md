---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateDataTableAttribute.html
---

# UpdateDataTableAttribute
<a name="API_UpdateDataTableAttribute"></a>

Updates all properties for an attribute using all properties from CreateDataTableAttribute. There are no other granular update endpoints. It does not act as a patch operation - all properties must be provided. System managed attributes are not mutable by customers. Changing an attribute's validation does not invalidate existing values since validation only runs when values are created or updated.

## Request Syntax
<a name="API_UpdateDataTableAttribute_RequestSyntax"></a>

```
POST /data-tables/{{InstanceId}}/{{DataTableId}}/attributes/{{AttributeName}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Primary": {{boolean}},
   "Validation": {
      "Enum": {
         "Strict": {{boolean}},
         "Values": [ "{{string}}" ]
      },
      "ExclusiveMaximum": {{number}},
      "ExclusiveMinimum": {{number}},
      "IgnoreCase": {{boolean}},
      "Maximum": {{number}},
      "MaxLength": {{number}},
      "MaxValues": {{number}},
      "Minimum": {{number}},
      "MinLength": {{number}},
      "MinValues": {{number}},
      "MultipleOf": {{number}}
   },
   "ValueType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDataTableAttribute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AttributeName](#API_UpdateDataTableAttribute_RequestSyntax) **   <a name="connect-UpdateDataTableAttribute-request-uri-AttributeName"></a>
The current name of the attribute to update. Used as an identifier since attribute names can be changed.
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** [DataTableId](#API_UpdateDataTableAttribute_RequestSyntax) **   <a name="connect-UpdateDataTableAttribute-request-uri-DataTableId"></a>
The unique identifier for the data table. Must also accept the table ARN with or without a version alias.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_UpdateDataTableAttribute_RequestSyntax) **   <a name="connect-UpdateDataTableAttribute-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateDataTableAttribute_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateDataTableAttribute_RequestSyntax) **   <a name="connect-UpdateDataTableAttribute-request-Description"></a>
The updated description for the attribute.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.
Pattern: `^[\\P{C}\r\n\t]+$`
Required: No

 ** [Name](#API_UpdateDataTableAttribute_RequestSyntax) **   <a name="connect-UpdateDataTableAttribute-request-Name"></a>
The new name for the attribute. Must conform to Connect human readable string specification and be unique within the data table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** [Primary](#API_UpdateDataTableAttribute_RequestSyntax) **   <a name="connect-UpdateDataTableAttribute-request-Primary"></a>
Whether the attribute should be treated as a primary key. Converting to primary attribute requires existing values to maintain uniqueness.
Type: Boolean
Required: No

 ** [Validation](#API_UpdateDataTableAttribute_RequestSyntax) **   <a name="connect-UpdateDataTableAttribute-request-Validation"></a>
The updated validation rules for the attribute. Changes do not affect existing values until they are modified.
Type: [Validation](API_Validation.md) object
Required: No

 ** [ValueType](#API_UpdateDataTableAttribute_RequestSyntax) **   <a name="connect-UpdateDataTableAttribute-request-ValueType"></a>
The updated value type for the attribute. When changing value types, existing values are not deleted but may return default values if incompatible.
Type: String
Valid Values: `TEXT | NUMBER | BOOLEAN | TEXT_LIST | NUMBER_LIST`
Required: Yes

## Response Syntax
<a name="API_UpdateDataTableAttribute_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LockVersion": {
      "Attribute": "string",
      "DataTable": "string",
      "PrimaryValues": "string",
      "Value": "string"
   },
   "Name": "string"
}
```

## Response Elements
<a name="API_UpdateDataTableAttribute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LockVersion](#API_UpdateDataTableAttribute_ResponseSyntax) **   <a name="connect-UpdateDataTableAttribute-response-LockVersion"></a>
The new lock version for the attribute after the update.
Type: [DataTableLockVersion](API_DataTableLockVersion.md) object

 ** [Name](#API_UpdateDataTableAttribute_ResponseSyntax) **   <a name="connect-UpdateDataTableAttribute-response-Name"></a>
The trimmed name and identifier for the updated attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`

## Errors
<a name="API_UpdateDataTableAttribute_Errors"></a>

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

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

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
<a name="API_UpdateDataTableAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateDataTableAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateDataTableAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateDataTableAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateDataTableAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateDataTableAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateDataTableAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateDataTableAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateDataTableAttribute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateDataTableAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateDataTableAttribute)
