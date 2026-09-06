---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GeocodePreferenceValue.html
---

# GeocodePreferenceValue
<a name="API_GeocodePreferenceValue"></a>

The preference value for the geocode preference.

## Contents
<a name="API_GeocodePreferenceValue_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Coordinate **   <a name="QS-Type-GeocodePreferenceValue-Coordinate"></a>
The preference coordinate for the geocode preference.
Type: [Coordinate](API_Coordinate.md) object
Required: No

 ** GeocoderHierarchy **   <a name="QS-Type-GeocodePreferenceValue-GeocoderHierarchy"></a>
The preference hierarchy for the geocode preference.
Type: [GeocoderHierarchy](API_GeocoderHierarchy.md) object
Required: No

## See Also
<a name="API_GeocodePreferenceValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GeocodePreferenceValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GeocodePreferenceValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GeocodePreferenceValue)
