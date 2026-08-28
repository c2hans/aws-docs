---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AgentStatus.html
---

# AgentStatus
<a name="API_AgentStatus"></a>

Contains information about an agent status.

## Contents
<a name="API_AgentStatus_Contents"></a>

 ** AgentStatusARN **   <a name="connect-Type-AgentStatus-AgentStatusARN"></a>
The Amazon Resource Name (ARN) of the agent status.
Type: String
Required: No

 ** AgentStatusId **   <a name="connect-Type-AgentStatus-AgentStatusId"></a>
The identifier of the agent status.
Type: String
Required: No

 ** Description **   <a name="connect-Type-AgentStatus-Description"></a>
The description of the agent status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** DisplayOrder **   <a name="connect-Type-AgentStatus-DisplayOrder"></a>
The display order of the agent status.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-AgentStatus-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-AgentStatus-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-AgentStatus-Name"></a>
The name of the agent status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

 ** State **   <a name="connect-Type-AgentStatus-State"></a>
The state of the agent status.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** Tags **   <a name="connect-Type-AgentStatus-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** Type **   <a name="connect-Type-AgentStatus-Type"></a>
The type of agent status.
Type: String
Valid Values: `ROUTABLE | CUSTOM | OFFLINE`
Required: No

## See Also
<a name="API_AgentStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AgentStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AgentStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AgentStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
