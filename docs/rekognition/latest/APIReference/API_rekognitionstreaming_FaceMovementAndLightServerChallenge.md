---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_FaceMovementAndLightServerChallenge.html
---

# FaceMovementAndLightServerChallenge
<a name="API_rekognitionstreaming_FaceMovementAndLightServerChallenge"></a>

Contains information regarding the `OvalParameters` and `LightChallengeType` for a challenge.

## Contents
<a name="API_rekognitionstreaming_FaceMovementAndLightServerChallenge_Contents"></a>

 ** ChallengeConfig **   <a name="rekognition-Type-rekognitionstreaming_FaceMovementAndLightServerChallenge-ChallengeConfig"></a>
Configurations for attributes of the Face Liveness movement and light challenges.
Type: [ChallengeConfig](API_rekognitionstreaming_ChallengeConfig.md) object
Required: Yes

 ** ColorSequences **   <a name="rekognition-Type-rekognitionstreaming_FaceMovementAndLightServerChallenge-ColorSequences"></a>
Used to generate a list of color sequences to be displayed on a user's screen.
Type: Array of [ColorSequence](API_rekognitionstreaming_ColorSequence.md) objects
Required: Yes

 ** LightChallengeType **   <a name="rekognition-Type-rekognitionstreaming_FaceMovementAndLightServerChallenge-LightChallengeType"></a>
Information on the type of colored light challenge.
Type: String
Valid Values: `SEQUENTIAL`
Required: Yes

 ** OvalParameters **   <a name="rekognition-Type-rekognitionstreaming_FaceMovementAndLightServerChallenge-OvalParameters"></a>
The parameters needed for an oval to display and to complete oval match challenge.
Type: [OvalParameters](API_rekognitionstreaming_OvalParameters.md) object
Required: Yes

## See Also
<a name="API_rekognitionstreaming_FaceMovementAndLightServerChallenge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognitionstreaming-2022-05-30/FaceMovementAndLightServerChallenge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognitionstreaming-2022-05-30/FaceMovementAndLightServerChallenge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognitionstreaming-2022-05-30/FaceMovementAndLightServerChallenge)
