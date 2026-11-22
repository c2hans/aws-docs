---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RoleProvisioning.html
---

# RoleProvisioning

Provides visibility into the role provisioning stage of a StackSet operation, including per-account progress counts and a completion percentage. For operations that do not provision IAM roles in target accounts, the `Status` is `NOT_APPLICABLE` and the progress counts are omitted.

## Contents
<a name="API_RoleProvisioning_Contents"></a>

 ** CompletedAccountsCount **
The number of accounts that have finished role provisioning, including both succeeded and failed accounts.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** FailedAccountsCount **
The number of accounts for which role provisioning failed.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PendingAccountsCount **
The number of accounts that are still awaiting role provisioning.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PercentageCompleted **
The percentage of accounts that have completed role provisioning.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Status **
The status of the role provisioning stage can be one of the following values:
+  `NOT_APPLICABLE`: The operation does not provision roles. This includes self-managed operations and service-managed operations whose configuration does not require role provisioning.
+  `NOT_STARTED`: Role provisioning has not started. The operation has not begun resolving target accounts, or it failed or stopped before the total number of target accounts was resolved.
+  `IN_PROGRESS`: Role provisioning is actively processing target accounts.
+  `SUCCEEDED`: Role provisioning finished and succeeded for all target accounts.
+  `PARTIAL_SUCCESS`: Role provisioning finished, but succeeded for only a subset of target accounts; one or more accounts failed.
+  `FAILED`: Role provisioning finished and failed for all target accounts.
Type: String
Valid Values: `PENDING | NOT_APPLICABLE | NOT_STARTED | IN_PROGRESS | SUCCEEDED | PARTIAL_SUCCESS | FAILED`
Required: No

 ** SucceededAccountsCount **
The number of accounts for which role provisioning succeeded.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_RoleProvisioning_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RoleProvisioning)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RoleProvisioning)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RoleProvisioning)
