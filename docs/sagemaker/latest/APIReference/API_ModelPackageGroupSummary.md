---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelPackageGroupSummary.html
---

# ModelPackageGroupSummary
<a name="API_ModelPackageGroupSummary"></a>

Summary information about a model group.

## Contents
<a name="API_ModelPackageGroupSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-ModelPackageGroupSummary-CreationTime"></a>
The time that the model group was created.
Type: Timestamp
Required: Yes

 ** ModelPackageGroupArn **   <a name="sagemaker-Type-ModelPackageGroupSummary-ModelPackageGroupArn"></a>
The Amazon Resource Name (ARN) of the model group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package-group/[\S]{1,2048}`
Required: Yes

 ** ModelPackageGroupName **   <a name="sagemaker-Type-ModelPackageGroupSummary-ModelPackageGroupName"></a>
The name of the model group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ModelPackageGroupStatus **   <a name="sagemaker-Type-ModelPackageGroupSummary-ModelPackageGroupStatus"></a>
The status of the model group.
Type: String
Valid Values: `Pending | InProgress | Completed | Failed | Deleting | DeleteFailed`
Required: Yes

 ** ManagedConfiguration **   <a name="sagemaker-Type-ModelPackageGroupSummary-ManagedConfiguration"></a>
The managed configuration of the model package group.
Type: [ManagedConfiguration](API_ManagedConfiguration.md) object
Required: No

 ** ModelPackageGroupDescription **   <a name="sagemaker-Type-ModelPackageGroupSummary-ModelPackageGroupDescription"></a>
A description of the model group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

## See Also
<a name="API_ModelPackageGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelPackageGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelPackageGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelPackageGroupSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
