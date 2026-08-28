---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_WorkerAccessConfiguration.html
---

# WorkerAccessConfiguration
<a name="API_WorkerAccessConfiguration"></a>

Use this optional parameter to constrain access to an Amazon S3 resource based on the IP address using supported IAM global condition keys. The Amazon S3 resource is accessed in the worker portal using a Amazon S3 presigned URL.

## Contents
<a name="API_WorkerAccessConfiguration_Contents"></a>

 ** S3Presign **   <a name="sagemaker-Type-WorkerAccessConfiguration-S3Presign"></a>
Defines any Amazon S3 resource constraints.
Type: [S3Presign](API_S3Presign.md) object
Required: No

## See Also
<a name="API_WorkerAccessConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/WorkerAccessConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/WorkerAccessConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/WorkerAccessConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
