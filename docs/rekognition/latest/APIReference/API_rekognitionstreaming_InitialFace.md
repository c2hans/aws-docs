---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_InitialFace.html
---

# InitialFace
<a name="API_rekognitionstreaming_InitialFace"></a>

 Contains bounding box of initial face position of the user on the device screen. Contains an epoch timestamp of when the user was detected in this position. Used for Face Liveness detection.

## Contents
<a name="API_rekognitionstreaming_InitialFace_Contents"></a>

 ** BoundingBox **   <a name="rekognition-Type-rekognitionstreaming_InitialFace-BoundingBox"></a>
The bounding box for the initial face position of the user on the device screen.
Type: [BoundingBox](API_rekognitionstreaming_BoundingBox.md) object
Required: Yes

 ** InitialFaceDetectedTimestamp **   <a name="rekognition-Type-rekognitionstreaming_InitialFace-InitialFaceDetectedTimestamp"></a>
Timestamp that a face was initially detected at.
Type: Long
Valid Range: Minimum value of 1640995200000. Maximum value of 2272147200000.
Required: Yes

## See Also
<a name="API_rekognitionstreaming_InitialFace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognitionstreaming-2022-05-30/InitialFace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognitionstreaming-2022-05-30/InitialFace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognitionstreaming-2022-05-30/InitialFace)
