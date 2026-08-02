---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GeoLocationTarget.html
---

# GeoLocationTarget
<a name="API_GeoLocationTarget"></a>

A geolocation target that you select to index. Each geolocation target contains a `name` and `order` key-value pair that specifies the geolocation target fields.

## Contents
<a name="API_GeoLocationTarget_Contents"></a>

 ** name **   <a name="iot-Type-GeoLocationTarget-name"></a>
The `name` of the geolocation target field. If the target field is part of a named shadow, you must select the named shadow using the `namedShadow` filter.
Type: String
Required: No

 ** order **   <a name="iot-Type-GeoLocationTarget-order"></a>
The `order` of the geolocation target field. This field is optional. The default value is `LatLon`.
Type: String
Valid Values: `LatLon | LonLat`
Required: No

## See Also
<a name="API_GeoLocationTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GeoLocationTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GeoLocationTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GeoLocationTarget)
