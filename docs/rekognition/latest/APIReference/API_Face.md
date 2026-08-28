---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Face.html
---

# Face
<a name="API_Face"></a>

Describes the face properties such as the bounding box, face ID, image ID of the input image, and external image ID that you assigned.

## Contents
<a name="API_Face_Contents"></a>

 ** BoundingBox **   <a name="rekognition-Type-Face-BoundingBox"></a>
Bounding box of the face.
Type: [BoundingBox](API_BoundingBox.md) object
Required: No

 ** Confidence **   <a name="rekognition-Type-Face-Confidence"></a>
Confidence level that the bounding box contains a face (and not a different object such as a tree).
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** ExternalImageId **   <a name="rekognition-Type-Face-ExternalImageId"></a>
Identifier that you assign to all the faces in the input image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.\-:]+`
Required: No

 ** FaceId **   <a name="rekognition-Type-Face-FaceId"></a>
Unique identifier that Amazon Rekognition assigns to the face.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** ImageId **   <a name="rekognition-Type-Face-ImageId"></a>
Unique identifier that Amazon Rekognition assigns to the input image.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** IndexFacesModelVersion **   <a name="rekognition-Type-Face-IndexFacesModelVersion"></a>
 The version of the face detect and storage model that was used when indexing the face vector.
Type: String
Pattern: `[0-9\.]+`
Required: No

 ** UserId **   <a name="rekognition-Type-Face-UserId"></a>
Unique identifier assigned to the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-:]+`
Required: No

## See Also
<a name="API_Face_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/Face)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/Face)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/Face)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
