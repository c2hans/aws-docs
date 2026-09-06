---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsBackupRecoveryPointLifecycleDetails.html
---

# AwsBackupRecoveryPointLifecycleDetails
<a name="API_AwsBackupRecoveryPointLifecycleDetails"></a>

Contains an array of Transition objects specifying how long in days before a recovery point transitions to cold storage or is deleted.

## Contents
<a name="API_AwsBackupRecoveryPointLifecycleDetails_Contents"></a>

 ** DeleteAfterDays **   <a name="securityhub-Type-AwsBackupRecoveryPointLifecycleDetails-DeleteAfterDays"></a>
Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus `MoveToColdStorageAfterDays`.
Type: Long
Required: No

 ** MoveToColdStorageAfterDays **   <a name="securityhub-Type-AwsBackupRecoveryPointLifecycleDetails-MoveToColdStorageAfterDays"></a>
Specifies the number of days after creation that a recovery point is moved to cold storage.
Type: Long
Required: No

## See Also
<a name="API_AwsBackupRecoveryPointLifecycleDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsBackupRecoveryPointLifecycleDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsBackupRecoveryPointLifecycleDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsBackupRecoveryPointLifecycleDetails)
