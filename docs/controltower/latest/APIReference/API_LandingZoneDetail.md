---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_LandingZoneDetail.html
---

# LandingZoneDetail
<a name="API_LandingZoneDetail"></a>

Information about the landing zone.

## Contents
<a name="API_LandingZoneDetail_Contents"></a>

 ** manifest **   <a name="controltower-Type-LandingZoneDetail-manifest"></a>
The landing zone manifest JSON text file that specifies the landing zone configurations.
Type: JSON value
Required: Yes

 ** version **   <a name="controltower-Type-LandingZoneDetail-version"></a>
The landing zone's current deployed version.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 10.
Pattern: `\d+.\d+`
Required: Yes

 ** arn **   <a name="controltower-Type-LandingZoneDetail-arn"></a>
The ARN of the landing zone.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** driftStatus **   <a name="controltower-Type-LandingZoneDetail-driftStatus"></a>
The drift status of the landing zone.
Type: [LandingZoneDriftStatusSummary](API_LandingZoneDriftStatusSummary.md) object
Required: No

 ** latestAvailableVersion **   <a name="controltower-Type-LandingZoneDetail-latestAvailableVersion"></a>
The latest available version of the landing zone.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 10.
Pattern: `\d+.\d+`
Required: No

 ** remediationTypes **   <a name="controltower-Type-LandingZoneDetail-remediationTypes"></a>
The types of remediation actions configured for the landing zone, such as automatic drift correction or compliance enforcement.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `INHERITANCE_DRIFT`
Required: No

 ** status **   <a name="controltower-Type-LandingZoneDetail-status"></a>
The landing zone deployment status. One of `ACTIVE`, `PROCESSING`, `FAILED`.
Type: String
Valid Values: `ACTIVE | PROCESSING | FAILED`
Required: No

## See Also
<a name="API_LandingZoneDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/LandingZoneDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/LandingZoneDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/LandingZoneDetail)
