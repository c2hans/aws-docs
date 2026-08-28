---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DatasetSource.html
---

# DatasetSource
<a name="API_DatasetSource"></a>

 The source that Amazon Rekognition Custom Labels uses to create a dataset. To use an Amazon Sagemaker format manifest file, specify the S3 bucket location in the `GroundTruthManifest` field. The S3 bucket must be in your AWS account. To create a copy of an existing dataset, specify the Amazon Resource Name (ARN) of an existing dataset in `DatasetArn`.

You need to specify a value for `DatasetArn` or `GroundTruthManifest`, but not both. if you supply both values, or if you don't specify any values, an InvalidParameterException exception occurs.

For more information, see [CreateDataset](API_CreateDataset.md).

## Contents
<a name="API_DatasetSource_Contents"></a>

 ** DatasetArn **   <a name="rekognition-Type-DatasetSource-DatasetArn"></a>
 The ARN of an Amazon Rekognition Custom Labels dataset that you want to copy.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/dataset\/(train|test)\/[0-9]+$)`
Required: No

 ** GroundTruthManifest **   <a name="rekognition-Type-DatasetSource-GroundTruthManifest"></a>
The S3 bucket that contains an Amazon Sagemaker Ground Truth format manifest file.
Type: [GroundTruthManifest](API_GroundTruthManifest.md) object
Required: No

## See Also
<a name="API_DatasetSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DatasetSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DatasetSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DatasetSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
