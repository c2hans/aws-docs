---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_CreateType.html
---

# CreateType
<a name="API_CreateType"></a>

 The `CreateType` operation creates a new user-defined type in the specified keyspace.

To configure the required permissions, see [Permissions to create a UDT](https://docs.aws.amazon.com/keyspaces/latest/devguide/configure-udt-permissions.html#udt-permissions-create) in the *Amazon Keyspaces Developer Guide*.

For more information, see [User-defined types (UDTs)](https://docs.aws.amazon.com/keyspaces/latest/devguide/udts.html) in the *Amazon Keyspaces Developer Guide*.

## Request Syntax
<a name="API_CreateType_RequestSyntax"></a>

```
{
   "fieldDefinitions": [
      {
         "name": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "keyspaceName": "{{string}}",
   "typeName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [fieldDefinitions](#API_CreateType_RequestSyntax) **   <a name="keyspaces-CreateType-request-fieldDefinitions"></a>
 The field definitions, consisting of names and types, that define this type.
Type: Array of [FieldDefinition](API_FieldDefinition.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [keyspaceName](#API_CreateType_RequestSyntax) **   <a name="keyspaces-CreateType-request-keyspaceName"></a>
 The name of the keyspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** [typeName](#API_CreateType_RequestSyntax) **   <a name="keyspaces-CreateType-request-typeName"></a>
 The name of the user-defined type.
UDT names must contain 48 characters or less, must begin with an alphabetic character, and can only contain alpha-numeric characters and underscores. Amazon Keyspaces converts upper case characters automatically into lower case characters.
Alternatively, you can declare a UDT name in double quotes. When declaring a UDT name inside double quotes, Amazon Keyspaces preserves upper casing and allows special characters.
You can also use double quotes as part of the name when you create the UDT, but you must escape each double quote character with an additional double quote character.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Required: Yes

## Response Syntax
<a name="API_CreateType_ResponseSyntax"></a>

```
{
   "keyspaceArn": "string",
   "typeName": "string"
}
```

## Response Elements
<a name="API_CreateType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [keyspaceArn](#API_CreateType_ResponseSyntax) **   <a name="keyspaces-CreateType-response-keyspaceArn"></a>
 The unique identifier of the keyspace that contains the new type in the format of an Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1000.
Pattern: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`

 ** [typeName](#API_CreateType_ResponseSyntax) **   <a name="keyspaces-CreateType-response-typeName"></a>
 The formatted name of the user-defined type that was created. Note that Amazon Keyspaces requires the formatted name of the type for other operations, for example `GetType`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.

## Errors
<a name="API_CreateType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have sufficient access permissions to perform this action.
 ** message **
You don't have the required permissions to perform this operation. Verify your IAM permissions and try again.
HTTP Status Code: 400

 [ConflictException](API_ConflictException.md)
Amazon Keyspaces couldn't complete the requested action. This error may occur if you try to perform an action and the same or a different action is already in progress, or if you try to create a resource that already exists.
 ** message **
The requested operation conflicts with the current state of the resource or another concurrent operation.
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
<a name="API_CreateType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/keyspaces-2022-02-10/CreateType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/keyspaces-2022-02-10/CreateType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/CreateType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/keyspaces-2022-02-10/CreateType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/CreateType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/keyspaces-2022-02-10/CreateType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/keyspaces-2022-02-10/CreateType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/keyspaces-2022-02-10/CreateType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/keyspaces-2022-02-10/CreateType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/CreateType)
