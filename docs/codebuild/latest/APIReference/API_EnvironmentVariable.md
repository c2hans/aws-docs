---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_EnvironmentVariable.html
---

# EnvironmentVariable
<a name="API_EnvironmentVariable"></a>

Information about an environment variable for a build project or a build.

## Contents
<a name="API_EnvironmentVariable_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** name **   <a name="CodeBuild-Type-EnvironmentVariable-name"></a>
The name or key of the environment variable.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** value **   <a name="CodeBuild-Type-EnvironmentVariable-value"></a>
The value of the environment variable.
We strongly discourage the use of `PLAINTEXT` environment variables to store sensitive values, especially AWS secret key IDs. `PLAINTEXT` environment variables can be displayed in plain text using the AWS CodeBuild console and the AWS CLI. For sensitive values, we recommend you use an environment variable of type `PARAMETER_STORE` or `SECRETS_MANAGER`.
Type: String
Required: Yes

 ** type **   <a name="CodeBuild-Type-EnvironmentVariable-type"></a>
The type of environment variable. Valid values include:
+  `PARAMETER_STORE`: An environment variable stored in Systems Manager Parameter Store. For environment variables of this type, specify the name of the parameter as the `value` of the EnvironmentVariable. The parameter value will be substituted for the name at runtime. You can also define Parameter Store environment variables in the buildspec. To learn how to do so, see [env/parameter-store](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec.env.parameter-store) in the * AWS CodeBuild User Guide*.
+  `PLAINTEXT`: An environment variable in plain text format. This is the default value.
+  `SECRETS_MANAGER`: An environment variable stored in AWS Secrets Manager. For environment variables of this type, specify the name of the secret as the `value` of the EnvironmentVariable. The secret value will be substituted for the name at runtime. You can also define AWS Secrets Manager environment variables in the buildspec. To learn how to do so, see [env/secrets-manager](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec.env.secrets-manager) in the * AWS CodeBuild User Guide*.
Type: String
Valid Values: `PLAINTEXT | PARAMETER_STORE | SECRETS_MANAGER`
Required: No

## See Also
<a name="API_EnvironmentVariable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/EnvironmentVariable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/EnvironmentVariable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/EnvironmentVariable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
