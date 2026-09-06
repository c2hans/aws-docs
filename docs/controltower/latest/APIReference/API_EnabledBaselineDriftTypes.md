---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledBaselineDriftTypes.html
---

# EnabledBaselineDriftTypes
<a name="API_EnabledBaselineDriftTypes"></a>

The types of drift that can be detected for an enabled baseline.
+  AWS Control Tower detects inheritance drift on the enabled baselines that target OUs: `AWSControlTowerBaseline` and `BackupBaseline`.
+  AWS Control Tower does not detect drift on the baselines that apply to your landing zone: `IdentityCenterBaseline`, `AuditBaseline`, `LogArchiveBaseline`, `BackupCentralVaultBaseline`, or `BackupAdminBaseline`. For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html).

Baselines enabled on an OU are inherited by its member accounts as child `EnabledBaseline` resources. The baseline on the OU serves as the parent `EnabledBaseline`, which governs the configuration of each child `EnabledBaseline`.

If the baseline configuration of a member account in an OU does not match the configuration of the parent OU, the parent and child baseline is in a state of inheritance drift. This drift could occur in the `AWSControlTowerBaseline` or the `BackupBaseline` related to that account.

## Contents
<a name="API_EnabledBaselineDriftTypes_Contents"></a>

 ** inheritance **   <a name="controltower-Type-EnabledBaselineDriftTypes-inheritance"></a>
At least one account within the target OU does not match the baseline configuration defined on that OU. An account is in inheritance drift when it does not match the configuration of a parent OU, possibly a new parent OU, if the account is moved.
Type: [EnabledBaselineInheritanceDrift](API_EnabledBaselineInheritanceDrift.md) object
Required: No

## See Also
<a name="API_EnabledBaselineDriftTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/EnabledBaselineDriftTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/EnabledBaselineDriftTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/EnabledBaselineDriftTypes)
