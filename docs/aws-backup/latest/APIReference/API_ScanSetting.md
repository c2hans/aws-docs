---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ScanSetting.html
---

# ScanSetting
<a name="API_ScanSetting"></a>

Contains configuration settings for malware scanning, including the scanner type, target resource types, and scanner role.

## Contents
<a name="API_ScanSetting_Contents"></a>

 ** MalwareScanner **   <a name="Backup-Type-ScanSetting-MalwareScanner"></a>
The malware scanner to use for scanning. Currently only `GUARDDUTY` is supported.
Type: String
Valid Values: `GUARDDUTY`
Required: No

 ** ResourceTypes **   <a name="Backup-Type-ScanSetting-ResourceTypes"></a>
An array of resource types to be scanned for malware.
Type: Array of strings
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Required: No

 ** ScannerRoleArn **   <a name="Backup-Type-ScanSetting-ScannerRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that the scanner uses to access resources; for example, `arn:aws:iam::123456789012:role/ScannerRole`.
Type: String
Required: No

## See Also
<a name="API_ScanSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ScanSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ScanSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ScanSetting)
