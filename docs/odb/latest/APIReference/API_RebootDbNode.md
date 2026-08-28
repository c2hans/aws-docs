---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_RebootDbNode.html
---

# RebootDbNode
<a name="API_RebootDbNode"></a>

Reboots the specified DB node in a VM cluster.

## Request Syntax
<a name="API_RebootDbNode_RequestSyntax"></a>

```
{
   "cloudVmClusterId": "{{string}}",
   "dbNodeId": "{{string}}",
   "exadbVmClusterId": "{{string}}"
}
```

## Request Parameters
<a name="API_RebootDbNode_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cloudVmClusterId](#API_RebootDbNode_RequestSyntax) **   <a name="odb-RebootDbNode-request-cloudVmClusterId"></a>
The unique identifier of the VM cluster that contains the DB node to reboot. You must specify either this parameter or `exadbVmClusterId`.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** [dbNodeId](#API_RebootDbNode_RequestSyntax) **   <a name="odb-RebootDbNode-request-dbNodeId"></a>
The unique identifier of the DB node to reboot.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: Yes

 ** [exadbVmClusterId](#API_RebootDbNode_RequestSyntax) **   <a name="odb-RebootDbNode-request-exadbVmClusterId"></a>
The unique identifier of the Exascale VM cluster that contains the DB node to reboot. You must specify either this parameter or `cloudVmClusterId`.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

## Response Syntax
<a name="API_RebootDbNode_ResponseSyntax"></a>

```
{
   "dbNodeId": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_RebootDbNode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dbNodeId](#API_RebootDbNode_ResponseSyntax) **   <a name="odb-RebootDbNode-response-dbNodeId"></a>
The unique identifier of the DB node that was rebooted.
Type: String

 ** [status](#API_RebootDbNode_ResponseSyntax) **   <a name="odb-RebootDbNode-response-status"></a>
The current status of the DB node after the reboot operation.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | STOPPING | STOPPED | STARTING`

 ** [statusReason](#API_RebootDbNode_ResponseSyntax) **   <a name="odb-RebootDbNode-response-statusReason"></a>
Additional information about the status of the DB node after the reboot operation.
Type: String

## Errors
<a name="API_RebootDbNode_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_RebootDbNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/RebootDbNode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/RebootDbNode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/RebootDbNode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/RebootDbNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/RebootDbNode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/RebootDbNode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/RebootDbNode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/RebootDbNode)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/RebootDbNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/RebootDbNode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
