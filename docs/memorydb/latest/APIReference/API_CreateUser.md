---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateUser.html
---

# CreateUser
<a name="API_CreateUser"></a>

Creates a MemoryDB user. For more information, see [Authenticating users with Access Contol Lists (ACLs)](https://docs.aws.amazon.com/MemoryDB/latest/devguide/clusters.acls.html).

## Request Syntax
<a name="API_CreateUser_RequestSyntax"></a>

```
{
   "AccessString": "{{string}}",
   "AuthenticationMode": {
      "Passwords": [ "{{string}}" ],
      "Type": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "UserName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateUser_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessString](#API_CreateUser_RequestSyntax) **   <a name="MemoryDB-CreateUser-request-AccessString"></a>
Access permissions string used for this user.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [AuthenticationMode](#API_CreateUser_RequestSyntax) **   <a name="MemoryDB-CreateUser-request-AuthenticationMode"></a>
Denotes the user's authentication properties, such as whether it requires a password to authenticate.
Type: [AuthenticationMode](API_AuthenticationMode.md) object
Required: Yes

 ** [Tags](#API_CreateUser_RequestSyntax) **   <a name="MemoryDB-CreateUser-request-Tags"></a>
A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** [UserName](#API_CreateUser_RequestSyntax) **   <a name="MemoryDB-CreateUser-request-UserName"></a>
The name of the user. This value must be unique as it also serves as the user identifier. This value is stored as a lowercase string.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: Yes

## Response Syntax
<a name="API_CreateUser_ResponseSyntax"></a>

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
<a name="API_CreateUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [User](#API_CreateUser_ResponseSyntax) **   <a name="MemoryDB-CreateUser-response-User"></a>
The newly-created user.
Type: [User](API_User.md) object

## Errors
<a name="API_CreateUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateUserNameFault **

HTTP Status Code: 400

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** TagQuotaPerResourceExceeded **

HTTP Status Code: 400

 ** UserAlreadyExistsFault **

HTTP Status Code: 400

 ** UserQuotaExceededFault **

HTTP Status Code: 400

## See Also
<a name="API_CreateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/CreateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/CreateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/CreateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/CreateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/CreateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/CreateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/CreateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/CreateUser)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/CreateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/CreateUser)
