---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_Task.html
---

# Task
<a name="API_Task"></a>

Represents an individual security test task within a pentest job. Each task targets a specific risk type or endpoint and executes independently.

## Contents
<a name="API_Task_Contents"></a>

 ** taskId **   <a name="securityagent-Type-Task-taskId"></a>
The unique identifier of the task.
Type: String
Required: Yes

 ** agentSpaceId **   <a name="securityagent-Type-Task-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: No

 ** categories **   <a name="securityagent-Type-Task-categories"></a>
The list of categories assigned to the task.
Type: Array of [Category](API_Category.md) objects
Required: No

 ** createdAt **   <a name="securityagent-Type-Task-createdAt"></a>
The date and time the task was created, in UTC format.
Type: Timestamp
Required: No

 ** description **   <a name="securityagent-Type-Task-description"></a>
A description of the task.
Type: String
Required: No

 ** executionStatus **   <a name="securityagent-Type-Task-executionStatus"></a>
The current execution status of the task.
Type: String
Valid Values: `IN_PROGRESS | ABORTED | COMPLETED | INTERNAL_ERROR | FAILED`
Required: No

 ** logsLocation **   <a name="securityagent-Type-Task-logsLocation"></a>
The location of the task execution logs.
Type: [LogLocation](API_LogLocation.md) object
Required: No

 ** pentestId **   <a name="securityagent-Type-Task-pentestId"></a>
The unique identifier of the pentest associated with the task.
Type: String
Required: No

 ** pentestJobId **   <a name="securityagent-Type-Task-pentestJobId"></a>
The unique identifier of the pentest job that contains the task.
Type: String
Required: No

 ** riskType **   <a name="securityagent-Type-Task-riskType"></a>
The type of security risk the task is testing for.
Type: String
Valid Values: `CROSS_SITE_SCRIPTING | DEFAULT_CREDENTIALS | INSECURE_DIRECT_OBJECT_REFERENCE | PRIVILEGE_ESCALATION | SERVER_SIDE_TEMPLATE_INJECTION | COMMAND_INJECTION | CODE_INJECTION | SQL_INJECTION | ARBITRARY_FILE_UPLOAD | INSECURE_DESERIALIZATION | LOCAL_FILE_INCLUSION | INFORMATION_DISCLOSURE | PATH_TRAVERSAL | SERVER_SIDE_REQUEST_FORGERY | JSON_WEB_TOKEN_VULNERABILITIES | XML_EXTERNAL_ENTITY | FILE_DELETION | OTHER | GRAPHQL_VULNERABILITIES | BUSINESS_LOGIC_VULNERABILITIES | CRYPTOGRAPHIC_VULNERABILITIES | DENIAL_OF_SERVICE | FILE_ACCESS | FILE_CREATION | DATABASE_MODIFICATION | DATABASE_ACCESS | OUTBOUND_SERVICE_REQUEST | UNKNOWN`
Required: No

 ** targetEndpoint **   <a name="securityagent-Type-Task-targetEndpoint"></a>
The target endpoint being tested by the task.
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** taskHours **   <a name="securityagent-Type-Task-taskHours"></a>
The number of active work hours consumed by the task during execution.
Type: Double
Required: No

 ** title **   <a name="securityagent-Type-Task-title"></a>
The title of the task.
Type: String
Required: No

 ** updatedAt **   <a name="securityagent-Type-Task-updatedAt"></a>
The date and time the task was last updated, in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_Task_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/Task)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/Task)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/Task)
