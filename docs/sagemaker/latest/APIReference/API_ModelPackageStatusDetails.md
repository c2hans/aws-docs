---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelPackageStatusDetails.html
---

# ModelPackageStatusDetails
<a name="API_ModelPackageStatusDetails"></a>

Specifies the validation and image scan statuses of the model package.

## Contents
<a name="API_ModelPackageStatusDetails_Contents"></a>

 ** ValidationStatuses **   <a name="sagemaker-Type-ModelPackageStatusDetails-ValidationStatuses"></a>
The validation status of the model package.
Type: Array of [ModelPackageStatusItem](API_ModelPackageStatusItem.md) objects
Required: Yes

 ** ImageScanStatuses **   <a name="sagemaker-Type-ModelPackageStatusDetails-ImageScanStatuses"></a>
The status of the scan of the Docker image container for the model package.
Type: Array of [ModelPackageStatusItem](API_ModelPackageStatusItem.md) objects
Required: No

## See Also
<a name="API_ModelPackageStatusDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelPackageStatusDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelPackageStatusDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelPackageStatusDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
