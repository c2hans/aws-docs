---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ResourceDetails.html
---

# ResourceDetails
<a name="API_automation_ResourceDetails"></a>

Detailed configuration information for a specific AWS resource, with type-specific details.

## Contents
<a name="API_automation_ResourceDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ebsVolume **   <a name="computeoptimizer-Type-automation_ResourceDetails-ebsVolume"></a>
Detailed configuration information specific to EBS volumes, including volume type, size, IOPS, and throughput settings.
Type: [EbsVolume](API_automation_EbsVolume.md) object
Required: No

## See Also
<a name="API_automation_ResourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/ResourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/ResourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/ResourceDetails)
