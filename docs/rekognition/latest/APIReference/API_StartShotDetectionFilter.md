---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartShotDetectionFilter.html
---

# StartShotDetectionFilter
<a name="API_StartShotDetectionFilter"></a>

Filters for the shot detection segments returned by `GetSegmentDetection`. For more information, see [StartSegmentDetectionFilters](API_StartSegmentDetectionFilters.md).

## Contents
<a name="API_StartShotDetectionFilter_Contents"></a>

 ** MinSegmentConfidence **   <a name="rekognition-Type-StartShotDetectionFilter-MinSegmentConfidence"></a>
Specifies the minimum confidence that Amazon Rekognition Video must have in order to return a detected segment. Confidence represents how certain Amazon Rekognition is that a segment is correctly identified. 0 is the lowest confidence. 100 is the highest confidence. Amazon Rekognition Video doesn't return any segments with a confidence level lower than this specified value.
If you don't specify `MinSegmentConfidence`, the `GetSegmentDetection` returns segments with confidence values greater than or equal to 50 percent.
Type: Float
Valid Range: Minimum value of 50. Maximum value of 100.
Required: No

## See Also
<a name="API_StartShotDetectionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StartShotDetectionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/StartShotDetectionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StartShotDetectionFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
