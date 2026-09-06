---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Image.html
---

# Image
<a name="API_Image"></a>

Contains an image that is one of the following:
+ An image file. Choose this option to upload a new image.
+ The ID of an existing image. Choose this option to keep an existing image.

## Contents
<a name="API_Image_Contents"></a>

 ** file **   <a name="iotsitewise-Type-Image-file"></a>
Contains an image file.
Type: [ImageFile](API_ImageFile.md) object
Required: No

 ** id **   <a name="iotsitewise-Type-Image-id"></a>
The ID of an existing image. Specify this parameter to keep an existing image.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

## See Also
<a name="API_Image_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/Image)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/Image)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/Image)
