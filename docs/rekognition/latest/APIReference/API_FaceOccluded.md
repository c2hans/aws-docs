---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_FaceOccluded.html
---

# FaceOccluded
<a name="API_FaceOccluded"></a>

 `FaceOccluded` should return "true" with a high confidence score if a detected face’s eyes, nose, and mouth are partially captured or if they are covered by masks, dark sunglasses, cell phones, hands, or other objects. `FaceOccluded` should return "false" with a high confidence score if common occurrences that do not impact face verification are detected, such as eye glasses, lightly tinted sunglasses, strands of hair, and others.

You can use `FaceOccluded` to determine if an obstruction on a face negatively impacts using the image for face matching.

## Contents
<a name="API_FaceOccluded_Contents"></a>

 ** Confidence **   <a name="rekognition-Type-FaceOccluded-Confidence"></a>
The confidence that the service has detected the presence of a face occlusion.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Value **   <a name="rekognition-Type-FaceOccluded-Value"></a>
True if a detected face’s eyes, nose, and mouth are partially captured or if they are covered by masks, dark sunglasses, cell phones, hands, or other objects. False if common occurrences that do not impact face verification are detected, such as eye glasses, lightly tinted sunglasses, strands of hair, and others.
Type: Boolean
Required: No

## See Also
<a name="API_FaceOccluded_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/FaceOccluded)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/FaceOccluded)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/FaceOccluded)
