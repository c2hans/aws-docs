---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_Coordinates.html
---

# Coordinates
<a name="API_Coordinates"></a>

 A complex type that lists the coordinates for a geoproximity resource record.

## Contents
<a name="API_Coordinates_Contents"></a>

 ** Latitude **   <a name="Route53-Type-Coordinates-Latitude"></a>
 Specifies a coordinate of the north–south position of a geographic point on the surface of the Earth (-90 - 90).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `[-+]?[0-9]{1,2}(\.[0-9]{0,2})?`
Required: Yes

 ** Longitude **   <a name="Route53-Type-Coordinates-Longitude"></a>
 Specifies a coordinate of the east–west position of a geographic point on the surface of the Earth (-180 - 180).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `[-+]?[0-9]{1,3}(\.[0-9]{0,2})?`
Required: Yes

## See Also
<a name="API_Coordinates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/Coordinates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/Coordinates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/Coordinates)
