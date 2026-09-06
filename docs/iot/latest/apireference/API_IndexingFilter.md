---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_IndexingFilter.html
---

# IndexingFilter
<a name="API_IndexingFilter"></a>

Provides additional selections for named shadows and geolocation data.

To add named shadows to your fleet indexing configuration, set `namedShadowIndexingMode` to be ON and specify your shadow names in `namedShadowNames` filter.

To add geolocation data to your fleet indexing configuration:
+ If you store geolocation data in a class/unnamed shadow, set `thingIndexingMode` to be `REGISTRY_AND_SHADOW` and specify your geolocation data in `geoLocations` filter.
+ If you store geolocation data in a named shadow, set `namedShadowIndexingMode` to be `ON`, add the shadow name in `namedShadowNames` filter, and specify your geolocation data in `geoLocations` filter. For more information, see [Managing fleet indexing](https://docs.aws.amazon.com/iot/latest/developerguide/managing-fleet-index.html).

## Contents
<a name="API_IndexingFilter_Contents"></a>

 ** connectivity **   <a name="iot-Type-IndexingFilter-connectivity"></a>
Provides additional connectivity filter selections for the fleet indexing configuration.
Type: [ConnectivityFilter](API_ConnectivityFilter.md) object
Required: No

 ** geoLocations **   <a name="iot-Type-IndexingFilter-geoLocations"></a>
The list of geolocation targets that you select to index. The default maximum number of geolocation targets for indexing is `1`. To increase the limit, see [AWS IoT Device Management Quotas](https://docs.aws.amazon.com/general/latest/gr/iot_device_management.html#fleet-indexing-limits) in the * AWS General Reference*.
Type: Array of [GeoLocationTarget](API_GeoLocationTarget.md) objects
Required: No

 ** namedShadowNames **   <a name="iot-Type-IndexingFilter-namedShadowNames"></a>
The shadow names that you select to index. The default maximum number of shadow names for indexing is 10. To increase the limit, see [AWS IoT Device Management Quotas](https://docs.aws.amazon.com/general/latest/gr/iot_device_management.html#fleet-indexing-limits) in the * AWS General Reference*.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[$a-zA-Z0-9:_-]+`
Required: No

## See Also
<a name="API_IndexingFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/IndexingFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/IndexingFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/IndexingFilter)
