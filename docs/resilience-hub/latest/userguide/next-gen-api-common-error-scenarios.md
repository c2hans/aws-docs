---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-api-common-error-scenarios.html
---

# Common error scenarios
<a name="next-gen-api-common-error-scenarios"></a>

| Scenario | Error | Resolution |
| --- | --- | --- |
| Starting assessment without topology | ConflictException | Run StartServiceTopologyDiscovery first. |
| Starting assessment while one is running | ConflictException | Wait for the current assessment to complete. |
| Deleting system with services | ConflictException | Remove all service associations first. |
| Cross-account access without role | AccessDeniedException | Configure cross-account roles or enable Organizations. |
| Exceeding 5 cross-account roles | ServiceQuotaExceededException | Use AWS Organizations for larger deployments. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
