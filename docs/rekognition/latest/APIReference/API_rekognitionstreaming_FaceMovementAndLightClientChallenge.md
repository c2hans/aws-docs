---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_FaceMovementAndLightClientChallenge.html
---

# FaceMovementAndLightClientChallenge
<a name="API_rekognitionstreaming_FaceMovementAndLightClientChallenge"></a>

Holds information about the type of face movement and light challenges that need to be performed.

## Contents
<a name="API_rekognitionstreaming_FaceMovementAndLightClientChallenge_Contents"></a>

 ** ChallengeId **   <a name="rekognition-Type-rekognitionstreaming_FaceMovementAndLightClientChallenge-ChallengeId"></a>
An ID that uniquely identifies a challenge from a client.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** ColorDisplayed **   <a name="rekognition-Type-rekognitionstreaming_FaceMovementAndLightClientChallenge-ColorDisplayed"></a>
Contains information regarding SequenceNumber, CurrentColor, PreviousColor, and CurrentColorStartTimestamp for a challenge.
Type: [ColorDisplayed](API_rekognitionstreaming_ColorDisplayed.md) object
Required: No

 ** InitialFace **   <a name="rekognition-Type-rekognitionstreaming_FaceMovementAndLightClientChallenge-InitialFace"></a>
Contains the bounding box of the initial face position for the user on the device screen. Also contains an epoch timestamp of when the user was detected in this position. Used for Face Liveness detection.
Type: [InitialFace](API_rekognitionstreaming_InitialFace.md) object
Required: No

 ** TargetFace **   <a name="rekognition-Type-rekognitionstreaming_FaceMovementAndLightClientChallenge-TargetFace"></a>
Contains the face position bounding box for the user on the device's screen, set at the target location constructed for the challenge. Generated using a precise oval location depending on the provided video
dimensions in the input stream. Contains start and end epoch timestamp of when the user was detected in this position.
Type: [TargetFace](API_rekognitionstreaming_TargetFace.md) object
Required: No

 ** VideoEndTimestamp **   <a name="rekognition-Type-rekognitionstreaming_FaceMovementAndLightClientChallenge-VideoEndTimestamp"></a>
Epoch timestamp indicating end of video recording.
Type: Long
Valid Range: Minimum value of 1640995200000. Maximum value of 2272147200000.
Required: No

 ** VideoStartTimestamp **   <a name="rekognition-Type-rekognitionstreaming_FaceMovementAndLightClientChallenge-VideoStartTimestamp"></a>
Epoch timestamp indicating start of video recording.
Type: Long
Valid Range: Minimum value of 1640995200000. Maximum value of 2272147200000.
Required: No

## See Also
<a name="API_rekognitionstreaming_FaceMovementAndLightClientChallenge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognitionstreaming-2022-05-30/FaceMovementAndLightClientChallenge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognitionstreaming-2022-05-30/FaceMovementAndLightClientChallenge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognitionstreaming-2022-05-30/FaceMovementAndLightClientChallenge)
