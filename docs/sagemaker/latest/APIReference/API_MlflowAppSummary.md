---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MlflowAppSummary.html
---

# MlflowAppSummary
<a name="API_MlflowAppSummary"></a>

The summary of the Mlflow App to list.

## Contents
<a name="API_MlflowAppSummary_Contents"></a>

 ** Arn **   <a name="sagemaker-Type-MlflowAppSummary-Arn"></a>
The ARN of a listed MLflow App.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:mlflow-app/.*`
Required: No

 ** CreationTime **   <a name="sagemaker-Type-MlflowAppSummary-CreationTime"></a>
The creation time of a listed MLflow App.
Type: Timestamp
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-MlflowAppSummary-LastModifiedTime"></a>
The last modified time of a listed MLflow App.
Type: Timestamp
Required: No

 ** MlflowVersion **   <a name="sagemaker-Type-MlflowAppSummary-MlflowVersion"></a>
The version of a listed MLflow App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Pattern: `[0-9]*.[0-9]*.[0-9]*`
Required: No

 ** Name **   <a name="sagemaker-Type-MlflowAppSummary-Name"></a>
The name of the MLflow App.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: No

 ** Status **   <a name="sagemaker-Type-MlflowAppSummary-Status"></a>
The status of the MLflow App.
Type: String
Valid Values: `Creating | Created | CreateFailed | Updating | Updated | UpdateFailed | Deleting | DeleteFailed | Deleted`
Required: No

## See Also
<a name="API_MlflowAppSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MlflowAppSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MlflowAppSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MlflowAppSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
