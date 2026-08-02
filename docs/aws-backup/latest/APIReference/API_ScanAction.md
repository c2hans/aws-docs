---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ScanAction.html
---

# ScanAction
<a name="API_ScanAction"></a>

Defines a scanning action that specifies the malware scanner and scan mode to use.

## Contents
<a name="API_ScanAction_Contents"></a>

 ** MalwareScanner **   <a name="Backup-Type-ScanAction-MalwareScanner"></a>
The malware scanner to use for the scan action. Currently only `GUARDDUTY` is supported.
Type: String
Valid Values: `GUARDDUTY`
Required: No

 ** ScanMode **   <a name="Backup-Type-ScanAction-ScanMode"></a>
The scanning mode to use for the scan action.
Valid values: `FULL_SCAN` \| `INCREMENTAL_SCAN`.
Type: String
Valid Values: `FULL_SCAN | INCREMENTAL_SCAN`
Required: No

## See Also
<a name="API_ScanAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ScanAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ScanAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ScanAction)
