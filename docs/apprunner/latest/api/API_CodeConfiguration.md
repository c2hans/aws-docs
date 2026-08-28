---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_CodeConfiguration.html
---

# CodeConfiguration
<a name="API_CodeConfiguration"></a>

Describes the configuration that AWS App Runner uses to build and run an App Runner service from a source code repository.

## Contents
<a name="API_CodeConfiguration_Contents"></a>

 ** ConfigurationSource **   <a name="apprunner-Type-CodeConfiguration-ConfigurationSource"></a>
The source of the App Runner configuration. Values are interpreted as follows:
+  `REPOSITORY` – App Runner reads configuration values from the `apprunner.yaml` file in the source code repository and ignores `CodeConfigurationValues`.
+  `API` – App Runner uses configuration values provided in `CodeConfigurationValues` and ignores the `apprunner.yaml` file in the source code repository.
Type: String
Valid Values: `REPOSITORY | API`
Required: Yes

 ** CodeConfigurationValues **   <a name="apprunner-Type-CodeConfiguration-CodeConfigurationValues"></a>
The basic configuration for building and running the App Runner service. Use it to quickly launch an App Runner service without providing a `apprunner.yaml` file in the source code repository (or ignoring the file if it exists).
Type: [CodeConfigurationValues](API_CodeConfigurationValues.md) object
Required: No

## See Also
<a name="API_CodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/CodeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/CodeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/CodeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
