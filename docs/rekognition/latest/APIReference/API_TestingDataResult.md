---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_TestingDataResult.html
---

# TestingDataResult
<a name="API_TestingDataResult"></a>

Sagemaker Groundtruth format manifest files for the input, output and validation datasets that are used and created during testing.

## Contents
<a name="API_TestingDataResult_Contents"></a>

 ** Input **   <a name="rekognition-Type-TestingDataResult-Input"></a>
The testing dataset that was supplied for training.
Type: [TestingData](API_TestingData.md) object
Required: No

 ** Output **   <a name="rekognition-Type-TestingDataResult-Output"></a>
The subset of the dataset that was actually tested. Some images (assets) might not be tested due to file formatting and other issues.
Type: [TestingData](API_TestingData.md) object
Required: No

 ** Validation **   <a name="rekognition-Type-TestingDataResult-Validation"></a>
The location of the data validation manifest. The data validation manifest is created for the test dataset during model training.
Type: [ValidationData](API_ValidationData.md) object
Required: No

## See Also
<a name="API_TestingDataResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/TestingDataResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/TestingDataResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/TestingDataResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
