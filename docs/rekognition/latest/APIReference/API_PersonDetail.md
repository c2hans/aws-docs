---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_PersonDetail.html
---

# PersonDetail
<a name="API_PersonDetail"></a>

Details about a person detected in a video analysis request.

## Contents
<a name="API_PersonDetail_Contents"></a>

 ** BoundingBox **   <a name="rekognition-Type-PersonDetail-BoundingBox"></a>
Bounding box around the detected person.
Type: [BoundingBox](API_BoundingBox.md) object
Required: No

 ** Face **   <a name="rekognition-Type-PersonDetail-Face"></a>
Face details for the detected person.
Type: [FaceDetail](API_FaceDetail.md) object
Required: No

 ** Index **   <a name="rekognition-Type-PersonDetail-Index"></a>
Identifier for the person detected person within a video. Use to keep track of the person throughout the video. The identifier is not stored by Amazon Rekognition.
Type: Long
Required: No

## See Also
<a name="API_PersonDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/PersonDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/PersonDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/PersonDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
