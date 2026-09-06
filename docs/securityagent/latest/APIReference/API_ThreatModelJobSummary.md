---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ThreatModelJobSummary.html
---

# ThreatModelJobSummary
<a name="API_ThreatModelJobSummary"></a>

Contains summary information about a threat model job.

## Contents
<a name="API_ThreatModelJobSummary_Contents"></a>

 ** threatModelId **   <a name="securityagent-Type-ThreatModelJobSummary-threatModelId"></a>
The unique identifier of the threat model associated with the job.
Type: String
Required: Yes

 ** threatModelJobId **   <a name="securityagent-Type-ThreatModelJobSummary-threatModelJobId"></a>
The unique identifier of the threat model job.
Type: String
Required: Yes

 ** agentSpaceId **   <a name="securityagent-Type-ThreatModelJobSummary-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: No

 ** createdAt **   <a name="securityagent-Type-ThreatModelJobSummary-createdAt"></a>
The date and time the threat model job was created, in UTC format.
Type: Timestamp
Required: No

 ** status **   <a name="securityagent-Type-ThreatModelJobSummary-status"></a>
The current status of the threat model job.
Type: String
Valid Values: `IN_PROGRESS | STOPPING | STOPPED | FAILED | COMPLETED`
Required: No

 ** title **   <a name="securityagent-Type-ThreatModelJobSummary-title"></a>
The title of the threat model job.
Type: String
Required: No

 ** updatedAt **   <a name="securityagent-Type-ThreatModelJobSummary-updatedAt"></a>
The date and time the threat model job was last updated, in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_ThreatModelJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ThreatModelJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ThreatModelJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ThreatModelJobSummary)
