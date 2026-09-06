---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateUser.html
---

# UpdateUser
<a name="API_UpdateUser"></a>

Changes user password(s) and/or access string.

## Request Syntax
<a name="API_UpdateUser_RequestSyntax"></a>

```
{
   "AccessString": "{{string}}",
   "AuthenticationMode": {
      "Passwords": [ "{{string}}" ],
      "Type": "{{string}}"
   },
   "UserName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateUser_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessString](#API_UpdateUser_RequestSyntax) **   <a name="MemoryDB-UpdateUser-request-AccessString"></a>
Access permissions string used for this user.
Type: String
Pattern: `.*\S.*`
Required: No

 ** [AuthenticationMode](#API_UpdateUser_RequestSyntax) **   <a name="MemoryDB-UpdateUser-request-AuthenticationMode"></a>
Denotes the user's authentication properties, such as whether it requires a password to authenticate.
Type: [AuthenticationMode](API_AuthenticationMode.md) object
Required: No

 ** [UserName](#API_UpdateUser_RequestSyntax) **   <a name="MemoryDB-UpdateUser-request-UserName"></a>
The name of the user
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: Yes

## Response Syntax
<a name="API_UpdateUser_ResponseSyntax"></a>

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
<a name="API_UpdateUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [User](#API_UpdateUser_ResponseSyntax) **   <a name="MemoryDB-UpdateUser-response-User"></a>
The updated user
Type: [User](API_User.md) object

## Errors
<a name="API_UpdateUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** InvalidUserStateFault **

HTTP Status Code: 400

 ** UserNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_UpdateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/UpdateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/UpdateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/UpdateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/UpdateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/UpdateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/UpdateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/UpdateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/UpdateUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/UpdateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/UpdateUser)
