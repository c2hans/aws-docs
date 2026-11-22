---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_StackSetOperationStatusDetails.html
---

# StackSetOperationStatusDetails

Detailed information about the StackSet operation.

## Contents
<a name="API_StackSetOperationStatusDetails_Contents"></a>

 ** FailedStackInstancesCount **
The number of stack instances for which the StackSet operation failed.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Stages **
The detailed progress information for the individual stages of the StackSet operation: the role provisioning stage and the stack instances deployment stage.
Type: [Stages](API_Stages.md) object
Required: No

 ** TotalAccountsCount **
The total number of accounts targeted by this StackSet operation. Self-managed operations and service-managed operations that do not provision roles also report this value when it is known. AWS CloudFormation populates this value after it resolves the target accounts. Until then, this field is not present.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TotalStackInstancesCount **
The total number of stack instances targeted by this StackSet operation. AWS CloudFormation populates this value after it resolves the target stack instances. Until then, this field is not present.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_StackSetOperationStatusDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSetOperationStatusDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSetOperationStatusDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSetOperationStatusDetails)
