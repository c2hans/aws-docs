---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelPackageSummary.html
---

# ModelPackageSummary
<a name="API_ModelPackageSummary"></a>

Provides summary information about a model package.

## Contents
<a name="API_ModelPackageSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-ModelPackageSummary-CreationTime"></a>
A timestamp that shows when the model package was created.
Type: Timestamp
Required: Yes

 ** ModelPackageArn **   <a name="sagemaker-Type-ModelPackageSummary-ModelPackageArn"></a>
The Amazon Resource Name (ARN) of the model package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`
Required: Yes

 ** ModelPackageStatus **   <a name="sagemaker-Type-ModelPackageSummary-ModelPackageStatus"></a>
The overall status of the model package.
Type: String
Valid Values: `Pending | InProgress | Completed | Failed | Deleting`
Required: Yes

 ** ModelApprovalStatus **   <a name="sagemaker-Type-ModelPackageSummary-ModelApprovalStatus"></a>
The approval status of the model. This can be one of the following values.
+  `APPROVED` - The model is approved
+  `REJECTED` - The model is rejected.
+  `PENDING_MANUAL_APPROVAL` - The model is waiting for manual approval.
Type: String
Valid Values: `Approved | Rejected | PendingManualApproval`
Required: No

 ** ModelLifeCycle **   <a name="sagemaker-Type-ModelPackageSummary-ModelLifeCycle"></a>
 A structure describing the current state of the model in its life cycle.
Type: [ModelLifeCycle](API_ModelLifeCycle.md) object
Required: No

 ** ModelPackageDescription **   <a name="sagemaker-Type-ModelPackageSummary-ModelPackageDescription"></a>
A brief description of the model package.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

 ** ModelPackageGroupName **   <a name="sagemaker-Type-ModelPackageSummary-ModelPackageGroupName"></a>
If the model package is a versioned model, the model group that the versioned model belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ModelPackageName **   <a name="sagemaker-Type-ModelPackageSummary-ModelPackageName"></a>
The name of the model package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ModelPackageRegistrationType **   <a name="sagemaker-Type-ModelPackageSummary-ModelPackageRegistrationType"></a>
 The package registration type of the model package summary.
Type: String
Valid Values: `Logged | Registered`
Required: No

 ** ModelPackageVersion **   <a name="sagemaker-Type-ModelPackageSummary-ModelPackageVersion"></a>
If the model package is a versioned model, the version of the model.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ModelPackageSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelPackageSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelPackageSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelPackageSummary)
