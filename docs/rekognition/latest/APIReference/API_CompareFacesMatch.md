---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CompareFacesMatch.html
---

# CompareFacesMatch
<a name="API_CompareFacesMatch"></a>

Provides information about a face in a target image that matches the source image face analyzed by `CompareFaces`. The `Face` property contains the bounding box of the face in the target image. The `Similarity` property is the confidence that the source image face matches the face in the bounding box.

## Contents
<a name="API_CompareFacesMatch_Contents"></a>

 ** Face **   <a name="rekognition-Type-CompareFacesMatch-Face"></a>
Provides face metadata (bounding box and confidence that the bounding box actually contains a face).
Type: [ComparedFace](API_ComparedFace.md) object
Required: No

 ** Similarity **   <a name="rekognition-Type-CompareFacesMatch-Similarity"></a>
Level of confidence that the faces match.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_CompareFacesMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CompareFacesMatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/CompareFacesMatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CompareFacesMatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
