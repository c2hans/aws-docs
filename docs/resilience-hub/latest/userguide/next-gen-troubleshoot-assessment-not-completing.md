---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-assessment-not-completing.html
---

# Assessment not completing
<a name="next-gen-troubleshoot-assessment-not-completing"></a>

**Symptom:** Assessment stays in `IN_PROGRESS` status for more than 30 minutes.

The following table lists possible causes and solutions.

| Cause | Solution |
| --- | --- |
| Large service (many resources) | Assessments for services with 1,000 or more resources may take longer. Wait up to 60 minutes. |
| Invoker role permissions issue | Verify the invoker role has ReadOnlyAccess and AWSResilienceHubV2AssessmentExecutionPolicy attached. |
| Topology not completed | Ensure StartServiceTopologyDiscovery completed successfully before starting an assessment. |
| Service error | If the assessment fails, check the error message in the GetFailureModeAssessment response. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
