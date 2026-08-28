---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_DataAutomationProjectSummary.html
---

# DataAutomationProjectSummary
<a name="API_data-automation_DataAutomationProjectSummary"></a>

A summary of a data automation project.

## Contents
<a name="API_data-automation_DataAutomationProjectSummary_Contents"></a>

 ** creationTime **   <a name="bedrock-Type-data-automation_DataAutomationProjectSummary-creationTime"></a>
The project's creation time.
Type: Timestamp
Required: Yes

 ** projectArn **   <a name="bedrock-Type-data-automation_DataAutomationProjectSummary-projectArn"></a>
The project's ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):data-automation-project/[a-zA-Z0-9-]{12,36}`
Required: Yes

 ** projectName **   <a name="bedrock-Type-data-automation_DataAutomationProjectSummary-projectName"></a>
The project's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** projectStage **   <a name="bedrock-Type-data-automation_DataAutomationProjectSummary-projectStage"></a>
The project's stage.
Type: String
Valid Values: `DEVELOPMENT | LIVE`
Required: No

 ** projectType **   <a name="bedrock-Type-data-automation_DataAutomationProjectSummary-projectType"></a>
The project's type.
Type: String
Valid Values: `ASYNC | SYNC`
Required: No

## See Also
<a name="API_data-automation_DataAutomationProjectSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/DataAutomationProjectSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/DataAutomationProjectSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/DataAutomationProjectSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
