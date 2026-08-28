---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ImageConfig.html
---

# ImageConfig
<a name="API_ImageConfig"></a>

Specifies whether the model container is in Amazon ECR or a private Docker registry accessible from your Amazon Virtual Private Cloud (VPC).

## Contents
<a name="API_ImageConfig_Contents"></a>

 ** RepositoryAccessMode **   <a name="sagemaker-Type-ImageConfig-RepositoryAccessMode"></a>
Set this to one of the following values:
+  `Platform` - The model image is hosted in Amazon ECR.
+  `Vpc` - The model image is hosted in a private Docker registry in your VPC.
Type: String
Valid Values: `Platform | Vpc`
Required: Yes

 ** RepositoryAuthConfig **   <a name="sagemaker-Type-ImageConfig-RepositoryAuthConfig"></a>
(Optional) Specifies an authentication configuration for the private docker registry where your model image is hosted. Specify a value for this property only if you specified `Vpc` as the value for the `RepositoryAccessMode` field, and the private Docker registry where the model image is hosted requires authentication.
Type: [RepositoryAuthConfig](API_RepositoryAuthConfig.md) object
Required: No

## See Also
<a name="API_ImageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ImageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ImageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ImageConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
