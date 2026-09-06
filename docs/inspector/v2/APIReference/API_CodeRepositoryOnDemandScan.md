---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeRepositoryOnDemandScan.html
---

# CodeRepositoryOnDemandScan
<a name="API_CodeRepositoryOnDemandScan"></a>

Contains information about on-demand scans performed on a code repository.

## Contents
<a name="API_CodeRepositoryOnDemandScan_Contents"></a>

 ** lastScanAt **   <a name="inspector2-Type-CodeRepositoryOnDemandScan-lastScanAt"></a>
The timestamp when the last on-demand scan was performed.
Type: Timestamp
Required: No

 ** lastScannedCommitId **   <a name="inspector2-Type-CodeRepositoryOnDemandScan-lastScannedCommitId"></a>
The ID of the last commit that was scanned during an on-demand scan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40.
Pattern: `([a-f0-9]{40})`
Required: No

 ** scanStatus **   <a name="inspector2-Type-CodeRepositoryOnDemandScan-scanStatus"></a>
The status of the scan.
Type: [ScanStatus](API_ScanStatus.md) object
Required: No

## See Also
<a name="API_CodeRepositoryOnDemandScan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CodeRepositoryOnDemandScan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CodeRepositoryOnDemandScan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CodeRepositoryOnDemandScan)
