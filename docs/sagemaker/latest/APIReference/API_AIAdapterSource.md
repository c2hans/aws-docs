---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIAdapterSource.html
---

# AIAdapterSource
<a name="API_AIAdapterSource"></a>

The source of LoRA adapters for an AI recommendation job. This is a union type — specify exactly one of the members.

## Contents
<a name="API_AIAdapterSource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ModelPackageArns **   <a name="sagemaker-Type-AIAdapterSource-ModelPackageArns"></a>
A list of LoRA adapters identified by their model package ARNs. Use this when your adapters were produced by a SageMaker AI fine-tuning workflow that registers model packages.
Type: Array of [AIAdapterModelPackageEntry](API_AIAdapterModelPackageEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** S3Uris **   <a name="sagemaker-Type-AIAdapterSource-S3Uris"></a>
A list of LoRA adapters identified by their Amazon S3 URIs. Use this when your adapters are stored as raw artifacts in Amazon S3.
Type: Array of [AIAdapterS3Entry](API_AIAdapterS3Entry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_AIAdapterSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIAdapterSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIAdapterSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIAdapterSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
