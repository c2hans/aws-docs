---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelPackageValidationSpecification.html
---

# ModelPackageValidationSpecification
<a name="API_ModelPackageValidationSpecification"></a>

Specifies batch transform jobs that SageMaker runs to validate your model package.

## Contents
<a name="API_ModelPackageValidationSpecification_Contents"></a>

 ** ValidationProfiles **   <a name="sagemaker-Type-ModelPackageValidationSpecification-ValidationProfiles"></a>
An array of `ModelPackageValidationProfile` objects, each of which specifies a batch transform job that SageMaker runs to validate your model package.
Type: Array of [ModelPackageValidationProfile](API_ModelPackageValidationProfile.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: Yes

 ** ValidationRole **   <a name="sagemaker-Type-ModelPackageValidationSpecification-ValidationRole"></a>
The IAM roles to be used for the validation of the model package.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

## See Also
<a name="API_ModelPackageValidationSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelPackageValidationSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelPackageValidationSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelPackageValidationSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
