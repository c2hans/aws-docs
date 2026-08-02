---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Agent.html
---

# Agent
<a name="API_Agent"></a>

An agent resource in Amazon QuickSight that provides AI-powered conversational experiences.

## Contents
<a name="API_Agent_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AgentId **   <a name="QS-Type-Agent-AgentId"></a>
The unique identifier for the agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9a-zA-Z-_.+]+`
Required: Yes

 ** AgentLifecycle **   <a name="QS-Type-Agent-AgentLifecycle"></a>
The lifecycle state of the agent. Valid values are `PREVIEW` and `PUBLISHED`.
Type: String
Valid Values: `PREVIEW | PUBLISHED`
Required: Yes

 ** AgentStatus **   <a name="QS-Type-Agent-AgentStatus"></a>
The status of the agent.
Type: String
Valid Values: `ACTIVE | UPDATING | FAILED | CREATING`
Required: Yes

 ** Arn **   <a name="QS-Type-Agent-Arn"></a>
The Amazon Resource Name (ARN) of the agent.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** CreatedAt **   <a name="QS-Type-Agent-CreatedAt"></a>
The date and time that the agent was created.
Type: Timestamp
Required: Yes

 ** Creator **   <a name="QS-Type-Agent-Creator"></a>
The identity of the user who created the agent.
Type: String
Required: Yes

 ** Name **   <a name="QS-Type-Agent-Name"></a>
The name of the agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(?!\s*$).+`
Required: Yes

 ** UpdatedAt **   <a name="QS-Type-Agent-UpdatedAt"></a>
The date and time that the agent was last updated.
Type: Timestamp
Required: Yes

 ** ActionConnectors **   <a name="QS-Type-Agent-ActionConnectors"></a>
The Amazon Resource Names (ARNs) of the action connectors attached to the agent.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** CustomPromptInterface **   <a name="QS-Type-Agent-CustomPromptInterface"></a>
The custom prompt interface configuration for the agent.
Type: [CustomPromptInterface](API_CustomPromptInterface.md) object
Required: No

 ** Description **   <a name="QS-Type-Agent-Description"></a>
A description of the agent.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `\P{C}*`
Required: No

 ** ErrorMessage **   <a name="QS-Type-Agent-ErrorMessage"></a>
An error message associated with the agent, if applicable.
Type: String
Required: No

 ** IconId **   <a name="QS-Type-Agent-IconId"></a>
The icon identifier for the agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** Spaces **   <a name="QS-Type-Agent-Spaces"></a>
The Amazon Resource Names (ARNs) of the spaces attached to the agent.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** StarterPrompts **   <a name="QS-Type-Agent-StarterPrompts"></a>
A list of starter prompts that are displayed to users when they begin interacting with the agent.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** WelcomeMessage **   <a name="QS-Type-Agent-WelcomeMessage"></a>
The welcome message that is displayed when a user starts a conversation with the agent.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Required: No

## See Also
<a name="API_Agent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Agent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Agent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Agent)
