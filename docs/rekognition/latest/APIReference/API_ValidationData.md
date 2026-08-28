---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ValidationData.html
---

# ValidationData
<a name="API_ValidationData"></a>

Contains the Amazon S3 bucket location of the validation data for a model training job.

The validation data includes error information for individual JSON lines in the dataset. For more information, see [Debugging a Failed Model Training](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tm-debugging.html).

You get the `ValidationData` object for the training dataset ([TrainingDataResult](API_TrainingDataResult.md)) and the test dataset ([TestingDataResult](API_TestingDataResult.md)) by calling [DescribeProjectVersions](API_DescribeProjectVersions.md).

The assets array contains a single [Asset](API_Asset.md) object. The [GroundTruthManifest](API_GroundTruthManifest.md) field of the Asset object contains the S3 bucket location of the validation data.

## Contents
<a name="API_ValidationData_Contents"></a>

 ** Assets **   <a name="rekognition-Type-ValidationData-Assets"></a>
The assets that comprise the validation data.
Type: Array of [Asset](API_Asset.md) objects
Required: No

## See Also
<a name="API_ValidationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ValidationData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ValidationData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ValidationData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
