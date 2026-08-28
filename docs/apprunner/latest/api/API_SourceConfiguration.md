---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_SourceConfiguration.html
---

# SourceConfiguration
<a name="API_SourceConfiguration"></a>

Describes the source deployed to an AWS App Runner service. It can be a code or an image repository.

## Contents
<a name="API_SourceConfiguration_Contents"></a>

 ** AuthenticationConfiguration **   <a name="apprunner-Type-SourceConfiguration-AuthenticationConfiguration"></a>
Describes the resources that are needed to authenticate access to some source repositories.
Type: [AuthenticationConfiguration](API_AuthenticationConfiguration.md) object
Required: No

 ** AutoDeploymentsEnabled **   <a name="apprunner-Type-SourceConfiguration-AutoDeploymentsEnabled"></a>
If `true`, continuous integration from the source repository is enabled for the App Runner service. Each repository change (including any source code commit or new image version) starts a deployment.
Default: App Runner sets to `false` for a source image that uses an ECR Public repository or an ECR repository that's in an AWS account other than the one that the service is in. App Runner sets to `true` in all other cases (which currently include a source code repository or a source image using a same-account ECR repository).
Type: Boolean
Required: No

 ** CodeRepository **   <a name="apprunner-Type-SourceConfiguration-CodeRepository"></a>
The description of a source code repository.
You must provide either this member or `ImageRepository` (but not both).
Type: [CodeRepository](API_CodeRepository.md) object
Required: No

 ** ImageRepository **   <a name="apprunner-Type-SourceConfiguration-ImageRepository"></a>
The description of a source image repository.
You must provide either this member or `CodeRepository` (but not both).
Type: [ImageRepository](API_ImageRepository.md) object
Required: No

## See Also
<a name="API_SourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/SourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/SourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/SourceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
