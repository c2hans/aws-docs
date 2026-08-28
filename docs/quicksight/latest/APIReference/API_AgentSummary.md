---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AgentSummary.html
---

# AgentSummary
<a name="API_AgentSummary"></a>

A summary of an agent, including its identifier, name, and metadata.

## Contents
<a name="API_AgentSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AgentId **   <a name="QS-Type-AgentSummary-AgentId"></a>
The unique identifier for the agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9a-zA-Z-_.+]+`
Required: Yes

 ** Arn **   <a name="QS-Type-AgentSummary-Arn"></a>
The Amazon Resource Name (ARN) of the agent.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** CreatedAt **   <a name="QS-Type-AgentSummary-CreatedAt"></a>
The date and time that the agent was created.
Type: Timestamp
Required: Yes

 ** Name **   <a name="QS-Type-AgentSummary-Name"></a>
The name of the agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(?!\s*$).+`
Required: Yes

 ** UpdatedAt **   <a name="QS-Type-AgentSummary-UpdatedAt"></a>
The date and time that the agent was last updated.
Type: Timestamp
Required: Yes

 ** Description **   <a name="QS-Type-AgentSummary-Description"></a>
A description of the agent.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `\P{C}*`
Required: No

 ** IconId **   <a name="QS-Type-AgentSummary-IconId"></a>
The icon identifier for the agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

## See Also
<a name="API_AgentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AgentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AgentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AgentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
