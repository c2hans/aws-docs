---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegionalStackInstancesDeployment.html
---

# RegionalStackInstancesDeployment

Provides visibility into the stack instances deployment stage for a single Region, including per-stack-instance progress counts and a completion percentage for that Region.

## Contents
<a name="API_RegionalStackInstancesDeployment_Contents"></a>

 ** CancelledStackInstancesCount **
The number of stack instances in this Region that were canceled because the operation exceeded its failure tolerance or was stopped.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** CompletedStackInstancesCount **
The number of stack instances in this Region that have reached a final state. This count includes stack instances that succeeded, failed, were skipped, or were canceled.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** FailedStackInstancesCount **
The number of stack instances that failed to deploy in this Region.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PendingStackInstancesCount **
The number of stack instances in this Region that have not reached a final state. This is the total number of stack instances in this Region minus the completed count.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PercentageCompleted **
The percentage of stack instances in this Region that have reached a final state.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** SkippedStackInstancesCount **
The number of stack instances in this Region that were skipped because role provisioning failed for their target account.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Status **
The status of the stack instances deployment stage can be one of the following values:
+  `NOT_APPLICABLE`: The operation does not deploy stack instances, such as a drift detection operation.
+  `NOT_STARTED`: Stack instances deployment has not started. The operation is still provisioning roles, has not begun, or failed before this stage was reached.
+  `IN_PROGRESS`: At least one stack instance has started deploying.
+  `SUCCEEDED`: Deployment finished and succeeded for all stack instances that were not skipped.
+  `PARTIAL_SUCCESS`: Deployment finished with a mix of succeeded, failed, and canceled stack instances.
+  `FAILED`: Deployment finished and every stack instance that was not skipped failed or was canceled.
Type: String
Valid Values: `PENDING | NOT_APPLICABLE | NOT_STARTED | IN_PROGRESS | SUCCEEDED | PARTIAL_SUCCESS | FAILED`
Required: No

 ** SucceededStackInstancesCount **
The number of stack instances that deployed successfully in this Region.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TotalStackInstancesCount **
The total number of stack instances targeted by this operation in this Region.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_RegionalStackInstancesDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RegionalStackInstancesDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RegionalStackInstancesDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RegionalStackInstancesDeployment)
