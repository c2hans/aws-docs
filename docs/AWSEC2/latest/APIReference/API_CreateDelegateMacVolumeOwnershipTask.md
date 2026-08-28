---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDelegateMacVolumeOwnershipTask.html
---

# CreateDelegateMacVolumeOwnershipTask
<a name="API_CreateDelegateMacVolumeOwnershipTask"></a>

Delegates ownership of the Amazon EBS root volume for an Apple silicon Mac instance to an administrative user.

## Request Parameters
<a name="API_CreateDelegateMacVolumeOwnershipTask_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId**
The ID of the Amazon EC2 Mac instance.
Type: String
Required: Yes

 **MacCredentials**
Specifies the following credentials:
+  **Internal disk administrative user**
  +  **Username** - Only the default administrative user (`aws-managed-user`) is supported and it is used by default. You can't specify a different administrative user.
  +  **Password** - If you did not change the default password for `aws-managed-user`, specify the default password, which is *blank*. Otherwise, specify your password.
+  **Amazon EBS root volume administrative user**
  +  **Username** - If you did not change the default administrative user, specify `ec2-user`. Otherwise, specify the username for your administrative user.
  +  **Password** - Specify the password for the administrative user.
The credentials must be specified in the following JSON format:
 `{ "internalDiskPassword":"internal-disk-admin_password", "rootVolumeUsername":"root-volume-admin_username", "rootVolumepassword":"root-volume-admin_password" }`
Type: String
Required: Yes

 **TagSpecification.N**
The tags to assign to the volume ownership delegation task.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateDelegateMacVolumeOwnershipTask_ResponseElements"></a>

The following elements are returned by the service.

 **macModificationTask**
Information about the volume ownership delegation task.
Type: [MacModificationTask](API_MacModificationTask.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateDelegateMacVolumeOwnershipTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateDelegateMacVolumeOwnershipTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateDelegateMacVolumeOwnershipTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateDelegateMacVolumeOwnershipTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateDelegateMacVolumeOwnershipTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateDelegateMacVolumeOwnershipTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateDelegateMacVolumeOwnershipTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateDelegateMacVolumeOwnershipTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateDelegateMacVolumeOwnershipTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateDelegateMacVolumeOwnershipTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateDelegateMacVolumeOwnershipTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateDelegateMacVolumeOwnershipTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
