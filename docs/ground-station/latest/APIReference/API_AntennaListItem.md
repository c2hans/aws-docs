---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AntennaListItem.html
---

# AntennaListItem
<a name="API_AntennaListItem"></a>

An antenna at a ground station.

## Contents
<a name="API_AntennaListItem_Contents"></a>

 ** antennaName **   <a name="groundstation-Type-AntennaListItem-antennaName"></a>
Name of the antenna.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 256.
Pattern: `[ a-zA-Z0-9-._:=]{4,256}`
Required: Yes

 ** groundStationName **   <a name="groundstation-Type-AntennaListItem-groundStationName"></a>
Name of the ground station the antenna is associated with.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 97.
Pattern: `[ a-zA-Z0-9-._:=]{4,97}`
Required: Yes

 ** region **   <a name="groundstation-Type-AntennaListItem-region"></a>
Region of the antenna.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w-]+`
Required: Yes

## See Also
<a name="API_AntennaListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/AntennaListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/AntennaListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/AntennaListItem)
