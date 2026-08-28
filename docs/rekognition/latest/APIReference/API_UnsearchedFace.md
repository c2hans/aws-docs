---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UnsearchedFace.html
---

# UnsearchedFace
<a name="API_UnsearchedFace"></a>

Face details inferred from the image but not used for search. The response attribute contains reasons for why a face wasn't used for Search.

## Contents
<a name="API_UnsearchedFace_Contents"></a>

 ** FaceDetails **   <a name="rekognition-Type-UnsearchedFace-FaceDetails"></a>
Structure containing attributes of the face that the algorithm detected.
A `FaceDetail` object contains either the default facial attributes or all facial attributes. The default attributes are `BoundingBox`, `Confidence`, `Landmarks`, `Pose`, and `Quality`.
 [GetFaceDetection](API_GetFaceDetection.md) is the only Amazon Rekognition Video stored video operation that can return a `FaceDetail` object with all attributes. To specify which attributes to return, use the `FaceAttributes` input parameter for [StartFaceDetection](API_StartFaceDetection.md). The following Amazon Rekognition Video operations return only the default attributes. The corresponding Start operations don't have a `FaceAttributes` input parameter:
+ GetCelebrityRecognition
+ GetPersonTracking
+ GetFaceSearch
The Amazon Rekognition Image [DetectFaces](API_DetectFaces.md) and [IndexFaces](API_IndexFaces.md) operations can return all facial attributes. To specify which attributes to return, use the `Attributes` input parameter for `DetectFaces`. For `IndexFaces`, use the `DetectAttributes` input parameter.
Type: [FaceDetail](API_FaceDetail.md) object
Required: No

 ** Reasons **   <a name="rekognition-Type-UnsearchedFace-Reasons"></a>
 Reasons why a face wasn't used for Search.
Type: Array of strings
Valid Values: `FACE_NOT_LARGEST | EXCEEDS_MAX_FACES | EXTREME_POSE | LOW_BRIGHTNESS | LOW_SHARPNESS | LOW_CONFIDENCE | SMALL_BOUNDING_BOX | LOW_FACE_QUALITY`
Required: No

## See Also
<a name="API_UnsearchedFace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/UnsearchedFace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/UnsearchedFace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/UnsearchedFace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
