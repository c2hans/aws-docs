---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_TargetFace.html
---

# TargetFace
<a name="API_rekognitionstreaming_TargetFace"></a>

Contains bounding box of face position of the user on the device screen at target location constructed for the challenge. This is generated using the random offsets provided by the server to the client at session start. Also contains start and end epoch timestamp of when the user was detected in this position.

## Contents
<a name="API_rekognitionstreaming_TargetFace_Contents"></a>

 ** BoundingBox **   <a name="rekognition-Type-rekognitionstreaming_TargetFace-BoundingBox"></a>
A bounding box for the target face.
Type: [BoundingBox](API_rekognitionstreaming_BoundingBox.md) object
Required: Yes

 ** FaceDetectedInTargetPositionEndTimestamp **   <a name="rekognition-Type-rekognitionstreaming_TargetFace-FaceDetectedInTargetPositionEndTimestamp"></a>
Ending timestamp at which a face was detected in the target position.
Type: Long
Valid Range: Minimum value of 1640995200000. Maximum value of 2272147200000.
Required: Yes

 ** FaceDetectedInTargetPositionStartTimestamp **   <a name="rekognition-Type-rekognitionstreaming_TargetFace-FaceDetectedInTargetPositionStartTimestamp"></a>
Starting timestamp at which a face was detected in the target position.
Type: Long
Valid Range: Minimum value of 1640995200000. Maximum value of 2272147200000.
Required: Yes

## See Also
<a name="API_rekognitionstreaming_TargetFace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognitionstreaming-2022-05-30/TargetFace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognitionstreaming-2022-05-30/TargetFace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognitionstreaming-2022-05-30/TargetFace)
