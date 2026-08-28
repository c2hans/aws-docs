---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-api-testing-actions.html
---

# Resilience testing
<a name="next-gen-api-testing-actions"></a>

| Action | Method | Description |
| --- | --- | --- |
| `ListTestTemplates` | GET | List the available test templates. |
| `GetTestTemplate` | GET | Retrieve a test template, including its actions and parameters. |
| `CreateTest` | POST | Create a test for a service from a test template. |
| `GetTest` | GET | Retrieve a test configuration including parameters, stop conditions, and role. |
| `UpdateTest` | POST | Update a test configuration including parameters, stop conditions, and role. |
| `ListTests` | GET | Lists tests for a service. |
| `DeleteTest` | POST | Delete a test. |
| `StartTestRun` | POST | Start a test run for a service. |
| `StopTestRun` | POST | Stop a test run. |
| `ListTestRuns` | GET | List test runs for a service. |
| `GetTestRun` | GET | Retrieve a test run including status, parameters, and timestamp. |
| `ListTestRunEvents` | GET | List the events in a test run's timeline. |
| `PutTestSources` | POST | Add or update success criteria alarms or observability alarms for a test. |
| `DeleteTestSources` | POST | Remove success criteria alarms or observability alarms from a test. |
| `ListTestSources` | GET | List success criteria alarms or observability alarms for a test. |
| `ListTestRunSources` | GET | List success criteria alarms or observability alarms for a test run. |
| `ListResolvedTestRunTargetResources` | GET | List the resources that were resolved as targets for a test run. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
