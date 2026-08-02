---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_QualityCheckStepMetadata.html
---

# QualityCheckStepMetadata
<a name="API_QualityCheckStepMetadata"></a>

Container for the metadata for a Quality check step. For more information, see the topic on [QualityCheck step](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html#step-type-quality-check) in the *Amazon SageMaker Developer Guide*.

## Contents
<a name="API_QualityCheckStepMetadata_Contents"></a>

 ** BaselineUsedForDriftCheckConstraints **   <a name="sagemaker-Type-QualityCheckStepMetadata-BaselineUsedForDriftCheckConstraints"></a>
The Amazon S3 URI of the baseline constraints file used for the drift check.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** BaselineUsedForDriftCheckStatistics **   <a name="sagemaker-Type-QualityCheckStepMetadata-BaselineUsedForDriftCheckStatistics"></a>
The Amazon S3 URI of the baseline statistics file used for the drift check.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** CalculatedBaselineConstraints **   <a name="sagemaker-Type-QualityCheckStepMetadata-CalculatedBaselineConstraints"></a>
The Amazon S3 URI of the newly calculated baseline constraints file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** CalculatedBaselineStatistics **   <a name="sagemaker-Type-QualityCheckStepMetadata-CalculatedBaselineStatistics"></a>
The Amazon S3 URI of the newly calculated baseline statistics file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** CheckJobArn **   <a name="sagemaker-Type-QualityCheckStepMetadata-CheckJobArn"></a>
The Amazon Resource Name (ARN) of the Quality check processing job that was run by this step execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** CheckType **   <a name="sagemaker-Type-QualityCheckStepMetadata-CheckType"></a>
The type of the Quality check step.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** ModelPackageGroupName **   <a name="sagemaker-Type-QualityCheckStepMetadata-ModelPackageGroupName"></a>
The model package group name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** RegisterNewBaseline **   <a name="sagemaker-Type-QualityCheckStepMetadata-RegisterNewBaseline"></a>
This flag indicates if a newly calculated baseline can be accessed through step properties `BaselineUsedForDriftCheckConstraints` and `BaselineUsedForDriftCheckStatistics`. If it is set to `False`, the previous baseline of the configured check type must also be available. These can be accessed through the `BaselineUsedForDriftCheckConstraints` and ` BaselineUsedForDriftCheckStatistics` properties.
Type: Boolean
Required: No

 ** SkipCheck **   <a name="sagemaker-Type-QualityCheckStepMetadata-SkipCheck"></a>
This flag indicates if the drift check against the previous baseline will be skipped or not. If it is set to `False`, the previous baseline of the configured check type must be available.
Type: Boolean
Required: No

 ** ViolationReport **   <a name="sagemaker-Type-QualityCheckStepMetadata-ViolationReport"></a>
The Amazon S3 URI of violation report if violations are detected.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_QualityCheckStepMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/QualityCheckStepMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/QualityCheckStepMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/QualityCheckStepMetadata)
