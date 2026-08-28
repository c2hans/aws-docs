---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-resilience-testing-runs-and-report.html
---

# Test runs and report
<a name="next-gen-resilience-testing-runs-and-report"></a>

Each time you start a test, a test run is created. You can view test runs in multiple places:
+ **Service level**: Navigate to your service → Testing tab → test runs at the bottom. Shows all runs for that service.
+ **Test runs page** (left nav): Shows test runs across all your services. Filter by service, test name, or status.
+ **Dashboard**: The test results chart shows pass/fail distribution across your organization.

Each test run includes the test status, timing information, success alarm results, a timeline of actions, and any dependencies blocked or log events captured during the run. You can drill into a test run to see full details including the AWS FIS experiment ID and individual action outcomes.

You can have multiple runs of the same test. For example, running your **Availability Zone: recovery** test monthly to track resilience improvements over time. You can also list test runs and retrieve test run details programmatically using the `ListTestRuns` and `GetTestRun` API operations. See the [API reference](next-gen-api-reference.md).

A test report is auto-generated after each test run completes, if a report destination (Amazon S3 bucket) is configured on your service. If no destination is configured, no report is generated.

Reports capture the test configuration, success criteria results, a visual timeline of how the service responded, and the overall pass/fail outcome.

Where to find reports:
+ **Reports page** (left nav): Shows all reports (assessment and test) across your services.
+ **Test run details**: Download directly from the test run detail page.

Test reports are included at no additional cost when using the next generation of Resilience Hub resilience testing.

You can also retrieve test run results and report metadata programmatically using the `GetTestRun` and `ListTestRunSources` API operations. See the [API reference](next-gen-api-reference.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
