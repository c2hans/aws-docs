---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchedFaceDetails.html
---

# SearchedFaceDetails
<a name="API_SearchedFaceDetails"></a>

Contains data regarding the input face used for a search.

## Contents
<a name="API_SearchedFaceDetails_Contents"></a>

 ** FaceDetail **   <a name="rekognition-Type-SearchedFaceDetails-FaceDetail"></a>
Structure containing attributes of the face that the algorithm detected.
A `FaceDetail` object contains either the default facial attributes or all facial attributes. The default attributes are `BoundingBox`, `Confidence`, `Landmarks`, `Pose`, and `Quality`.
 [GetFaceDetection](API_GetFaceDetection.md) is the only Amazon Rekognition Video stored video operation that can return a `FaceDetail` object with all attributes. To specify which attributes to return, use the `FaceAttributes` input parameter for [StartFaceDetection](API_StartFaceDetection.md). The following Amazon Rekognition Video operations return only the default attributes. The corresponding Start operations don't have a `FaceAttributes` input parameter:
+ GetCelebrityRecognition
+ GetPersonTracking
+ GetFaceSearch
The Amazon Rekognition Image [DetectFaces](API_DetectFaces.md) and [IndexFaces](API_IndexFaces.md) operations can return all facial attributes. To specify which attributes to return, use the `Attributes` input parameter for `DetectFaces`. For `IndexFaces`, use the `DetectAttributes` input parameter.
Type: [FaceDetail](API_FaceDetail.md) object
Required: No

## See Also
<a name="API_SearchedFaceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/SearchedFaceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/SearchedFaceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/SearchedFaceDetails)
