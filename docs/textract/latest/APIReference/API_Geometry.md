---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_Geometry.html
---

# Geometry
<a name="API_Geometry"></a>

Information about where the following items are located on a document page: detected page, text, key-value pairs, tables, table cells, and selection elements.

## Contents
<a name="API_Geometry_Contents"></a>

 ** BoundingBox **   <a name="Textract-Type-Geometry-BoundingBox"></a>
An axis-aligned coarse representation of the location of the recognized item on the document page.
Type: [BoundingBox](API_BoundingBox.md) object
Required: No

 ** Polygon **   <a name="Textract-Type-Geometry-Polygon"></a>
Within the bounding box, a fine-grained polygon around the recognized item.
Type: Array of [Point](API_Point.md) objects
Required: No

 ** RotationAngle **   <a name="Textract-Type-Geometry-RotationAngle"></a>
Provides a numerical value corresponding to the rotation of the WORD block. Possible values are 0, 90, 180, and 270.
Type: Float
Required: No

## See Also
<a name="API_Geometry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/Geometry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/Geometry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/Geometry)
