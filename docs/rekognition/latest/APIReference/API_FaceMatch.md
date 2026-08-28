---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_FaceMatch.html
---

# FaceMatch
<a name="API_FaceMatch"></a>

Provides face metadata. In addition, it also provides the confidence in the match of this face with the input face.

## Contents
<a name="API_FaceMatch_Contents"></a>

 ** Face **   <a name="rekognition-Type-FaceMatch-Face"></a>
Describes the face properties such as the bounding box, face ID, image ID of the source image, and external image ID that you assigned.
Type: [Face](API_Face.md) object
Required: No

 ** Similarity **   <a name="rekognition-Type-FaceMatch-Similarity"></a>
Confidence in the match of this face with the input face.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_FaceMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/FaceMatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/FaceMatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/FaceMatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
