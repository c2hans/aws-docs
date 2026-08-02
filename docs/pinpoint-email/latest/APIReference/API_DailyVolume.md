---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DailyVolume.html
---

# DailyVolume
<a name="API_DailyVolume"></a>

An object that contains information about the volume of email sent on each day of the analysis period.

## Contents
<a name="API_DailyVolume_Contents"></a>

 ** DomainIspPlacements **   <a name="pinpoint-Type-DailyVolume-DomainIspPlacements"></a>
An object that contains inbox placement metrics for a specified day in the analysis period, broken out by the recipient's email provider.
Type: Array of [DomainIspPlacement](API_DomainIspPlacement.md) objects
Required: No

 ** StartDate **   <a name="pinpoint-Type-DailyVolume-StartDate"></a>
The date that the DailyVolume metrics apply to, in Unix time.
Type: Timestamp
Required: No

 ** VolumeStatistics **   <a name="pinpoint-Type-DailyVolume-VolumeStatistics"></a>
An object that contains inbox placement metrics for a specific day in the analysis period.
Type: [VolumeStatistics](API_VolumeStatistics.md) object
Required: No

## See Also
<a name="API_DailyVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/DailyVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/DailyVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/DailyVolume)
