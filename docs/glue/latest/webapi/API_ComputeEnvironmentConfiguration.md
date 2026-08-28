---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ComputeEnvironmentConfiguration.html
---

# ComputeEnvironmentConfiguration
<a name="API_ComputeEnvironmentConfiguration"></a>

An object containing configuration for a compute environment (such as Spark, Python or Athena) returned by the `DescribeConnectionType` API.

## Contents
<a name="API_ComputeEnvironmentConfiguration_Contents"></a>

 ** ComputeEnvironment **   <a name="Glue-Type-ComputeEnvironmentConfiguration-ComputeEnvironment"></a>
The type of compute environment.
Type: String
Valid Values: `SPARK | ATHENA | PYTHON`
Required: Yes

 ** ConnectionOptionNameOverrides **   <a name="Glue-Type-ComputeEnvironmentConfiguration-ConnectionOptionNameOverrides"></a>
The connection option name overrides for the compute environment.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** ConnectionOptions **   <a name="Glue-Type-ComputeEnvironmentConfiguration-ConnectionOptions"></a>
The parameters used as connection options for the compute environment.
Type: String to [Property](API_Property.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** ConnectionPropertiesRequiredOverrides **   <a name="Glue-Type-ComputeEnvironmentConfiguration-ConnectionPropertiesRequiredOverrides"></a>
The connection properties that are required as overrides for the compute environment.
Type: Array of strings
Required: Yes

 ** ConnectionPropertyNameOverrides **   <a name="Glue-Type-ComputeEnvironmentConfiguration-ConnectionPropertyNameOverrides"></a>
The connection property name overrides for the compute environment.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Description **   <a name="Glue-Type-ComputeEnvironmentConfiguration-Description"></a>
A description of the compute environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** Name **   <a name="Glue-Type-ComputeEnvironmentConfiguration-Name"></a>
A name for the compute environment configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** SupportedAuthenticationTypes **   <a name="Glue-Type-ComputeEnvironmentConfiguration-SupportedAuthenticationTypes"></a>
The supported authentication types for the compute environment.
Type: Array of strings
Valid Values: `BASIC | OAUTH2 | CUSTOM | IAM`
Required: Yes

 ** PhysicalConnectionPropertiesRequired **   <a name="Glue-Type-ComputeEnvironmentConfiguration-PhysicalConnectionPropertiesRequired"></a>
Indicates whether `PhysicalConnectionProperties` are required for the compute environment.
Type: Boolean
Required: No

## See Also
<a name="API_ComputeEnvironmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ComputeEnvironmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ComputeEnvironmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ComputeEnvironmentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
