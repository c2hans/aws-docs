---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_S3Presign.html
---

# S3Presign
<a name="API_S3Presign"></a>

This object defines the access restrictions to Amazon S3 resources that are included in custom worker task templates using the Liquid filter, `grant_read_access`.

To learn more about how custom templates are created, see [Create custom worker task templates](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-custom-templates.html).

## Contents
<a name="API_S3Presign_Contents"></a>

 ** IamPolicyConstraints **   <a name="sagemaker-Type-S3Presign-IamPolicyConstraints"></a>
Use this parameter to specify the allowed request source. Possible sources are either `SourceIp` or `VpcSourceIp`.
Type: [IamPolicyConstraints](API_IamPolicyConstraints.md) object
Required: No

## See Also
<a name="API_S3Presign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/S3Presign)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/S3Presign)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/S3Presign)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
