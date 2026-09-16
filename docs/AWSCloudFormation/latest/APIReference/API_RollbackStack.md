---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RollbackStack.html
---

# RollbackStack
<a name="API_RollbackStack"></a>

When specifying `RollbackStack`, you preserve the state of previously provisioned resources when an operation fails. You can check the status of the stack through the [DescribeStacks](API_DescribeStacks.md) operation.

Rolls back the specified stack to the last known stable state from `CREATE_FAILED` or `UPDATE_FAILED` stack statuses.

This operation will delete a stack if it doesn't contain a last known stable state. A last known stable state includes any status in a `*_COMPLETE`. This includes the following stack statuses.
+  `CREATE_COMPLETE`
+  `UPDATE_COMPLETE`
+  `UPDATE_ROLLBACK_COMPLETE`
+  `IMPORT_COMPLETE`
+  `IMPORT_ROLLBACK_COMPLETE`

## Request Parameters
<a name="API_RollbackStack_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClientRequestToken **
A unique identifier for this `RollbackStack` request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`
Required: No

 ** RetainExceptOnCreate **
When set to `true`, newly created resources are deleted when the operation rolls back. This includes newly created resources marked with a deletion policy of `Retain`.
Default: `false`
Type: Boolean
Required: No

 ** RoleARN **
The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to rollback the stack.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** StackName **
The name that's associated with the stack.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-cn)\b:[-a-zA-Z0-9:/._+]*)`
Required: Yes

## Response Elements
<a name="API_RollbackStack_ResponseElements"></a>

The following elements are returned by the service.

 ** OperationId **
A unique identifier for this rollback operation that can be used to track the operation's progress and events.
Type: String

 ** StackId **
Unique identifier of the stack.
Type: String

## Errors
<a name="API_RollbackStack_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** TokenAlreadyExists **
A client request token already exists.
HTTP Status Code: 400

## See Also
<a name="API_RollbackStack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/RollbackStack)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/RollbackStack)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RollbackStack)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/RollbackStack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RollbackStack)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/RollbackStack)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/RollbackStack)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/RollbackStack)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/RollbackStack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RollbackStack)
