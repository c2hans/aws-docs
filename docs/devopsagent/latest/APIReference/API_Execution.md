---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_Execution.html
---

# Execution
<a name="API_Execution"></a>

Represents an execution instance with its lifecycle information

## Contents
<a name="API_Execution_Contents"></a>

 ** agentSpaceId **   <a name="devopsagent-Type-Execution-agentSpaceId"></a>
The unique identifier for the agent space containing this execution
Type: String
Required: Yes

 ** agentSubTask **   <a name="devopsagent-Type-Execution-agentSubTask"></a>
The specific subtask being executed by the agent
Type: String
Required: Yes

 ** createdAt **   <a name="devopsagent-Type-Execution-createdAt"></a>
Timestamp when this execution was created
Type: Timestamp
Required: Yes

 ** executionId **   <a name="devopsagent-Type-Execution-executionId"></a>
The unique identifier for this execution
Type: String
Required: Yes

 ** executionStatus **   <a name="devopsagent-Type-Execution-executionStatus"></a>
The current status of this execution
Type: String
Valid Values: `FAILED | RUNNING | STOPPED | CANCELED | TIMED_OUT`
Required: Yes

 ** updatedAt **   <a name="devopsagent-Type-Execution-updatedAt"></a>
Timestamp when this execution was last updated
Type: Timestamp
Required: Yes

 ** agentType **   <a name="devopsagent-Type-Execution-agentType"></a>
The type of agent that performed this execution.
Type: String
Required: No

 ** parentExecutionId **   <a name="devopsagent-Type-Execution-parentExecutionId"></a>
The identifier of the parent execution, if this is a child execution
Type: String
Required: No

 ** uid **   <a name="devopsagent-Type-Execution-uid"></a>
The unique identifier for the user session associated with this execution
Type: String
Required: No

## See Also
<a name="API_Execution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/Execution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/Execution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/Execution)
