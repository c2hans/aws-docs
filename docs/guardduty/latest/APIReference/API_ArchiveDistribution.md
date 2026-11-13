---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ArchiveDistribution.html
---

# ArchiveDistribution
<a name="API_ArchiveDistribution"></a>

Contains the number and percentage of archived and unarchived findings.

## Contents
<a name="API_ArchiveDistribution_Contents"></a>

 ** archivedCount **   <a name="guardduty-Type-ArchiveDistribution-archivedCount"></a>
The number of archived findings.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** archivedPercentage **   <a name="guardduty-Type-ArchiveDistribution-archivedPercentage"></a>
The percentage of findings that are archived, from 0 to 100.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** unarchivedCount **   <a name="guardduty-Type-ArchiveDistribution-unarchivedCount"></a>
The number of unarchived findings.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** unarchivedPercentage **   <a name="guardduty-Type-ArchiveDistribution-unarchivedPercentage"></a>
The percentage of findings that are unarchived, from 0 to 100.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_ArchiveDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ArchiveDistribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ArchiveDistribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ArchiveDistribution)
