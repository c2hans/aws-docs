---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AgentStatusSummary.html
---

# AgentStatusSummary
<a name="API_AgentStatusSummary"></a>

Summary information for an agent status.

## Contents
<a name="API_AgentStatusSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-AgentStatusSummary-Arn"></a>
The Amazon Resource Name (ARN) for the agent status.
Type: String
Required: No

 ** Id **   <a name="connect-Type-AgentStatusSummary-Id"></a>
The identifier for an agent status.
Type: String
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-AgentStatusSummary-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-AgentStatusSummary-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-AgentStatusSummary-Name"></a>
The name of the agent status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

 ** Type **   <a name="connect-Type-AgentStatusSummary-Type"></a>
The type of the agent status.
Type: String
Valid Values: `ROUTABLE | CUSTOM | OFFLINE`
Required: No

## See Also
<a name="API_AgentStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AgentStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AgentStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AgentStatusSummary)
