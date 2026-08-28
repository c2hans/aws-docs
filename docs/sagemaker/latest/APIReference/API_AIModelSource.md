---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIModelSource.html
---

# AIModelSource
<a name="API_AIModelSource"></a>

The source of the model for an AI recommendation job. This is a union type.

## Contents
<a name="API_AIModelSource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** S3 **   <a name="sagemaker-Type-AIModelSource-S3"></a>
The Amazon S3 location of the model artifacts.
Type: [AIModelSourceS3](API_AIModelSourceS3.md) object
Required: No

## See Also
<a name="API_AIModelSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIModelSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIModelSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIModelSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
