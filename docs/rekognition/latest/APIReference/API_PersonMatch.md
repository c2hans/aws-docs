---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_PersonMatch.html
---

# PersonMatch
<a name="API_PersonMatch"></a>

Information about a person whose face matches a face(s) in an Amazon Rekognition collection. Includes information about the faces in the Amazon Rekognition collection ([FaceMatch](API_FaceMatch.md)), information about the person ([PersonDetail](API_PersonDetail.md)), and the time stamp for when the person was detected in a video. An array of `PersonMatch` objects is returned by [GetFaceSearch](API_GetFaceSearch.md).

## Contents
<a name="API_PersonMatch_Contents"></a>

 ** FaceMatches **   <a name="rekognition-Type-PersonMatch-FaceMatches"></a>
Information about the faces in the input collection that match the face of a person in the video.
Type: Array of [FaceMatch](API_FaceMatch.md) objects
Required: No

 ** Person **   <a name="rekognition-Type-PersonMatch-Person"></a>
Information about the matched person.
Type: [PersonDetail](API_PersonDetail.md) object
Required: No

 ** Timestamp **   <a name="rekognition-Type-PersonMatch-Timestamp"></a>
The time, in milliseconds from the beginning of the video, that the person was matched in the video.
Type: Long
Required: No

## See Also
<a name="API_PersonMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/PersonMatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/PersonMatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/PersonMatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
