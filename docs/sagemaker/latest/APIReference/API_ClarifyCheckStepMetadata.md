---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClarifyCheckStepMetadata.html
---

# ClarifyCheckStepMetadata
<a name="API_ClarifyCheckStepMetadata"></a>

The container for the metadata for the ClarifyCheck step. For more information, see the topic on [ClarifyCheck step](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html#step-type-clarify-check) in the *Amazon SageMaker Developer Guide*.

## Contents
<a name="API_ClarifyCheckStepMetadata_Contents"></a>

 ** BaselineUsedForDriftCheckConstraints **   <a name="sagemaker-Type-ClarifyCheckStepMetadata-BaselineUsedForDriftCheckConstraints"></a>
The Amazon S3 URI of baseline constraints file to be used for the drift check.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** CalculatedBaselineConstraints **   <a name="sagemaker-Type-ClarifyCheckStepMetadata-CalculatedBaselineConstraints"></a>
The Amazon S3 URI of the newly calculated baseline constraints file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** CheckJobArn **   <a name="sagemaker-Type-ClarifyCheckStepMetadata-CheckJobArn"></a>
The Amazon Resource Name (ARN) of the check processing job that was run by this step's execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** CheckType **   <a name="sagemaker-Type-ClarifyCheckStepMetadata-CheckType"></a>
The type of the Clarify Check step
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** ModelPackageGroupName **   <a name="sagemaker-Type-ClarifyCheckStepMetadata-ModelPackageGroupName"></a>
The model package group name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** RegisterNewBaseline **   <a name="sagemaker-Type-ClarifyCheckStepMetadata-RegisterNewBaseline"></a>
This flag indicates if a newly calculated baseline can be accessed through step properties `BaselineUsedForDriftCheckConstraints` and `BaselineUsedForDriftCheckStatistics`. If it is set to `False`, the previous baseline of the configured check type must also be available. These can be accessed through the `BaselineUsedForDriftCheckConstraints` property.
Type: Boolean
Required: No

 ** SkipCheck **   <a name="sagemaker-Type-ClarifyCheckStepMetadata-SkipCheck"></a>
This flag indicates if the drift check against the previous baseline will be skipped or not. If it is set to `False`, the previous baseline of the configured check type must be available.
Type: Boolean
Required: No

 ** ViolationReport **   <a name="sagemaker-Type-ClarifyCheckStepMetadata-ViolationReport"></a>
The Amazon S3 URI of the violation report if violations are detected.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_ClarifyCheckStepMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClarifyCheckStepMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClarifyCheckStepMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClarifyCheckStepMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
