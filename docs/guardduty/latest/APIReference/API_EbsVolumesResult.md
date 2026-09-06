---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_EbsVolumesResult.html
---

# EbsVolumesResult
<a name="API_EbsVolumesResult"></a>

Describes the configuration of scanning EBS volumes as a data source.

## Contents
<a name="API_EbsVolumesResult_Contents"></a>

 ** reason **   <a name="guardduty-Type-EbsVolumesResult-reason"></a>
Specifies the reason why scanning EBS volumes (Malware Protection) was not enabled as a data source.
Type: String
Required: No

 ** status **   <a name="guardduty-Type-EbsVolumesResult-status"></a>
Describes whether scanning EBS volumes is enabled as a data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_EbsVolumesResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/EbsVolumesResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/EbsVolumesResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/EbsVolumesResult)
