---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_DataAutomationConfiguration.html
---

# DataAutomationConfiguration
<a name="API_data-automation-runtime_DataAutomationConfiguration"></a>

Details about a data automation project.

## Contents
<a name="API_data-automation-runtime_DataAutomationConfiguration_Contents"></a>

 ** dataAutomationProjectArn **   <a name="bedrock-Type-data-automation-runtime_DataAutomationConfiguration-dataAutomationProjectArn"></a>
The ARN of the project you're using in your configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):data-automation-project/[a-zA-Z0-9-_]+`
Required: Yes

 ** stage **   <a name="bedrock-Type-data-automation-runtime_DataAutomationConfiguration-stage"></a>
The project's stage.
Type: String
Valid Values: `LIVE | DEVELOPMENT`
Required: No

## See Also
<a name="API_data-automation-runtime_DataAutomationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-runtime-2024-06-13/DataAutomationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-runtime-2024-06-13/DataAutomationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-runtime-2024-06-13/DataAutomationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
