---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartTextDetectionFilters.html
---

# StartTextDetectionFilters
<a name="API_StartTextDetectionFilters"></a>

Set of optional parameters that let you set the criteria text must meet to be included in your response. `WordFilter` looks at a word's height, width and minimum confidence. `RegionOfInterest` lets you set a specific region of the screen to look for text in.

## Contents
<a name="API_StartTextDetectionFilters_Contents"></a>

 ** RegionsOfInterest **   <a name="rekognition-Type-StartTextDetectionFilters-RegionsOfInterest"></a>
Filter focusing on a certain area of the frame. Uses a `BoundingBox` object to set the region of the screen.
Type: Array of [RegionOfInterest](API_RegionOfInterest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** WordFilter **   <a name="rekognition-Type-StartTextDetectionFilters-WordFilter"></a>
Filters focusing on qualities of the text, such as confidence or size.
Type: [DetectionFilter](API_DetectionFilter.md) object
Required: No

## See Also
<a name="API_StartTextDetectionFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StartTextDetectionFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/StartTextDetectionFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StartTextDetectionFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
