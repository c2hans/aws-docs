---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_GetHookResult.html
---

# GetHookResult
<a name="API_GetHookResult"></a>

Retrieves detailed information and remediation guidance for a Hook invocation result.

If the Hook uses a KMS key to encrypt annotations, callers of the `GetHookResult` operation must have `kms:Decrypt` permissions. For more information, see [AWS KMS key policy and permissions for encrypting AWS CloudFormation Hooks results at rest](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-kms-key-policy.html) in the * CloudFormation Hooks User Guide*.

## Request Parameters
<a name="API_GetHookResult_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** HookResultId **
The unique identifier (ID) of the Hook invocation result that you want details about. You can get the ID from the [ListHookResults](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListHookResults.html) operation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

## Response Elements
<a name="API_GetHookResult_ResponseElements"></a>

The following elements are returned by the service.

 **Annotations.member.N**
A list of objects with additional information and guidance that can help you resolve a failed Hook invocation.
Type: Array of [Annotation](API_Annotation.md) objects

 ** FailureMode **
The failure mode of the invocation.
Type: String
Valid Values: `FAIL | WARN`

 ** HookResultId **
The unique identifier of the Hook result.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** HookStatusReason **
A message that provides additional details about the Hook invocation status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** InvocationPoint **
The specific point in the provisioning process where the Hook is invoked.
Type: String
Valid Values: `PRE_PROVISION`

 ** InvokedAt **
The timestamp when the Hook was invoked.
Type: Timestamp

 ** OriginalTypeName **
The original public type name of the Hook when an alias is used.
For example, if you activate `AWS::Hooks::GuardHook` with alias `MyCompany::Custom::GuardHook`, then `TypeName` will be `MyCompany::Custom::GuardHook` and `OriginalTypeName` will be `AWS::Hooks::GuardHook`.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 196.

 ** Status **
The status of the Hook invocation. The following statuses are possible:
+  `HOOK_IN_PROGRESS`: The Hook is currently running.
+  `HOOK_COMPLETE_SUCCEEDED`: The Hook completed successfully.
+  `HOOK_COMPLETE_FAILED`: The Hook completed but failed validation.
+  `HOOK_FAILED`: The Hook encountered an error during execution.
Type: String
Valid Values: `HOOK_IN_PROGRESS | HOOK_COMPLETE_SUCCEEDED | HOOK_COMPLETE_FAILED | HOOK_FAILED`

 ** Target **
Information about the target of the Hook invocation.
Type: [HookTarget](API_HookTarget.md) object

 ** TypeArn **
The Amazon Resource Name (ARN) of the Hook.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/hook/[A-Za-z0-9-]+/?`

 ** TypeConfigurationVersionId **
The version identifier of the Hook configuration data that was used during invocation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-]+`

 ** TypeName **
The name of the Hook that was invoked.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 196.

 ** TypeVersionId **
The version identifier of the Hook that was invoked.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-]+`

## Errors
<a name="API_GetHookResult_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** HookResultNotFound **
The specified target doesn't have any requested Hook invocations.
HTTP Status Code: 404

## See Also
<a name="API_GetHookResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/GetHookResult)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/GetHookResult)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/GetHookResult)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/GetHookResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/GetHookResult)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/GetHookResult)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/GetHookResult)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/GetHookResult)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/GetHookResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/GetHookResult)
