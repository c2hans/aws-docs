---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartSegmentDetectionFilters.html
---

# StartSegmentDetectionFilters
<a name="API_StartSegmentDetectionFilters"></a>

Filters applied to the technical cue or shot detection segments. For more information, see [StartSegmentDetection](API_StartSegmentDetection.md).

## Contents
<a name="API_StartSegmentDetectionFilters_Contents"></a>

 ** ShotFilter **   <a name="rekognition-Type-StartSegmentDetectionFilters-ShotFilter"></a>
Filters that are specific to shot detections.
Type: [StartShotDetectionFilter](API_StartShotDetectionFilter.md) object
Required: No

 ** TechnicalCueFilter **   <a name="rekognition-Type-StartSegmentDetectionFilters-TechnicalCueFilter"></a>
Filters that are specific to technical cues.
Type: [StartTechnicalCueDetectionFilter](API_StartTechnicalCueDetectionFilter.md) object
Required: No

## See Also
<a name="API_StartSegmentDetectionFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StartSegmentDetectionFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/StartSegmentDetectionFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StartSegmentDetectionFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
