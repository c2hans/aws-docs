---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_VulnerablePackage.html
---

# VulnerablePackage
<a name="API_VulnerablePackage"></a>

Information on the vulnerable package identified by a finding.

## Contents
<a name="API_VulnerablePackage_Contents"></a>

 ** name **   <a name="inspector2-Type-VulnerablePackage-name"></a>
The name of the vulnerable package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** version **   <a name="inspector2-Type-VulnerablePackage-version"></a>
The version of the vulnerable package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** arch **   <a name="inspector2-Type-VulnerablePackage-arch"></a>
The architecture of the vulnerable package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** epoch **   <a name="inspector2-Type-VulnerablePackage-epoch"></a>
The epoch of the vulnerable package.
Type: Integer
Required: No

 ** filePath **   <a name="inspector2-Type-VulnerablePackage-filePath"></a>
The file path of the vulnerable package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** fixedInVersion **   <a name="inspector2-Type-VulnerablePackage-fixedInVersion"></a>
The version of the package that contains the vulnerability fix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** packageManager **   <a name="inspector2-Type-VulnerablePackage-packageManager"></a>
The package manager of the vulnerable package.
Type: String
Valid Values: `BUNDLER | CARGO | COMPOSER | NPM | NUGET | PIPENV | POETRY | YARN | GOBINARY | GOMOD | JAR | OS | PIP | PYTHONPKG | NODEPKG | POM | GEMSPEC | DOTNET_CORE`
Required: No

 ** release **   <a name="inspector2-Type-VulnerablePackage-release"></a>
The release of the vulnerable package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** remediation **   <a name="inspector2-Type-VulnerablePackage-remediation"></a>
The code to run in your environment to update packages with a fix available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** sourceLambdaLayerArn **   <a name="inspector2-Type-VulnerablePackage-sourceLambdaLayerArn"></a>
The Amazon Resource Number (ARN) of the AWS Lambda function affected by a finding.
Type: String
Pattern: `arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+:[0-9]+`
Required: No

 ** sourceLayerHash **   <a name="inspector2-Type-VulnerablePackage-sourceLayerHash"></a>
The source layer hash of the vulnerable package.
Type: String
Length Constraints: Fixed length of 71.
Pattern: `sha256:[a-z0-9]{64}`
Required: No

## See Also
<a name="API_VulnerablePackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/VulnerablePackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/VulnerablePackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/VulnerablePackage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
