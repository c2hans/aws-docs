---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_ChallengeConfig.html
---

# ChallengeConfig
<a name="API_rekognitionstreaming_ChallengeConfig"></a>

Configuration options for Face Liveness challenges performed at the client side.

## Contents
<a name="API_rekognitionstreaming_ChallengeConfig_Contents"></a>

 ** BlazeFaceDetectionThreshold **   <a name="rekognition-Type-rekognitionstreaming_ChallengeConfig-BlazeFaceDetectionThreshold"></a>
Threshold for face detection done using blaze face.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** FaceDistanceThreshold **   <a name="rekognition-Type-rekognitionstreaming_ChallengeConfig-FaceDistanceThreshold"></a>
Threshold for face distance threshold face liveness challenge.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** FaceDistanceThresholdMax **   <a name="rekognition-Type-rekognitionstreaming_ChallengeConfig-FaceDistanceThresholdMax"></a>
Threshold for the maximum distance that face can be from the camera before face oval match challenge starts.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** FaceDistanceThresholdMin **   <a name="rekognition-Type-rekognitionstreaming_ChallengeConfig-FaceDistanceThresholdMin"></a>
Threshold for the minimum distance that face can be from the camera before face oval match challenge starts.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** FaceIouHeightThreshold **   <a name="rekognition-Type-rekognitionstreaming_ChallengeConfig-FaceIouHeightThreshold"></a>
 Threshold for height during face IOU (Intersection over Union) match.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** FaceIouWidthThreshold **   <a name="rekognition-Type-rekognitionstreaming_ChallengeConfig-FaceIouWidthThreshold"></a>
Threshold for width during face IOU (Intersection over Union) match.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** OvalFitTimeout **   <a name="rekognition-Type-rekognitionstreaming_ChallengeConfig-OvalFitTimeout"></a>
Timeout limit in which the end-users need to fit in the oval, in miliseconds.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

 ** OvalHeightWidthRatio **   <a name="rekognition-Type-rekognitionstreaming_ChallengeConfig-OvalHeightWidthRatio"></a>
Height to width ratio of oval used for face oval match.
Type: Float
Required: No

 ** OvalIouHeightThreshold **   <a name="rekognition-Type-rekognitionstreaming_ChallengeConfig-OvalIouHeightThreshold"></a>
Threshold for height during oval IOU (Intersection over Union) match.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** OvalIouThreshold **   <a name="rekognition-Type-rekognitionstreaming_ChallengeConfig-OvalIouThreshold"></a>
Threshold for face oval match using IoU (Intersection over Union).
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** OvalIouWidthThreshold **   <a name="rekognition-Type-rekognitionstreaming_ChallengeConfig-OvalIouWidthThreshold"></a>
Threshold for width during oval IOU (Intersection over Union) match.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

## See Also
<a name="API_rekognitionstreaming_ChallengeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognitionstreaming-2022-05-30/ChallengeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognitionstreaming-2022-05-30/ChallengeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognitionstreaming-2022-05-30/ChallengeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
