---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateACL.html
---

# UpdateACL
<a name="API_UpdateACL"></a>

Changes the list of users that belong to the Access Control List.

## Request Syntax
<a name="API_UpdateACL_RequestSyntax"></a>

```
{
   "ACLName": "{{string}}",
   "UserNamesToAdd": [ "{{string}}" ],
   "UserNamesToRemove": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateACL_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ACLName](#API_UpdateACL_RequestSyntax) **   <a name="MemoryDB-UpdateACL-request-ACLName"></a>
The name of the Access Control List.
Type: String
Required: Yes

 ** [UserNamesToAdd](#API_UpdateACL_RequestSyntax) **   <a name="MemoryDB-UpdateACL-request-UserNamesToAdd"></a>
The list of users to add to the Access Control List.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

 ** [UserNamesToRemove](#API_UpdateACL_RequestSyntax) **   <a name="MemoryDB-UpdateACL-request-UserNamesToRemove"></a>
The list of users to remove from the Access Control List.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

## Response Syntax
<a name="API_UpdateACL_ResponseSyntax"></a>

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
<a name="API_UpdateACL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ACL](#API_UpdateACL_ResponseSyntax) **   <a name="MemoryDB-UpdateACL-response-ACL"></a>
The updated Access Control List.
Type: [ACL](API_ACL.md) object

## Errors
<a name="API_UpdateACL_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ACLNotFoundFault **

HTTP Status Code: 400

 ** DefaultUserRequired **

HTTP Status Code: 400

 ** DuplicateUserNameFault **

HTTP Status Code: 400

 ** InvalidACLStateFault **

HTTP Status Code: 400

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** UserNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_UpdateACL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/UpdateACL)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/UpdateACL)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/UpdateACL)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/UpdateACL)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/UpdateACL)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/UpdateACL)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/UpdateACL)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/UpdateACL)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/UpdateACL)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/UpdateACL)
