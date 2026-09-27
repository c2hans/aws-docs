---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_FeedbackItem.html
---

# FeedbackItem
<a name="API_FeedbackItem"></a>

Describes a condition that was detected in the Face Liveness video and that contributed to the confidence score returned for the session.

## Contents
<a name="API_FeedbackItem_Contents"></a>

 ** Code **   <a name="rekognition-Type-FeedbackItem-Code"></a>
A code identifying the condition that was detected during the Face Liveness session.
Type: String
Valid Values: `FACE_NOT_VISIBLE | FACE_OBSTRUCTION_DETECTED | LOW_VIDEO_QUALITY_DETECTED | FACE_NOT_ALIGNED | EYES_CLOSED_DETECTED | LOW_LIGHTING_DETECTED | HIGH_LIGHTING_DETECTED`
Required: Yes

 ** Message **   <a name="rekognition-Type-FeedbackItem-Message"></a>
A human-readable description of the detected condition, suitable for displaying to an end user before they retry a Face Liveness check. Use `Code` rather than this message for programmatic decisions, because the message text can change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

## See Also
<a name="API_FeedbackItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/FeedbackItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/FeedbackItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/FeedbackItem)
