---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_TechnicalCueSegment.html
---

# TechnicalCueSegment
<a name="API_TechnicalCueSegment"></a>

Information about a technical cue segment. For more information, see [SegmentDetection](API_SegmentDetection.md).

## Contents
<a name="API_TechnicalCueSegment_Contents"></a>

 ** Confidence **   <a name="rekognition-Type-TechnicalCueSegment-Confidence"></a>
The confidence that Amazon Rekognition Video has in the accuracy of the detected segment.
Type: Float
Valid Range: Minimum value of 50. Maximum value of 100.
Required: No

 ** Type **   <a name="rekognition-Type-TechnicalCueSegment-Type"></a>
The type of the technical cue.
Type: String
Valid Values: `ColorBars | EndCredits | BlackFrames | OpeningCredits | StudioLogo | Slate | Content`
Required: No

## See Also
<a name="API_TechnicalCueSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/TechnicalCueSegment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/TechnicalCueSegment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/TechnicalCueSegment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
