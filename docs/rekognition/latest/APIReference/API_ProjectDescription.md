---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ProjectDescription.html
---

# ProjectDescription
<a name="API_ProjectDescription"></a>

A description of an Amazon Rekognition Custom Labels project. For more information, see [DescribeProjects](API_DescribeProjects.md).

## Contents
<a name="API_ProjectDescription_Contents"></a>

 ** AutoUpdate **   <a name="rekognition-Type-ProjectDescription-AutoUpdate"></a>
Indicates whether automatic retraining will be attempted for the versions of the project. Applies only to adapters.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** CreationTimestamp **   <a name="rekognition-Type-ProjectDescription-CreationTimestamp"></a>
The Unix timestamp for the date and time that the project was created.
Type: Timestamp
Required: No

 ** Datasets **   <a name="rekognition-Type-ProjectDescription-Datasets"></a>
 Information about the training and test datasets in the project.
Type: Array of [DatasetMetadata](API_DatasetMetadata.md) objects
Required: No

 ** Feature **   <a name="rekognition-Type-ProjectDescription-Feature"></a>
Specifies the project that is being customized.
Type: String
Valid Values: `CONTENT_MODERATION | CUSTOM_LABELS`
Required: No

 ** ProjectArn **   <a name="rekognition-Type-ProjectDescription-ProjectArn"></a>
The Amazon Resource Name (ARN) of the project.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
Required: No

 ** Status **   <a name="rekognition-Type-ProjectDescription-Status"></a>
The current status of the project.
Type: String
Valid Values: `CREATING | CREATED | DELETING`
Required: No

## See Also
<a name="API_ProjectDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ProjectDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ProjectDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ProjectDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
