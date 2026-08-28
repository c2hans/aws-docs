---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ModerationLabel.html
---

# ModerationLabel
<a name="API_ModerationLabel"></a>

Provides information about a single type of inappropriate, unwanted, or offensive content found in an image or video. Each type of moderated content has a label within a hierarchical taxonomy. For a list of moderation labels in Amazon Rekognition, see [Using the image and video moderation APIs](https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html#moderation-api). For more information, see [Moderating content](https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html).

## Contents
<a name="API_ModerationLabel_Contents"></a>

 ** Confidence **   <a name="rekognition-Type-ModerationLabel-Confidence"></a>
Specifies the confidence that Amazon Rekognition has that the label has been correctly identified.
If you don't specify the `MinConfidence` parameter in the call to `DetectModerationLabels`, the operation returns labels with a confidence value greater than or equal to 50 percent.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Name **   <a name="rekognition-Type-ModerationLabel-Name"></a>
The label name for the type of unsafe content detected in the image.
Type: String
Required: No

 ** ParentName **   <a name="rekognition-Type-ModerationLabel-ParentName"></a>
The name for the parent label. Labels at the top level of the hierarchy have the parent label `""`.
Type: String
Required: No

 ** TaxonomyLevel **   <a name="rekognition-Type-ModerationLabel-TaxonomyLevel"></a>
The level of the moderation label with regard to its taxonomy, from 1 to 3.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ModerationLabel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ModerationLabel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ModerationLabel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ModerationLabel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
