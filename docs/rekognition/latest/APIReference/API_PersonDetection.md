---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_PersonDetection.html
---

# PersonDetection
<a name="API_PersonDetection"></a>

Details and path tracking information for a single time a person's path is tracked in a video. Amazon Rekognition operations that track people's paths return an array of `PersonDetection` objects with elements for each time a person's path is tracked in a video.

For more information, see [GetPersonTracking](API_GetPersonTracking.md).

## Contents
<a name="API_PersonDetection_Contents"></a>

 ** Person **   <a name="rekognition-Type-PersonDetection-Person"></a>
Details about a person whose path was tracked in a video.
Type: [PersonDetail](API_PersonDetail.md) object
Required: No

 ** Timestamp **   <a name="rekognition-Type-PersonDetection-Timestamp"></a>
The time, in milliseconds from the start of the video, that the person's path was tracked. Note that `Timestamp` is not guaranteed to be accurate to the individual frame where the person's path first appears.
Type: Long
Required: No

## See Also
<a name="API_PersonDetection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/PersonDetection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/PersonDetection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/PersonDetection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
