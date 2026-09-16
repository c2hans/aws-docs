---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_GetType.html
---

# GetType
<a name="API_GetType"></a>

 The `GetType` operation returns information about the type, for example the field definitions, the timestamp when the type was last modified, the level of nesting, the status, and details about if the type is used in other types and tables.

To read keyspace metadata using `GetType`, the IAM principal needs `Select` action permissions for the system keyspace. To configure the required permissions, see [Permissions to view a UDT](https://docs.aws.amazon.com/keyspaces/latest/devguide/configure-udt-permissions.html#udt-permissions-view) in the *Amazon Keyspaces Developer Guide*.

## Request Syntax
<a name="API_GetType_RequestSyntax"></a>

```
{
   "keyspaceName": "{{string}}",
   "typeName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [keyspaceName](#API_GetType_RequestSyntax) **   <a name="keyspaces-GetType-request-keyspaceName"></a>
 The name of the keyspace that contains this type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** [typeName](#API_GetType_RequestSyntax) **   <a name="keyspaces-GetType-request-typeName"></a>
The formatted name of the type. For example, if the name of the type was created without double quotes, Amazon Keyspaces saved the name in lower-case characters. If the name was created in double quotes, you must use double quotes to specify the type name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Required: Yes

## Response Syntax
<a name="API_GetType_ResponseSyntax"></a>

```
{
   "directParentTypes": [ "string" ],
   "directReferringTables": [ "string" ],
   "fieldDefinitions": [
      {
         "name": "string",
         "type": "string"
      }
   ],
   "keyspaceArn": "string",
   "keyspaceName": "string",
   "lastModifiedTimestamp": number,
   "maxNestingDepth": number,
   "status": "string",
   "typeName": "string"
}
```

## Response Elements
<a name="API_GetType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [directParentTypes](#API_GetType_ResponseSyntax) **   <a name="keyspaces-GetType-response-directParentTypes"></a>
 The types that use this type.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 48.

 ** [directReferringTables](#API_GetType_ResponseSyntax) **   <a name="keyspaces-GetType-response-directReferringTables"></a>
 The tables that use this type.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`

 ** [fieldDefinitions](#API_GetType_ResponseSyntax) **   <a name="keyspaces-GetType-response-fieldDefinitions"></a>
 The names and types that define this type.
Type: Array of [FieldDefinition](API_FieldDefinition.md) objects
Array Members: Minimum number of 1 item.

 ** [keyspaceArn](#API_GetType_ResponseSyntax) **   <a name="keyspaces-GetType-response-keyspaceArn"></a>
 The unique identifier of the keyspace that contains this type in the format of an Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1000.
Pattern: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`

 ** [keyspaceName](#API_GetType_ResponseSyntax) **   <a name="keyspaces-GetType-response-keyspaceName"></a>
 The name of the keyspace that contains this type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`

 ** [lastModifiedTimestamp](#API_GetType_ResponseSyntax) **   <a name="keyspaces-GetType-response-lastModifiedTimestamp"></a>
 The timestamp that shows when this type was last modified.
Type: Timestamp

 ** [maxNestingDepth](#API_GetType_ResponseSyntax) **   <a name="keyspaces-GetType-response-maxNestingDepth"></a>
 The level of nesting implemented for this type.
Type: Integer

 ** [status](#API_GetType_ResponseSyntax) **   <a name="keyspaces-GetType-response-status"></a>
 The status of this type.
Type: String
Valid Values: `ACTIVE | CREATING | DELETING | RESTORING`

 ** [typeName](#API_GetType_ResponseSyntax) **   <a name="keyspaces-GetType-response-typeName"></a>
 The name of the type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.

## Errors
<a name="API_GetType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have sufficient access permissions to perform this action.
 ** message **
You don't have the required permissions to perform this operation. Verify your IAM permissions and try again.
HTTP Status Code: 400

 [InternalServerException](API_InternalServerException.md)
Amazon Keyspaces was unable to fully process this request because of an internal server error.
 ** message **
An internal service error occurred. Retry your request. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The specified resource was not found. Verify the resource identifier and ensure the resource exists and is in an ACTIVE state.
 ** resourceArn **
The unique identifier in the format of Amazon Resource Name (ARN) for the resource couldn't be found.
HTTP Status Code: 400

 [ServiceQuotaExceededException](API_ServiceQuotaExceededException.md)
The operation exceeded the service quota for this resource. For more information on service quotas, see [Quotas](https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html) in the *Amazon Keyspaces Developer Guide*.
 ** message **
The requested operation would exceed the service quota for this resource. Review the service quotas and adjust your request accordingly.
HTTP Status Code: 400

 [ValidationException](API_ValidationException.md)
The operation failed due to an invalid or malformed request.
 ** message **
The request parameters are invalid or malformed. Review the API documentation and correct the request format.
HTTP Status Code: 400

## See Also
<a name="API_GetType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/keyspaces-2022-02-10/GetType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/keyspaces-2022-02-10/GetType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/GetType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/keyspaces-2022-02-10/GetType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/GetType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/keyspaces-2022-02-10/GetType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/keyspaces-2022-02-10/GetType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/keyspaces-2022-02-10/GetType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/keyspaces-2022-02-10/GetType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/GetType)
