---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineAvoidanceOptions.html
---

# IsolineAvoidanceOptions
<a name="API_IsolineAvoidanceOptions"></a>

Specifies features of the road network to avoid when calculating reachable areas. These preferences guide route calculations but may be overridden when no reasonable alternative exists. For example, if avoiding toll roads would make an area unreachable, toll roads may still be used.

Avoidance options include physical features (like ferries and tunnels), road characteristics (like dirt roads and highways), and regulated areas (like congestion zones). They can be combined to match specific routing needs, such as avoiding both toll roads and ferries.

## Contents
<a name="API_IsolineAvoidanceOptions_Contents"></a>

 ** Areas **   <a name="location-Type-IsolineAvoidanceOptions-Areas"></a>
Specifies geographic areas to avoid where possible. Routes may still pass through these areas if no reasonable alternative exists.
Type: Array of [IsolineAvoidanceArea](API_IsolineAvoidanceArea.md) objects
Required: No

 ** CarShuttleTrains **   <a name="location-Type-IsolineAvoidanceOptions-CarShuttleTrains"></a>
Indicates a preference to avoid car shuttle trains (auto trains) where possible. These may still be included if no reasonable alternative route exists.
Type: Boolean
Required: No

 ** ControlledAccessHighways **   <a name="location-Type-IsolineAvoidanceOptions-ControlledAccessHighways"></a>
Indicates a preference to avoid controlled-access highways (such as interstate highways or motorways) where possible. If a viable route cannot be calculated using only local roads, controlled-access highways may still be included.
Type: Boolean
Required: No

 ** DirtRoads **   <a name="location-Type-IsolineAvoidanceOptions-DirtRoads"></a>
Indicates a preference to avoid unpaved or dirt roads where possible. Routes may still include dirt roads if no reasonable paved alternative exists.
Type: Boolean
Required: No

 ** Ferries **   <a name="location-Type-IsolineAvoidanceOptions-Ferries"></a>
Indicates a preference to avoid ferries where possible. If a viable route cannot be calculated without using ferries, they may still be included.
Type: Boolean
Required: No

 ** SeasonalClosure **   <a name="location-Type-IsolineAvoidanceOptions-SeasonalClosure"></a>
Indicates a preference to avoid roads that may be subject to seasonal closures where possible. These roads may still be included if no reasonable year-round alternative exists.
Type: Boolean
Required: No

 ** TollRoads **   <a name="location-Type-IsolineAvoidanceOptions-TollRoads"></a>
Indicates a preference to avoid toll roads where possible. If a viable route cannot be calculated without using toll roads, they may still be included.
Type: Boolean
Required: No

 ** TollTransponders **   <a name="location-Type-IsolineAvoidanceOptions-TollTransponders"></a>
Indicates a preference to avoid roads that require electronic toll collection transponders where possible. These roads may still be included if no viable alternative route exists.
Type: Boolean
Required: No

 ** TruckRoadTypes **   <a name="location-Type-IsolineAvoidanceOptions-TruckRoadTypes"></a>
For truck travel modes, indicates specific road classification types in Sweden (` BK1` through `BK4`) and Mexico (`A2, A4, B2, B4, C, D, ET2, ET4`) to avoid where possible. These road types may still be used if no reasonable alternative exists.
There are currently no other supported values as of 26th April 2024.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 12 items.
Length Constraints: Minimum length of 1. Maximum length of 3.
Required: No

 ** Tunnels **   <a name="location-Type-IsolineAvoidanceOptions-Tunnels"></a>
Indicates a preference to avoid tunnels where possible. If a viable route cannot be calculated without using tunnels, they may still be included.
Type: Boolean
Required: No

 ** UTurns **   <a name="location-Type-IsolineAvoidanceOptions-UTurns"></a>
Indicates a preference to avoid U-turns where possible. U-turns may still be included if necessary to reach certain areas or when no reasonable alternative exists.
Type: Boolean
Required: No

 ** ZoneCategories **   <a name="location-Type-IsolineAvoidanceOptions-ZoneCategories"></a>
Indicates types of regulated zones (such as congestion pricing or environmental zones) to avoid where possible. Routes may still pass through these zones if no reasonable alternative exists.
Type: Array of [IsolineAvoidanceZoneCategory](API_IsolineAvoidanceZoneCategory.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

## See Also
<a name="API_IsolineAvoidanceOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineAvoidanceOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineAvoidanceOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineAvoidanceOptions)
