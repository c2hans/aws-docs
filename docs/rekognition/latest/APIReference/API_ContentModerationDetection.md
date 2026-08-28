---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ContentModerationDetection.html
---

# ContentModerationDetection
<a name="API_ContentModerationDetection"></a>

Information about an inappropriate, unwanted, or offensive content label detection in a stored video.

## Contents
<a name="API_ContentModerationDetection_Contents"></a>

 ** ContentTypes **   <a name="rekognition-Type-ContentModerationDetection-ContentTypes"></a>
A list of predicted results for the type of content an image contains. For example, the image content might be from animation, sports, or a video game.
Type: Array of [ContentType](API_ContentType.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** DurationMillis **   <a name="rekognition-Type-ContentModerationDetection-DurationMillis"></a>
 The time duration of a segment in milliseconds, I.e. time elapsed from StartTimestampMillis to EndTimestampMillis.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** EndTimestampMillis **   <a name="rekognition-Type-ContentModerationDetection-EndTimestampMillis"></a>
 The time in milliseconds defining the end of the timeline segment containing a continuously detected moderation label.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** ModerationLabel **   <a name="rekognition-Type-ContentModerationDetection-ModerationLabel"></a>
The content moderation label detected by in the stored video.
Type: [ModerationLabel](API_ModerationLabel.md) object
Required: No

 ** StartTimestampMillis **   <a name="rekognition-Type-ContentModerationDetection-StartTimestampMillis"></a>
The time in milliseconds defining the start of the timeline segment containing a continuously detected moderation label.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** Timestamp **   <a name="rekognition-Type-ContentModerationDetection-Timestamp"></a>
Time, in milliseconds from the beginning of the video, that the content moderation label was detected. Note that `Timestamp` is not guaranteed to be accurate to the individual frame where the moderated content first appears.
Type: Long
Required: No

## See Also
<a name="API_ContentModerationDetection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ContentModerationDetection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ContentModerationDetection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ContentModerationDetection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
