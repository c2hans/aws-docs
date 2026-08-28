---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-supported-events.html
---

# Supported Next generation Resilience Hub events
<a name="next-gen-supported-events"></a>

All Next generation Resilience Hub API actions are logged in CloudTrail, including the following.

| Category | Example events |
| --- | --- |
| Systems | CreateSystem, DeleteSystem, GetSystem, ListSystems |
| Services | CreateService, UpdateService, DeleteService, ListServices |
| Policies | CreateResiliencePolicy, UpdateResiliencePolicy, DeleteResiliencePolicy |
| Assessments | StartFailureModeAssessment, GetFailureModeAssessment, ListFailureModeFindings |
| Discovery | StartServiceTopologyDiscovery, ListDependencies, ClassifyDependency |
| Resilience testing | CreateTest, GetTest, ListTests, UpdateTest, DeleteTest, StartTestRun, StopTestRun, GetTestRun, ListTestRuns, ListTestTemplates, GetTestTemplate, PutTestSources, DeleteTestSources, ListTestSources, ListTestRunSources, ListTestRunEvents, ListResolvedTestRunTargetResources |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
