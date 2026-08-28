---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchDescribeModelPackageSummary.html
---

# BatchDescribeModelPackageSummary
<a name="API_BatchDescribeModelPackageSummary"></a>

Provides summary information about the model package.

## Contents
<a name="API_BatchDescribeModelPackageSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-BatchDescribeModelPackageSummary-CreationTime"></a>
The creation time of the mortgage package summary.
Type: Timestamp
Required: Yes

 ** InferenceSpecification **   <a name="sagemaker-Type-BatchDescribeModelPackageSummary-InferenceSpecification"></a>
Defines how to perform inference generation after a training job is run.
Type: [InferenceSpecification](API_InferenceSpecification.md) object
Required: Yes

 ** ModelPackageArn **   <a name="sagemaker-Type-BatchDescribeModelPackageSummary-ModelPackageArn"></a>
The Amazon Resource Name (ARN) of the model package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`
Required: Yes

 ** ModelPackageGroupName **   <a name="sagemaker-Type-BatchDescribeModelPackageSummary-ModelPackageGroupName"></a>
The group name for the model package
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ModelPackageStatus **   <a name="sagemaker-Type-BatchDescribeModelPackageSummary-ModelPackageStatus"></a>
The status of the mortgage package.
Type: String
Valid Values: `Pending | InProgress | Completed | Failed | Deleting`
Required: Yes

 ** ModelApprovalStatus **   <a name="sagemaker-Type-BatchDescribeModelPackageSummary-ModelApprovalStatus"></a>
The approval status of the model.
Type: String
Valid Values: `Approved | Rejected | PendingManualApproval`
Required: No

 ** ModelPackageDescription **   <a name="sagemaker-Type-BatchDescribeModelPackageSummary-ModelPackageDescription"></a>
The description of the model package.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

 ** ModelPackageRegistrationType **   <a name="sagemaker-Type-BatchDescribeModelPackageSummary-ModelPackageRegistrationType"></a>
 The package registration type of the model package summary.
Type: String
Valid Values: `Logged | Registered`
Required: No

 ** ModelPackageVersion **   <a name="sagemaker-Type-BatchDescribeModelPackageSummary-ModelPackageVersion"></a>
The version number of a versioned model.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_BatchDescribeModelPackageSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/BatchDescribeModelPackageSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/BatchDescribeModelPackageSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/BatchDescribeModelPackageSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
