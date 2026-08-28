---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_AIAgentSummary.html
---

# AIAgentSummary
<a name="API_amazon-q-connect_AIAgentSummary"></a>

The summary of the AI Agent.

## Contents
<a name="API_amazon-q-connect_AIAgentSummary_Contents"></a>

 ** aiAgentArn **   <a name="connect-Type-amazon-q-connect_AIAgentSummary-aiAgentArn"></a>
The Amazon Resource Name (ARN) of the AI agent.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** aiAgentId **   <a name="connect-Type-amazon-q-connect_AIAgentSummary-aiAgentId"></a>
The identifier of the AI Agent.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** assistantArn **   <a name="connect-Type-amazon-q-connect_AIAgentSummary-assistantArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** assistantId **   <a name="connect-Type-amazon-q-connect_AIAgentSummary-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_AIAgentSummary-name"></a>
The name of the AI Agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** type **   <a name="connect-Type-amazon-q-connect_AIAgentSummary-type"></a>
The type of the AI Agent.
Type: String
Valid Values: `MANUAL_SEARCH | ANSWER_RECOMMENDATION | SELF_SERVICE | EMAIL_RESPONSE | EMAIL_OVERVIEW | EMAIL_GENERATIVE_ANSWER | ORCHESTRATION | NOTE_TAKING | CASE_SUMMARIZATION`
Required: Yes

 ** visibilityStatus **   <a name="connect-Type-amazon-q-connect_AIAgentSummary-visibilityStatus"></a>
The visibility status of the AI Agent.
Type: String
Valid Values: `SAVED | PUBLISHED`
Required: Yes

 ** configuration **   <a name="connect-Type-amazon-q-connect_AIAgentSummary-configuration"></a>
The configuration for the AI Agent.
Type: [AIAgentConfiguration](API_amazon-q-connect_AIAgentConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** description **   <a name="connect-Type-amazon-q-connect_AIAgentSummary-description"></a>
The description of the AI Agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** modifiedTime **   <a name="connect-Type-amazon-q-connect_AIAgentSummary-modifiedTime"></a>
The time the AI Agent was last modified.
Type: Timestamp
Required: No

 ** origin **   <a name="connect-Type-amazon-q-connect_AIAgentSummary-origin"></a>
The origin of the AI Agent. `SYSTEM` for a default AI Agent created by Q in Connect or `CUSTOMER` for an AI Agent created by calling AI Agent creation APIs.
Type: String
Valid Values: `SYSTEM | CUSTOMER`
Required: No

 ** status **   <a name="connect-Type-amazon-q-connect_AIAgentSummary-status"></a>
The status of the AI Agent.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_IN_PROGRESS | DELETE_FAILED | DELETED`
Required: No

 ** tags **   <a name="connect-Type-amazon-q-connect_AIAgentSummary-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_amazon-q-connect_AIAgentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/AIAgentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/AIAgentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/AIAgentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
