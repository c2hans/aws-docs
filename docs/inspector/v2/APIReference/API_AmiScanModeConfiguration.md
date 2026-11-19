---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AmiScanModeConfiguration.html
---

# AmiScanModeConfiguration

The scan mode configuration that determines which Amazon Machine Images (AMIs) are scanned.

## Contents
<a name="API_AmiScanModeConfiguration_Contents"></a>

 ** scanMode **   <a name="inspector2-Type-AmiScanModeConfiguration-scanMode"></a>
The scan mode that determines whether all AMIs are scanned or only those matching the specified tags.
Type: String
Valid Values: `SCAN_ALL | TARGET_SCANNING`
Required: Yes

 ** excludeBackupDlmAmis **   <a name="inspector2-Type-AmiScanModeConfiguration-excludeBackupDlmAmis"></a>
Whether to exclude AMIs created by Amazon Data Lifecycle Manager (DLM) backups from scanning.
Type: Boolean
Required: No

 ** excludeCopiedAmis **   <a name="inspector2-Type-AmiScanModeConfiguration-excludeCopiedAmis"></a>
Whether to exclude AMIs that are copies of other AMIs from scanning.
Type: Boolean
Required: No

 ** tags **   <a name="inspector2-Type-AmiScanModeConfiguration-tags"></a>
The tag filters used to select which AMIs are scanned when using targeted scanning.
Type: Array of [AmiTagFilter](API_AmiTagFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## See Also
<a name="API_AmiScanModeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AmiScanModeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AmiScanModeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AmiScanModeConfiguration)
