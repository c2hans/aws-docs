---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GroundStationData.html
---

# GroundStationData
<a name="API_GroundStationData"></a>

Information about the ground station data.

## Contents
<a name="API_GroundStationData_Contents"></a>

 ** groundStationId **   <a name="groundstation-Type-GroundStationData-groundStationId"></a>
ID of a ground station.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 97.
Pattern: `[ a-zA-Z0-9-._:=]{4,97}`
Required: No

 ** groundStationName **   <a name="groundstation-Type-GroundStationData-groundStationName"></a>
Name of a ground station.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 97.
Pattern: `[ a-zA-Z0-9-._:=]{4,97}`
Required: No

 ** region **   <a name="groundstation-Type-GroundStationData-region"></a>
Ground station Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w-]+`
Required: No

## See Also
<a name="API_GroundStationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/GroundStationData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/GroundStationData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/GroundStationData)
