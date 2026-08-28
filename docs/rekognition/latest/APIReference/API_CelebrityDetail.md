---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CelebrityDetail.html
---

# CelebrityDetail
<a name="API_CelebrityDetail"></a>

Information about a recognized celebrity.

## Contents
<a name="API_CelebrityDetail_Contents"></a>

 ** BoundingBox **   <a name="rekognition-Type-CelebrityDetail-BoundingBox"></a>
Bounding box around the body of a celebrity.
Type: [BoundingBox](API_BoundingBox.md) object
Required: No

 ** Confidence **   <a name="rekognition-Type-CelebrityDetail-Confidence"></a>
The confidence, in percentage, that Amazon Rekognition has that the recognized face is the celebrity.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Face **   <a name="rekognition-Type-CelebrityDetail-Face"></a>
Face details for the recognized celebrity.
Type: [FaceDetail](API_FaceDetail.md) object
Required: No

 ** Id **   <a name="rekognition-Type-CelebrityDetail-Id"></a>
The unique identifier for the celebrity.
Type: String
Pattern: `[0-9A-Za-z]*`
Required: No

 ** KnownGender **   <a name="rekognition-Type-CelebrityDetail-KnownGender"></a>
Retrieves the known gender for the celebrity.
Type: [KnownGender](API_KnownGender.md) object
Required: No

 ** Name **   <a name="rekognition-Type-CelebrityDetail-Name"></a>
The name of the celebrity.
Type: String
Required: No

 ** Urls **   <a name="rekognition-Type-CelebrityDetail-Urls"></a>
An array of URLs pointing to additional celebrity information.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 255 items.
Required: No

## See Also
<a name="API_CelebrityDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CelebrityDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/CelebrityDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CelebrityDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
