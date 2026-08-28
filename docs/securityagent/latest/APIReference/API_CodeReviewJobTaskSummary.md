---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CodeReviewJobTaskSummary.html
---

# CodeReviewJobTaskSummary
<a name="API_CodeReviewJobTaskSummary"></a>

Contains summary information about a code review job task.

## Contents
<a name="API_CodeReviewJobTaskSummary_Contents"></a>

 ** taskId **   <a name="securityagent-Type-CodeReviewJobTaskSummary-taskId"></a>
The unique identifier of the task.
Type: String
Required: Yes

 ** agentSpaceId **   <a name="securityagent-Type-CodeReviewJobTaskSummary-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: No

 ** codeReviewId **   <a name="securityagent-Type-CodeReviewJobTaskSummary-codeReviewId"></a>
The unique identifier of the code review associated with the task.
Type: String
Required: No

 ** codeReviewJobId **   <a name="securityagent-Type-CodeReviewJobTaskSummary-codeReviewJobId"></a>
The unique identifier of the code review job that contains the task.
Type: String
Required: No

 ** createdAt **   <a name="securityagent-Type-CodeReviewJobTaskSummary-createdAt"></a>
The date and time the task was created, in UTC format.
Type: Timestamp
Required: No

 ** executionStatus **   <a name="securityagent-Type-CodeReviewJobTaskSummary-executionStatus"></a>
The current execution status of the task.
Type: String
Valid Values: `IN_PROGRESS | ABORTED | COMPLETED | INTERNAL_ERROR | FAILED`
Required: No

 ** riskType **   <a name="securityagent-Type-CodeReviewJobTaskSummary-riskType"></a>
The type of security risk the task is testing for.
Type: String
Valid Values: `CROSS_SITE_SCRIPTING | DEFAULT_CREDENTIALS | INSECURE_DIRECT_OBJECT_REFERENCE | PRIVILEGE_ESCALATION | SERVER_SIDE_TEMPLATE_INJECTION | COMMAND_INJECTION | CODE_INJECTION | SQL_INJECTION | ARBITRARY_FILE_UPLOAD | INSECURE_DESERIALIZATION | LOCAL_FILE_INCLUSION | INFORMATION_DISCLOSURE | PATH_TRAVERSAL | SERVER_SIDE_REQUEST_FORGERY | JSON_WEB_TOKEN_VULNERABILITIES | XML_EXTERNAL_ENTITY | FILE_DELETION | OTHER | GRAPHQL_VULNERABILITIES | BUSINESS_LOGIC_VULNERABILITIES | CRYPTOGRAPHIC_VULNERABILITIES | DENIAL_OF_SERVICE | FILE_ACCESS | FILE_CREATION | DATABASE_MODIFICATION | DATABASE_ACCESS | OUTBOUND_SERVICE_REQUEST | UNKNOWN`
Required: No

 ** title **   <a name="securityagent-Type-CodeReviewJobTaskSummary-title"></a>
The title of the task.
Type: String
Required: No

 ** updatedAt **   <a name="securityagent-Type-CodeReviewJobTaskSummary-updatedAt"></a>
The date and time the task was last updated, in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_CodeReviewJobTaskSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CodeReviewJobTaskSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CodeReviewJobTaskSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CodeReviewJobTaskSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
