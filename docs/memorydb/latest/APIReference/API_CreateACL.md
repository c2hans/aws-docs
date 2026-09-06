---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateACL.html
---

# CreateACL
<a name="API_CreateACL"></a>

Creates an Access Control List. For more information, see [Authenticating users with Access Contol Lists (ACLs)](https://docs.aws.amazon.com/MemoryDB/latest/devguide/clusters.acls.html).

## Request Syntax
<a name="API_CreateACL_RequestSyntax"></a>

```
{
   "ACLName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "UserNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_CreateACL_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ACLName](#API_CreateACL_RequestSyntax) **   <a name="MemoryDB-CreateACL-request-ACLName"></a>
The name of the Access Control List. This value is stored as a lowercase string.
Type: String
Required: Yes

 ** [Tags](#API_CreateACL_RequestSyntax) **   <a name="MemoryDB-CreateACL-request-Tags"></a>
A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** [UserNames](#API_CreateACL_RequestSyntax) **   <a name="MemoryDB-CreateACL-request-UserNames"></a>
The list of users that belong to the Access Control List.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

## Response Syntax
<a name="API_CreateACL_ResponseSyntax"></a>

```
{
   "ACL": {
      "ARN": "string",
      "Clusters": [ "string" ],
      "MinimumEngineVersion": "string",
      "Name": "string",
      "PendingChanges": {
         "UserNamesToAdd": [ "string" ],
         "UserNamesToRemove": [ "string" ]
      },
      "Status": "string",
      "UserNames": [ "string" ]
   }
}
```

## Response Elements
<a name="API_CreateACL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ACL](#API_CreateACL_ResponseSyntax) **   <a name="MemoryDB-CreateACL-response-ACL"></a>
The newly-created Access Control List.
Type: [ACL](API_ACL.md) object

## Errors
<a name="API_CreateACL_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ACLAlreadyExistsFault **

HTTP Status Code: 400

 ** ACLQuotaExceededFault **

HTTP Status Code: 400

 ** DefaultUserRequired **

HTTP Status Code: 400

 ** DuplicateUserNameFault **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** TagQuotaPerResourceExceeded **

HTTP Status Code: 400

 ** UserNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_CreateACL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/CreateACL)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/CreateACL)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/CreateACL)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/CreateACL)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/CreateACL)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/CreateACL)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/CreateACL)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/CreateACL)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/CreateACL)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/CreateACL)
