---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UnsuccessfulFaceDisassociation.html
---

# UnsuccessfulFaceDisassociation
<a name="API_UnsuccessfulFaceDisassociation"></a>

Contains metadata like FaceId, UserID, and Reasons, for a face that was unsuccessfully disassociated.

## Contents
<a name="API_UnsuccessfulFaceDisassociation_Contents"></a>

 ** FaceId **   <a name="rekognition-Type-UnsuccessfulFaceDisassociation-FaceId"></a>
A unique identifier assigned to the face.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** Reasons **   <a name="rekognition-Type-UnsuccessfulFaceDisassociation-Reasons"></a>
The reason why the deletion was unsuccessful.
Type: Array of strings
Valid Values: `FACE_NOT_FOUND | ASSOCIATED_TO_A_DIFFERENT_USER`
Required: No

 ** UserId **   <a name="rekognition-Type-UnsuccessfulFaceDisassociation-UserId"></a>
A provided ID for the UserID. Unique within the collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-:]+`
Required: No

## See Also
<a name="API_UnsuccessfulFaceDisassociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/UnsuccessfulFaceDisassociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/UnsuccessfulFaceDisassociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/UnsuccessfulFaceDisassociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
