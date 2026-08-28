---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_EbsVolumeDetails.html
---

# EbsVolumeDetails
<a name="API_EbsVolumeDetails"></a>

Contains list of scanned and skipped EBS volumes with details.

## Contents
<a name="API_EbsVolumeDetails_Contents"></a>

 ** scannedVolumeDetails **   <a name="guardduty-Type-EbsVolumeDetails-scannedVolumeDetails"></a>
List of EBS volumes that were scanned.
Type: Array of [VolumeDetail](API_VolumeDetail.md) objects
Required: No

 ** skippedVolumeDetails **   <a name="guardduty-Type-EbsVolumeDetails-skippedVolumeDetails"></a>
List of EBS volumes that were skipped from the malware scan.
Type: Array of [VolumeDetail](API_VolumeDetail.md) objects
Required: No

## See Also
<a name="API_EbsVolumeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/EbsVolumeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/EbsVolumeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/EbsVolumeDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
