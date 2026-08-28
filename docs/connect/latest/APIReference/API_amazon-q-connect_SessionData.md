---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SessionData.html
---

# SessionData
<a name="API_amazon-q-connect_SessionData"></a>

Information about the session.

## Contents
<a name="API_amazon-q-connect_SessionData_Contents"></a>

 ** name **   <a name="connect-Type-amazon-q-connect_SessionData-name"></a>
The name of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** sessionArn **   <a name="connect-Type-amazon-q-connect_SessionData-sessionArn"></a>
The Amazon Resource Name (ARN) of the session.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** sessionId **   <a name="connect-Type-amazon-q-connect_SessionData-sessionId"></a>
The identifier of the session.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** aiAgentConfiguration **   <a name="connect-Type-amazon-q-connect_SessionData-aiAgentConfiguration"></a>
The configuration of the AI Agents (mapped by AI Agent Type to AI Agent version) that should be used by Amazon Q in Connect for this Session.
Type: String to [AIAgentConfigurationData](API_amazon-q-connect_AIAgentConfigurationData.md) object map
Valid Keys: `MANUAL_SEARCH | ANSWER_RECOMMENDATION | SELF_SERVICE | EMAIL_RESPONSE | EMAIL_OVERVIEW | EMAIL_GENERATIVE_ANSWER | ORCHESTRATION | NOTE_TAKING | CASE_SUMMARIZATION`
Required: No

 ** description **   <a name="connect-Type-amazon-q-connect_SessionData-description"></a>
The description of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** integrationConfiguration **   <a name="connect-Type-amazon-q-connect_SessionData-integrationConfiguration"></a>
The configuration information for the session integration.
Type: [SessionIntegrationConfiguration](API_amazon-q-connect_SessionIntegrationConfiguration.md) object
Required: No

 ** orchestratorConfigurationList **   <a name="connect-Type-amazon-q-connect_SessionData-orchestratorConfigurationList"></a>
The list of orchestrator configurations for the session.
Type: Array of [OrchestratorConfigurationEntry](API_amazon-q-connect_OrchestratorConfigurationEntry.md) objects
Required: No

 ** origin **   <a name="connect-Type-amazon-q-connect_SessionData-origin"></a>
The origin of the Session to be listed. `SYSTEM` for a default Session created by Amazon Q in Connect or `CUSTOMER` for a Session created by calling [CreateSession](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_CreateSession.html) API.
Type: String
Valid Values: `SYSTEM | CUSTOMER`
Required: No

 ** tagFilter **   <a name="connect-Type-amazon-q-connect_SessionData-tagFilter"></a>
An object that can be used to specify Tag conditions.
Type: [TagFilter](API_amazon-q-connect_TagFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** tags **   <a name="connect-Type-amazon-q-connect_SessionData-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_amazon-q-connect_SessionData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SessionData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SessionData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SessionData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
