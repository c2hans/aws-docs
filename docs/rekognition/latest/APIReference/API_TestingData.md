---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_TestingData.html
---

# TestingData
<a name="API_TestingData"></a>

The dataset used for testing. Optionally, if `AutoCreate` is set, Amazon Rekognition uses the training dataset to create a test dataset with a temporary split of the training dataset.

## Contents
<a name="API_TestingData_Contents"></a>

 ** Assets **   <a name="rekognition-Type-TestingData-Assets"></a>
The assets used for testing.
Type: Array of [Asset](API_Asset.md) objects
Required: No

 ** AutoCreate **   <a name="rekognition-Type-TestingData-AutoCreate"></a>
If specified, Rekognition splits training dataset to create a test dataset for the training job.
Type: Boolean
Required: No

## See Also
<a name="API_TestingData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/TestingData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/TestingData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/TestingData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
