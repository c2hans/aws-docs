---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Summary.html
---

# Summary
<a name="API_Summary"></a>

The S3 bucket that contains the training summary. The training summary includes aggregated evaluation metrics for the entire testing dataset and metrics for each individual label.

You get the training summary S3 bucket location by calling [DescribeProjectVersions](API_DescribeProjectVersions.md).

## Contents
<a name="API_Summary_Contents"></a>

 ** S3Object **   <a name="rekognition-Type-Summary-S3Object"></a>
Provides the S3 bucket name and object name.
The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.
For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see [How Amazon Rekognition works with IAM](https://docs.aws.amazon.com/rekognition/latest/dg/security_iam_service-with-iam.html).
Type: [S3Object](API_S3Object.md) object
Required: No

## See Also
<a name="API_Summary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/Summary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/Summary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/Summary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
