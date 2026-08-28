---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_DevEnvironmentSessionConfiguration.html
---

# DevEnvironmentSessionConfiguration
<a name="API_DevEnvironmentSessionConfiguration"></a>

Information about the configuration of a Dev Environment session.

## Contents
<a name="API_DevEnvironmentSessionConfiguration_Contents"></a>

 ** sessionType **   <a name="codecatalyst-Type-DevEnvironmentSessionConfiguration-sessionType"></a>
The type of the session.
Type: String
Valid Values: `SSM | SSH`
Required: Yes

 ** executeCommandSessionConfiguration **   <a name="codecatalyst-Type-DevEnvironmentSessionConfiguration-executeCommandSessionConfiguration"></a>
Information about optional commands that will be run on the Dev Environment when the SSH session begins.
Type: [ExecuteCommandSessionConfiguration](API_ExecuteCommandSessionConfiguration.md) object
Required: No

## See Also
<a name="API_DevEnvironmentSessionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/DevEnvironmentSessionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/DevEnvironmentSessionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/DevEnvironmentSessionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
