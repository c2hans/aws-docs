---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIAdapterModelPackageEntry.html
---

# AIAdapterModelPackageEntry
<a name="API_AIAdapterModelPackageEntry"></a>

A LoRA adapter entry identified by a model package ARN.

## Contents
<a name="API_AIAdapterModelPackageEntry_Contents"></a>

 ** AdapterId **   <a name="sagemaker-Type-AIAdapterModelPackageEntry-AdapterId"></a>
A unique identifier for the adapter. This ID is used as the inference component name when the adapter is deployed. The ID must start and end with an alphanumeric character, can contain hyphens between alphanumeric characters, and can be up to 63 characters long.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** ModelPackageArn **   <a name="sagemaker-Type-AIAdapterModelPackageEntry-ModelPackageArn"></a>
The Amazon Resource Name (ARN) of the model package that contains the LoRA adapter artifacts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`
Required: Yes

## See Also
<a name="API_AIAdapterModelPackageEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIAdapterModelPackageEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIAdapterModelPackageEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIAdapterModelPackageEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
