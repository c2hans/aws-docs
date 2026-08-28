---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCodeBuildProjectEnvironment.html
---

# AwsCodeBuildProjectEnvironment
<a name="API_AwsCodeBuildProjectEnvironment"></a>

Information about the build environment for this build project.

## Contents
<a name="API_AwsCodeBuildProjectEnvironment_Contents"></a>

 ** Certificate **   <a name="securityhub-Type-AwsCodeBuildProjectEnvironment-Certificate"></a>
The certificate to use with this build project.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EnvironmentVariables **   <a name="securityhub-Type-AwsCodeBuildProjectEnvironment-EnvironmentVariables"></a>
A set of environment variables to make available to builds for the build project.
Type: Array of [AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetails](API_AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetails.md) objects
Required: No

 ** ImagePullCredentialsType **   <a name="securityhub-Type-AwsCodeBuildProjectEnvironment-ImagePullCredentialsType"></a>
The type of credentials AWS CodeBuild uses to pull images in your build.
Valid values:
+  `CODEBUILD` specifies that AWS CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust the AWS CodeBuild service principal.
+  `SERVICE_ROLE` specifies that AWS CodeBuild uses your build project's service role.
When you use a cross-account or private registry image, you must use `SERVICE_ROLE` credentials. When you use an AWS CodeBuild curated image, you must use `CODEBUILD` credentials.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PrivilegedMode **   <a name="securityhub-Type-AwsCodeBuildProjectEnvironment-PrivilegedMode"></a>
Whether to allow the Docker daemon to run inside a Docker container. Set to `true` if the build project is used to build Docker images.
Type: Boolean
Required: No

 ** RegistryCredential **   <a name="securityhub-Type-AwsCodeBuildProjectEnvironment-RegistryCredential"></a>
The credentials for access to a private registry.
Type: [AwsCodeBuildProjectEnvironmentRegistryCredential](API_AwsCodeBuildProjectEnvironmentRegistryCredential.md) object
Required: No

 ** Type **   <a name="securityhub-Type-AwsCodeBuildProjectEnvironment-Type"></a>
The type of build environment to use for related builds.
The environment type `ARM_CONTAINER` is available only in Regions US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Sydney), and Europe (Frankfurt).
The environment type `LINUX_CONTAINER` with compute type build.general1.2xlarge is available only in Regions US East (N. Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), Europe (Ireland), Europe (London), Europe (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).
The environment type `LINUX_GPU_CONTAINER` is available only in Regions US East (N. Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), Europe (Ireland), Europe (London), Europe (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).
Valid values: `WINDOWS_CONTAINER` \| `LINUX_CONTAINER` \| `LINUX_GPU_CONTAINER` \| `ARM_CONTAINER`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsCodeBuildProjectEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCodeBuildProjectEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCodeBuildProjectEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCodeBuildProjectEnvironment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
