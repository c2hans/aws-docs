---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_EcrConfiguration.html
---

# EcrConfiguration
<a name="API_EcrConfiguration"></a>

Settings that Image Builder uses to configure the ECR repository and the output container images that Amazon Inspector scans.

## Contents
<a name="API_EcrConfiguration_Contents"></a>

 ** containerTags **   <a name="imagebuilder-Type-EcrConfiguration-containerTags"></a>
Tags for Image Builder to apply to the output container image that Amazon Inspector scans. Tags can help you identify and manage your scanned images.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** repositoryName **   <a name="imagebuilder-Type-EcrConfiguration-repositoryName"></a>
The name of the container repository that Amazon Inspector scans to identify findings for your container images. The name includes the path for the repository location. If you don’t provide this information, Image Builder creates a repository in your account named `image-builder-image-scanning-repository` for vulnerability scans of your output container images.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_EcrConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/EcrConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/EcrConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/EcrConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
