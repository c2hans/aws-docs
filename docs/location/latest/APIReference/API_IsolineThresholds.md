---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineThresholds.html
---

# IsolineThresholds
<a name="API_IsolineThresholds"></a>

Specifies the time or distance limits used to calculate reachable areas. You can provide up to five thresholds for a single type to generate multiple isolines in a single request. For example, you might request areas reachable within 5, 10, and 15 minutes, or within 1, 2, and 5 kilometers.

## Contents
<a name="API_IsolineThresholds_Contents"></a>

 ** Distance **   <a name="location-Type-IsolineThresholds-Distance"></a>
List of travel distances in meters. For example, [1000, 2000, 5000] would calculate areas reachable within 1, 2, and 5 kilometers.
Type: Array of longs
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Range: Minimum value of 0. Maximum value of 300000.
Required: No

 ** Time **   <a name="location-Type-IsolineThresholds-Time"></a>
List of travel times in seconds. For example, [300, 600, 900] would calculate areas reachable within 5, 10, and 15 minutes.
Type: Array of longs
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Range: Minimum value of 0. Maximum value of 10800.
Required: No

## See Also
<a name="API_IsolineThresholds_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineThresholds)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineThresholds)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineThresholds)
