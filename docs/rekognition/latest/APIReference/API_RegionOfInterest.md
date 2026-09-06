---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RegionOfInterest.html
---

# RegionOfInterest
<a name="API_RegionOfInterest"></a>

Specifies a location within the frame that Rekognition checks for objects of interest such as text, labels, or faces. It uses a `BoundingBox` or `Polygon` to set a region of the screen.

A word, face, or label is included in the region if it is more than half in that region. If there is more than one region, the word, face, or label is compared with all regions of the screen. Any object of interest that is more than half in a region is kept in the results.

## Contents
<a name="API_RegionOfInterest_Contents"></a>

 ** BoundingBox **   <a name="rekognition-Type-RegionOfInterest-BoundingBox"></a>
The box representing a region of interest on screen.
Type: [BoundingBox](API_BoundingBox.md) object
Required: No

 ** Polygon **   <a name="rekognition-Type-RegionOfInterest-Polygon"></a>
 Specifies a shape made up of up to 10 `Point` objects to define a region of interest.
Type: Array of [Point](API_Point.md) objects
Required: No

## See Also
<a name="API_RegionOfInterest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/RegionOfInterest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/RegionOfInterest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/RegionOfInterest)
