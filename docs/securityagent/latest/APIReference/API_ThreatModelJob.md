---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ThreatModelJob.html
---

# ThreatModelJob
<a name="API_ThreatModelJob"></a>

Represents a threat model job, which is an execution instance of a threat model.

## Contents
<a name="API_ThreatModelJob_Contents"></a>

 ** agentSpaceId **   <a name="securityagent-Type-ThreatModelJob-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: No

 ** createdAt **   <a name="securityagent-Type-ThreatModelJob-createdAt"></a>
The date and time the threat model job was created, in UTC format.
Type: Timestamp
Required: No

 ** documents **   <a name="securityagent-Type-ThreatModelJob-documents"></a>
The list of documents used for threat modeling.
Type: Array of [DocumentInfo](API_DocumentInfo.md) objects
Required: No

 ** errorInformation **   <a name="securityagent-Type-ThreatModelJob-errorInformation"></a>
Error information if the threat model job encountered an error.
Type: [ErrorInformation](API_ErrorInformation.md) object
Required: No

 ** executionEndTime **   <a name="securityagent-Type-ThreatModelJob-executionEndTime"></a>
The date and time the threat model job execution ended, in UTC format.
Type: Timestamp
Required: No

 ** executionStartTime **   <a name="securityagent-Type-ThreatModelJob-executionStartTime"></a>
The date and time the threat model job execution started, in UTC format.
Type: Timestamp
Required: No

 ** integratedRepositories **   <a name="securityagent-Type-ThreatModelJob-integratedRepositories"></a>
The list of integrated repositories used for threat modeling.
Type: Array of [IntegratedRepository](API_IntegratedRepository.md) objects
Required: No

 ** scopeDocs **   <a name="securityagent-Type-ThreatModelJob-scopeDocs"></a>
The scoped documents for the agent to focus on during threat modeling.
Type: Array of [DocumentInfo](API_DocumentInfo.md) objects
Required: No

 ** sourceCode **   <a name="securityagent-Type-ThreatModelJob-sourceCode"></a>
The list of source code repositories used for threat modeling.
Type: Array of [SourceCodeRepository](API_SourceCodeRepository.md) objects
Required: No

 ** status **   <a name="securityagent-Type-ThreatModelJob-status"></a>
The current status of the threat model job.
Type: String
Valid Values: `IN_PROGRESS | STOPPING | STOPPED | FAILED | COMPLETED`
Required: No

 ** systemOverview **   <a name="securityagent-Type-ThreatModelJob-systemOverview"></a>
The system overview generated during threat modeling.
Type: String
Required: No

 ** threatModelId **   <a name="securityagent-Type-ThreatModelJob-threatModelId"></a>
The unique identifier of the threat model associated with the job.
Type: String
Required: No

 ** threatModelJobId **   <a name="securityagent-Type-ThreatModelJob-threatModelJobId"></a>
The unique identifier of the threat model job.
Type: String
Required: No

 ** title **   <a name="securityagent-Type-ThreatModelJob-title"></a>
The title of the threat model job.
Type: String
Required: No

 ** updatedAt **   <a name="securityagent-Type-ThreatModelJob-updatedAt"></a>
The date and time the threat model job was last updated, in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_ThreatModelJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ThreatModelJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ThreatModelJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ThreatModelJob)
