---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteUser.html
---

# DeleteUser
<a name="API_DeleteUser"></a>

Deletes a user. The user will be removed from all ACLs and in turn removed from all clusters.

## Request Syntax
<a name="API_DeleteUser_RequestSyntax"></a>

```
{
   "UserName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteUser_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [UserName](#API_DeleteUser_RequestSyntax) **   <a name="MemoryDB-DeleteUser-request-UserName"></a>
The name of the user to delete
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: Yes

## Response Syntax
<a name="API_DeleteUser_ResponseSyntax"></a>

```
{
   "User": {
      "AccessString": "string",
      "ACLNames": [ "string" ],
      "ARN": "string",
      "Authentication": {
         "PasswordCount": number,
         "Type": "string"
      },
      "MinimumEngineVersion": "string",
      "Name": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_DeleteUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [User](#API_DeleteUser_ResponseSyntax) **   <a name="MemoryDB-DeleteUser-response-User"></a>
The user object that has been deleted.
Type: [User](API_User.md) object

## Errors
<a name="API_DeleteUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** InvalidUserStateFault **

HTTP Status Code: 400

 ** UserNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_DeleteUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DeleteUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DeleteUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DeleteUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DeleteUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DeleteUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DeleteUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DeleteUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DeleteUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DeleteUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DeleteUser)
