---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_AgentFilter.html
---

# AgentFilter
<a name="API_AgentFilter"></a>

Contains information about an Amazon Inspector Classic agent. This data type is used as a request parameter in the [ListAssessmentRunAgents](API_ListAssessmentRunAgents.md) action.

## Contents
<a name="API_AgentFilter_Contents"></a>

 ** agentHealthCodes **   <a name="Inspector-Type-AgentFilter-agentHealthCodes"></a>
The detailed health state of the agent. Values can be set to **IDLE**, **RUNNING**, **SHUTDOWN**, **UNHEALTHY**, **THROTTLED**, and **UNKNOWN**.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Valid Values: `IDLE | RUNNING | SHUTDOWN | UNHEALTHY | THROTTLED | UNKNOWN`
Required: Yes

 ** agentHealths **   <a name="Inspector-Type-AgentFilter-agentHealths"></a>
The current health state of the agent. Values can be set to **HEALTHY** or **UNHEALTHY**.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Valid Values: `HEALTHY | UNHEALTHY | UNKNOWN`
Required: Yes

## See Also
<a name="API_AgentFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/AgentFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/AgentFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/AgentFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
