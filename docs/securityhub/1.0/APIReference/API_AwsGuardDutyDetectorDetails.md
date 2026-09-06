---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsGuardDutyDetectorDetails.html
---

# AwsGuardDutyDetectorDetails
<a name="API_AwsGuardDutyDetectorDetails"></a>

 Provides details about an Amazon GuardDuty detector. A detector is an object that represents the GuardDuty service. A detector is required for GuardDuty to become operational.

## Contents
<a name="API_AwsGuardDutyDetectorDetails_Contents"></a>

 ** DataSources **   <a name="securityhub-Type-AwsGuardDutyDetectorDetails-DataSources"></a>
 Describes which data sources are activated for the detector.
Type: [AwsGuardDutyDetectorDataSourcesDetails](API_AwsGuardDutyDetectorDataSourcesDetails.md) object
Required: No

 ** Features **   <a name="securityhub-Type-AwsGuardDutyDetectorDetails-Features"></a>
 Describes which features are activated for the detector.
Type: Array of [AwsGuardDutyDetectorFeaturesDetails](API_AwsGuardDutyDetectorFeaturesDetails.md) objects
Required: No

 ** FindingPublishingFrequency **   <a name="securityhub-Type-AwsGuardDutyDetectorDetails-FindingPublishingFrequency"></a>
 The publishing frequency of the finding.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ServiceRole **   <a name="securityhub-Type-AwsGuardDutyDetectorDetails-ServiceRole"></a>
 The GuardDuty service role.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsGuardDutyDetectorDetails-Status"></a>
 The activation status of the detector.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsGuardDutyDetectorDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsGuardDutyDetectorDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsGuardDutyDetectorDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsGuardDutyDetectorDetails)
