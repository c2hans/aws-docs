---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateDataTableAttribute.html
---

# CreateDataTableAttribute
<a name="API_CreateDataTableAttribute"></a>

Adds an attribute to an existing data table. Creating a new primary attribute uses the empty value for the specified value type for all existing records. This should not affect uniqueness of published data tables since the existing primary values will already be unique. Creating attributes does not create any values. System managed tables may not allow customers to create new attributes.

## Request Syntax
<a name="API_CreateDataTableAttribute_RequestSyntax"></a>

```
PUT /data-tables/{{InstanceId}}/{{DataTableId}}/attributes HTTP/1.1
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
<a name="API_CreateDataTableAttribute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataTableId](#API_CreateDataTableAttribute_RequestSyntax) **   <a name="connect-CreateDataTableAttribute-request-uri-DataTableId"></a>
The unique identifier for the data table. Must also accept the table ARN with or without a version alias. If the version is provided as part of the identifier or ARN, the version must be one of the two available system managed aliases, $SAVED or $LATEST.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_CreateDataTableAttribute_RequestSyntax) **   <a name="connect-CreateDataTableAttribute-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateDataTableAttribute_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateDataTableAttribute_RequestSyntax) **   <a name="connect-CreateDataTableAttribute-request-Description"></a>
An optional description for the attribute. Must conform to Connect human readable string specification and have 0-250 characters. Whitespace trimmed before persisting.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.
Pattern: `^[\\P{C}\r\n\t]+$`
Required: No

 ** [Name](#API_CreateDataTableAttribute_RequestSyntax) **   <a name="connect-CreateDataTableAttribute-request-Name"></a>
The name for the attribute. Must conform to Connect human readable string specification and have 1-127 characters. Must not start with the reserved case insensitive values 'connect:' and 'aws:'. Whitespace trimmed before persisting. Must be unique for the data table using case-insensitive comparison.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** [Primary](#API_CreateDataTableAttribute_RequestSyntax) **   <a name="connect-CreateDataTableAttribute-request-Primary"></a>
Optional boolean that defaults to false. Determines if the value is used to identify a record in the table. Values for primary attributes must not be expressions.
Type: Boolean
Required: No

 ** [Validation](#API_CreateDataTableAttribute_RequestSyntax) **   <a name="connect-CreateDataTableAttribute-request-Validation"></a>
Optional validation rules for the attribute. Borrows heavily from JSON Schema - Draft 2020-12. The maximum length of arrays within validations and depth of validations is 5. There are default limits that apply to all types. Customer specified limits in excess of the default limits are not permitted.
Type: [Validation](API_Validation.md) object
Required: No

 ** [ValueType](#API_CreateDataTableAttribute_RequestSyntax) **   <a name="connect-CreateDataTableAttribute-request-ValueType"></a>
The type of value allowed or the resultant type after the value's expression is evaluated. Must be one of TEXT, TEXT\_LIST, NUMBER, NUMBER\_LIST, and BOOLEAN.
Type: String
Valid Values: `TEXT | NUMBER | BOOLEAN | TEXT_LIST | NUMBER_LIST`
Required: Yes

## Response Syntax
<a name="API_CreateDataTableAttribute_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AttributeId": "string",
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
<a name="API_CreateDataTableAttribute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttributeId](#API_CreateDataTableAttribute_ResponseSyntax) **   <a name="connect-CreateDataTableAttribute-response-AttributeId"></a>
The unique identifier assigned to the created attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [LockVersion](#API_CreateDataTableAttribute_ResponseSyntax) **   <a name="connect-CreateDataTableAttribute-response-LockVersion"></a>
The lock version information for the data table and attribute, used for optimistic locking and versioning.
Type: [DataTableLockVersion](API_DataTableLockVersion.md) object

 ** [Name](#API_CreateDataTableAttribute_ResponseSyntax) **   <a name="connect-CreateDataTableAttribute-response-Name"></a>
The name of the created attribute since it also serves as the identifier. This could be different than the parameter passed in since it will be trimmed for whitespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`

## Errors
<a name="API_CreateDataTableAttribute_Errors"></a>

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
<a name="API_CreateDataTableAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateDataTableAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateDataTableAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateDataTableAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateDataTableAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateDataTableAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateDataTableAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateDataTableAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateDataTableAttribute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateDataTableAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateDataTableAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
