---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ThingIndexingConfiguration.html
---

# ThingIndexingConfiguration
<a name="API_ThingIndexingConfiguration"></a>

The thing indexing configuration. For more information, see [Managing Thing Indexing](https://docs.aws.amazon.com/iot/latest/developerguide/managing-index.html).

## Contents
<a name="API_ThingIndexingConfiguration_Contents"></a>

 ** thingIndexingMode **   <a name="iot-Type-ThingIndexingConfiguration-thingIndexingMode"></a>
Thing indexing mode. Valid values are:
+ REGISTRY – Your thing index contains registry data only.
+ REGISTRY\_AND\_SHADOW - Your thing index contains registry and shadow data.
+ OFF - Thing indexing is disabled.
Type: String
Valid Values: `OFF | REGISTRY | REGISTRY_AND_SHADOW`
Required: Yes

 ** customFields **   <a name="iot-Type-ThingIndexingConfiguration-customFields"></a>
Contains custom field names and their data type.
Type: Array of [Field](API_Field.md) objects
Required: No

 ** deviceDefenderIndexingMode **   <a name="iot-Type-ThingIndexingConfiguration-deviceDefenderIndexingMode"></a>
Device Defender indexing mode. Valid values are:
+ VIOLATIONS – Your thing index contains Device Defender violations. To enable Device Defender indexing, *deviceDefenderIndexingMode* must not be set to OFF.
+ OFF - Device Defender indexing is disabled.
For more information about Device Defender violations, see [Device Defender Detect.](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-detect.html)
Type: String
Valid Values: `OFF | VIOLATIONS`
Required: No

 ** filter **   <a name="iot-Type-ThingIndexingConfiguration-filter"></a>
Provides additional selections for named shadows and geolocation data.
To add named shadows to your fleet indexing configuration, set `namedShadowIndexingMode` to be ON and specify your shadow names in `namedShadowNames` filter.
To add geolocation data to your fleet indexing configuration:
+ If you store geolocation data in a class/unnamed shadow, set `thingIndexingMode` to be `REGISTRY_AND_SHADOW` and specify your geolocation data in `geoLocations` filter.
+ If you store geolocation data in a named shadow, set `namedShadowIndexingMode` to be `ON`, add the shadow name in `namedShadowNames` filter, and specify your geolocation data in `geoLocations` filter. For more information, see [Managing fleet indexing](https://docs.aws.amazon.com/iot/latest/developerguide/managing-fleet-index.html).
Type: [IndexingFilter](API_IndexingFilter.md) object
Required: No

 ** managedFields **   <a name="iot-Type-ThingIndexingConfiguration-managedFields"></a>
Contains fields that are indexed and whose types are already known by the Fleet Indexing service. This is an optional field. For more information, see [Managed fields](https://docs.aws.amazon.com/iot/latest/developerguide/managing-fleet-index.html#managed-field) in the * AWS IoT Core Developer Guide*.
You can't modify managed fields by updating fleet indexing configuration.
Type: Array of [Field](API_Field.md) objects
Required: No

 ** namedShadowIndexingMode **   <a name="iot-Type-ThingIndexingConfiguration-namedShadowIndexingMode"></a>
Named shadow indexing mode. Valid values are:
+ ON – Your thing index contains named shadow. To enable thing named shadow indexing, *namedShadowIndexingMode* must not be set to OFF.
+ OFF - Named shadow indexing is disabled.
For more information about Shadows, see [AWS IoT Device Shadow service.](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html)
Type: String
Valid Values: `OFF | ON`
Required: No

 ** thingConnectivityIndexingMode **   <a name="iot-Type-ThingIndexingConfiguration-thingConnectivityIndexingMode"></a>
Thing connectivity indexing mode. Valid values are:
+ STATUS – Your thing index contains connectivity status. To enable thing connectivity indexing, *thingIndexMode* must not be set to OFF.
+ OFF - Thing connectivity status indexing is disabled.
Type: String
Valid Values: `OFF | STATUS`
Required: No

## See Also
<a name="API_ThingIndexingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ThingIndexingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ThingIndexingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ThingIndexingConfiguration)
