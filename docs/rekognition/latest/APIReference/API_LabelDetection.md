---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_LabelDetection.html
---

# LabelDetection
<a name="API_LabelDetection"></a>

Information about a label detected in a video analysis request and the time the label was detected in the video.

## Contents
<a name="API_LabelDetection_Contents"></a>

 ** DurationMillis **   <a name="rekognition-Type-LabelDetection-DurationMillis"></a>
The time duration of a segment in milliseconds, I.e. time elapsed from StartTimestampMillis to EndTimestampMillis.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** EndTimestampMillis **   <a name="rekognition-Type-LabelDetection-EndTimestampMillis"></a>
The time in milliseconds defining the end of the timeline segment containing a continuously detected label.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** Label **   <a name="rekognition-Type-LabelDetection-Label"></a>
Details about the detected label.
Type: [Label](API_Label.md) object
Required: No

 ** StartTimestampMillis **   <a name="rekognition-Type-LabelDetection-StartTimestampMillis"></a>
The time in milliseconds defining the start of the timeline segment containing a continuously detected label.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** Timestamp **   <a name="rekognition-Type-LabelDetection-Timestamp"></a>
Time, in milliseconds from the start of the video, that the label was detected. Note that `Timestamp` is not guaranteed to be accurate to the individual frame where the label first appears.
Type: Long
Required: No

## See Also
<a name="API_LabelDetection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/LabelDetection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/LabelDetection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/LabelDetection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
