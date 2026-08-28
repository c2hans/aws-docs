---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ScannedResourceDetails.html
---

# ScannedResourceDetails
<a name="API_ScannedResourceDetails"></a>

Contains additional information about a resource that was scanned.

## Contents
<a name="API_ScannedResourceDetails_Contents"></a>

 ** ebsSnapshot **   <a name="guardduty-Type-ScannedResourceDetails-ebsSnapshot"></a>
Contains information about the EBS snapshot that was scanned.
Type: [EbsSnapshot](API_EbsSnapshot.md) object
Required: No

 ** ebsVolume **   <a name="guardduty-Type-ScannedResourceDetails-ebsVolume"></a>
Contains information about the EBS volume that was scanned.
Type: [VolumeDetail](API_VolumeDetail.md) object
Required: No

## See Also
<a name="API_ScannedResourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ScannedResourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ScannedResourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ScannedResourceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
