---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Emotion.html
---

# Emotion
<a name="API_Emotion"></a>

The API returns a prediction of an emotion based on a person's facial expressions, along with the confidence level for the predicted emotion. It is not a determination of the person’s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally. The API is not intended to be used, and you may not use it, in a manner that violates the EU Artificial Intelligence Act or any other applicable law.

## Contents
<a name="API_Emotion_Contents"></a>

 ** Confidence **   <a name="rekognition-Type-Emotion-Confidence"></a>
Level of confidence in the determination.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Type **   <a name="rekognition-Type-Emotion-Type"></a>
Type of emotion detected.
Type: String
Valid Values: `HAPPY | SAD | ANGRY | CONFUSED | DISGUSTED | SURPRISED | CALM | UNKNOWN | FEAR`
Required: No

## See Also
<a name="API_Emotion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/Emotion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/Emotion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/Emotion)
