---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ScanResourceCriteria.html
---

# ScanResourceCriteria
<a name="API_ScanResourceCriteria"></a>

Contains information about criteria used to filter resources before triggering malware scan.

## Contents
<a name="API_ScanResourceCriteria_Contents"></a>

 ** exclude **   <a name="guardduty-Type-ScanResourceCriteria-exclude"></a>
Represents condition that when matched will prevent a malware scan for a certain resource.
Type: String to [ScanCondition](API_ScanCondition.md) object map
Valid Keys: `EC2_INSTANCE_TAG`
Required: No

 ** include **   <a name="guardduty-Type-ScanResourceCriteria-include"></a>
Represents condition that when matched will allow a malware scan for a certain resource.
Type: String to [ScanCondition](API_ScanCondition.md) object map
Valid Keys: `EC2_INSTANCE_TAG`
Required: No

## See Also
<a name="API_ScanResourceCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ScanResourceCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ScanResourceCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ScanResourceCriteria)
