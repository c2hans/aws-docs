---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_AssociateVirtualMachinesToExadbVmCluster.html
---

# AssociateVirtualMachinesToExadbVmCluster
<a name="API_AssociateVirtualMachinesToExadbVmCluster"></a>

Adds virtual machines to the specified Exascale VM cluster.

## Request Syntax
<a name="API_AssociateVirtualMachinesToExadbVmCluster_RequestSyntax"></a>

```
{
   "desiredNodeCount": {{number}},
   "exadbVmClusterId": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateVirtualMachinesToExadbVmCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [desiredNodeCount](#API_AssociateVirtualMachinesToExadbVmCluster_RequestSyntax) **   <a name="odb-AssociateVirtualMachinesToExadbVmCluster-request-desiredNodeCount"></a>
The desired number of nodes in the Exascale VM cluster after the association.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** [exadbVmClusterId](#API_AssociateVirtualMachinesToExadbVmCluster_RequestSyntax) **   <a name="odb-AssociateVirtualMachinesToExadbVmCluster-request-exadbVmClusterId"></a>
The unique identifier of the Exascale VM cluster to add virtual machines to.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

## Response Syntax
<a name="API_AssociateVirtualMachinesToExadbVmCluster_ResponseSyntax"></a>

```
{
   "displayName": "string",
   "exadbVmClusterId": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_AssociateVirtualMachinesToExadbVmCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [displayName](#API_AssociateVirtualMachinesToExadbVmCluster_ResponseSyntax) **   <a name="odb-AssociateVirtualMachinesToExadbVmCluster-response-displayName"></a>
The user-friendly name for the Exascale VM cluster.
Type: String

 ** [exadbVmClusterId](#API_AssociateVirtualMachinesToExadbVmCluster_ResponseSyntax) **   <a name="odb-AssociateVirtualMachinesToExadbVmCluster-response-exadbVmClusterId"></a>
The unique identifier of the Exascale VM cluster.
Type: String

 ** [status](#API_AssociateVirtualMachinesToExadbVmCluster_ResponseSyntax) **   <a name="odb-AssociateVirtualMachinesToExadbVmCluster-response-status"></a>
The current status of the Exascale VM cluster.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_AssociateVirtualMachinesToExadbVmCluster_ResponseSyntax) **   <a name="odb-AssociateVirtualMachinesToExadbVmCluster-response-statusReason"></a>
Additional information about the status of the Exascale VM cluster.
Type: String

## Errors
<a name="API_AssociateVirtualMachinesToExadbVmCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of resource that caused the conflict.
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

 ** ServiceQuotaExceededException **
You have exceeded the service quota.
 ** quotaCode **
The unqiue identifier of the service quota that was exceeded.
 ** resourceId **
The identifier of the resource that exceeded the service quota.
 ** resourceType **
The type of resource that exceeded the service quota.
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
<a name="API_AssociateVirtualMachinesToExadbVmCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/AssociateVirtualMachinesToExadbVmCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/AssociateVirtualMachinesToExadbVmCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/AssociateVirtualMachinesToExadbVmCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/AssociateVirtualMachinesToExadbVmCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/AssociateVirtualMachinesToExadbVmCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/AssociateVirtualMachinesToExadbVmCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/AssociateVirtualMachinesToExadbVmCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/AssociateVirtualMachinesToExadbVmCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/AssociateVirtualMachinesToExadbVmCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/AssociateVirtualMachinesToExadbVmCluster)
