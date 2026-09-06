---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_StopDbNode.html
---

# StopDbNode
<a name="API_StopDbNode"></a>

Stops the specified DB node in a VM cluster.

## Request Syntax
<a name="API_StopDbNode_RequestSyntax"></a>

```
{
   "cloudVmClusterId": "{{string}}",
   "dbNodeId": "{{string}}",
   "exadbVmClusterId": "{{string}}"
}
```

## Request Parameters
<a name="API_StopDbNode_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cloudVmClusterId](#API_StopDbNode_RequestSyntax) **   <a name="odb-StopDbNode-request-cloudVmClusterId"></a>
The unique identifier of the VM cluster that contains the DB node to stop. You must specify either this parameter or `exadbVmClusterId`.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** [dbNodeId](#API_StopDbNode_RequestSyntax) **   <a name="odb-StopDbNode-request-dbNodeId"></a>
The unique identifier of the DB node to stop.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: Yes

 ** [exadbVmClusterId](#API_StopDbNode_RequestSyntax) **   <a name="odb-StopDbNode-request-exadbVmClusterId"></a>
The unique identifier of the Exascale VM cluster that contains the DB node to stop. You must specify either this parameter or `cloudVmClusterId`.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

## Response Syntax
<a name="API_StopDbNode_ResponseSyntax"></a>

```
{
   "dbNodeId": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_StopDbNode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dbNodeId](#API_StopDbNode_ResponseSyntax) **   <a name="odb-StopDbNode-response-dbNodeId"></a>
The unique identifier of the DB node that was stopped.
Type: String

 ** [status](#API_StopDbNode_ResponseSyntax) **   <a name="odb-StopDbNode-response-status"></a>
The current status of the DB node after the stop operation.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | STOPPING | STOPPED | STARTING`

 ** [statusReason](#API_StopDbNode_ResponseSyntax) **   <a name="odb-StopDbNode-response-statusReason"></a>
Additional information about the status of the DB node after the stop operation.
Type: String

## Errors
<a name="API_StopDbNode_Errors"></a>

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
<a name="API_StopDbNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/StopDbNode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/StopDbNode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/StopDbNode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/StopDbNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/StopDbNode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/StopDbNode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/StopDbNode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/StopDbNode)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/StopDbNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/StopDbNode)
