---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteACL.html
---

# DeleteACL
<a name="API_DeleteACL"></a>

Deletes an Access Control List. The ACL must first be disassociated from the cluster before it can be deleted. For more information, see [Authenticating users with Access Contol Lists (ACLs)](https://docs.aws.amazon.com/MemoryDB/latest/devguide/clusters.acls.html).

## Request Syntax
<a name="API_DeleteACL_RequestSyntax"></a>

```
{
   "ACLName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteACL_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ACLName](#API_DeleteACL_RequestSyntax) **   <a name="MemoryDB-DeleteACL-request-ACLName"></a>
The name of the Access Control List to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteACL_ResponseSyntax"></a>

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
<a name="API_DeleteACL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ACL](#API_DeleteACL_ResponseSyntax) **   <a name="MemoryDB-DeleteACL-response-ACL"></a>
The Access Control List object that has been deleted.
Type: [ACL](API_ACL.md) object

## Errors
<a name="API_DeleteACL_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ACLNotFoundFault **

HTTP Status Code: 400

 ** InvalidACLStateFault **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

## See Also
<a name="API_DeleteACL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DeleteACL)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DeleteACL)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DeleteACL)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DeleteACL)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DeleteACL)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DeleteACL)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DeleteACL)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DeleteACL)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DeleteACL)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DeleteACL)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
