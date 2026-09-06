---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UnsuccessfulFaceAssociation.html
---

# UnsuccessfulFaceAssociation
<a name="API_UnsuccessfulFaceAssociation"></a>

Contains metadata like FaceId, UserID, and Reasons, for a face that was unsuccessfully associated.

## Contents
<a name="API_UnsuccessfulFaceAssociation_Contents"></a>

 ** Confidence **   <a name="rekognition-Type-UnsuccessfulFaceAssociation-Confidence"></a>
Match confidence with the UserID, provides information regarding if a face association was unsuccessful because it didn't meet UserMatchThreshold.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** FaceId **   <a name="rekognition-Type-UnsuccessfulFaceAssociation-FaceId"></a>
A unique identifier assigned to the face.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** Reasons **   <a name="rekognition-Type-UnsuccessfulFaceAssociation-Reasons"></a>
 The reason why the association was unsuccessful.
Type: Array of strings
Valid Values: `FACE_NOT_FOUND | ASSOCIATED_TO_A_DIFFERENT_USER | LOW_MATCH_CONFIDENCE`
Required: No

 ** UserId **   <a name="rekognition-Type-UnsuccessfulFaceAssociation-UserId"></a>
A provided ID for the UserID. Unique within the collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-:]+`
Required: No

## See Also
<a name="API_UnsuccessfulFaceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/UnsuccessfulFaceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/UnsuccessfulFaceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/UnsuccessfulFaceAssociation)
